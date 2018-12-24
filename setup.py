from setuptools import setup

setup(
    name="atcoder-scraper",
    version="1.0.0",
    install_requires=["requests", "beautifulsoup4"],
    extra_require={"develop": ["pylint", "yapf"]},
    entry_points={"console_scripts": ["atcoder-scraper = app:main"]})
