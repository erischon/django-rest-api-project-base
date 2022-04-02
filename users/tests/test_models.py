import pytest

from django.contrib.auth import get_user_model


@pytest.mark.django_db
class TestCustomUserModel:
    """
    Test
    """

    def setup_method(self):
        self.email_1 = "test@email.com"
        self.email_2 = "test@EMAiL.cOm"
        self.password = "Test123"

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with email is successful.
        """
        user = get_user_model().objects.create_user(
            email=self.email_1,
            password=self.password,
        )

        assert user.email == self.email_1
        assert user.check_password(self.password) is True

    def test_new_user_email_normalized(self):
        """
        Test the email for a new user is normalize.
        """
        user = get_user_model().objects.create_user(self.email_2, "test123")

        assert user.email == self.email_2.lower()

    def test_new_user_invalid_email(self):
        """
        Test creating user with no email raises error.
        """
        with pytest.raises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """
        Test creating a new superuser.
        """
        user = get_user_model().objects.create_superuser(
            self.email_1,
            self.password,
        )

        assert user.is_superuser is True
        assert user.is_staff is True
