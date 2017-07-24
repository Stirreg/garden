from setuptools import setup

setup(
    name='garden',
    packages=['garden'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_pymongo',
        'flask_wtf'
    ],
)