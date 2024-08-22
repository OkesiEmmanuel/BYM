from django.contrib import admin
from django.urls import include, path
from members.views import home_view, contact_us

admin.site.site_header = "BYM System"
admin.site.site_title = "BYM System"
urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_us, name='contact'),

    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
]
