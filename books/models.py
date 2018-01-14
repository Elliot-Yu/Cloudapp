from django.db import models
from django.core.urlresolvers import reverse


'''STATUS_CHOICES = (
    ('u', 'un_go'),
    ('d', 'done'),
)'''

# python manage.py makemigrations books
# python manage.py sqlmigrate books 0001
# python manage.py migrate
# python manage.py runserver


class User(models.Model):
    email = models.EmailField(max_length=100,default='DEFAULT VALUE')
    username = models.CharField(max_length=30, default='DEFAULT VALUE')
    password = models.CharField(max_length=128, default='DEFAULT VALUE')
    firstname = models.CharField(max_length=30, default='DEFAULT VALUE')
    lastname = models.CharField(max_length=30, default='DEFAULT VALUE')

    def __str__(self):
        return self.username


class Country(models.Model):
    c_name = models.CharField(max_length=30,default='DEFAULT VALUE')
    c_url_photo = models.URLField(default='DEFAULT VALUE', null=True, blank=True)

    def __str__(self):
        return self.c_name


class City(models.Model):
    ct_name = models.CharField(max_length=30,default='DEFAULT VALUE')
    ct_country = models.CharField(max_length=30,default='DEFAULT VALUE',null=True, blank=True)

    def __str__(self):
        return self.ct_name


class Group(models.Model):
    g_name = models.CharField(max_length=30,default='DEFAULT VALUE')
    g_organiser = models.CharField(max_length=30,default='DEFAULT VALUE')
    g_member = models.IntegerField(max_length=100, default='DEFAULT VALUE')
    g_place = models.CharField(max_length=30,default='DEFAULT VALUE')
    g_city = models.CharField(max_length=30,default='DEFAULT VALUE')
    g_content = models.TextField(max_length=100, null=True, blank=True)
    g_state = models.CharField(max_length=1, default='DEFAULT VALUE')
    g_country = models.CharField(max_length=30,default='DEFAULT VALUE')
    g_createdtime = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return self.g_name


    def get_absolute_url(self):
        return reverse('app:detail', kwargs={'g_id': self.pk})


class Comment(models.Model):
    group = models.ForeignKey(Group, related_name='article_comment')
    detail = models.TextField(max_length=128,default='DEFAULT VALUE')
    user = models.CharField(max_length=30,default='DEFAULT VALUE',null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.detail[:20]


class GroupMember(models.Model):
    member = models.CharField(max_length=30,default='DEFAULT VALUE',null=True, blank=True)
    group = models.ForeignKey(Group, related_name='user_group')



