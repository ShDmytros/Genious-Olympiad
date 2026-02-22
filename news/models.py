from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

import os
from datetime import date


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=News.Status.PUBLISHED)
# Create your models here.
class News(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Draft'  
        PUBLISHED = 1, 'Published'
    title = models.CharField("Name of the news", max_length=255)
    content = models.TextField("Content of the news", blank=True)
    is_published = models.BooleanField("Is published", choices=Status.choices, default=Status.PUBLISHED)
    image = models.ImageField("Image", upload_to="news/", default="")
    url = models.SlugField(max_length=160, unique=True, allow_unicode=True, blank=True)
    # language = models.ForeignKey('Language', on_delete=models.PROTECT, null=True)
    date = models.DateField("Date", default=date.today)
    author = models.CharField("Author of the news", max_length=255)
    

    objects = models.Manager()
    published = PublishedManager()


    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['url', 'lang_from'],
    #             name='unique_url_per_lang_from'
    #         )
    #     ]

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse("read_news", kwargs={"lang_slug": self.language.slug,"text_slug": self.url})
        return reverse("read_news", kwargs={"text_slug": self.url})
    
    def __str__(self):
        return self.title

    
    def save(self, *args, **kwargs):

        # якщо slug пустий → генеруємо його з title
        if not self.url:
            base_slug = slugify(self.title, allow_unicode=True)
            slug = base_slug

            # перевіряємо унікальність
            counter = 1
            while News.objects.filter(url=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.url = slug

        try:
            old_news = News.objects.get(pk=self.pk)
            if old_news.image and old_news.image != self.image:
                if os.path.isfile(old_news.image.path):
                    os.remove(old_news.image.path)
        except News.DoesNotExist:
            pass

        super().save(*args, **kwargs)