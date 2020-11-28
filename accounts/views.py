from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from accounts.forms import SignUpForm
from django.shortcuts import render, redirect

@login_required
def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
