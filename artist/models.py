from django.db import models
import  datetime
# Create your models here.

class Tagname(models.Model):
    tag = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.tag
    
    def register(self):
        self.save()
    
    @staticmethod
    def get_all_tags():
        return Tagname.objects.all()


class Artist(models.Model):
    artist_name = models.CharField(max_length=50, default="anonymous")
    artist_link = models.CharField(max_length=200,default="", null=True, blank=True)
    likes = models.CharField(max_length=50, default=0, null=True)
    elapsed_time = models.CharField(max_length=50, null=True)
    post_time = models.CharField(max_length=50, null=True)
    post_link = models.CharField(max_length=500, null=True)
    artist_pp  =models.CharField(max_length=500, null=True, default="")
    instagram_post =models.ImageField(upload_to='posts', null=True, blank=True, default="images/paper.jpg" ) 
    tagname = models.ForeignKey(Tagname, on_delete=models.CASCADE, null=True, blank=True, default="")

    def __str__(self):
        return f"{self.artist_name} {self.tagname}"

    def register(self):
        self.save()

    @staticmethod
    def get_all_artists():
        return Artist.objects.all()

    @staticmethod
    def get_all_artists_by_tagid(tag_id):
        if tag_id:
            return Artist.objects.filter(tagname =tag_id)

        else:
            return Artist.get_all_artists()

    @staticmethod
    def get_artists_by_id(ids):
        return Artist.objects.filter(id__in = ids)