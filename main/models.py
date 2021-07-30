import sys
sys.path.append("..")
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

from users.models import User



class Illness(models.Model):
    illnessname = models.CharField(max_length=100)
    description=  models.TextField(null=True)
    image = CloudinaryField('image',null=True)
    symptoms = models.TextField(null=True)
    recommendation = models.TextField(null=True)
    
    
    def save_illness(self):
        self.save()

    def delete_illness(self):
        self.delete()
        
    @classmethod
    def get_illness_by_id(cls,id):
        illness = Illness.objects.filter(pk=id)
        return illness
    
    @classmethod
    def search_illness_by_search_term(cls,search_term):
        return cls.objects.filter(illnessname__icontains=search_term).all()
    
    
    def __str__(self):
        return self.illness_name
    
    
class Drug(models.Model):
    drug_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100,null=True)
    description=  models.TextField(null=True)
    usage_information = models.TextField(null=True)
    side_effects= models.TextField(null=True)
    overCounter = models.BooleanField(default=False)

    safety_advice_alcohol = models.TextField(null=True)
    safety_advice_pregnancy = models.TextField(null=True)
    safety_advice_breast_feeding = models.TextField(null=True)
    safety_advice_driving = models.TextField(null=True)
    
    
    def save_drug(self):
        self.save()

    def delete_drug(self):
        self.delete()
        
    @classmethod
    def get_drug_by_id(cls,id):
        drug = Drug.objects.filter(pk=id)
        return drug
    
    @classmethod
    def search_drug_by_search_term(cls,search_term):
        return cls.objects.filter(drug_name__icontains=search_term).all()
    
    
    def __str__(self):
        return self.drug_name


class Post(models.Model):
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
        
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
        
    @classmethod
    def get_post_by_user_id(cls,id):
        post =Post.objects.filter(user=id)
        return post
            
    def __str__(self):
        return self.post
    
class Reply(models.Model):
    reply = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def save_reply(self):
        self.save()

    def delete_reply(self):
        self.delete()
        
    @classmethod
    def get_replies_by_post(cls,id):
        replies = Reply.objects.filter(post=id).all()
        return replies
            
    def __str__(self):
        return self.reply
    
