from django import forms

#class CropPredictionForms(forms.Form):
    #N = forms.IntegerField(label='Nitrogen', min_value=0,help_text = "Enter the value (example:50)")
    #P = forms.IntegerField(label='Phosphorous', min_value=0,help_text = "Enter the value (example:50)")
   # K = forms.IntegerField(label='Potassium', min_value=0,help_text = "Enter the value (example:50)")
    #temperature = forms.DecimalField(label='Temperature', min_value=0, decimal_places=2,help_text = "Enter the value (example:50)")
    #humidity = forms.DecimalField(label='Humidity', min_value=0, decimal_places=2,help_text = "Enter the value (example:50)")
    #Ph = forms.DecimalField(label='Ph', min_value=0,help_text = "Enter the Ph value (value between 0-14)")
    #rainfall = forms.DecimalField(label='Rainfall', min_value=0, decimal_places=2,help_text = "Enter the value (example:50)")
class CropPredictionForms(forms.Form):
    N = forms.IntegerField(
        label='Nitrogen',
        min_value=0,
        max_value=200,
        help_text="Enter the value (example:50)",
        error_messages={
            'required': 'Nitrogen value is required.',
            'min_value': 'Value cannot be negative.',
            'max_value': 'Value cannot be greater than 100.'
        }
    )
    P = forms.IntegerField(
        label='Phosphorous',
        min_value=0,
        max_value=200,
        help_text="Enter the value (example:50)",
        error_messages={
            'required': 'Phosphorous value is required.',
            'min_value': 'Value cannot be negative.',
            'max_value': 'Value cannot be greater than 100.'
        }
    )
    K = forms.IntegerField(
        label='Potassium',
        min_value=0,
        max_value=300,
        help_text="Enter the value (example:50)",
        error_messages={
            'required': 'Potassium value is required.',
            'min_value': 'Value cannot be negative.',
            'max_value': 'Value cannot be greater than 100.'
        }
    )
    temperature = forms.DecimalField(
        label='Temperature',
        min_value=0,
        max_value=50,
        decimal_places=2,
        help_text="Enter the value (example:50)",
        error_messages={
            'required': 'Temperature value is required.',
            'min_value': 'Value cannot be negative.',
            'max_value': 'Value cannot be greater than 50.Because it is less Possible.Which may give Inaccurate result'
        }
    )
    humidity = forms.DecimalField(
        label='Humidity',
        min_value=0,
        max_value=100,
        decimal_places=2,
        help_text="Enter the value (example:50)",
        error_messages={
            'required': 'Humidity value is required.',
            'min_value': 'Value cannot be negative.',
            'max_value': 'Value cannot be greater than 100.'
        }
    )
    Ph = forms.DecimalField(
        label='Ph',
        min_value=0,
        max_value=14,
        help_text="Enter the Ph value (value between 0-14)",
        error_messages={
            'required': 'Ph value is required.',
            'min_value': 'Value cannot be negative.',
            'max_value': 'Value cannot be greater than 14.'
        }
    )
    rainfall = forms.DecimalField(
        label='Rainfall',
        min_value=0,
        max_value=500,
        decimal_places=2,
        help_text="Enter the value (example:50) Rainfall MM",
        error_messages={
            'required': 'Rainfall value is required.',
            'min_value': 'Value cannot be negative.',
            'max_value': 'Value cannot be greater than 200.'
        }
    )


from django import forms

from django import forms

class FertilizerForm(forms.Form):
    crop_choices = [
        ('rice', 'Rice'),
        ('wheat', 'Wheat'),
        ('maize', 'maize'),
        ('chickpea', 'chickpea'),
        ('chickpea', 'chickpea'),
        ('kidneybeans', 'kidneybeans'),
        ('pigeonpeas', 'pigeonpeas'),
        ('mothbeans', 'mothbeans'),
        ('pomegranate', 'pomegranate'),
        ('mango', 'mango'),
        ('banana', 'banana'),
        ('papaya', 'papaya'),
        
        
        # Add more crop choices as needed
    ]

    crop_name = forms.ChoiceField(
        choices=crop_choices,
        help_text="Select the crop name",
        error_messages={
            'required': 'Crop name is required.',
        }
    )

    nitrogen = forms.IntegerField(
        min_value=0,
        max_value=200,
        help_text="Enter the value (example:50)",
        error_messages={
            'required': 'Nitrogen value is required.',
            'min_value': 'Value cannot be negative.',
            'max_value': 'Value cannot be greater than 200.'
        }
    )

    phosphorous = forms.IntegerField(
        min_value=0,
        max_value=200,
        help_text="Enter the value (example:50)",
        error_messages={
            'required': 'Phosphorous value is required.',
            'min_value': 'Value cannot be negative.',
            'max_value': 'Value cannot be greater than 200.'
        }
    )

    pottasium = forms.IntegerField(
        min_value=0,
        max_value=300,
        help_text="Enter the value (example:50)",
        error_messages={
            'required': 'Pottasium value is required.',
            'min_value': 'Value cannot be negative.',
            'max_value': 'Value cannot be greater than 300.'
        }
    )

class SoilTestRequestForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    address = forms.CharField(widget=forms.Textarea, label='Detailed Address')
    city = forms.CharField(max_length=100, label='City')
    state = forms.CharField(max_length=100, label='State')
    pincode = forms.CharField(max_length=10, label='Pincode')

class TrackSoilTestForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Full Name')
















"""
# forms.py
from django import forms

# Define state_arr and s_a at the module level
state_arr = ["Andaman & Nicobar", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", 
             "Chandigarh", "Chhattisgarh", "Dadra & Nagar Haveli", "Daman & Diu", "Delhi", 
             "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand", 
             "Karnataka", "Kerala", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", 
             "Meghalaya", "Mizoram", "Nagaland", "Orissa", "Pondicherry", "Punjab", "Rajasthan", 
             "Sikkim", "Tamil Nadu", "Tripura", "Uttar Pradesh", "Uttaranchal", "West Bengal"]

s_a = [
    "",
    "Anandapur|Angul|Anugul|Aska|Athgarh|Athmallik|Attabira|Bagdihi|Balangir|Balasore|Baleswar|Baliguda|Balugaon|Banaigarh|Bangiriposi|Barbil|Bargarh|Baripada|Barkot|Basta|Berhampur|Betanati|Bhadrak|Bhanjanagar|Bhawanipatna|Bhubaneswar|Birmaharajpur|Bisam Cuttack|Boriguma|Boudh|Buguda|Chandbali|Chhatrapur|Chhendipada|Cuttack|Daringbadi|Daspalla|Deodgarh|Deogarh|Dhanmandal|Dharamgarh|Dhenkanal|Digapahandi|Dunguripali|G. Udayagiri|Gajapati|Ganjam|Ghatgaon|Gudari|Gunupur|Hemgiri|Hindol|Jagatsinghapur|Jajpur|Jamankira|Jashipur|Jayapatna|Jeypur|Jharigan|Jharsuguda|Jujumura|Kalahandi|Kalimela|Kamakhyanagar|Kandhamal|Kantabhanji|Kantamal|Karanjia|Kashipur|Kendrapara|Kendujhar|Keonjhar|Khalikote|Khordha|Khurda|Komana|Koraput|Kotagarh|Kuchinda|Lahunipara|Laxmipur|M. Rampur|Malkangiri|Mathili|Mayurbhanj|Mohana|Motu|Nabarangapur|Naktideul|Nandapur|Narlaroad|Narsinghpur|Nayagarh|Nimapara|Nowparatan|Nowrangapur|Nuapada|Padampur|Paikamal|Palla Hara|Papadhandi|Parajang|Pardip|Parlakhemundi|Patnagarh|Pattamundai|Phiringia|Phulbani|Puri|Puruna Katak|R. Udayigiri|Rairakhol|Rairangpur|Rajgangpur|Rajkhariar|Rayagada|Rourkela|Sambalpur|Sohela|Sonapur|Soro|Subarnapur|Sunabeda|Sundergarh|Surada|T. Rampur|Talcher|Telkoi|Titlagarh|Tumudibandha|Udala|Umerkote",
    # Add more city entries for each state...
]

class CropPredictionForms(forms.Form):
    state = forms.ChoiceField(choices=[(state, state) for state in state_arr], label="State")
    city = forms.ChoiceField(choices=[], label="City")

    N = forms.IntegerField(
        label='Nitrogen',
        min_value=0,
        max_value=200,
        help_text="Enter the value (example: 50)"
    )
    P = forms.IntegerField(
        label='Phosphorous',
        min_value=0,
        max_value=200,
        help_text="Enter the value (example: 50)"
    )
    K = forms.IntegerField(
        label='Potassium',
        min_value=0,
        max_value=300,
        help_text="Enter the value (example: 50)"
    )
    Ph = forms.DecimalField(
        label='Ph',
        min_value=0,
        max_value=14,
        help_text="Enter the Ph value (value between 0-14)"
    )

    class Meta:
        fields = ['state', 'city', 'N', 'P', 'K', 'Ph']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'state' in self.data:
            state_name = self.data.get('state')
            if state_name in state_arr:
                state_index = state_arr.index(state_name)
                self.fields['city'].choices = [(city, city) for city in s_a[state_index].split("|")]
"""
