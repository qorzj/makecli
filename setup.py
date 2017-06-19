from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path
import subprocess
from setuptools.command.install import install

here = path.abspath(path.dirname(__file__))

class MyInstall(install):
    def run(self):
        print("-- installing... (powered by makecli) --")
        install.run(self)

setup(
        name = 'makecli',
        version='0.0.2',
        description='Tookit for generating command line interfaces',
        long_description='Tookit for generating command line interfaces',
        url='https://github.com/qorzj/makecli',
        author='qorzj',
        author_email='inull@qq.com',
        license='MIT',
        platforms=['any'],

        classifiers=[
            ],
        keywords='makecli cli fire',
        packages = ['makecli'],

        cmdclass={'install': MyInstall},
        entry_points={
            'console_scripts': [
                'makecli = makecli.makecli:main',
                ],
            },
    )

