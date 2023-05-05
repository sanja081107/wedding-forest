from django.db import models


def upload_photos(instance, filename):
    return 'photos/wedding/{0}/{1}'.format(instance.post.title, filename)


class Wedding(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Свадьба'
        verbose_name_plural = 'Свадьба'
        ordering = ['title']


class WeddingPhotos(models.Model):
    photos = models.ImageField(upload_to=upload_photos, verbose_name='фото')
    post = models.ForeignKey(Wedding, related_name='wedding_photos', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Все фото'
