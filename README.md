# Firestore common python library

Firestore common python library es una libreria para uso general, la cual contiene logica relacionado a firestore. Agregar, eliminar, etc.

## Authors

- [@Serialk89](https://github.com/Serialk89)


## Crear y activar venv
python -m venv <directory>
source ../python-venv/bin/activate
 
# Update pip
python3 -m pip install --upgrade pip

# src
packaging_tutorial/
└── src/
    └── example_package_YOUR_USERNAME_HERE/
        ├── __init__.py
        └── example.py

__init__.py is required to import the directory as a package, and should be empty.

# Creando el paquete, crear los archivos correspondientes
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── example_package_YOUR_USERNAME_HERE/
│       ├── __init__.py
│       └── example.py
└── tests/

# Creating pyproject.toml
pyproject.toml tells “frontend” build tools like pip and build what “backend” tool to use to create distribution packages for your project. You can choose from a number of backends; this tutorial uses Hatchling by default, but it will work identically with setuptools, Flit, PDM, and others that support the [project] table for metadata.

Note Some build backends are part of larger tools that provide a command-line interface with additional features like project initialization and version management, as well as building, uploading, and installing packages. This tutorial uses single-purpose tools that work independently.
Open pyproject.toml and enter one of these [build-system] tables:

```
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```
- requires is a list of packages that are needed to build your package. You don’t need to install them; build frontends like pip will install them automatically in a temporary, isolated virtual environment for use during the build process.

- build-backend is the name of the Python object that frontends will use to perform the build.

# Configuring metadata
En el archivo pyproyect.toml

[project]
name = "firebase_tools_jimmykvick"
version = "0.0.1"
authors = [
  { name="Author", email="jaime.quinones.t@gmail.com" },
]
description = "A small example package for common use"
readme = "README.md"
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/pypa/sampleproject"
"Bug Tracker" = "https://github.com/pypa/sampleproject/issues"


name is the distribution name of your package. This can be any name as long as it only contains letters, numbers, ., _ , and -. It also must not already be taken on PyPI. Be sure to update this with your username for this tutorial, as this ensures you won’t try to upload a package with the same name as one which already exists.

version is the package version. See the version specifier specification for more details on versions. Some build backends allow it to be specified another way, such as from a file or a git tag.

authors is used to identify the author of the package; you specify a name and an email for each author. You can also list maintainers in the same format.

description is a short, one-sentence summary of the package.

readme is a path to a file containing a detailed description of the package. This is shown on the package detail page on PyPI. In this case, the description is loaded from README.md (which is a common pattern). There also is a more advanced table form described in the project metadata specification.

requires-python gives the versions of Python supported by your project. Installers like pip will look back through older versions of packages until it finds one that has a matching Python version.

classifiers gives the index and pip some additional metadata about your package. In this case, the package is only compatible with Python 3, is licensed under the MIT license, and is OS-independent. You should always include at least which version(s) of Python your package works on, which license your package is available under, and which operating systems your package will work on. For a complete list of classifiers, see https://pypi.org/classifiers/.

urls lets you list any number of extra links to show on PyPI. Generally this could be to the source, documentation, issue trackers, etc.

# License
Creating a LICENSE

# Generating distribution archives
Make sure you have the latest version of PyPA’s build installed:

python3 -m pip install --upgrade build

## Build
python3 -m build

This command should output a lot of text and once completed should generate two files in the dist directory:

dist/
├── example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
└── example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz
The tar.gz file is a source distribution whereas the .whl file is a built distribution. Newer pip versions preferentially install built distributions, but will fall back to source distributions if needed. You should always upload a source distribution and provide built distributions for the platforms your project is compatible with. In this case, our example package is compatible with Python on any platform so only one built distribution is needed.

# Uploading the distribution archives
- Crear TOKEN
- Now that you are registered, you can use twine to upload the distribution packages., Upgrade twine
python3 -m pip install --upgrade twine

# upload file under dist
python3 -m twine upload --repository testpypi dist/*

You will be prompted for a username and password. For the username, use __token__. For the password, use the token value, including the pypi- prefix.

# Instalando package
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps firebase_tools_jimmykvick

