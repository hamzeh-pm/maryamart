from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from utils.validators import validate_mobile


# Create your models here.
class AccountManager(BaseUserManager):
    """
    Model manager for Account Class create_user, create_superuser
    email, mobile, password must be set
    """

    def create_user(self, email, mobile, password, **extra_fields):
        """
        Create and save a User with the given email, mobile and password.
        """
        if not email:
            raise ValueError("Email must be set")

        if not mobile:
            raise ValueError("Mobile must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, mobile, password, **extra_fields):
        """
        Create and save a SuperUser with the given email, mobile and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", "AD")

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, mobile, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        CLIENT = "CL", "Client"
        ARTIST = "AR", "Artist"
        ADMIN = "AD", "Admin"

    email = models.EmailField("email_address", unique=True)
    mobile = models.CharField(
        "cellphone_number", max_length=10, unique=True, validators=[validate_mobile]
    )
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=2, choices=Role.choices, default=Role.CLIENT)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # specific field for artist role
    picture = models.ImageField(upload_to="profile/'%Y/%m/%d'")
    bio = models.TextField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile"]

    objects = AccountManager()

    def __str__(self):
        return self.email
