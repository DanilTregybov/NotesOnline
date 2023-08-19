from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Theme(models.Model):
    theme_name = models.CharField(max_length=30) #help_text="Note theme",
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "{}".format(self.theme_name)

    def get_absolute_url(self):
        return reverse('notes_on_theme', kwargs={"edit_slug": self.slug})
class Note(models.Model):
    topic = models.ForeignKey(to=Theme, on_delete=models.CASCADE ) #verbose_name="Note Theme"
    name = models.CharField(max_length=50) #verbose_name="Note Name" help_text="Note name",
    text = models.TextField()#help_text="Note text"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)



    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "{}:{}".format(self.pk,self.name)

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={"pk" : self.pk})