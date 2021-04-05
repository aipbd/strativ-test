from django_filters import FilterSet, CharFilter

from strativ_test.apps.countries.models import Country


class CountryFilter(FilterSet):
    def get_neighbouring_country(self, queryset, name, value):
        country = Country.objects.filter(alpha_code3=value)
        if not country:
            return self.queryset.none()
        return self.queryset.filter(
            alpha_code3__in=country.last().neighbouring_countries
        )

    def get_same_language_country(self, queryset, name, value):
        return self.queryset.filter(languages__contains=value)

    name = CharFilter(lookup_expr="icontains")
    neighbouring_country = CharFilter(method='get_neighbouring_country')
    same_language_country = CharFilter(method='get_same_language_country')

    class Meta:
        model = Country
        fields = []
