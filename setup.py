from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='app-graphs',
    version='0.0.1',
    description='Draws graphs.',
    py_modules=["app-graphs"],
    package_dir={'': 'src'},
    classifiers=[
        "Programing Language :: Python :: 3",
        "Programing Language :: Python :: 3.6",
        "Programing Language :: Python :: 3.7",
        "Programing Language :: Python :: 3.8",
        "Programing Language :: Python :: 3.9",
        "Programing Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "pandas >= 1.4.0",
        "ogdf-python >= 0.1.2.dev0"
    ],
    url="https://github.com/skorjanc/app-graphs",
    author="Blaž Škorjanc",
    author_email="skorjanc.blazy@gmail.com",
)
