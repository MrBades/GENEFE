from django.db import models
import secrets
import uuid
from .paystack import Paystack


def ref_gen(self)->str:
    while not self:
        refgen = secrets.token_urlsafe(50)
        similar_ref = Products.objects.filter(ref=refgen)
        if not similar_ref:
            self = refgen
    return self
class Products(models.Model):
    name = models.CharField(max_length=255,)
    description = models.TextField(max_length=2083)
    price = models.PositiveBigIntegerField()
    stock = models.IntegerField()
    ref = models.CharField(max_length = 200, default=secrets.token_urlsafe(50) + str(uuid.uuid4), unique=True)
    image = models.CharField(max_length=2083)


class Contact(models.Model):
    name = models.CharField(max_length=255,)
    email = models.CharField(max_length=255)
    message = models.TextField(max_length=2083)



class AboutUs(models.Model):
    about = models.CharField(max_length=2083)
    

class Address(models.Model):
    phone = models.CharField(max_length=255,)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=2038)
    
class Home(models.Model):
    img = models.CharField(max_length=2083,)
    title = models.CharField(max_length=255)
    describtion = models.TextField(max_length=2038)
    url = models.CharField(max_length=2083,)
    
    
class Payment(models.Model):
    amount = models.PositiveBigIntegerField()
    prodRef = models.CharField(max_length = 200)
    ref = models.CharField(max_length = 200)
    addressTo = models.CharField(max_length=2083, null = True)
    email = models.EmailField(null = True)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self) -> str:
        return f"Payment: {self.amount}"
    
    def Save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super.save(*args, **kwargs)

    def ref_gen(self)->str:
        while not self.ref:
            refgen = secrets.token_urlsafe(50)
            similar_ref = Payment.objects.filter(ref=refgen)
            if not similar_ref:
                self.ref = refgen
        super.save()
        
    def amount_value(self) -> int:
        amnt = self.amount
        if amnt < 1100:
            return ((1100 - self.amount) + self.amount) * 100
        else:
            return self.amount * 100

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        #status, result = paystack.verify_payment(self.ref)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
                self.save()
        if self.verified:
            return True
        return False
