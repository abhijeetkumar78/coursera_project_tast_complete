from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    # Redirect root URL to students list
    path('', RedirectView.as_view(url='/students/', permanent=False)),
]
