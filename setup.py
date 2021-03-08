from setuptools import setup, find_packages

setup(name="monopoly", packages=find_packages())

setup(
    name="monopoly",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        monopoly=cli:monopoly
    """,
)