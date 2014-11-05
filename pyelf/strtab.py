class StringTable(object):
    def __init__(self, elf, sheader):
        self.sheader = sheader

        elf.stream.seek(sheader.sh_offset)
        self.array = elf.stream.read(sheader.sh_size)

    def __getattr__(self, name):
        return getattr(self.sheader, name)

    def __getitem__(self, start):
        if start >= len(self.array):
            return '\0'

        stop = start

        while self.array[stop] != '\0' and stop < len(self.array):
            stop += 1

        return self.array[start:stop]
