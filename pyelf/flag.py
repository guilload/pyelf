class Flag(object):

    flags = ()

    def __init__(self, value):
        self.value = value

    def __str__(self):
        lst = []

        for _, mask, description in reversed(self.flags):
            if self.value & mask == mask:
                lst.append(description)

        return ''.join(lst)
