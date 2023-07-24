from django.db import models
from django.contrib.auth.models import User, Group, AbstractUser, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def add_user_to_common_group(sender, instance, created, **kwargs):
    if created:
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(instance)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_users_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='custom_users_permissions'
    )

    def is_author(self):
        return self.groups.filter(name='authors').exists()

    def __str__(self):
        return self.username
