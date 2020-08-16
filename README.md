# pytest-chinese-doc
`pytest`[官方文档（5.1.3版本）](https://docs.pytest.org/en/5.1.3/contents.html)的中文翻译，但不仅仅是简单的翻译：

- 更多的例子，尽量做到每一知识点都有例子；
- 更多的拓展阅读，部分章节添加了作者学习时，所查阅的资料；

所以这也是作者自身学习`pytest`的历程，希望能有更多的人了解这款优秀的测试框架；


# 环境

- `pytest`版本：5.1.3
- `python`版本：3.7.3


# 使用
1. clone本仓库到本地
    ```bash
    git clone https://github.com/passerby223/pytest-chinese-doc.git
    ```
2. 目录说明
    ```bash
    `docs/`目录下包含所有的文章，以[markdown](https://daringfireball.net/projects/markdown/)格式编写
    `src/`目录下包含所有的示例源码，以章节划分
    ```
3. 运行项目,进入项目的根目录下,执行以下命令
    ```bash
    # 创建虚拟环境
    $ python3 -m venv venv-5.1.3
    # 激活虚拟环境，不同的操作系统命令可能不一样
    $ source .venv-5.1.3/bin/activate
    # 安装依赖
    $ pip install -i https://pypi.douban.com/simple -r requirements.txt
    # 查看当前pytest的版本
    $ pytest --version
    ```

# 目录

- [1-安装和入门](docs/1-安装和入门.md)
- [2-使用和调用](docs/2-使用和调用.md)
- [3-编写断言](docs/3-编写断言.md)
- [4-fixtures：明确的-模块化的和可扩展的](docs/4-fixtures：明确的-模块化的和可扩展的.md)
- [5-猴子补丁](docs/5-猴子补丁.md)
- [6-临时目录和文件](docs/6-临时目录和文件.md)
- [7-捕获标准输出和标准错误输出](docs/7-捕获标准输出和标准错误输出.md)
- [8-捕获告警信息](docs/8-捕获告警信息.md)
- [9-集成文档测试](docs/9-集成文档测试.md)
- [10-skip和xfail标记](docs/10-skip和xfail标记.md)
- [11-测试的参数化](docs/11-测试的参数化.md)
- [12-缓存：记录执行的状态](docs/12-缓存：记录执行的状态.md)
