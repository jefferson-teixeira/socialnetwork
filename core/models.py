from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    date_of_birth = models.DateField()


class Profile(models.Model):
    name = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    contacts = models.ManyToManyField('self')


class Post(models.Model):
    text = models.TextField()
    date = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')


class Comment(models.Model):
    text = models.TextField()
    date = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


class Reaction(models.Model):
    REACTION_CHOICES = (
        ('Like', 'Like'),
        ('Love', 'Love'),
        ('Haha', 'Haha'),
        ('Wow', 'Wow'),
        ('Sad', 'Sad'),
        ('Angry', 'Angry'),
    )

    category = models.CharField(max_length=5, choices=REACTION_CHOICES)
    date = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    weight = models.IntegerField()
