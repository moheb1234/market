
from .models import Asset_Position , Export
import json
import datetime



def export_create(**validated_data):
    asset_position_list = json.loads(json.dumps(validated_data['asset_position_list'], default=str))

    del validated_data['asset_position_list']
    del validated_data['password']

    export = Export.objects.create(**validated_data)

    for asset in asset_position_list:
        asset['export'] = export
        asset_obj = Asset_Position.objects.create(**asset)
    
    return export
    
