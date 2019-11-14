<div align="center"><h1>Dependency Parser</h1>

**DependencyParser** is a dependencies parser for c++ in python using cvesearch, defaulting on https://cve.circl.lu.

This script is based on the work of [Martin Simon](https://github.com/mrsmn/ares) and [Kai Renken](https://github.com/elektrischermoench/ares3).

<img src="https://business.bell.ca/web/SHOP/Responsive/content/img/ent/Banner_Security.jpg" alt="Vulnerability" /></div>

## How it works

### Conanfile

The script requires a **requires** prefix in conan class

Replace the * name of class * by the name of your class in the conanfile.py in the header and in the main loop

## Usage

### Get the project

Clone the [repository](https://github.com/HugoSohm/DependencyParser):

```
git clone https://github.com/HugoSohm/DependencyParser
```

### Installation

- Install conan
```
$ pip3 install conan
```

- Install cvesearch api python wrapper
```
$ git clone https://github.com/cve-search/PyCVESearch.git
$ cd PyCVESearch && pip3 install . && cd ..
```


### Execute

- Execute the python script

```
$ python3 dependencyParser.py
```

## Implementation in Gitlab CI

### Gitlab-ci yml

To add the dependencyParser to the gitlab-ci.yml, creating a non-blocking warning in pipe, include this:
```
dependencyparser:
  image: "python:3.7"
  stage: vulnerability
  before_script:
    - pip3 install conan
    - git clone https://github.com/cve-search/PyCVESearch.git
    - cd PyCVESearch && pip3 install . && cd ..
  script:
    - python3 dependencyParser.py
  allow_failure: true
```

Don't forget to add the vulnerability stage in stages
```
stages:
  - vulnerability
```
