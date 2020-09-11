# OSQP Conan package

This repo holds a [Conan](https://conan.io) recipe for the [OSQP](https://github.com/oxfordcontrol/osqp) library.

The package is available on [Bintray](https://bintray.com/benjaminnavarro/bnavarro/osqp%3Abnavarro).
To add the corresponding remote you can run:
```
conan remote add bnavarro https://api.bintray.com/conan/benjaminnavarro/bnavarro
```
And then use `osqp/0.6.0@bnavarro/stable` as dependency in your conanfile.

Please note that there are no precompiled binaries currently available, so you have to use the `--build=missing` option when calling `conan install`, e.g: 
```
conan install . --build=missing
```
