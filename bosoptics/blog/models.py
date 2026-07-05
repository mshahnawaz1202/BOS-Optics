from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    static_image = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=100, default="BOS Optics Team")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def get_image_url(self):
        if self.image:
            return self.image.url
        if self.static_image:
            return self.static_image
        return "/static/core/images/placeholder.jpg"
