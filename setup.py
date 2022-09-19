from setuptools import setup

setup(
    name="raiderio-async",
    version="1.1.1",
    packages=["raiderio_async"],
    author="karlsbjorn",
    install_requires=["aiohttp", "aiolimiter"],
    python_requires=">=3.8",
)
