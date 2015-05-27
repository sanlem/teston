from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100, blank=True)
    questions_number = models.IntegerField()
    password = models.CharField(max_length=6, unique=True)
    owner = models.CharField(max_length=20) # username of creator

    def __unicode__(self):
        return self.title


class Question(models.Model):
    poll = models.ForeignKey("Poll")
    title = models.CharField(max_length=100)
    variant_1 = models.CharField(max_length=100)
    variant_2 = models.CharField(max_length=100)
    variant_3 = models.CharField(max_length=100)
    variant_4 = models.CharField(max_length=100)
    correct = models.IntegerField(default=0)
    number = models.IntegerField(null=True)

    class Meta:
        ordering = ["number"]

    def __unicode__(self):
        return self.title



class Sollution(models.Model):
    poll = models.ForeignKey("Poll")
    submitter = models.TextField(max_length=30) # who submited a sollution
    group = models.CharField(max_length=30) # submitter's group
    mark = models.IntegerField()

    def __unicode__(self):
        title = unicode(self.submitter) + u" " + unicode(self.group)
        return title