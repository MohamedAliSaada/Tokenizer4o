from setuptools import setup, find_packages

setup(
    name="tokenizer4o",
    version="1.0.0",
    packages=find_packages(),
    install_requires=['regex>=2023.10.3'],
    python_requires='>=3.8',
)
