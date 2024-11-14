from setuptools import setup, find_packages

# Safely read README.md
long_description = ""
try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A Python Selenium framework for automation."

setup(
    name="webserpent",
    version="0.1.0",
    author="Joshua Bowery",
    author_email="joshua@example.com",  # Add your email here for contact
    description="A Python Selenium framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jcbowery/web_serpent",
    packages=find_packages(),  # Automatically finds all packages and subpackages
    install_requires=[
        "selenium>=4.26.1,<=5.0.0"
    ],
    python_requires=">=3.12",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
)
