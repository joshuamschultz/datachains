import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Data Science for Supply Chain", # Replace with your own username
    version="0.0.1",
    author="Joshua Schultz",
    author_email="joshua@procurem.io",
    description="A package for working with business data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshuamschultz/datachains",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)