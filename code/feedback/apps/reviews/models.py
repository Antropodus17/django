from django.db import models  # type: ignore

# Create your models here.


class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.id}. Review"


class NovellServiceModel(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(
        max_length=50,
    )
    city = models.CharField(max_length=50)
    web_server = models.IntegerField()
    role = models.IntegerField()
    sign_on = models.CharField(max_length=20)

    def save(self):
        if type(self.sign_on) == list:
            try:
                self.sign_on = ":".join(self.sign_on)
            except:
                raise ValueError("Could`nt parse the role")
        return super().save()
