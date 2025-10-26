from django.db import models

# Create your models here.

class TimelineEvent(models.Model):
    year = models.CharField(max_length=10)  # e.g., "2022"
    title = models.CharField(max_length=200)  # e.g., "Started Learning HTML & CSS"
    description = models.TextField()  # e.g., "Explored the basics of web development..."

    def __str__(self):
        return f"{self.year} - {self.title}"


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Ugyen Lhaden")
    introduction = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    hobbies = models.TextField(help_text="Comma-separated list of hobbies")  
    strengths = models.TextField(help_text="Comma-separated list of strengths")
    weaknesses = models.TextField(help_text="Comma-separated list of weaknesses")

    def get_hobbies_list(self):
        return [hobby.strip() for hobby in self.hobbies.split(',')]

    def get_strengths_list(self):
        return [strength.strip() for strength in self.strengths.split(',')]

    def get_weaknesses_list(self):
        return [weakness.strip() for weakness in self.weaknesses.split(',')]

    def __str__(self):
        return self.name
