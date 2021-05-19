from rest_framework.serializers import ModelSerializer
from .models import authModel

class authModelSerializers(ModelSerializer):
    class Meta:
        model = authModel
        fields = ('id','username','password','mail_id')

