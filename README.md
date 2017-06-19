# [** English Version **](https://github.com/qorzj/makecli/blob/master/README-en.md)

# 简介
makecli可以帮你轻松地编写命令行工具，除了`makecli -h`这个命令以外不需要任何记忆。你唯一需要做的，就是生成代码模板，在模板的基础上进行修改。修改后的工具能轻松地安装和卸载，还能提交到pypi上供所有人使用。而这一切都不需要你去**记**任何规则！

# 安装
运行命令：`pip install makecli`

# 怎样使用makecli
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

# 怎样创建命令行工具
1. 假设你的命令行工具取名叫mytool，首先要创建一个mytool的模板：
```
$ makecli create mytool                                                                                                           21:52:37
-- OK --
please edit mytool/mytool/mytool.py for your need

```

2. 按照提示修改 mytool/mytool/mytool.py
3. 有三种方法可以执行mytool：
    * 安装mytool并执行：`makecli install mytool; mytool -h`
    * 直接运行python脚本：`python mytool/mytool/mytool.py -h`
    * 用加载模块的方式执行：`cd mytool; python -m mytool.mytool -h`

# 卸载命令行工具
`makecli uninstall mytool`

# 把你的工具提交到 pypi.python.org  

```
$ makecli submit
Please edit your own ~/.pypirc, and then run this command below:
  python setup.py sdist register upload
```

### ~/.pypirc的例子
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
