from django import forms
from .models import UserInfo
import hashlib

class UserRegisterForm(forms.ModelForm):
    upassword = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20)
    upasswordConfirm = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20)
    uname = forms.CharField(min_length=5, max_length=20)
    uemail = forms.EmailField()

    class Meta:
        model = UserInfo
        fields = ('uname','upassword','uemail')

    def clean_upasswordConfirm(self):
        pwd1 = self.cleaned_data['upassword']
        pwd2 = self.cleaned_data['upasswordConfirm']
        if pwd1 == pwd2:
            return pwd1
        else:
            raise forms.ValidationError('两次密码输入不一致', code='两次密码输入不一致')

    # 自定义加密算法
    def doPwd(self):
        password = self.cleaned_data['upassword']
        sha = hashlib.sha1()
        sha.update(password.encode('utf8'))
        pwd = sha.hexdigest()
        return pwd
