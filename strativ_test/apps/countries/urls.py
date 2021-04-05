from django.urls import path

from strativ_test.apps.countries.views import CountryListAPIView, CountryRetrieveUpdateDestroyAPIView

app_name = 'country'

urlpatterns = [
    path('', CountryListAPIView.as_view(), name='country_list'),
    path('<int:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country_detail'),

]
