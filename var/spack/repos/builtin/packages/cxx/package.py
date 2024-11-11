# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Cxx(Package):
    """Virtual package for the C++ language."""

    homepage = "https://isocpp.org/std/the-standard"
    virtual = True

    def test_cxx(self):
        """Compile and run 'Hello World'"""
        expected = ["Hello world", "YES!"]
        cxx = Executable(self.cxx)
        test_source = self.test_suite.current_test_data_dir
        for test in os.listdir(test_source):
            exe_name = f"{test}.exe"
            with test_part(self, f"test_cxx_{test}", f"build and run {exe_name}"):
                filepath = join_path(test_source, test)
                cxx("-o", exe_name, filepath)
                exe = which(exe_name)
                out = exe(output=str.split, error=str.split)
                check_outputs(expected, out)
