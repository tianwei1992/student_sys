from django.test import TestCase

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
