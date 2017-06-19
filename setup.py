from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path
import subprocess
from setuptools.command.install import install

here = path.abspath(path.dirname(__file__))

class MyInstall(install):
    def run(self):
        print("------")
        install.run(self)

setup(
        name = 'makecli',
        version='0.0.1',
        description='Tookit for generating command line interfaces',
        long_description='Tookit for generating command line interfaces',
        url='',
        author='',
        author_email='',
        license='MIT',
        platforms=['any'],

        classifiers=[
            ],
        keywords='makecli cli',
        packages = ['makecli'],

        cmdclass={'install': MyInstall},
        entry_points={
            'console_scripts': [
                'makecli = makecli.makecli:main',
                ],
            },
    )

