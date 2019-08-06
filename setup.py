#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
import platform
import shutil
from pathlib import Path

from skbuild import setup
from setuptools import find_packages
from setuptools.dist import Distribution

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = ["numpy"]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]


class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""

    def has_ext_modules(self):
        return True


source_folder = "src"
packages = find_packages(where=source_folder)
root_package = packages[0]

root_folder = Path(__file__).parent
clib_ext_by_platform = {"Darwin": "dylib", "Linux": "so", "Windows": "dll"}
clib_ext = clib_ext_by_platform[platform.system()]


cmake_args = ([
    "-G", "Visual Studio 14" + (" Win64" if x64 else '')
] if os.name == 'nt' else [
    "-G", "Unix Makefiles"  # don't make CMake try (and fail) Ninja first
]) #+ [
#     # skbuild inserts PYTHON_* vars. That doesn't satisfy opencv build scripts in case of Py3
#     "-DPYTHON%d_EXECUTABLE=%s" % (sys.version_info[0], sys.executable),
#     "-DBUILD_opencv_python%d=ON" % sys.version_info[0],

#     # When off, adds __init__.py and a few more helper .py's. We use our own helper files with a different structure.
#     "-DOPENCV_SKIP_PYTHON_LOADER=ON",
#     # Relative dir to install the built module to in the build tree.
#     # The default is generated from sysconfig, we'd rather have a constant for simplicity
#     "-DOPENCV_PYTHON%d_INSTALL_PATH=python" % sys.version_info[0],
#     # Otherwise, opencv scripts would want to install `.pyd' right into site-packages,
#     # and skbuild bails out on seeing that
#     "-DINSTALL_CREATE_DISTRIB=ON",

#     # See opencv/CMakeLists.txt for options and defaults
#     "-DBUILD_opencv_apps=OFF",
#     "-DBUILD_SHARED_LIBS=OFF",
#     "-DBUILD_TESTS=OFF",
#     "-DBUILD_PERF_TESTS=OFF",
#     "-DBUILD_DOCS=OFF"
# ] + (["-DOPENCV_EXTRA_MODULES_PATH=" + os.path.abspath("opencv_contrib/modules")] if build_contrib else [])


setup(
    author="Pupil Labs GmbH",
    author_email="pypi@pupil-labs.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Python bindings for apriltags v3",
    distclass=BinaryDistribution,
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="apriltags",
    name="pupil-apriltags3",
    packages=packages,
    package_dir={"": "src"},
    package_data={"apriltags3": [f"*.{clib_ext}"]},
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/pupil-labs/apriltags",
    version="1",
    zip_safe=False,
    cmake_args=cmake_args,
    cmake_source_dir="apriltags-source",
    # cmake_install_dir='src/apriltags3',
    cmake_with_sdist=True,
)
