#!/usr/bin/env python
#
# Copyright (C) 2018 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""This file contains unit tests for elf_parser."""

import os
import unittest

from vts.utils.python.library import elf_parser as elf


_SECTION_NAMES = {'test.rela', 'test.honeycomb', 'test.jellybean',
                  'test.nougat', 'test.oreo', 'test.pie', 'test.dup'}

_EXPORTED_SYMBOLS = {'global_var_1', 'global_var_2',
                     '_Z15exported_func_1v', '_Z15exported_func_2v'}

R_X86_64_GLOB_DAT = 6

_RELOCATIONS = {(R_X86_64_GLOB_DAT, 'global_var_1', 0),
                (R_X86_64_GLOB_DAT, 'global_var_2', 0)}

_ANDROID_RELOCATIONS = [(0x200008, (1 << 32) | 1, 0),
                        (0x200010, (2 << 32) | 1, 0),
                        (0x200020, 8, 128),
                        (0x200030, 8, 136),
                        (0x200040, 8, 152),
                        (0x200050, 8, 184)]

_DEPENDENCIES = ['libc.so.6', 'libm.so.6']


class ElfParserTest(unittest.TestCase):
    """Unit tests for ElfParser from elf_parser."""

    def setUp(self):
        """Creates an ElfParser."""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.elf_file_path = os.path.join(dir_path, 'elf', 'testing',
                                          'libtest.so')
        self.elf_file = elf.ElfParser(self.elf_file_path)

    def tearDown(self):
        """Closes the ElfParser."""
        self.elf_file.Close()

    def testGetSectionName(self):
        """Tests that GetSectionName parses section names correctly."""
        sh_names = [self.elf_file.GetSectionName(sh)
                    for sh in self.elf_file.Shdr]
        self.assertFalse(_SECTION_NAMES.difference(sh_names))

    def testGetSectionsByName(self):
        """Tests that GetSectionsByName finds all sections of the same name."""
        none_secs = list(self.elf_file.GetSectionsByName('no.such.section'))
        dup_secs = list(self.elf_file.GetSectionsByName('test.dup'))
        self.assertEqual(len(none_secs), 0)
        self.assertEqual(len(dup_secs), 2)

    def testGetSectionByName(self):
        """Tests that GetSectionByName finds section by name correctly."""
        none_sec = self.elf_file.GetSectionByName('no.such.section')
        self.assertEqual(none_sec, None)
        for section_name in _SECTION_NAMES:
            sh = self.elf_file.GetSectionByName(section_name)
            self.assertIsNotNone(sh)

    def testGetSymbols(self):
        """Tests that GetSymbols parses symbol table correctly."""
        symtab = self.elf_file.GetSectionByName('.symtab')
        strtab = self.elf_file.Shdr[symtab.sh_link]
        syms = self.elf_file.GetSymbols(symtab)
        sym_names = [self.elf_file.GetString(strtab, sym.st_name)
                     for sym in syms]
        self.assertFalse(_EXPORTED_SYMBOLS.difference(sym_names))

    def testGetRelocations(self):
        """Tests that GetRelocations parses relocation table correctly."""
        reltab = self.elf_file.GetSectionByName('.rela.dyn')
        symtab = self.elf_file.Shdr[reltab.sh_link]
        strtab = self.elf_file.Shdr[symtab.sh_link]
        relocs = []
        for rela in self.elf_file.GetRelocations(reltab):
            sym = self.elf_file.GetRelocationSymbol(symtab, rela)
            sym_name = self.elf_file.GetString(strtab, sym.st_name)
            relocs.append((rela.GetType(), sym_name, rela.r_addend))
        self.assertFalse(_RELOCATIONS.difference(relocs))

    def testGetRelocations_Android(self):
        """Tests that GetRelocations parses Android packed format correctly."""
        android_rela = self.elf_file.GetSectionByName('test.rela')
        relocs = []
        for rela in self.elf_file.GetRelocations(android_rela):
            relocs.append((rela.r_offset, rela.r_info, rela.r_addend))
        self.assertEqual(relocs, _ANDROID_RELOCATIONS)

    def testIsExecutable(self):
        """Tests that IsExecutable determines file type correctly."""
        is_executable = self.elf_file.IsExecutable()
        self.assertFalse(is_executable)

    def testIsSharedObject(self):
        """Tests that IsSharedObject determines file type correctly."""
        is_shared_object = self.elf_file.IsSharedObject()
        self.assertTrue(is_shared_object)

    def testHasAndroidIdent(self):
        """Tests that HasAndroidIdent finds .note.android.ident section."""
        has_android_ident = self.elf_file.HasAndroidIdent()
        self.assertTrue(has_android_ident)

    def testMatchCpuAbi(self):
        """Tests that MatchCpuAbi determines machine type correctly."""
        self.assertTrue(self.elf_file.MatchCpuAbi("x86_64"))
        self.assertFalse(self.elf_file.MatchCpuAbi("x86"))

    def testListDependencies(self):
        """Tests that ListDependencies lists ELF dependencies correctly."""
        deps = self.elf_file.ListDependencies()
        self.assertEqual(deps, _DEPENDENCIES)

    def testListGlobalSymbols(self):
        """Tests that ListGlobalSymbols lists global symbols correctly."""
        syms = self.elf_file.ListGlobalSymbols(False, '.dynsym', '.dynstr')
        self.assertFalse(_EXPORTED_SYMBOLS.difference(syms))

    def testGetProgramInterpreter(self):
        """Tests that GetProgramInterpreter parses segment type correctly."""
        interp = self.elf_file.GetProgramInterpreter()
        self.assertEqual(interp, "/lib64/ld-linux-x86-64.so.2")


if __name__ == '__main__':
    unittest.main()
