#!/usr/bin/env python

from setuptools import setup

name = "acronym-bot"
version = "0.1"

setup(
    name=name,
    version=version,
    description="A Slack Bot to expand CTDS acronyms",
    license="GPLv3",
    url="https://github.com/uc-cdis/acronym-bot",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GPLv3 License",
    ],
    py_modules=["acronymbot"],
    install_requires=[
        "requests==2.22.0",
        "SlackClient==2.2.1"
    ],
    extras_require={},
    entry_points={"console_scripts": ["acronymbot = acronymbot:main"]},
    setup_requires=[],
)
