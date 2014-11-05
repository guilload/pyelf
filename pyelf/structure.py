from collections import OrderedDict
from struct import calcsize, unpack


class Structure(object):

    display = ()
    members = ()

    def __new__(cls, *args, **kwargs):
        if cls.members and not isinstance(cls.members, OrderedDict):
            cls.members = OrderedDict((m['name'], Member(**m)) for m in cls.members)

        return super(Structure, cls).__new__(cls, *args, **kwargs)

    def __init__(self, elf, offset, endianness):
        self.elf = elf
        self.offset = offset
        self.endianness = endianness

        elf.stream.seek(offset)
        data = elf.stream.read(self.size)
        values = unpack(self.format, data)

        for member, value in zip(self.members.values(), values):
            if member.enum:
                value = member.enum.get(value, value)

            if member.flag:
                value = member.flag(value)

            setattr(self, member.name, value)

    @property
    def attrs(self):
        return {k: getattr(self, k) for k in self.members}

    @property
    def format(self):
        lst = [self.endianness]
        lst.extend([m.type for m in self.members.values() if m.type != 'property'])
        return ''.join(lst)

    @classmethod
    def labels(cls):
        return [cls.members[k].label for k in cls.display]

    def values(self):
        return [getattr(self, k) for k in self.display]

    @property
    def size(self):
        return calcsize(self.format)


class Member(object):
    def __init__(self, name, type, enum=None, flag=None, label=None):
        self.name = name
        self.type = type
        self.enum = enum or {}
        self.flag = flag

        self._label = label

    @property
    def label(self):
        if self._label:
            return self._label

        if '_' in self.name:
            _, label = self.name.rsplit('_', 1)
        else:
            label = self.name

        return label.capitalize()
