from setuptools import setup, find_packages

def long_description():
    with open("README.md", "r") as f:
        return f.read()

setup (
    name="Flask & OpenAPI Backend",
    version="0.0.1",
    description="Flask OpenAPI Backend",
    author_email="simon@torrentofshame.com",
    url="",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["server=server.__main__:main"]
    },
    long_description=long_description()
)
