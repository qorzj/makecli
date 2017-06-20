#coding: utf-8
import os

from makecli import cli, template


def create(args):
    '''
    makecli create <name>       : Create template of CLI tool
    <name> : tool name
    '''
    if not args['<name>']: raise cli.help()
    name = args['<name>']
    os.mkdir(name)
    os.mkdir('{name}/{name}'.format(name=name))
    with open(name + '/__init__.py', 'w') as f:
        f.write('')
    with open(name + '/setup.py', 'w') as f:
        f.write(template.setup_text.replace('{name}', name))
    with open('{name}/{name}/run.py'.format(name=name), 'w') as f:
        tpl = template.sample_text.replace('{name}', name).replace('___', '\'\'\'')
        f.write(tpl)
    print('-- OK --')
    print('please edit {name}/{name}/{name}.py for your need\n'.format(name=name))


def install(args):
    '''
    makecli install <name>      : Install CLI tool
    <name> : tool name
    '''
    if not args['<name>']: raise cli.help()
    name = args['<name>']
    cmd = 'cd {}; python setup.py install'.format(name)
    print(cmd)
    os.system(cmd)


def uninstall(args):
    '''
    makecli uninstall <name>    : Uninstall CLI tool
    <name> : tool name
    '''
    if not args['<name>']: raise cli.help()
    name = args['<name>']
    cmd = 'pip uninstall ' + name
    print(cmd)
    os.system(cmd)


def submit(args):
    '''
    makecli submit              : Submit your tool to pypi.python.org
    '''
    text = 'Please edit your own ~/.pypirc, and then run this command below:\n  python setup.py sdist register upload\n'
    print(text)


def main():
    overview = "Tookit for generating command line interfaces"
    app = cli.Cli(overview)
    app.add("create", create)
    app.add("install", install)
    app.add("uninstall", uninstall)
    app.add("submit", submit)
    app.run()
