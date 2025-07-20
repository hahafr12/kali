# setup.py

from setuptools import setup, find_packages

setup(
    name='kali',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pyfiglet',
        'termcolor'
    ],
    entry_points={
        'console_scripts': [
            'kali = kali.terminal:main'
        ]
    },
    author='Muhammet Can Altan',
    description='Kali Linux terminal benzeri bir Python simülasyonu',
    keywords='kali linux terminal simulator ethical hacking',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
)
