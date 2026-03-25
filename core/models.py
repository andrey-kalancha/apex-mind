from django.db import models


class PartnerRequest(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SurveyResponse(models.Model):
    company = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)

    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company or 'Без компании'} - {self.created_at:%d.%m.%Y %H:%M}"