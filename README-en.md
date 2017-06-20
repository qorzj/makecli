# Install
`pip install makecli`

# How to use makecli
```
$ makecli -h                                                                                                     [master] 21:47:02
OVERVIEW
  Tookit for generating command line interfaces

USAGE
  makecli create <name>       : Create template of CLI tool
    <name> : tool name

  makecli install <name>      : Install CLI tool
    <name> : tool name

  makecli uninstall <name>    : Uninstall CLI tool
    <name> : tool name

  makecli submit              : Submit your tool to pypi.python.org

  -h --help : for more information on a command.

```

# How to create CLI tool
1. Create template of mytool
```
$ makecli create mytool                                                                                                           21:52:37
-- OK --
please edit mytool/mytool/run.py for your need

```

2. Edit mytool/mytool/run.py
3. There are three ways to run mytool
    * `makecli install mytool; mytool -h`
    * `python mytool/mytool/run.py -h`
    * `cd mytool; python -m mytool.run -h`

# Uninstall CLI tool
`makecli uninstall mytool`

# Submit your tool to pypi.python.org  

```
$ makecli submit
Please edit your own ~/.pypirc and setup.py, and then run this command below:
  cd <name>; python setup.py sdist register upload
```

Steps of submit your tool to PyPI:
 1. register on https://pypi.python.org/ and https://testpypi.python.org/
 2. edit `~/.pypirc`
 3. edit `<name>/setup.py`
 4. run `cd <name>; python setup.py sdist register upload`

### Example of ~/.pypirc
```
[distutils]
index-servers =
    pypi
    test

[pypi]
username:{username}
password:{password}

[test]
repository:https://testpypi.python.org/pypi
username:{username}
password:{password}
```
