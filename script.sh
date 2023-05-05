#! /bin/bash

set -e

if [ "$1" != "--no-update" ]; then
    conan create base base/1.1@
    conan create compat compatible/1.1@ -s os=Linux
    conan lock create consumer/conanfile.py -s os=Windows --lockfile-out=deps.lock
    conan lock create consumer/conanfile.py -s os=Windows --lockfile=deps.lock --lockfile-out=deps-out.lock
fi

conan install consumer/conanfile.py --lockfile=deps-out.lock