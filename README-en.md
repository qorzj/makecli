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
please edit mytool/mytool/mytool.py for your need

```

2. Edit mytool/mytool/mytool.py
3. There are three ways to run mytool
    * `makecli install mytool; mytool -h`
    * `python mytool/mytool/mytool.py -h`
    * `cd mytool; python -m mytool.mytool -h`

# Uninstall CLI tool
`makecli uninstall mytool`

# Submit your tool to pypi.python.org  

```
$ makecli submit
Please edit your own ~/.pypirc, and then run this command below:
  python setup.py sdist register upload
```

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
