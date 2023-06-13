from rest_framework import serializers
from appteste.models import Brand

class BrandSerializers(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "_all__"
