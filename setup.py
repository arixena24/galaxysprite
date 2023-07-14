from setuptools import setup, find_packages, Extension

import numpy, sys
import re


# auto-updating version code stolen from RadVel
def get_property(prop, project):
    result = re.search(
        r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop),
        open(project + "/__init__.py").read(),
    )
    return result.group(1)

def get_requires():
    reqs = []
    for line in open("requirements.txt", "r").readlines():
        reqs.append(line)
    return reqs



setup(
    name="galaxysprite",
    version=get_property("__version__", "galaxysprite"),
    description="galaxysprite: make gifs!",
    url="https://github.com/arixena24/galaxysprite",
    author="Ariel Elizabeth Eunhee",
    author_email="",
    license=" ",
    packages=find_packages(),
    install_requires=get_requires(),
    include_package_data=True
)

