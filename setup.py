#!/usr/bin/env python
from setuptools import setup

setup(
    name='redisbackup',
    version='0.0.0',
    description='Backup Redis RDB.',
    author='Shintaro Maeda',
    author_email='maesin@renjaku.jp',
    url='https://github.com/maesin/redisbackup',
    py_modules=['redisbackup'],
    install_requires=['redis'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    entry_points={
        'console_scripts': [
            'redisbackup = redisbackup:main'
        ]
    }
)
