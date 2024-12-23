from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
users = [
    {'username': 'user1', 'password': 12345678, 'age': 22},
    {'username': 'user2', 'password': 23456789, 'age': 35},
    {'username': 'user3', 'password': 34567890, 'age': 40},
]


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            error = check_sign_up(username, password, repeat_password, age)
            if error:
                info['error'] = error
            else:
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        error = check_sign_up(username, password, repeat_password, age)
        if error:
            info['error'] = error
        else:
            return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'fifth_task/registration_page.html', info)


def check_sign_up(*args):
    error = None
    username, password, repeat_password, age = args
    if username in (user['username'] for user in users):
        error = 'Пользователь уже существует'
    elif age < 18:
        error = 'Вы должны быть старше 18'
    elif password != repeat_password:
        error = 'Пароли не совпадают'
    return error
