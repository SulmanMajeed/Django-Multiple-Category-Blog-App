from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
from django.utils.text import slugify

class Writer(models.Model):
    Name = models.CharField(max_length=10, blank=True, default='Sulman')
    Pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.Name  # Corrected the field name to `Name`

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, blank=True)
    desc = models.TextField()
    img = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Corrected field names here
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name  # Corrected the field name to `name`

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    keywords = models.TextField(max_length=160)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, max_length=200)
    img = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    imgalt = models.TextField()
    desc = models.TextField()
    content = HTMLField()
    readtime = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    author = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='blogs', null=True, blank=True)
    views = models.PositiveBigIntegerField(default=0)
    publishedtime = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-publishedtime']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def increment_views(self):
        self.views += 1
        self.save()

    def __str__(self):
        author_name = self.author.Name if self.author else "Unknown"
        return f"{self.title[0:20]} -Author:{author_name} -Views:{self.views}"

    @property
    def authorname(self):
        return self.author.Name if self.author else "Unknown"
    
    @property
    def authorprofilepic(self):
        return self.author.Pic if self.author else 'default/writerdefaultpic.png'

class Newsletter(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.EmailField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sno}, Name:{self.email[:10]}"

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sno}, Name:{self.name[:10]}"