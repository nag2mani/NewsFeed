from django.db import models
# Create your models here.

class Contest(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=1000)
    link = models.URLField()


class Job(models.Model):
    company_name = models.CharField(max_length=1000)
    skills = models.CharField(max_length=10000)
    posted_date = models.CharField(max_length=1000, null=True)
    apply_link = models.URLField()


class News(models.Model):
    headline = models.CharField(max_length=1000)
    summary = models.CharField(max_length=10000000)
    link = models.URLField()
