from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

STATUS = ((0, 'Draft'), (1, 'Posted'))

STATUSM = ((0, 'Pending'), (1, 'In Process'), (2, 'Completed'))

STATUSH = ((0, 'Pending'), (1, 'In Process'), (2, 'Completed'))

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
        return self.name

    def get_absolute_url(self):
        # return reverse('post_detail', args=(str(self.id)))
        return reverse('upcoming')


class PostM(models.Model):
    titlem = models.CharField(max_length=255)
    authorm = models.ForeignKey(User, on_delete=models.CASCADE)
    bodym = models.TextField()
    createdatem = models.DateTimeField(auto_now_add=True)
    updatedatem = models.DateTimeField(auto_now=True)
    statusm = models.IntegerField(choices=STATUSM, default=0)

    def __str__(self):
        return self.titlem + ' | ' + str(self.authorm)

    def get_absolute_url(self):
        # return reverse('post_detail', args=(str(self.id)))
        return reverse('maintenance')


class MComment(models.Model):
    postm = models.ForeignKey(PostM, on_delete=models.CASCADE, related_name="mcomments")
    mauthor = models.ForeignKey(User, on_delete=models.CASCADE)
    mbody = models.TextField()
    mcreatedate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-mcreatedate"]

    def __str__(self):
        return "Comment {} by {}".format(self.mbody, self.mauthor)


class PostH(models.Model):
    titleh = models.CharField(max_length=255)
    authorh = models.ForeignKey(User, on_delete=models.CASCADE)
    bodyh = models.TextField()
    createdateh = models.DateTimeField(auto_now_add=True)
    updatedateh = models.DateTimeField(auto_now=True)
    statush = models.IntegerField(choices=STATUSH, default=0)

    def __str__(self):
        return self.titleh + ' | ' + str(self.authorh)

    def get_absolute_url(self):
        # return reverse('post_detail', args=(str(self.id)))
        return reverse('housekeeping')


class HComment(models.Model):
    posth = models.ForeignKey(PostH, on_delete=models.CASCADE, related_name="hcomments")
    hauthor = models.ForeignKey(User, on_delete=models.CASCADE)
    hbody = models.TextField()
    hcreatedate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-hcreatedate"]

    def __str__(self):
        return "Comment {} by {}".format(self.hbody, self.hauthor)
