from tabulate import tabulate

from .strtab import StringTable
from .structs import STRUCTS


class SectionHeaderTable(object):

    def __init__(self, elf):
        self.elf = elf
        self.sheaders = []
        self.struct = STRUCTS[elf.word_size]['Elf_Shdr']

        for offset in self.offsets():
            sheader = self.struct(elf, offset, elf.endianness)
            self.sheaders.append(sheader)

    def __getitem__(self, i):
        return self.sheaders[i]

    def __iter__(self):
        for sheader in self.sheaders:
            yield sheader

    def __str__(self):
        headers = self.struct.labels()
        table = [sh.values() for sh in self]
        return tabulate(table, headers=headers, tablefmt='plain')

    def offset(self, i):
        return self.elf.header.e_shoff + self.elf.header.e_shentsize * i

    def offsets(self):
        for i in range(self.elf.header.e_shnum):
            yield self.offset(i)
