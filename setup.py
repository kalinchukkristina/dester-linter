"""
creates a cli tool dester
"""
from setuptools import setup, find_packages

setup(
    name="dester",
    version="1.0.0",
    description="a test cli",
    author="Krystyna Kalinchuk",
    author_email="christinakalinchuk@gmail.com",
    packages=find_packages(),
    install_requires=["click==8.1.3"],
    entry_points="""
    [console_scripts]
    dester-linter=dester:main
    """
)
