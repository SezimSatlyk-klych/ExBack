from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from notes.models import Note
from django.contrib.auth.models import User

class CustomAdminSite(admin.AdminSite):
    site_header = "Notes Administration"
    site_title = "Notes Admin"
    index_title = "Welcome to Notes Admin Panel"
    logout_template = "admin/logout.html"

    def profile_view(self, request):
        request.current_app = self.name
        context = self.each_context(request)
        return TemplateResponse(request, "admin/admin_profile.html", context)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('admin_profile/', self.profile_view, name='admin_profile'),
        ]
        return custom_urls + urls

custom_admin_site = CustomAdminSite(name="custom_admin")
custom_admin_site.register(Note)
custom_admin_site.register(User)
