sample_text = '''___
$ {name} -c --output out main.c -n 10
FOO OK
$ {name} copy -f a.txt
COPY OK
___
from makecli import cli

def foo(args):
    ___
    {name} [OPTIONS] <in-file>             Usage of foo.
    <in-file>              : input file
    -c --compile           : compile
    -o --output <out-file> : output file
    -n <num:n>             : set a number
    -w --warning           : enable warning
    -I --include <path>    : include path
    ___
    print(args)
    print('FOO OK')

def copy(args):
    ___
    {name} copy [OPTIONS] ...              Usage of copy.
    -f <file>              : input file
    ___
    if args['-f'] is False: raise cli.help()
    try:
        cli.copy(open(args['-f']).read())
        print('COPY OK')
    except:
        raise cli.error('-f <file> : file not exist')

def main():
    overview = "This is overview of {name}"
    cli.Cli(overview).add('', foo).add('copy', copy).run()

if __name__ == '__main__':
    main()
'''

setup_text = '''from setuptools import setup, find_packages  # Always prefer setuptools over distutils
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
        name = '{name}',
        version='0.0.1',
        description='',
        long_description='',
        url='',
        author='',
        author_email='',
        license='MIT',
        platforms=['any'],

        classifiers=[
            ],
        keywords='{name}',
        packages = ['{name}'],

        cmdclass={'install': MyInstall},
        entry_points={
            'console_scripts': [
                '{name} = {name}.{name}:main',
                ],
            },
    )
'''
