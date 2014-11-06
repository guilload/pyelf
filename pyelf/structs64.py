from .enums import *
from .flags import *
from .structure import Structure


Elf64_Addr = 'Q'
Elf64_Byte = 'B'
Elf64_Half = 'H'
Elf64_Off = 'Q'
Elf64_SHalf = 'h'
Elf64_Sword = 'i'
Elf64_Sxword = 'q'
Elf64_Word = 'I'
Elf64_Xword = 'Q'


class Elf64_Ehdr(Structure):
    """
    File header.
    """
    members = ({'name': 'e_type', 'type': Elf64_Half, 'enum': E_TYPE},
               {'name': 'e_machine', 'type': Elf64_Half, 'enum': E_MACHINE},
               {'name': 'e_version', 'type': Elf64_Word},
               {'name': 'e_entry', 'type': Elf64_Addr},
               {'name': 'e_phoff', 'type': Elf64_Off},
               {'name': 'e_shoff', 'type': Elf64_Off},
               {'name': 'e_flags', 'type': Elf64_Word},
               {'name': 'e_ehsize', 'type': Elf64_Half},
               {'name': 'e_phentsize', 'type': Elf64_Half},
               {'name': 'e_phnum', 'type': Elf64_Half},
               {'name': 'e_shentsize', 'type': Elf64_Half},
               {'name': 'e_shnum', 'type': Elf64_Half},
               {'name': 'e_shstrndx', 'type': Elf64_Half},)


class Elf64_Shdr(Structure):
    """
    Section header.
    """
    members = ({'name': 'sh_name', 'type': Elf64_Word},
               {'name': 'sh_type', 'type': Elf64_Word, 'enum': SH_TYPE},
               {'name': 'sh_flags', 'type': Elf64_Xword, 'flag': SH_FLAG},
               {'name': 'sh_addr', 'type': Elf64_Addr, 'label': 'Address'},
               {'name': 'sh_offset', 'type': Elf64_Off},
               {'name': 'sh_size', 'type': Elf64_Xword},
               {'name': 'sh_link', 'type': Elf64_Word},
               {'name': 'sh_info', 'type': Elf64_Word},
               {'name': 'sh_addralign', 'type': Elf64_Xword, 'label': 'Align'},
               {'name': 'sh_entsize', 'type': Elf64_Xword, 'label': 'Entry size'},
               {'name': 'name', 'type': 'property'},
               {'name': 'number', 'type': 'property', 'label': 'No.'})

    display = ('number',
               'name',
               'sh_type',
               'sh_addr',
               'sh_offset',
               'sh_size',
               'sh_entsize',
               'sh_flags',
               'sh_link',
               'sh_info',
               'sh_addralign')

    @property
    def name(self):
        return self.elf.shstrtab[self.sh_name]

    @property
    def number(self):
        return (self.offset - self.elf.header.e_shoff) / self.elf.header.e_shentsize


class Elf64_Phdr(Structure):
    """
    Program header.
    """
    members = ({'name': 'p_type', 'type': Elf64_Word},
               {'name': 'p_flags', 'type': Elf64_Word},
               {'name': 'p_offset', 'type': Elf64_Off},
               {'name': 'p_vaddr', 'type': Elf64_Addr},
               {'name': 'p_paddr', 'type': Elf64_Addr},
               {'name': 'p_filesz', 'type': Elf64_Xword},
               {'name': 'p_memsz', 'type': Elf64_Xword},
               {'name': 'p_align', 'type': Elf64_Xword})


class Elf64_Sym(Structure):
    """
    Symbol section entry.
    """
    members = ({'name': 'st_name', 'type': Elf64_Word},
               {'name': 'st_info', 'type': Elf64_Byte},
               {'name': 'st_other', 'type': Elf64_Byte, 'enum': ST_VISIBILITY, 'label': 'VIS'},
               {'name': 'st_shndx', 'type': Elf64_Half, 'enum': SH_Nindex},
               {'name': 'st_value', 'type': Elf64_Addr},
               {'name': 'st_size', 'type': Elf64_Xword},
               {'name': 'st_bind', 'type': 'property'},
               {'name': 'st_type', 'type': 'property'},
               {'name': 'name', 'type': 'property'},
               {'name': 'number', 'type': 'property', 'label': 'No.'})

    display = ('number',
               'st_value',
               'st_size',
               'st_type',
               'st_bind',
               'st_other',
               'st_shndx',
               'name')

    @property
    def name(self):
        symtab = self.elf.sections[self.sheader.sh_link]
        return symtab[self.st_name]

    @property
    def number(self):
        return (self.offset - self.sheader.sh_offset) / self.sheader.sh_entsize

    @property
    def st_bind(self):
        return ST_BIND[self.st_info >> 4]

    @property
    def st_type(self):
        return ST_TYPE[self.st_info & 0xf]


class Elf64_Rel(Structure):
    """
    'SHT_REL' relocation section entry.
    """
    members = ({'name': 'r_offset', 'type': Elf64_Addr},
               {'name': 'r_info', 'type': Elf64_Xword},
               {'name': 'r_sym', 'type': 'property'},
               {'name': 'r_type', 'type': 'property'},)

    @property
    def r_sym(self):
        return (self.r_info >> 32) & 0xffffffff

    @property
    def r_type(self):
        return self.r_info & 0xffffffff


class Elf64_Rela(Structure):
    """
    'SHT_RELA' relocation section entry.
    """
    members = ({'name': 'r_offset', 'type': Elf64_Addr},
               {'name': 'r_info', 'type': Elf64_Xword},
               {'name': 'r_addend', 'type': Elf64_Sxword},
               {'name': 'r_sym', 'type': 'property'},
               {'name': 'r_type', 'type': 'property'},
               {'name': 'name', 'type': 'property', 'label': "Symbol's name + addend"},
               {'name': 'value', 'type': 'property', 'label': "Symbol's value"})

    display = ('r_offset',
               'r_info',
               'r_type',
               'value',
               'name')

    @property
    def r_sym(self):
        return (self.r_info >> 32) & 0xffffffff

    @property
    def r_type(self):
        return R_RELOCATION[self.r_info & 0xffffffff]

    @property
    def name(self):
        if self.r_sym == 0:
            return ''

        if self.symbol.st_name == 0:
            sheader = self.elf.sheaders[self.symbol.st_shndx]
            name = sheader.name
        else:
            name = self.symbol.name

        return '{} {} {}'.format(name, '+' if self.r_addend >= 0 else '-',
                                 abs(self.r_addend))

    @property
    def symbol(self):
        symtab = self.elf.sections[self.sheader.sh_link]
        symbol = symtab[self.r_sym]
        return symbol

    @property
    def value(self):
        if self.r_sym == 0:
            return ''

        return self.symbol.st_value


class Elf64_Dyn(Structure):
    """
    Dynamic section entry.
    """
    members = ({'name': 'd_tag', 'type': Elf64_Sxword},
               {'name': 'd_val', 'type': Elf64_Xword},
               {'name': 'd_type', 'type': 'property'},
               {'name': 'name', 'type': 'property', 'label': 'Name or value'})

    display = ('d_tag',
               'd_type',
               'name',)

    @property
    def d_type(self):
        return D_TAG[self.d_tag]

    @property
    def name(self):  # TODO: there're more d_types to deal with
        if self.d_type == DT_NEEDED:
            symtab = self.elf.sections[self.sheader.sh_link]
            return 'Shared library: [{}]'.format(symtab[self.d_val])
        else:
            return self.d_val
