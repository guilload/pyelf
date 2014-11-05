from .header import Header
from .section import SectionTable
from .sheader import SectionHeaderTable


class ELF(object):
    def __init__(self, filepath):
        self.stream = open(filepath, mode='rb')
        self.header = Header(self)
        self.sheaders = SectionHeaderTable(self)
        self.sections = SectionTable(self)

    def __del__(self):
        self.stream.close()

    @property
    def dynamic(self):
        return self.sections.dynamic

    @property
    def endianness(self):
        return self.header.endianness

    @property
    def relocations(self):
        return self.sections.relocations

    @property
    def shstrtab(self):
        return self.sections[self.header.e_shstrndx]

    @property
    def symbols(self):
        return self.sections.symbols

    @property
    def word_size(self):
        return self.header.word_size
