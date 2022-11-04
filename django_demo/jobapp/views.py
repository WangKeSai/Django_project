from django import forms
from django.core.validators import RegexValidator
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from jobapp import models
import base64
from jobapp.utils.md5 import to_md5
from jobapp.utils.code import check_code
from jobapp.utils.random_data import recommend_data, stu_data, random_all
from jobapp.utils.filter import query_for_name
from jobapp.utils.pagiantion import Pagination
from jobapp.utils.bootstrap import BootStrapModelForm
from io import BytesIO


def home(request):
    p_data = recommend_data(4, "Python")
    j_data = recommend_data(4, "Java")
    b_data = recommend_data(4, "大数据")
    s_data = stu_data(5)
    return render(request, 'home.html',
                  {"python_data": p_data, "java_data": j_data, "big_data": b_data, "student_data": s_data})


def regist(request):
    if request.method == "GET":
        return render(request, 'regist.html')
    password = request.POST.get("password")
    username = request.POST.get("username")
    password2 = request.POST.get("password2")
    password_md5 = to_md5(password)
    user_isexit = models.Users.objects.filter(user_name=username)
    if user_isexit:
        res = {"err_str": "用户名已存在！", "status": "1"}
        return JsonResponse(res)
    if len(username) > 11:
        res = {"err_str": "用户名的长度应小于11位！", "status": "1"}
        return JsonResponse(res)
    if len(password) < 6:
        res = {"err_str": "请输入大于等于6位的密码！", "status": "1"}
        return JsonResponse(res)
    if password == password2:
        userModel = models.Users(user_name=username, password=password_md5)
        userModel.save()
        res = {"status": "0"}
        return JsonResponse(res)
    res = {"err_str": "两次密码输入不一样，请重新输入！", "status": "1"}
    return JsonResponse(res)


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    password = request.POST.get("password")
    username = request.POST.get("username")
    code_str = request.POST.get("code")
    user_isexit = models.Users.objects.filter(user_name=username)
    password_md5 = to_md5(password)
    if not username:
        res = {"err_str": '请输入用户名！', "status": "1"}
        return JsonResponse(res)
    if not password:
        res = {"err_str": '请输入密码！', "status": "1"}
        return JsonResponse(res)
    if not code_str:
        res = {"err_str": '请输入验证码！', "status": "1"}
        return JsonResponse(res)
    if request.session.get("image_code") is None:
        res = {"err_str": '验证码超时，请刷新！', "status": "1"}
        return JsonResponse(res)
    if code_str.upper() != request.session.get("image_code").upper():
        res = {"err_str": '验证码错误，请重新输入！', "status": "1"}
        return JsonResponse(res)
    if user_isexit:
        if user_isexit.get(user_name=username).password == password_md5:
            res = {"status": "0"}
            request.session['info'] = {'username': username, "user_id": user_isexit.get(user_name=username).id}
            request.session.set_expiry(60 * 60 * 24 * 2)
            return JsonResponse(res)
        res = {"err_str": '用户名或密码输入错误！', "status": "1"}
        return JsonResponse(res)
    res = {"err_str": '用户名不存在，请注册！', "status": "1"}
    return JsonResponse(res)


def image_code(request):
    img, code_string = check_code()
    stream = BytesIO()
    img.save(stream, "png")
    request.session["image_code"] = code_string
    request.session.set_expiry(60)
    return HttpResponse(stream.getvalue())


def logout(request):
    request.session.clear()
    return redirect(login)


def work_list(request):
    key = []
    val = []
    for k, v in request.GET.items():
        key.append(k)
        val.append(v)
    if key[0] == 'query':
        work_type = '搜索'
    else:
        work_type = val[0].replace(" ", '').title()
    sort_info = "id"
    educa = "edu所有"
    work_year = "wor所有"
    if request.GET.get("sort"):
        sort_info = request.GET.get("sort")
    if request.GET.get("educa"):
        educa = request.GET.get("educa")
        if educa == "高中/中技/中专":
            educa = "高中"
    if request.GET.get("work_year"):
        work_year = request.GET.get("work_year")
        if work_year == "在校生/应届生":
            work_year = "在校生"

    result = query_for_name(key[0], val[0].replace(" ", ''), sort_info, educa, work_year)
    print(result)
    recommen_random = random_all(5)
    page_object = Pagination(request, result)
    content = {"job_list": page_object.page_queryset,
               "work_type": work_type,
               "recommend_random": recommen_random,
               "page_string": page_object.html(),
               "sort_info": sort_info,
               "educa_info":educa,
               "work_info": work_year}
    return render(request, 'works.html', content)


def reset_pw(request):
    if request.method == "GET":
        return render(request, '404.html')

    password = request.POST.get("password")
    new_pwd = request.POST.get("new_pwd")
    new_pwd2 = request.POST.get("new_pwd2")
    if password == '' or new_pwd == '' or new_pwd2 == '':
        res = {"err_str": "请输入密码", "status": "1"}
        return JsonResponse(res)
    username = request.session.get("info").get("username")
    pwd = models.Users.objects.filter(user_name=username).values("password")[0]["password"]
    if pwd != to_md5(password):
        res = {"err_str": "原密码错误，请重新输入！", "status": "1"}
        return JsonResponse(res)
    if len(new_pwd) < 6:
        res = {"err_str": "请输入大于等于6位的密码！", "status": "1"}
        return JsonResponse(res)
    if new_pwd != new_pwd2:
        res = {"err_str": "两次密码输入不一样，请重新输入！", "status": "1"}
        return JsonResponse(res)
    if to_md5(new_pwd) == pwd:
        res = {"err_str": "新密码不能与原密码相同！", "status": "1"}
        return JsonResponse(res)
    models.Users.objects.filter(user_name=username).update(password=to_md5(new_pwd))
    res = {"status": "0"}
    return JsonResponse(res)


class UserInfoModalForm(BootStrapModelForm):
    project_content = forms.CharField(
        min_length=10,
        max_length=440,
        label="项目描述",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "不少于10字"})
    )
    work_content = forms.CharField(
        min_length=10,
        max_length=440,
        label="工作内容",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    evaluation = forms.CharField(
        min_length=10,
        max_length=440,
        label="自我评价",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    phone = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
    )
    email = forms.CharField(
        label="邮箱",
        validators=[RegexValidator(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', '邮箱格式错误'), ],
    )

    gender = forms.ChoiceField(
        label="性别",
        choices=(("男", "男"), ("女", "女"))
    )

    class Meta:
        model = models.UserInfo
        fields = ["name", "age", "gender", "phone", "email", "school", "school_starttime", "school_endtime",
                  "major", "project", "project_starttime", "project_endtime", "project_duty", "project_content",
                  "work", "work_starttime", "work_endtime", "work_duty", "work_content", "evaluation"]


def person_info(request):
    user_obj = models.UserInfo.objects.filter(user_id=request.session.get("info")["user_id"]).first()
    form = UserInfoModalForm()
    if user_obj:
        form = UserInfoModalForm(instance=user_obj)
        img = user_obj.user_img
        base_img = str(base64.b64encode(img), "utf-8")
    else:
        base_img = None
    return render(request, 'person.html', {"form": form, "user_obj": user_obj, "img_64": base_img})


def reset_info(request):
    user_obj = models.UserInfo.objects.filter(user_id=request.session.get("info")["user_id"]).first()
    if user_obj:
        form = UserInfoModalForm(data=request.POST, instance=user_obj)
    else:
        form = UserInfoModalForm(data=request.POST)
    if form.is_valid():
        form.instance.user_id = request.session.get("info")["user_id"]
        form.save()
        return JsonResponse({"status": True})
    else:
        return JsonResponse({"error": form.errors})


def reset_headimg(request):
    files = request.FILES.getlist('files')
    user_obj = models.UserInfo.objects.filter(user_id=request.session.get("info")["user_id"]).first()
    for f in files:
        img = f.read()
        if user_obj:
            user_obj.user_img = img
            user_obj.save()
        else:
            user_obj = models.UserInfo(user_img=img, user_id=request.session.get("info")["user_id"])
            user_obj.save()
    return JsonResponse({"status": True})