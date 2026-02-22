from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

import os
# Create your models here.
class GameProblems(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    # slug = models.SlugField(max_length=255)
    description = models.TextField("Description of the solution", blank=True)
    # image = models.ImageField("Image", upload_to="game/", default="")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("game_lang", kwargs={"game_slug": self.slug})
    
    # def delete(self, *args, **kwargs):
    #     if self.image:
    #         if os.path.isfile(self.image.path):
    #             os.remove(self.image.path)
    #     super().delete(*args, **kwargs)
    

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         try:
    #             old_game = GameProblems.objects.get(pk=self.pk)
    #             if old_game.image and old_game.image != self.image:
    #                 if os.path.isfile(old_game.image.path):
    #                     os.remove(old_game.image.path)
    #         except GameProblems.DoesNotExist:
    #             pass

    #     super().save(*args, **kwargs)