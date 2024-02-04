# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Projects(models.Model):

    #__Projects_FIELDS__
    project_name = models.CharField(max_length=255, null=True, blank=True)

    #__Projects_FIELDS__END

    class Meta:
        verbose_name        = _("Projects")
        verbose_name_plural = _("Projects")


class User(models.Model):

    #__User_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    org_id = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Interactions(models.Model):

    #__Interactions_FIELDS__
    interaction_count = models.CharField(max_length=255, null=True, blank=True)

    #__Interactions_FIELDS__END

    class Meta:
        verbose_name        = _("Interactions")
        verbose_name_plural = _("Interactions")



#__MODELS__END
