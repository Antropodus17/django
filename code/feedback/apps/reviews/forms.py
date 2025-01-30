from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(
        label="Your name",
        max_length=100,
        error_messages={
            "required": "U Bastard",
            f"max_length": "No nobiliary titles, Please",
        },
    )
    review_text = forms.CharField(label="Your feedback", widget=forms.Textarea)
    rating = forms.IntegerField(label="Your rating", max_value=5)

    def __str__(self):
        return super().__str__()


class NovellServicesForm(forms.Form):
    user_name = forms.CharField(
        label="Username",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter Username"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter the password"}),
    )
    city = forms.CharField(
        label="City of enployment:",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter city"}),
    )
    web_server = forms.ChoiceField(
        label="Web Server",
        choices=[("apache", "Apache"), ("nginx", "Nginx")],
        required=False,
    )
    role = forms.ChoiceField(
        label="Chose your role:",
        choices=[
            ("admin", "Admin"),
            ("engineer", "Engineer"),
            ("manager", "Manager"),
            ("guest", "Guest"),
        ],
        required=False,
        widget=forms.RadioSelect(),
    )
    mail = forms.BooleanField(
        label="Mail", required=False, widget=forms.CheckboxInput()
    )
    payroll = forms.BooleanField(
        label="Payroll", required=False, widget=forms.CheckboxInput()
    )
    self_service = forms.BooleanField(
        label="Self Service", required=False, widget=forms.CheckboxInput()
    )
