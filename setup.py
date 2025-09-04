from setuptools import setup, find_packages

setup(
    name="sample_ptc",          # package name
    version="0.1.6",           # version
    author="Your Name",
    author_email="you@example.com",
    description="A sample Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypackage",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests",  # dependencies
    ],
)
