from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
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


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, 
        on_delete=models.CASCADE,
        related_name='comments',
        )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey( 
        get_user_model(),
        on_delete=models.CASCADE,
        
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("home")
    
    