from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., Verified Buyer, Islamabad")
    comment = models.TextField()
    rating = models.IntegerField(default=5)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    static_avatar = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.client_name} ({self.rating} stars)"

    @property
    def get_avatar_url(self):
        if self.image:
            return self.image.url
        if self.static_avatar:
            return self.static_avatar
        return f"https://api.dicebear.com/7.x/avataaars/svg?seed={self.client_name}"

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Statistic(models.Model):
    title = models.CharField(max_length=100)
    count = models.IntegerField()
    suffix = models.CharField(max_length=10, default="+", help_text="e.g., +, %")
    icon = models.CharField(max_length=50, help_text="SVG icon code identifier")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title}: {self.count}{self.suffix}"
