from django.db import models
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    # Foreign key for a authenticated user relationship
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=now)
    published_at = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_at = now
        self.save()
        
    def approve_commets(self):
        return self.comments.filter(approved_comments=True)
    
    def get_absolute_url(self):
        return reverse("pos_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
        
    def get_absolute_url(self):
        return reverse("post_list")
    
    def __str__(self):
        return self.text
