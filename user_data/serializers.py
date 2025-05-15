from rest_framework import serializers
from user_data.models import User

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        related_fields = kwargs.pop('related_fields', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if related_fields:
            for field_name, field_serializer in related_fields.items():
                if field_name in self.fields:
                    self.fields[field_name] = field_serializer

class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request', None)
        if request:
            main_fields = request.query_params.get('fields', None)
            if main_fields:
                main_fields = main_fields.split(',')
                fields = {key: value for key, value in fields.items() if key in main_fields}
        return fields    

    
class CreateuserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = "__all__"