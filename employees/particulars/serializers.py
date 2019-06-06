from rest_framework import serializers
from . import models


class ParticularsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'firstname', 'lastname', 'companyname', 'state','city','zip','web','age',)
        model = models.Particulars