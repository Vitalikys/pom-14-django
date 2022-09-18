from django.contrib import messages
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from .forms import  AuthenticateUserForm
from django.urls import reverse_lazy

from .models import CustomUser
from .forms import UserLoginFormEmail, AuthenticateUserForm


def list_users(request):
    active_user = CustomUser.objects.filter(is_active=True).first()

    return render(request, 'authentication/users_list.html', {'users': CustomUser.get_all()})


@login_required(login_url='login_url')
def delete_user(request, id):
    if request.user.role != 1:
        # якщо ми звичайний відвідувач то нема доступу
        from django.http import HttpResponse
        return HttpResponse(status=403, content=' HttpResponse,status=403 \b - якщо ми звичайний відвідувач то нема доступу')  # HTTP 403 Forbidden

    CustomUser.delete_by_id(id)
    messages.success(request, 'You have delete user. Success !')
    return redirect('list_users')


@login_required(login_url='login_url')
def edit_user(request, user_id):
    if request.user.role != 1:
        # якщо ми звичайний відвідувач то нема доступу
        from django.http import HttpResponse
        return HttpResponse(status=403, content=' HttpResponse,status=403 \b - якщо ми звичайний відвідувач то нема доступу')  # HTTP 403 Forbidden

    if user_id:
        user_to_edit = CustomUser.get_by_id(user_id)
    form = AuthenticateUserForm(request.POST or None, instance=user_to_edit)
    if request.POST and form.is_valid():
        print('valid')
        form.save()
        messages.success(request, f'Changes to user: {user_to_edit.last_name} success !')
        return redirect('list_users')
    context = {'form': form, 'user': user_to_edit}
    return render(request, 'authentication/edit_user.html', context=context)


@login_required(login_url='login_url')
def detail_user(request, id):
    user_data = CustomUser.get_by_id(id).to_dict()
    return render(request, 'authentication/single_user_detail.html', {'user': user_data})


def register(request):
    if request.method == 'POST':  # приймаємо дані з форми
        # form = UserCreationForm(request.POST) replace to .forms-> UserRegisterForm
        #  можна залишити без створення в формі
        form = AuthenticateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # print('cleaned_data_FORM', form.cleaned_data, new_user)
            # user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request, new_user)  # щоб зразу зайти після реєстрацї
            messages.success(request, 'Reg success *!')

            # first_name = request.POST.get('first_name')
            # # first_name = request.POST['username']
            # last_name = request.POST.get('last_name')
            # midle_name = request.POST.get('middle_name')
            # email = request.POST.get('email')
            # password = request.POST.get('password')
            # role = request.POST.get('role')
            # # is_staff = False
            # # is_superuser = False
            # # print('email = ', email)
            # # print('form.cleaned_data = ', form.cleaned_data)
            # # if role:
            # #     print('role = ', role)
            # #     is_staff = True
            # #     is_superuser = True
            # try:
            #     new_usr = CustomUser.objects.create(email=email,
            #                                 password=password,
            #                                 first_name=first_name,
            #                                 middle_name=midle_name,
            #                                 last_name=last_name, role=role)
            #     # new_usr.is_active = True
            #     # new_usr.is_superuser = is_superuser
            #     # new_usr.is_staff = is_staff
            #     new_usr.save()
            #     print(new_usr,'after Create',new_usr.__dict__)
            #     # user = authenticate(request, email=form.cleaned_data['email'],
            #     #                     password=form.cleaned_data['password'])
            #     login(request, new_usr)
            #     messages.success(request, 'Registation success !')
            #     return redirect('home')
            # except:
            #     messages.error(request, 'Error of registration')
        else:
            print(form.errors)
            messages.error(request, 'Error valid form щось пішло не так')
    else:
        form = AuthenticateUserForm()
    return render(request, 'authentication/register.html', {'form': form})


def user_login(request):
    ''' login CustomUser  from HTML FORMs by email'''
    if request.method == 'POST':
        form = UserLoginFormEmail(data=request.POST)
        if form.is_valid():
            # user = form.get_user()
            mail = request.POST.get('email')
            password = request.POST.get('password')
            usr = CustomUser.get_by_email(mail)
        print('username, pass, before try', mail, password, usr)
        try:
            # usr = form.get_user()
            # usr = CustomUser.objects.get(first_name=username)
            print(usr.first_name, 'username, pass after try :', usr.first_name, password, usr)
            if usr.password == password:
                print("Hello login")
                login(request, usr)
                messages.success(request, f'Login success {usr.email}')
                print(usr.is_active)
                # usr.is_active = True
#                 usr.save()
                # print(usr.username, 'username usernameusernameusername')
            else:
                messages.error(request, 'Error, wrong password')
        except Exception as e:
            messages.error(request, 'Error, щось пішло не так')
    else:
        form = UserLoginFormEmail()
    return render(request, 'authentication/login.html', {'form': form})


# def login_django(request):
#     ''' login Django_User using DJango FORMs.by mail, password'''
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             messages.success(request, f'Ви успішно зайшли як {user.email} !')
#             return redirect('home')
#     else:
#         form = UserLoginForm()
#     return render(request, 'authentication/login_django_usr.html', {'form': form})


def user_logout(request):
    # from django.contrib.auth import logout # locally
    # current_user = CustomUser.objects.filter(is_active=True).first()
    # current_user = request.user
    # current_user.is_active = False
    # current_user.save()
    logout(request)  # standart method django
    messages.success(request, 'Logout success !')
    return redirect('home')
