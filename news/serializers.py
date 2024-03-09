from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = News
        fields = '__all__'
        extra_kwargs = {'category' : {'read_only' : True}}


class BulkNewsSerializer(serializers.Serializer):
    articles = NewsSerializer(write_only= True,many = True)

    def create(self , validated_data):
        category = self.context['view'].kwargs['category']
        for article in validated_data['articles']:
            new = NewsSerializer(instance=article).data
            new['category'] = category
            News.objects.create(**new)
        return validated_data 