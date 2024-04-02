from django.db import models


class Email(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="nombre")
    email = models.EmailField(max_length=150, null=False,
                              blank=False,
                              unique=True, verbose_name="correo electronico")
    time = models.DateTimeField(auto_now_add=True,
                                verbose_name="hora")
    status = models.BooleanField(default=False,
                                 verbose_name="estado")

    def __str__(self):
        return self.name
