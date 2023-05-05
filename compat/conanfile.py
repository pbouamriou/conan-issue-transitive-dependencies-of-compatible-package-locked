from conans import ConanFile

class LibCompatibleConanFile(ConanFile):
    settings = "os"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    requires = "base/[>= 1.0 < 2.0]"

    def package_id(self):
        #if self.settings.compiler == "intel":
        #    p = self.info.clone()
        #    p.base_compatible()
        #    self.compatible_packages.append(p)
        if self.settings.os == "Windows":
            compatible_pkg = self.info.clone()
            compatible_pkg.settings.os = "Linux"
            self.compatible_packages.append(compatible_pkg)