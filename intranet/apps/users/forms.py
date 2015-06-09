from django import forms

class ProfileEditForm(forms.Form):
    """A form containing editable fields in the User model."""
    student_id = forms.IntegerField(label="FCPS Student ID")
    first_name = forms.CharField(label="First Name")
    middle_name = forms.CharField(label="Middle Name")
    last_name = forms.CharField(label="Last Name")
    title = forms.CharField(label="Title")
    nickname = forms.CharField(label="Nickname")
    graduation_year = forms.IntegerField(label="Grade")
    sex = forms.CharField(label="Sex (M or F)")
    birthday = forms.DateField(label="Birth Date")
    home_phone = forms.CharField(label="Home Phone")

    street = forms.CharField(label="Street")
    city = forms.CharField(label="City")
    state = forms.CharField(label="State")
    postal_code = forms.CharField(label="ZIP")
    #counselor = forms.CharField(label="Counselor")
    #locker = forms.CharField(label="Locker")
    
    FIELDS = ["student_id",
               "first_name",
               "middle_name",
               "last_name",
               "title",
               "nickname",
               "graduation_year",
               "sex",
               "birthday",
               "home_phone",
               "counselor"]
    ADDRESS_FIELDS = ["street",
                       "city",
                       "state",
                       "postal_code"]
