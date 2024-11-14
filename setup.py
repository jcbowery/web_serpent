from setuptools import setup, find_packages

setup(
    name="webserpent",
    version="0.1.0",
    author="Joshua Bowery",
    description="A python selenium framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jcbowery/web_serpent",
    packages=find_packages(),  # Automatically finds all packages and subpackages
    install_requires=[
        "selenium==4.26.1"
    ],
    python_requires=">=3.12",
)
