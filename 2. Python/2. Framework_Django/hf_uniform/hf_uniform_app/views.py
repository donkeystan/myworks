from django.shortcuts import render, redirect
from hf_uniform_app.models import perm, Uniform
from django.http import HttpResponse
from hf_uniform_app.forms import PostForm
import datetime
from datetime import datetime, date
from hf_uniform_app.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.contrib import auth
from django.contrib.auth import authenticate
import os

####################################################################################################
# < ----- Log in/Log Out -----> 
def index(request):
    if (request.user.is_authenticated):
        username = request.user.username
    return render(request, 'index.html', locals())

def logout(request):
    log_content = f'USER ID:[ {request.user.id} ], USER:[ {request.user.username} ], Time:[ {get_time_stamp()} ], Log out'
    get_log(log_content)
    auth.logout(request)
    return redirect('/login/')

def login(request):
    if (request.user.id != None):
        return redirect('/main/')
    
    message = '尚未登入'
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if (user != None):
            if (user.is_active):
                auth.login(request, user)
                log_content = f'USER ID:[ {request.user.id} ], USER:[ {request.user.username} ], Time:[ {get_time_stamp()} ], Log in'
                get_log(log_content)
                return redirect('/main/')
            else:
                message = '無此帳號！'
        else:
            message = '帳號密碼錯誤，登入失敗！'
    
    return render(request, 'login.html', locals())

####################################################################################################
# < ----- Side Functions -----> 

def get_log(log_content):
    print('Log Added ---> ' + log_content)
    with open('Log.txt', 'a') as file:
        file.write(log_content + '\n')

def get_time_stamp():
    today = date.today()
    now = datetime.now().time()
    today = list(str(today))
    now = list(str(now))
    for i in range(len(now)):
        if ( '.' == now[i] or ':'== now[i] ):
            now[i] = '_'
    for j in range(len(today)):
        if ( '-' == today[j]):
            today[j] ='_'
    date_stamp = ''.join(today)
    time_stamp = ''.join(now)
    stamp = date_stamp + '_(' + time_stamp[0:8] +')'
    return stamp

####################################################################################################
# < ----- Query Section -----> 

def assertDate(date_string:str):
    date_format = '%Y-%m-%d'
    try:
        date_string = datetime.strptime(date_string, date_format)
        print(f'Correct Date Value Parsed ---> {date_string}')
        return date_string
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        return ''

def get_query_set(uniforms, cust_name:str, orgnization_name:str, date_of_created:str, message:str):
    if (cust_name != ''):
        # uniforms = uniforms.filter(CustName = cust_name).order_by('-DateOfCreated')
        uniforms = uniforms.filter(CustName__contains = cust_name ).order_by('-DateOfCreated')
    if (orgnization_name != ''):
        uniforms = uniforms.filter(OrgnizationName__contains = orgnization_name).order_by('-DateOfCreated')          
    if (date_of_created != ''):
        date_of_created = assertDate(date_of_created)
        if (date_of_created == ''):
            message = '日期格式錯誤'
        else :
            uniforms = uniforms.filter(DateOfCreated = date_of_created).order_by('-DateOfCreated')        
    context = {'uniforms':uniforms, 'cust_name':cust_name, 'orgnization_name':orgnization_name, 'date_of_created':date_of_created, 'message':message}
    return context

def query(request):
    if (request.user.id == None):
        return redirect('/login/')

    today = date.today()
    uniforms = Uniform.objects.filter(DateOfCreated = today).order_by('-DateOfCreated')
    message = '無系統訊息'

    if (request.method == "POST"):
        uniforms = Uniform.objects.all().order_by('-DateOfCreated')
        message = '系統接收過濾標準 [最多顯示200筆]'
        cust_name = request.POST['cust_name']
        orgnization_name = request.POST['orgnization_name']
        date_of_created = request.POST['date_of_created']
        context = get_query_set(uniforms, cust_name, orgnization_name, date_of_created, message)
        return render(request, 'query.html', context)

    context = {'uniforms':uniforms, 'cust_name':'尚未輸入', 'orgnization_name':'尚未輸入', 'date_of_created':'尚未輸入', 'message':message}
    return render(request, 'query.html', context)


####################################################################################################
# < ----- Edit Handeling ----- >

def edit_save_uniform_object(request, uniform):
    uniform.CustName = request.POST['cust_name']
    uniform.CustNo = request.POST['cust_no']
    uniform.OrgnizationName = request.POST['orgnization_name']
    uniform.Gender = request.POST['gender']
    uniform.CustPhone = request.POST['cust_phone']
    uniform.CustEmail = request.POST['cust_email']
    uniform.CustAddr = request.POST['cust_addr']
    uniform.Hat = request.POST['hat']
    uniform.ShoulderWidth = request.POST['shoulder_width']
    uniform.SleeveLength = request.POST['sleeve_length']
    uniform.BackLength = request.POST['back_length']
    uniform.CenterBack = request.POST['center_back']
    uniform.ShirtLength = request.POST['shirt_length']
    uniform.Collar = request.POST['collar']
    uniform.Chest = request.POST['chest']
    uniform.Waist = request.POST['waist']
    uniform.Seat = request.POST['seat']
    uniform.WaistBelt = request.POST['waist_belt']
    uniform.Hip = request.POST['hip']
    uniform.Crotch = request.POST['crotch']
    uniform.FrontCrotch = request.POST['front_crotch']
    uniform.Thigh = request.POST['thigh']
    uniform.PantsLength = request.POST['pants_length']
    uniform.SkirtLength = request.POST['skirt_length']
    uniform.Remark = request.POST['remark']
    print(f'Uniform Object Created ---> id:{uniform.id} : name {uniform.CustName}---> {type(uniform)}')
    uniform.save()
    return uniform

def edit_from_detail(request, uniform_id=None, mode=None):
    if (request.user.id == None):
        return redirect('/login/')

    if (mode == "save"):
        uniform = Uniform.objects.get(id=uniform_id)
        uniform = edit_save_uniform_object(request, uniform)
        if (uniform.CustName == ''):
            message = '姓名不得空白!'        
            context = {'uniform':uniform, 'message':message}
            return render(request, 'edit_from_detail.html', context)
        uniform.save()
        log_content = f'USER ID:[ {request.user.id} ], USER:[ {request.user.username} ], Time:[ {get_time_stamp()} ], Edit:[ {uniform.CustName} ]'
        get_log(log_content)
        path = '/detail/' + str(uniform_id) + '/'
        return redirect(path)
    else:
        try:
            uniform = Uniform.objects.get(id=uniform_id)
            message = '請輸入欲修改之資料！'
        except:
            message = "資料不存在！"
            return render(request, 'query.html', locals())
        context = {'uniform':uniform, 'message':message}
        return render(request, 'edit_from_detail.html', context)

def edit_from_multi_input(request, uniform_id=None, mode=None):
    if (request.user.id == None):
        return redirect('/login/')

    if (mode == "save"):
        uniform = Uniform.objects.get(id=uniform_id)
        uniform = edit_save_uniform_object(request, uniform)
        if (uniform.CustName == ''):
            message = '姓名不得空白!'        
            context = {'uniform':uniform, 'message':message}
            return render(request, 'edit_from_multi_input.html', context)
        uniform.save()
        log_content = f'USER ID:[ {request.user.id} ], USER:[ {request.user.username} ], Time:[ {get_time_stamp()} ], Edit:[ {uniform.CustName} ]'
        get_log(log_content)
        path = '/multi_input/' + str(uniform.OrgnizationName) + '/'
        return redirect(path)
    else:
        try:
            uniform = Uniform.objects.get(id=uniform_id)
            message = '請輸入欲修改之資料！'
        except:
            message = "資料不存在！"
            return render(request, 'query.html', locals())
            
        context = {'uniform':uniform, 'message':message}
        return render(request, 'edit_from_multi_input.html', context)

'''
Required section
CustName cust_name
Gender - radio checked default M

'''

####################################################################################################
# < ----- Detail Handeling ----- >

def detail(request, uniform_id=None):
    if (request.user.id == None):
        return redirect('/login/')

    uniform = Uniform.objects.get(id=uniform_id)
    return render(request, "detail.html", locals())

####################################################################################################
# < ----- Delete Section -----> 

def delete_in_query(request, uniform_id=None):
    if (request.user.id == None):
        return redirect('/login/')

    if (uniform_id != None):
        if (request.method == "POST"):
            uniform_id = request.POST['uniform_id']
        try:
            uniform = Uniform.objects.get(id=uniform_id)
            log_content = f'USER ID:[ {request.user.id} ], USER:[ {request.user.username} ], Time:[ {get_time_stamp()} ], Delete:[ {uniform.CustName}]'
            get_log(log_content)
            uniform.delete()
            return redirect('/query')
        except:
            message = "讀取錯誤!"
    return render(request, "delete_in_query.html", locals())

def delete_return_query(request, uniform_id=None):
    if (request.user.id == None):
        return redirect('/login/')

    if (uniform_id != None):
        uniform = Uniform.objects.get(id=uniform_id)
        return render(request, 'delete_return_query.html', locals())

def delete_in_multi_input(request, uniform_id=None):
    if (request.user.id == None):
        return redirect('/login/')

    if (uniform_id != None):
        if (request.method == "POST"):
            uniform_id = request.POST['uniform_id']
        try:
            uniform = Uniform.objects.get(id=uniform_id)
            organization_name = uniform.OrgnizationName
            path = '/multi_input/' + organization_name
            print(f'organization_name ---> {path}')
            log_content = f'USER ID:[ {request.user.id} ], USER:[ {request.user.username} ], Time:[ {get_time_stamp()} ], Delete:[ {uniform.CustName} ]'
            get_log(log_content)
            uniform.delete()
            return redirect(path)
        except:
            message = "讀取錯誤!"
    return render(request, "delete_in_multi_input.html", locals())

def delete_return_multi_input(request, uniform_id=None):
    if (request.user.id == None):
        return redirect('/login/')

    if (uniform_id != None):
        uniform = Uniform.objects.get(id=uniform_id)
        return render(request, 'delete_return_multi_input.html', locals())

####################################################################################################
# < ----- Data Input ----->

def save_uniform_object(uniform_form):
    cust_name = uniform_form.cleaned_data['cust_name']
    cust_no = uniform_form.cleaned_data['cust_no']
    orgnization_name = uniform_form.cleaned_data['orgnization_name']
    gender = uniform_form.cleaned_data['gender']
    cust_phone = uniform_form.cleaned_data['cust_phone']
    cust_email = uniform_form.cleaned_data['cust_email']
    cust_addr = uniform_form.cleaned_data['cust_addr']
    date_of_created = uniform_form.cleaned_data['date_of_created']
    hat = uniform_form.cleaned_data['hat']
    shoulder_width = uniform_form.cleaned_data['shoulder_width']
    sleeve_length = uniform_form.cleaned_data['sleeve_length']
    back_length = uniform_form.cleaned_data['back_length']
    center_back = uniform_form.cleaned_data['center_back']
    shirt_length = uniform_form.cleaned_data['shirt_length']
    collar = uniform_form.cleaned_data['collar']
    chest = uniform_form.cleaned_data['chest']
    waist = uniform_form.cleaned_data['waist']
    seat = uniform_form.cleaned_data['seat']
    waist_belt = uniform_form.cleaned_data['waist_belt']
    hip = uniform_form.cleaned_data['hip']
    crotch = uniform_form.cleaned_data['crotch']
    front_crotch = uniform_form.cleaned_data['front_crotch']
    thigh = uniform_form.cleaned_data['thigh']
    pants_length = uniform_form.cleaned_data['pants_length']
    skirt_length = uniform_form.cleaned_data['skirt_length']
    remark = uniform_form.cleaned_data['remark']

    uniform = Uniform.objects.create(
                                        CustName = cust_name,
                                        CustNo = cust_no,
                                        OrgnizationName =orgnization_name,
                                        Gender = gender,
                                        CustPhone =cust_phone,
                                        CustEmail =cust_email,
                                        CustAddr = cust_addr,
                                        DateOfCreated = date_of_created,
                                        Hat = hat,
                                        ShoulderWidth = shoulder_width,
                                        SleeveLength = sleeve_length,
                                        BackLength = back_length,
                                        CenterBack = center_back,
                                        ShirtLength = shirt_length,
                                        Collar = collar,
                                        Chest = chest,
                                        Waist = waist,
                                        Seat = seat,
                                        WaistBelt = waist_belt,
                                        Hip = hip,
                                        Crotch = crotch,
                                        FrontCrotch = front_crotch,
                                        Thigh = thigh,
                                        PantsLength = pants_length,
                                        SkirtLength = skirt_length,
                                        Remark = remark
                                    )
    print(f'Uniform Object Created ---> id:{uniform.id} : name {cust_name}---> {type(uniform)}')
    uniform.save()
    return uniform

def single_input(request):
    if (request.user.id == None):
        return redirect('/login/')

    if (request.method == "POST"):
        uniform_form = PostForm( request.POST )
        if (uniform_form.is_valid()):
            print('Fomr is valid')
            uniform = save_uniform_object(uniform_form)
            log_content = f'USER ID:[ {request.user.id} ], USER:[ {request.user.username} ], Time:[ {get_time_stamp()} ], Create:[ {uniform.CustName} ]'
            get_log(log_content)
            message = '制服量測單新增完成...'
        else:
            print('Fomr is NOT valid')
            print(uniform_form.errors.as_data())
            message = '資料錯誤！'
        # context = {'uniform_form':uniform_form, 'message':message}
    else:
        message = '姓名不可空白'
        print('Into Empty Form')
        uniform_form = PostForm()
        # context = {'uniform_form':uniform_form, 'message':message}
    return render(request, 'single_input.html', locals())

def multi_input(request, orgnization_name=None):
    if (request.user.id == None):
        return redirect('/login/')

    unifomrs = Uniform.objects.filter(OrgnizationName=orgnization_name).order_by('-id')
    today = date.today()
    uniforms = unifomrs.filter(DateOfCreated = today).order_by('-id')

    if (request.method == "POST"):
        uniform_form = PostForm( request.POST )
        if (uniform_form.is_valid()):
            print('Fomr is valid')
            uniform = save_uniform_object(uniform_form)
            uniform = Uniform.objects.get(id=uniform.id)
            uniform.OrgnizationName = orgnization_name
            log_content = f'USER ID:[ {request.user.id} ], USER:[ {request.user.username} ], Time:[ {get_time_stamp()} ], Create:[ {uniform.OrgnizationName} :{uniform.CustName} ]'
            get_log(log_content)
            uniform.save()
            return redirect('.')
        else:
            print('Fomr is NOT valid')
            print(uniform_form.errors.as_data())
            return redirect('.')

    message = '姓名不可空白'
    uniform_form = PostForm()
    context = {'uniform_form':uniform_form, 'uniforms':uniforms , 'message':message, 'orgnization_name':orgnization_name}  
    return render(request, 'multi_input.html', context)

####################################################################################################
# < ----- main  ----- >

def main(request):
    if (request.user.id == None):
        return redirect('/login/')
    username = request.user.username

    if (request.method == "POST"):
        cust_name = request.POST['cust_name']
        if (cust_name != ''):
            path = '/multi_input/'+cust_name
            return redirect(path)
        else :        
            message = "輸入團體/公司名進行「建立批量制服量測單」作業！"
            return render(request, 'main.html', locals())    
    else:
        return render(request, 'main.html', locals())

####################################################################################################
# < ----- Hidden Function for System Test ----- >

def list_perm(request, inputString=None):
    print(f'GET:{str(inputString)} ---> TYPE:{type(inputString)}')
    type_check = f'GET:{str(inputString)} ---> TYPE:{type(inputString)}'
    heading = str(inputString)
    nums = list(inputString)
    result = perm().permutaion(nums)
    return render(request, 'test.html', locals())

if (__name__ == '__main__'):
    main()