from django.db import models


class Job(models.Model):
    TYPE_CHOICE = (
        ('N', 'New Grads'),
        ('I', 'Internship')
    )

    company = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=TYPE_CHOICE, null=False, default='N')
    title = models.CharField(max_length=200)
    link = models.URLField()
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.company, self.title)
