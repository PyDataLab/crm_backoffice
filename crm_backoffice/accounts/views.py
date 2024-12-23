from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


# Функция для отображения страницы входа
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Убедитесь, что маршрут 'index' доступен
        else:
            return render(request, 'accounts/login.html', {'form': form, 'errors': form.errors})

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

# Функция для выхода пользователя
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')  # Перенаправление на страницу входа
