from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from ckeditor.fields import RichTextField

STATUS = ((0, 'Draft'), (1, 'Posted'))

STATUSM = ((0, 'Pending'), (1, 'In Process'), (2, 'Completed'))

STATUSH = ((0, 'Pending'), (1, 'In Process'), (2, 'Completed'))

UPSTAT = ((0, 'Upcoming'), (1, 'Completed'))

LOSTFOUND = ((0, 'Lost'), (1, 'Found'), (2, 'Claimed'))

DEPARTMENT = ((0, 'Operations'), (1, 'Sales'), (2, 'Maintenance'), (3, 'Housekeeping'))


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS)
    views = models.ManyToManyField(User, related_name='user_viewed')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('post_detail', args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["-createdate"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.author)


class Upcoming(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    details = RichTextField(blank=True, null=True)
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
    bodym = RichTextField(blank=True, null=True)
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
    mbody = RichTextField(blank=True, null=True)
    mcreatedate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-mcreatedate"]

    def __str__(self):
        return "Comment {} by {}".format(self.mbody, self.mauthor)


class PostH(models.Model):
    titleh = models.CharField(max_length=255)
    authorh = models.ForeignKey(User, on_delete=models.CASCADE)
    bodyh = RichTextField(blank=True, null=True)
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
    hbody = RichTextField(blank=True, null=True)
    hcreatedate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-hcreatedate"]

    def __str__(self):
        return "Comment {} by {}".format(self.hbody, self.hauthor)


class LostFound(models.Model):
    item = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=LOSTFOUND, default=0)

    def __str__(self):
        return self.item + ' | ' + str(self.creator)

    def get_absolute_url(self):
        # return reverse('post_detail', args=(str(self.id)))
        return reverse('lostfound')


class LFComment(models.Model):
    lostfound = models.ForeignKey(LostFound, on_delete=models.CASCADE, related_name="lfcomments")
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-createdate"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.creator)


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    department = models.IntegerField(choices=DEPARTMENT)
    start_date = models.DateField(auto_now_add=False)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="static/Images")

    def __str__(self):
        return str(self.user)

