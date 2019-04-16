# Chapter3 第一个例子
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
# Chapter4 编码规范
## Python规范（pep8）
参考：[google Python规范](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#indentation)
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
## Django编码规范
参考：[Django官方编码规范](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
1. 引用顺序
    ```python
    # future
    from __future__ import unicode_literals
    
    # standard library
    import json
    from itertools import chain
    
    # third-party
    import bcrypt
    
    # Django
    from django.http import Http404
    from django.http.response import (
        Http404, HttpResponse, HttpResponseNotAllowed, StreamingHttpResponse,
        cookie,
    )
    
    # local Django
    from .models import LogEntry
    
    # try/except
    try:
        import yaml
    except ImportError:
        yaml = None
    
    CONSTANT = 'foo'
    
    
    class Example:
        # ...
    ```
2. Model中的规范
    + 注意空格、小写下划线命名、字段之后再class Meta的顺序:
    ```python
    class Person(models.Model):
       first_name = models.CharField(max_length=20)
       last_name = models.CharField(max_length=40)

       class Meta:
           verbose_name_plural = 'people'
    ```
    + 应当遵循的顺序:
    ```python
    All database fields
    Custom manager attributes
    class Meta
    def __str__()
    def save()
    def get_absolute_url()
    Any custom methods
    ```
3. 使用更方便的引用，如：
    ```from django.views import View```
    而不是
    ```from django.views.generic.base import View```
    。
    
    （django.views是一个文件夹，__init__.py中引入了django.views.generic.base:
    ```python
    from django.views.generic.base import View

    __all__ = ['View']
    ```
     参考:[](https://github.com/django/django/blob/master/django/views/__init__.py)
4. Django Settings相关
    + [Django Settings官方](https://docs.djangoproject.com/en/2.1/topics/settings/)
    + [编码风格](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
    1. 为了指定用哪个settings文件 -》指定环境变量DJANGO_SETTINGS_MODULE的值为mysite.settings
        ```python
        import os   
        os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
        ```
        或者
        ```python
        export DJANGO_SETTINGS_MODULE=mysite.settings
        django-admin runserver
    
        ```
        用python manage.py是自动帮你找到settings，不用显式指定
    
    2. 如果没有显式指定，则用默认的 global_settings.py；否则先加载 global_settings.py，再按指定修改。
        查看有哪些修改 -》 python manage.py diffsettings
    3. 在app里面，如果需要读取settings的值来判断状态：
        ```python
           from django.conf import settings

           if settings.DEBUG:
                # Do something
        ```
    4. DJANGO_SETTINGS_MODULE 和 django.conf.settings.configure()二选一
    5. 使用单独的文件，必须有django.setup()
        ```python
        import django
        from django.conf import settings
        from myapp import myapp_defaults
        
        settings.configure(default_settings=myapp_defaults, DEBUG=True)
        django.setup()
        
        # Now this script or any imported module can use any part of Django it needs.
        from myapp import models
                ```
    
    6. 仅引入还不行，要settings.configure()才生效。
        ```python
        from django.conf import settings
        settings.configure({}, SOME_SETTING='foo')
        ```
 ## 项目结构与拆分
 1. 项目名称和源码名称一致
 2. 一个通用python项目结构：
    + LICENSE
    + MANIFEST.in
    + README.md
    + conf/
    + fabfile/
    + others/
    + requirements.txt
    + setup.py
    + src/
 3. 一个Django项目也应该拆分，settings、urls拆分、views都要拆分……
    如settings.py拆分为一个文件夹settings，包含：
    + __init__.py
    + base.py
    + develop.py
    + product.py
    
    随后修改manage.py和wsgi.py文件
 ## Git协作
1. ~/.gitconfig & .git/config
2. git rebase -i HEAD~3   
 