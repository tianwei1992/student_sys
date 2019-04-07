from django import forms

from .models import Student


# form可以不急于model，一个一个重新定义，但基于现成的model会更方便
class StudentForm(forms.ModelForm):
    def clean_qq(self):
        # 针对qq号输入进行过滤，要求必须是数字，否则报错
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError("必须是数字!")
        return int(cleaned_data)

    class Meta:
        model = Student
        # Model Student里面包含8个字段，form只取其中6个
        fields = ('name', 'sex', 'profession', 'email', 'qq', 'phone')