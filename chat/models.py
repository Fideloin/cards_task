from django.db import models
from django.contrib.auth.models import User


class Letter(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    theme = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    letter_body = models.TextField()

    def get_absolute_url(self):
        return "/letters/%i/" % self.id
