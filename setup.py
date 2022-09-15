from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name="dester",
    description="a test cli",
    author="Krystyna Kalinchuk",
    author_email="christinakalinchuk@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["click==8.1.3"],
    entry_points="""
    [console_scripts]
    dester-linter=dester:main
    """
)