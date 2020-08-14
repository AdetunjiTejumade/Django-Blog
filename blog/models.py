from django.db import models
from django.urls import reverse
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post_detail', args=[str(self.id)])
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
