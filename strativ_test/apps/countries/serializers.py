from rest_framework import serializers

from strativ_test.apps.countries.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CountryDetailsSerializer(CountrySerializer):

    def get_neighbouring_country_list(self, country_object):
        country = Country.objects.filter(alpha_code3=country_object.alpha_code3)
        if not country:
            return
        queryset = Country.objects.filter(
            alpha_code3__in=country.last().neighbouring_countries
        )
        return CountrySerializer(queryset, many=True).data

    neighbouring_country_list = serializers.SerializerMethodField()

    class Meta(CountrySerializer.Meta):
        fields = [field.name for field in Country._meta.get_fields()] + ["neighbouring_country_list"]
