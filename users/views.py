from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
        else:
            messages.error(
                request, f'Please correct the error below: {form.errors.as_data()}')
    else:
        # GET request.. return the form
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# def register(request):
#     # Если ПОСТ запрос то открыть форму с данными
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         print(request.POST)

#         # Проверим форму на валидность и получим из нее данные
#         if form.is_valid():
#             print('form is valid')
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             # Редирект после успешного сообщения и открытия аккаунта
#             return redirect('blog-home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/register.html', {'form': form})
