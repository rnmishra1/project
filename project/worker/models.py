from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    contact = models.CharField(max_length=10,blank = True,null = True)
    address = models.CharField(max_length=100,blank = True, null = True)
    start_date = models.DateField(blank = True, null = True)
    end_date = models.DateField(blank = True, null = True)
    skills = models.TextField(max_length = 50,blank = True, null = True)
    def __str__(self):
    	return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()

post_save.connect(create_user_profile, sender=User)