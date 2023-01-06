# Build

### 0. Make sure conan is installed.
Conan is used as a package manager in this project. For more details visit [conan.io/](https://conan.io/).

To check if conan is installed:
```sh
conan --version
```

To install conan:
```sh
pip3 install conan
```

### 1. Install requirements.
```sh
conan install . -if ./build
```

### 2. Build project.

Note: all available presets are presented in `CMakePresets.json`.

```sh
cmake --preset gcc -S . -B ./build
cmake --build ./build
```

### 3. Install executables
```sh
cmake --install ./build
```
All executable files will be placed in the `./{{bin_folder}}` folder.
