from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='my-first-python-library',
    version='0.0.2',
    author="Divyesh Vaghani",
    author_email="divyeshvaghani96@gmail.com",
    description="Sample code to create python package for PyPI library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/divyeshvaghani",
    license="MIT",
    packages=['my-first-python-library'],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
