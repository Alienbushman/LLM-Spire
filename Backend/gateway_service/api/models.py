from django.db import models


class LLMOpinionModel(models.Model):
    question = models.CharField(max_length=2000)
    model = models.CharField(max_length=100, null=True, blank=True)
    answer = models.CharField(max_length=10000)

    class Meta:
        db_table = "testing_model_prediction"
