from django.test import TestCase, Client

from .models import Student


# Create your tests here.
class StudentTestCse(TestCase):
    def SetUp(self):
        Student.objects.create(
            name='stu1',
            sex=2,
            profession='teacher',
            email='stu1@qq.com',
            qq='12345',
            phone='9090950',
        )

    """以下case测试models"""
    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='stu2',
            sex=1,
            profession='programmer',
            email='stu2@qq.com',
            qq='123456',
            phone='9090950',
        )
        self.assertEqual(student.sex_show, '男', '性别展示不符合预期')

    def test_filter(self):
        student = Student.objects.create(
            name='stu2',
            sex=1,
            profession='programmer',
            email='stu2@qq.com',
            qq='123456',
            phone='9090950',
        )
        name = 'stu2'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{}的记录'.format(name))

    """以下case测试views"""
    def test_get_index(self):
        client = Client()
        res = client.get('/')
        self.assertEqual(res.status_code, 200, 'status code must be 200')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='stu3@qq.com',
            profession='teacher',
            qq='123',
            phone='12335'
        )
        # 既验证返回status code还验证内容结果
        res = client.post('/', data)
        self.assertEqual(res.status_code, 302, 'status code must be 302')

        res = client.get('/')
        self.assertTrue(b'test_for_post' in res.content, 'response content must contain "test_for_post"')