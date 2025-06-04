from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100)  # Category name with a max length of 100 characters
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the record is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the record is updated

    def __str__(self):
        return self.category_name  # This makes the object print/display by its name

    class Meta:
        verbose_name_plural = 'Categories'  # Admin panel will show 'Categories' instead of 'Categorys'

STATUS_CHOICE = (
    ('draft', 'Draft'),
    ('public', 'Published'),
)

class Blogs(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to='uploads/%y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=1000)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blogs'