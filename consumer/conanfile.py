from conans import ConanFile

class LibCompatibleConanFile(ConanFile):
    requires = "compatible/[>= 1.0 < 2.0]"