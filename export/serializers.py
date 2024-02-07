from rest_framework import serializers
from .models import Asset_Position , Export
from .logic import export_create

class AssetPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset_Position
        fields = '__all__'
        read_only_fields = ['export']
    

class ExportSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required= True  , write_only= True )
    asset_position_list = AssetPositionSerializer(many = True)

    class Meta:
        model = Export
        fields= '__all__'
    
    def create(self , validated_data):
        return export_create(**validated_data)

    
