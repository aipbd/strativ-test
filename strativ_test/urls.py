"""strativ_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from strativ_test.apps.countries.urls import html_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

auth_patterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

api_patterns = [
    path('countries/', include('strativ_test.apps.countries.urls', namespace="countries")),
    path('token/', include(arg=(auth_patterns, "auth_patterns"), namespace="auth")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "api/",
        include(arg=(api_patterns, "strativ_test_api"), namespace="api"),
    ),
    path(
        "",
        include(arg=(html_view, "html_view"), namespace="web"),
    ),
]
