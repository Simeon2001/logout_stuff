from django.db import models
from account.models import User

class BlackListJWT(models.Model):
    token = models.CharField(max_length=5000)
    user = models.ForeignKey(User, related_name="token_user", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("token", "user")