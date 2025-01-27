from django.db import models

class Contact(models.Model):
    nom = models.TextField()
    email = models.EmailField()
    message = models.TextField()
  

    def __str__(self):
        return f"{self.nom} - {self.email}"
