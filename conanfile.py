#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class LibnameConan(ConanFile):
    name = "msgpack"
    version = "2.1.5"
    url = "https://github.com/bincrafters/conan-msgpack"
    description = "Keep it short"
    license = "https://github.com/someauthor/somelib/blob/master/LICENSES"
    exports_sources = ["CMakeLists.txt", "LICENSE"]
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = 'cmake'

    def source(self):
        source_url = "https://github.com/msgpack/msgpack-c"
        tools.get("{0}/archive/cpp-{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-c-cpp-" + self.version
        os.rename(extracted_dir, "sources")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["MSGPACK_ENABLE_SHARED"] = self.options.shared
        cmake.definitions["MSGPACK_CXX11"] = True
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = self.package_folder

        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        # files are copied by cmake.install()
        pass

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
