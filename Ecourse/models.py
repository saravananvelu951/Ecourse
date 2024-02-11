from django.db import models 

# Create your models here.

class Registration(models.Model):
    First_name = models.CharField (max_length=100,default='',null = True)
    Last_name = models.CharField (max_length=100,default='',null = True)
    Email = models.CharField (max_length=100,default='',null = True)
    Password = models.CharField (max_length=100,default='',null = True)
    Mobile = models.BigIntegerField(default='1')
    Gender = models.CharField (max_length=100,default='',null = True)

    def __str__(self):
        return self.First_name

class Category(models.Model):
    category_image = models.ImageField(upload_to="uploads/category/")
    category_name = models.CharField (max_length=100,default='',null = True)

    def __str__(self):
        return self.category_name

class Course(models.Model):
    course_image = models.ImageField(upload_to="uploads/course/")
    course_name = models.CharField (max_length=100,default='',null = True)
    course_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    course_price = models.IntegerField(default=1)
    course_desc = models.CharField(max_length=100,default='',null = True)  

    def __str__(self):
        return self.course_name 

class Order(models.Model):
    address = models.CharField (max_length=100,default='',null = True)
    mobile =  models.BigIntegerField(default=1)
    customer = models.ForeignKey(Registration,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    price = models.IntegerField(default = 1)
    quantity = models.IntegerField(default =1)
    status = models.BooleanField(default = False)

    def __str__(self):
        return self.course.course_name
    

class Videos(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='uploads/videos/', blank=True, null=True)
    video_disc = models.CharField(max_length=100,default='',null = True)  
    is_preview = models.BooleanField(default=False)

    

    def __str__(self):
        return self.title
