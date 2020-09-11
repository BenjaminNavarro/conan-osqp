from conans import ConanFile, CMake, tools


class OsqpConan(ConanFile):
    name = "osqp"
    version = "0.6.0"
    license = "MIT"
    author = "Benjamin Navarro <navarro.benjamin13@gmail.com>"
    url = "https://github.com/BenjaminNavarro/conan-osqp"
    description = "Conan package for the OSQP library, the Operator Splitting QP solver"
    topics = ("C++", "QP", "Solver")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    _libs = ["osqp", "qdldl"]

    def source(self):
        self.run(
            "git clone --recursive https://github.com/oxfordcontrol/osqp.git --branch v{}".format(self.version))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="osqp")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/osqp", src="osqp/include")
        self.copy("*.h", dst="include/qdldl",
                  src="osqp/lin_sys/direct/qdldl/qdldl_sources/include")
        self.copy("LICENSE", src="osqp")
        self.copy("NOTICE", src="osqp")

        for lib in self._libs:
            self.copy("*{}.lib".format(lib), dst="lib", keep_path=False)
            self.copy("*{}.dll".format(lib), dst="bin", keep_path=False)
            self.copy("*{}.so".format(lib), dst="lib", keep_path=False)
            self.copy("*{}.dylib".format(lib), dst="lib", keep_path=False)
            self.copy("*{}.a".format(lib), dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = self._libs
        self.cpp_info.includedirs = ["include/osqp", "include/qdldl"]
