from django.db import models

# Create your models here.
class Play(models.Model):
    """Represents a single performance in the database.
	
	The class/table contains static data regarding the performance. Data that will
	change over time will be store elsewhere."""

    # Note: these lengths are arbitrary.
    url_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)

    # default string representation
    def __str__(self):
        return self.title
