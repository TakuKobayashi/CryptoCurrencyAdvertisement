from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=255, null=False, blank=False)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login_at = models.DateTimeField(null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    type = models.CharField(max_length=32, null=True, blank=True)
    uid = models.CharField(max_length=255, null=False, blank=False)
    token = models.TextField(null=True, blank=True)
    token_secret = models.TextField(null=True, blank=True)
    expired_at = models.DateTimeField(null=True, blank=True)
    options = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
