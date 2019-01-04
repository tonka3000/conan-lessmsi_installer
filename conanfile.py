#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
from conans.errors import ConanException


class LessmsiInstallerConan(ConanFile):
    name = "lessmsi_installer"
    version = "1.6.3"
    description = "lessmsi binaries for use in recipes"
    topics = ("conan", "lessmsi_installer")
    url = "https://github.com/bincrafters/conan-lessmsi_installer"
    homepage = "https://github.com/activescott/lessmsi"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    settings = "os_build", "arch_build"

    def build(self):
        if not tools.os_info.is_windows:
            raise ConanException("lessmsi is only available on windows")

        source_url = "{}/releases/download/v{}/lessmsi-v{}.zip".format(self.homepage, self.version, self.version)
        self.output.info("Download {}".format(source_url))
        tools.get(source_url)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src="")
        self.copy(pattern="*", dst="", src="", keep_path=True)

    def package_info(self):
        self.env_info.PATH.append(self.package_folder)
