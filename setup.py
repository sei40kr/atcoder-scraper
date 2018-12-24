from setuptools import setup

setup(
    install_requires=["requests", "beautifulsoup4"],
    entry_points={"console_scripts": ["atcoder-scraper = app:main"]})
