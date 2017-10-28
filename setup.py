from setuptools import setup

setup(
    name='garden',
    packages=['garden'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-WTF',
        'Flask_PyMongo',
        'python-dotenv',
        'uWSGI'
    ],
)
