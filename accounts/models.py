from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import datetime
from django.urls import reverse
# from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to='profile_img', blank=True, null=True)
    image_ar = models.ImageField(_("image"), upload_to='profile_img', blank=True, null=True)
 
    address = models.CharField(max_length=100,verbose_name=_("Address"))
    address_ar = models.CharField(max_length=100)
    join_date = models.DateTimeField(_("join date"),default = datetime.datetime.now)
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
    admin_photo.short_description = 'Imageee'
    admin_photo.allow_tags = True



    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return  '%s' %(self.user.first_name +' '+self.user.last_name)

    def get_absolute_url(self):
        return reverse("accounts:Profile_detail", kwargs={"slug": self.slug})


def create_profile(sender , **kwargs):
    print(kwargs)
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile , sender=User)