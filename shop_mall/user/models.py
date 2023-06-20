from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=64)
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'my_user'
        verbose_name = '고객'
        verbose_name_plural = '고객'
