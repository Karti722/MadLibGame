from django.db import models

class MadLib(models.Model):
    template_text = models.TextField()
    filled_text = models.TextField(blank=True, null=True)
