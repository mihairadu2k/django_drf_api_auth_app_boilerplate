from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, role, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email,
                          last_name=last_name,
                          first_name=first_name,
                          role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, role, password=None):
        user = self.create_user(email=email, last_name=last_name, first_name=first_name, role=role)
        user.set_password(password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user
