from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = ((0, 'Draft'), (1, 'Posted'))

UPSTAT = ((0, 'Upcoming'), (1, 'Completed'))


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('post_detail', args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    createdate = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["-createdate"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.author)


class Upcoming(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    num_rooms = models.CharField(max_length=4)
    status = models.IntegerField(choices=UPSTAT, default=0)


    def __str__(self):
        return self.name + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('post_detail', args=(str(self.id)))
        return reverse('upcoming')
# Create your models here.
