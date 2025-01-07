from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            # Automatically login newly registered users
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect("index")
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {"form": form})


# class EmailLoginView(LoginView):
#     authentication_form = EmailAuthenticationForm
