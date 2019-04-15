# Chapter 3 第一个例子
## 使用Class-based view
+ View可以是方法，也可以是一个类，如IndexView.as_view()。
+ 1个函数-》1个类+多个方法：在IndexView中定义def get()和def post()以及公用的get_context()，代码变多但实际上get和post功能分开，更清晰。
## 使用自定义middleware
类似装饰器，在请求到最终返回中间插入一些处理。
要重载5个process开头的方法：
```
    def process_request():
    def process_view():
    def process_exception():
    def process_template_response():
    def process_response
```
最后再settings中配置生效。
## 单元测试
1. 测试点
    - 对Models测试
    - 对Views测试（功能）
2. 测试启动命令 
    ```
    python manage.py test
    ```
    or
    ```
    python manage.py test student.tests
    ```
3. tests.py编写
    ```
    from django.test import TestCase, Client
    ```
    继承TestCase, 3个常用方法:
    ```
       def setUp(self)
       def test_xxxx(self)
       def tearDown(seff)
    ```
    2个验证方法:
    
    ```
    self.assertEqual()
    self.assertTrue()
    ```
# Chapter  编码规范
## Python规范（pep8）
1. 缩进
    1. 垂直对齐
        ```python
        foo = long_function_name(var_one, var_two,
                                var_three, var_four)
       ```
    2. 悬挂对齐
        ```python
        foo = long_function_name(
            var_one, var_two, var_three,
            var_four)
        ```
        或者
        ```python
        foo = long_function_name(
            var_one, var_two, var_three,
            var_four)
        ```
2. Tab和Space不要混用（python3不允许python2允许）
3. 从一个model中import很多东西：
    ```python
    from xx_model import(
       a,b,c,
       d,e,f,
    )
    ```
4. import独立一行
    ```python
    import sys
    import os
    ```
5. 分组引用，组与组之间空行分割
    ```python
    import time
    from datetime import datetime
    from os import path

    import django
    from django.conf import settings

    from blog.models import Post
    ```
6. 推荐绝对路径引用，易于排查错误；绝对引用过长，明确的相对引用也可。
7. 一般禁止from xx import *，但__init__是常见的例外，需要引入当前包下所有模块需要对外暴露的接口。
8. dunder双下划线变量的位置：docstring之后，其他import之前，from __future__ import除外：
    ```python
    """This is the example module.
    This module does stuff.
    """
    from __future__ import barry_as_FLUFL

    __all__ = ['a', 'b', 'c']
    __version__ = '0.1'
    __author__ = 'Grace'
    
    improt os
    import sys
    ```