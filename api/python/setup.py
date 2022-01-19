from setuptools import setup
import os


setup(
    name='spylizard',
    maintainer="spylizard Developers",
    maintainer_email="example@python.org",
    description="PEP 561 type stubs for spylizard",
    version='1.0',
    packages=['spylizard'],
    package_dir={'spylizard':'./package'},
    include_package_data = True,
    package_data={"": ["stubs/__init__.pyi", "spylizard.so", "__init__.py"]},
)