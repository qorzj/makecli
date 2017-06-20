# [** English Version **](https://github.com/qorzj/makecli/blob/master/README-en.md)

# 简介
makecli可以帮你轻松地编写命令行工具，除了`makecli -h`这个命令以外不需要任何记忆。你唯一需要做的，就是生成代码模板，再在模板的基础上进行修改。修改后的工具能轻松地安装和卸载，还能提交到pypi上供所有人使用。而这一切都不需要你去**记**任何规则！

# 安装
运行命令：`pip install makecli`  
如果本地有多个版本的python，建议运行：`python -m pip install makecli`  

注意虽然makecli同时支持python2和3，但不要用`pip3`或`python3 -m pip`进行安装，否则无法执行`makecli install`和`makecli uninstall`。如果想安装到python3环境建议用virtualenv。

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
    * 直接运行python脚本：`python mytool/mytool/run.py -h`
    * 用加载模块的方式执行：`cd mytool; python -m mytool.run -h`

# 卸载命令行工具
`makecli uninstall mytool`

# 把你的工具提交到 pypi.python.org  

```
$ makecli submit
Please edit your own ~/.pypirc, and then run this command below:
  cd <name>; python setup.py sdist register upload
```
请先在 https://pypi.python.org/ 和 https://testpypi.python.org/ 上注册账号，然后按照下面例子新建`~/.pypirc`文件。提交前还要修改`setup.py`，修改工具的描述、网址、依赖包等信息，一切就绪后敲入`makecli submit`提示的命令，就可以把你的工具提交到PyPI了。任何人只要用`pip install mytool`命令就可以安装你提交的工具。

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

参考文章：[Uploading to PyPI](https://tom-christie.github.io/articles/pypi/)
