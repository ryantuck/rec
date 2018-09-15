from setuptools import setup, find_packages

setup(
    name='rec',
    version='0.0.0.1',
    install_requires=[
        'click',
        'petl',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rec = rec.cli:cli',
        ],
    },
)
