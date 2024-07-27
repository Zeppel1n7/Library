from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from users.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = "__all__"


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = "__all__"


class CustomAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Войти'))
