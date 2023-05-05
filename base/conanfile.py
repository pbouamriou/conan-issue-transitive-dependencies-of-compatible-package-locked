from conans import ConanFile

class LibBaseConanFile(ConanFile):
    options = {"shared": [True, False]}
    default_options = {"shared": True}