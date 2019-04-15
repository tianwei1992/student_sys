# 使用Class-based view
+ View可以是方法，也可以是一个类，如IndexView.as_view()。
+ 1个函数-》1个类+多个方法：在IndexView中定义def get()和def post()以及公用的get_context()，代码变多但实际上get和post功能分开，更清晰。
# 使用自定义middleware
类似装饰器，在请求到最终返回中间插入一些处理。
要重载5个process开头的方法：
```python
    def process_request():
    def process_view():
    def process_exception():
    def process_template_response():
    def process_response
```
最后再settings中配置生效。

# 单元测试
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
