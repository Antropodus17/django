from django import forms  # type: ignore

from .models import Review, NovellServiceModel


# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = "__all__"
#         labels = {
#             "user_name": "Enter your username",
#             "review_text": "Review Content",
#             "rating": "Your Raiting",
#         }
#         error_messages = {
#             "user_name": {
#                 "required": "U Bastard",
#                 "max_length": "No nobiliary titles, Please",
#             }
#         }

############    WITH MODEL.FORM    #######


#     user_name = forms.CharField(
#         label="Your name",
#         max_length=100,
#         error_messages={
#             "required": "U Bastard",
#             f"max_length": "No nobiliary titles, Please",
#         },
#     )
#     review_text = forms.CharField(label="Your feedback", widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your rating", max_value=5)

#     def __str__(self):
#         return super().__str__()


# class NovellServicesForm(forms.Form):
#     user_name = forms.CharField(
#         label="Username",
#         max_length=50,
#         required=True,
#         widget=forms.TextInput(attrs={"placeholder": "Enter Username"}),
#     )
#     password = forms.CharField(
#         label="Password",
#         widget=forms.PasswordInput(attrs={"placeholder": "Enter the password"}),
#     )
#     city = forms.CharField(
#         label="City of enployment:",
#         max_length=50,
#         required=True,
#         widget=forms.TextInput(attrs={"placeholder": "Enter city"}),
#     )
#     web_server = forms.ChoiceField(
#         label="Web Server",
#         choices=[("1", "Apache"), ("2", "Nginx")],
#     )
#     role = forms.ChoiceField(
#         label="Chose your role:",
#         choices=[
#             ("1", "Admin"),
#             ("2", "Engineer"),
#             ("3", "Manager"),
#             ("4", "Guest"),
#         ],
#         required=False,
#         widget=forms.RadioSelect(),
#     )

#     sign_on = forms.MultipleChoiceField(
#         choices=[("1", "Mail"), ("2", "Payroll"), ("3", "Self-Service")],
#         required=False,
#         widget=forms.CheckboxSelectMultiple(),
#     )


####START EJERCICIO 5.2
class NovellServicesForm(forms.ModelForm):
    class Meta:
        model = NovellServiceModel
        fields = "__all__"
        labels = {
            "user_name": "Username",
            "password": "Password",
            "city": "City of enployment:",
            "web_server": "Web server",
            "role": "Chose your role",
        }
        widgets = {
            "password": forms.PasswordInput(),
            "role": forms.RadioSelect(
                choices=[
                    ("1", "Admin"),
                    ("2", "Engineer"),
                    ("3", "Manager"),
                    ("4", "Guest"),
                ],
            ),
            "web_server": forms.Select(choices=[("1", "Apache"), ("2", "Nginx")]),
            "sign_on": forms.CheckboxSelectMultiple(
                choices=[("1", "Mail"), ("2", "Payroll"), ("3", "Self-Service")],
            ),
        }
