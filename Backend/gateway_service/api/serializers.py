from rest_framework import serializers

from api.models import LLMOpinionModel


class LLMOpinionModelSerializer(serializers.ModelSerializer):
    # model_name = serializers.CharField(source='model.model_name')
    class Meta:
        model = LLMOpinionModel
        # fields = ('id','prediction', 'model', 'model__model_name')
        fields = '__all__'

