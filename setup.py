from setuptools import setup

setup(
    name="raiderio-async",
    version="1.2.0",
    packages=["raiderio_async"],
    author="karlsbjorn",
    install_requires=["aiohttp-client-cache==0.7.3", "aiosqlite~=0.17.0", "aiolimiter~=1.0.0"],
    python_requires=">=3.8",
)
