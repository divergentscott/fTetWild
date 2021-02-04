import os
from conans import ConanFile, CMake


class FTetWildConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    # comma-separated list of requirements
    generators = "cmake"
    # requires = ["eigen/3.3.7@d3d/testing"]
                # "TBB/2020.1@d3d/testing"]
                # "libigl/git@d3d/testing"]

    def requirements(self):
        if self.settings.os == "Windows":
            self.requires("mpir/3.0.0")
        else:
            self.requires("gmp/6.1.2@bincrafters/stable")


    def build(self):
        cmake = CMake(self)
        cmake.verbose()
        cmake.configure()
        cmake.build()
