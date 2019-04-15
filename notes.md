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
