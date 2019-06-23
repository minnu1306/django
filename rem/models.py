# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

class Rem(models.Model):
    text = models.TextField()
    complete = models.BooleanField(default= False)
    time = models.DateField(default=datetime.now)
    def __str__(self):
        return self.text
