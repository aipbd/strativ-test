from django.urls import path

from strativ_test.apps.countries.views import CountryListAPIView, CountryRetrieveUpdateDestroyAPIView, country_list, country_details

app_name = 'country'


html_view = [
    path('', country_list, name='country_list'),
    path('details/', country_details, name='country_details'),
]


urlpatterns = [
    path('', CountryListAPIView.as_view(), name='country_list'),
    path('<int:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country_detail'),

]
