from django.db import models


class LanguageCourse(models.Model):
    title = models.CharField(max_length=120)
    course_overview = models.TextField()
    logo = models.ImageField(upload_to='Language_Course', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.title
