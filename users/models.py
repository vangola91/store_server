from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'


    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={'email':self.user.email, 'code':self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subjact = f"Подверждение учетной записи для {self.user.username}"
        message = 'Для подверждения учотной записи для {} перейдите по ссылке: {}'.format(
            self.user.email,
            verification_link
        )
        send_mail(
            subject=subjact,
            message=message,
            from_email='vangola91@gmail.com',
            recipient_list =[self.user.email],
            fail_silently=False,
        )
