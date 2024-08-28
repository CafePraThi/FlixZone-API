from rest_framework import serializers
from movies.models import Movie
from datetime import date


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        return 5

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('The release data must be bigger then 1970.')
        elif value.year > (date.today().year + 1):
            print(date.today().year+1)
            raise  serializers.ValidationError(f'The release must be iqual or lower than {date.today().year} ')
        return value
    
    def validate_resume(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError('Resume must have max 1000 caracters.')
