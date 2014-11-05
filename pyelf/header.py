from .structs import Elf_Eident, STRUCTS


class Header(object):

    template = '\n'.join(['ELF Header:',
                          '  Magic:                             7f 45 4c 46',
                          '  Class:                             {ei_class}',
                          '  Data:                              {ei_data}',
                          '  Version:                           {ei_version}',
                          '  OS/ABI:                            {ei_osabi}',
                          '  ABI Version:                       {ei_abiversion}',
                          '  Type:                              {e_type}',
                          '  Machine:                           {e_machine}',
                          '  Version:                           {e_version}',
                          '  Entry point address:               {e_entry:#x}',
                          '  Start of program headers:          {e_phoff} (bytes into file)',
                          '  Start of section headers:          {e_shoff} (bytes into file)',
                          '  Flags:                             {e_flags}',
                          '  Size of this header:               {e_shentsize} (bytes)',
                          '  Size of program headers:           {e_phentsize} (bytes)',
                          '  Number of program headers:         {e_phnum}',
                          '  Size of section headers:           {e_shentsize} (bytes)',
                          '  Number of section headers:         {e_shnum}',
                          '  Section header string table index: {e_shstrndx}'])

    def __init__(self, elf):
        self.eident = Elf_Eident(elf, offset=0, endianness='@')

        struct = STRUCTS[self.word_size]['Elf_Ehdr']
        self.ehdr = struct(elf, elf.stream.tell(), self.endianness)

    def __getattr__(self, name):
        return getattr(self.eident, name, None) or getattr(self.ehdr, name)

    def __str__(self):
        attrs = self.eident.attrs
        attrs.update(self.ehdr.attrs)
        return self.template.format(**attrs)

    @property
    def endianness(self):
        return '<' if self.ei_data == 1 else '>'

    @property
    def word_size(self):
        return 32 if self.ei_class == 1 else 64
