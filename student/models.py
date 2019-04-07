from django.db import models


# Create your models here.
class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (3, '未知'),
    ]    # for IntergerFiled
    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝')
    ]
    # 一共8个个字段，其中前6个是个人细腻，最后2个是状态相关
    name = models.CharField(max_length=128, verbose_name='姓名')
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name='性别')
    profession = models.CharField(max_length=128, verbose_name='职业')
    email = models.EmailField(verbose_name='Email')    # 有现成的Email字段
    qq = models.CharField(max_length=128, verbose_name='QQ')
    phone = models.CharField(max_length=128, verbose_name='电话')

    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name='审核状态')
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间')

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = '学员信息'  # 定义字段在后台显示的名称