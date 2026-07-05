from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="SVG icon code identifier (e.g., eye, frame, lens, corporate)")
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., 30 mins, 1 hour")

    def __str__(self):
        return self.title

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='appointments')
    date = models.DateField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service.title if self.service else 'General'} on {self.date}"
