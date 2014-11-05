from tabulate import tabulate

from .enums import SHT_DYNAMIC, SHT_DYNSYM, SHT_REL, SHT_RELA, SHT_STRTAB, SHT_SYMTAB
from .strtab import StringTable
from .structs import STRUCTS


SECTIONS = {SHT_DYNAMIC: 'Elf_Dyn',
            SHT_DYNSYM: 'Elf_Sym',
            SHT_REL: 'Elf_Rel',
            SHT_RELA: 'Elf_Rela',
            SHT_SYMTAB: 'Elf_Sym',
            }


class SectionTable(object):

    def __init__(self, elf):
        self.index = {}
        self.sections = []

        for i, sheader in enumerate(elf.sheaders):

            if sheader.sh_type == SHT_STRTAB:
                section = StringTable(elf, sheader)
            else:
                try:
                    name = SECTIONS[sheader.sh_type]
                except KeyError:
                    continue

                struct = STRUCTS[elf.word_size][name]
                section = Section(elf, sheader, struct)

            self.index[i] = section
            self.sections.append(section)

    def __contains__(self, i):
        return i in self.index

    def __getitem__(self, i):
        return self.index[i]

    def __iter__(self):
        for section in self.sections:
            yield section

    @property
    def dynamic(self):
        for section in self:
            if section.sh_type == SHT_DYNAMIC:
                return section

    @property
    def relocations(self):
        for section in self:
            if section.sh_type in (SHT_REL, SHT_RELA):
                yield section

    @property
    def symbols(self):
        for section in self:
            if section.sh_type in (SHT_DYNSYM, SHT_SYMTAB):
                yield section


class Section(object):

    def __init__(self, elf, sheader, struct):
        self.entries = []
        self.sheader = sheader
        self.struct = struct

        for offset in self.offsets():
            entry = struct(elf, offset, elf.endianness)
            entry.sheader = sheader
            self.entries.append(entry)

    def __getattr__(self, name):
        return getattr(self.sheader, name)

    def __getitem__(self, index):
        return self.entries[index]

    def __iter__(self):
        for entry in self.entries:
            yield entry

    def __len__(self):
        return len(self.entries)

    def __str__(self):
        headers = self.struct.labels()
        table = [entry.values() for entry in self]
        return tabulate(table, headers=headers, tablefmt='plain')

    def offsets(self):
        start = self.sheader.sh_offset
        stop = start + self.sheader.sh_size
        step = self.sheader.sh_entsize
        return range(start, stop, step)
