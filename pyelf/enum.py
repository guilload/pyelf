class Enum(object):

    members = ()

    def __new__(cls, namespace, *args, **kwargs):
        cls.index = {}

        for name, value, description in cls.members:
            constant = Constant(name, value, description)
            cls.index[value] = constant
            namespace[name] = constant

        return super(Enum, cls).__new__(cls, *args, **kwargs)

    def __getitem__(self, key):
        return self.index[key]

    def get(self, key, default=None):
        return self.index.get(key, default)


class Constant(object):

    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description

    def __eq__(self, other):
        return self.value == other

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return self.description
