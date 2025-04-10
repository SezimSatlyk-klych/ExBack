from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy

# Login
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        # Сохраняем количество входов в сессии
        request = self.request
        request.session['logins'] = request.session.get('logins', 0) + 1
        messages.success(request, "Login successful!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error! Check your data.")
        return super().form_invalid(form)


# Logout
class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'
    next_page = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        messages.info(request, "You have been logged out.")
        return super().post(request, *args, **kwargs)


# Logout confirmation view
def logout_confirm(request):
    return render(request, 'accounts/logout_confirm.html')


# Signup
class SignupView(FormView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request, f"Account {username} is created")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error during registration")
        return super().form_invalid(form)
