from django.db import models

# Create your models here.


class Post(models.Model):
    username = models.CharField(max_length=12)
    caption = models.CharField(max_length=255)
    # post_image = models.ImageField()
    # profile_picture = models.image
    likes = models.IntegerField()
    time_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title 



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)