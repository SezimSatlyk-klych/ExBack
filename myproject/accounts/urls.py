from django.urls import path
from .views import CustomLoginView, CustomLogoutView, SignupView, logout_confirm

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('logout-confirm/', logout_confirm, name='logout_confirm'),
    path('signup/', SignupView.as_view(), name='signup'),
]
