# Fallowing command is used to upload to pipy
#    python setup.py register sdist upload
# Always prefer setuptools over distutils
from os import path
import pathlib

from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="pythontemplate",
    description="",
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version="0.0.0",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/{{githublogin}}/pythontemplate",
    author="{{name_and_surname}}",
    author_email="{{email}}",
    license="MIT",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.6",
    ],
    # What does your project relate to?
    keywords="",
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=["dist", "docs", "tests*", "devel*", "examples"]),
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
    install_requires=[
        # 'numpy', 'conda'
    ],
    # 'SimpleITK'],  # Removed becaouse of errors when pip is installing
    dependency_links=[],
    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        # "sample1": ["scaffan_icon256.png"],
        # "": ["*.png", "*.ico", "*.joblib", "*.pkl", "*.model",
        # "*.h5"
        # ],
        # "sample2": ["scaffan/scaffan_icon256.png"],
        # "sni_per-pixel_not_working": ["scaffan/SNI_per-pixel_regressor.joblib"],
    },
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages.
    # see
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
