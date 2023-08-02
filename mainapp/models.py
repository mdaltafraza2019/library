from django.db import models

# Create your models here.
TYPE=(
    ('Bpsc','Bpsc'),
    ('IIT','IIT'),
    ('NEET','NEET'),
    ('UPSC','UPSC'),
    ('JEE','JEE'),
    ('SSC','SSC'),
    ('Railway','Railway'),
    ('Banking','Banking'),
)
SHIFT=(
    ('7am_to_12pm','7am_to_12pm'),
    ('12pm to 5pm','12pm_to_5pm'),
    ('5pm_to 10pm','5pm _to_10pm'),
   
)
class Category(models.Model):
    course=models.CharField(max_length=30, choices=TYPE)
    slug=models.SlugField()

    def __str__(self):
        return self.course
class Shift(models.Model):
    shift_title=models.CharField(max_length=40,choices=SHIFT,default=None,blank=True,null=True)
    slug=models.SlugField()

    def __str__(self):
        return self.shift_title

class Student(models.Model):
    reg_no=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    mob_no=models.CharField(max_length=15)
    adhar_no=models.CharField(max_length=20)
    prep_for=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    shift=models.ForeignKey(Shift,on_delete=models.CASCADE,null=True,blank=True)
    date_of_joining=models.DateField(help_text='year-month-day')
    mode_of_payment=models.CharField(max_length=40,choices=(('UPI','UPI'),('CASH','CASH')))
    payment=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.reg_no +" "+self.name
