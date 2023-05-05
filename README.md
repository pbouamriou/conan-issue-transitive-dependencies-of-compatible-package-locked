# Conan issue reproduction

## Context

base has an option (shared = [ True, False]).
compatible has a package compatibility for os (windows == linux). compat depends on base.
consumer depends on compat.

Create a lock for consumer is OK.
Re-create a lock for consomer using the previous lock as lock is NOK (transitive options are lost).

Conan version : 1.59
Python: 3.7.2

## Way to reproduce

Reproduction on linux or windows (git-bash required): 

```console
git clone git@github.com:pbouamriou/conan-issue-transitive-dependencies-of-compatible-package-locked.git
cd conan-issue-transitive-dependencies-of-compatible-package-locked
./script.sh
```

## Error

```console
ERROR: compatible/1.1: Locked options do not match computed options
Locked options:
shared=False
Computed options:
shared=False
base:shared=True
```

## Correction

The correction is available with this [patch](./0001-Correct-transitive-dependencies-options-lost-on-comp.patch).
A test is added to validate the correction.