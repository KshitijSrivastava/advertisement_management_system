from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self,email,password,is_staff,is_superuser,**extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,is_staff=is_staff,is_active=True,is_superuser=is_superuser,last_login=now,date_joined=now,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password,False,False,**extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password,True,True,**extra_fields)



class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=256,blank=True)
    first_name = models.CharField(max_length=256,blank=True)
    last_name = models.CharField(max_length=256,blank=True)
    email = models.EmailField(blank=True, unique=True)
    address1 = models.CharField(max_length=256,blank=True)
    address2 = models.CharField(max_length=256,blank=True)
    area_code = models.CharField(max_length=10,blank=True)
    country_code = models.CharField(max_length=10,blank=True)

    date_joined = models.DateTimeField(_('date_joined'),default=timezone.now())
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural =_('users')



class Post(models.Model):
    title  = models.CharField(max_length=256)
    start_date  = models.DateField(default = datetime.date.today())
    end_date = models.DateField(default = datetime.date.today())
    amount_per_month = models.IntegerField(default=0)
    amount_per_day = models.IntegerField(default=0)
    start_date_pic = models.ImageField(upload_to='profile_image',blank=True,null=True)
    end_date_pic = models.ImageField(upload_to='profile_image',blank=True,null=True)
    rev1_status = models.IntegerField(default = 0)
    rev2_status = models.IntegerField(default = 0)
    rev3_status = models.IntegerField(default = 0)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('blog:post_list')


    def __str__(self):
        return self.title

    def approve(self):
        self.status =True
        self.save()

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments')
    author = models.CharField(max_length=256,null=True,blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
