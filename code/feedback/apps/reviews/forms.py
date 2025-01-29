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
        widget={"attrs": {"placeholder": "Enter Username"}},
    )
    password = forms.PasswordInput()
    # city =
