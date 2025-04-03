import pickle
import sklearn 
import os
import joblib
import numpy as np
from django.shortcuts import render
from .forms import CropPredictionForms
from django.contrib.auth.decorators import login_required

@login_required(login_url='/authlogin/')        
def predict_crop(request):
    if request.method == 'POST':
        form = CropPredictionForms(request.POST)
        if form.is_valid():
            # Load the trained  model
            #model_path = os.path.join(os.path.dirname(__file__), 'savedModels', 'finalized_model.sav')
            #model = joblib.load(model_path)
            #model_path = '/Project_master/Agriexpert/savedModels/finalized_model.sav'
            model_path = 'C:\\Users\\HP\\Desktop\\Project_master\\Agriexpert\\savedModels\\randomforestmodelpickle1.pkl'
            
            model = joblib.load(model_path)
            #print(type(model))   #----------------- <This is only to check the model Type>
            # Extract input data from the form
            new_data = np.array(list(form.cleaned_data.values())).reshape(1, -1)

            # Perform prediction
            predicted_crop = model.predict(new_data)
            #print(predicted_crop)----- For debugging

            # Prepare the response
            context = {
                'form': form,
                #'predicted_crop': (predicted_crop),
                'predicted_crop': str(predicted_crop)[1:-1],
            }
            return render(request, 'croppred.html', context)
    else:
        form = CropPredictionForms()

        context = {'form': form}
    return render(request, 'croppred.html', context)


"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CropPredictionForms
import numpy as np
import joblib
import requests

@login_required(login_url='/authlogin/')
def predict_crop(request):
    if request.method == 'POST':
        form = CropPredictionForms(request.POST)
        if form.is_valid():
            # Load the trained model
            model_path = 'C:\\Users\\HP\\Desktop\\Project_master\\Agriexpert\\savedModels\\randomforestmodelpickle1.pkl'
            model = joblib.load(model_path)
            
            # Extract input data from the form
            inputs = list(form.cleaned_data.values())
            state, city = inputs[0], inputs[1]
            inputs = inputs[2:]  # Get the remaining inputs (N, P, K, Ph)
            
            # Fetch weather data
            api_key = "4f80a23f86c76378175438fff6a163e6"
            weather_data = get_weather_data(api_key, city)
            temperature = weather_data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
            humidity = weather_data['main']['humidity']
            rainfall = get_rainfall_data(weather_data)  # Assuming a function to extract rainfall

            # Include weather data in the inputs
            inputs.extend([temperature, humidity, rainfall])
            new_data = np.array(inputs).reshape(1, -1)
            
            # Perform prediction
            predicted_crop = model.predict(new_data)[0]
            
            # Prepare the response
            context = {
                'form': form,
                'predicted_crop': predicted_crop,
                'weather_data': weather_data,
            }
            return render(request, 'croppred.html', context)
    else:
        form = CropPredictionForms()

    context = {'form': form}
    return render(request, 'croppred.html', context)

def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def get_rainfall_data(weather_data):
    if 'rain' in weather_data and '1h' in weather_data['rain']:
        return weather_data['rain']['1h']
    return 0  # Return 0 if no rainfall data is available


def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def get_rainfall_data(weather_data):
    # Extract rainfall data from the weather API response
    if 'rain' in weather_data and '1h' in weather_data['rain']:
        return weather_data['rain']['1h']
    return 0  # Return 0 if no rainfall data is available
"""
#importing requirements
import pandas as pd
from django.utils.safestring import mark_safe
from .forms import FertilizerForm


@login_required(login_url='/authlogin/')
def fert_recommend(request):
    title = 'AgriAi - Fertilizer Suggestion'
    if request.method == 'POST':
        form = FertilizerForm(request.POST)
        if form.is_valid():
            crop_name = form.cleaned_data['crop_name']
            N = form.cleaned_data['nitrogen']
            P = form.cleaned_data['phosphorous']
            K = form.cleaned_data['pottasium']
            fertilizer_path = 'C:\\Users\\HP\\Desktop\\Project_master\\Agriexpert\\Notebooks\\fertilizer.csv'
            df = pd.read_csv(fertilizer_path)
            nr = df[df['Crop'] == crop_name]['N'].iloc[0]
            pr = df[df['Crop'] == crop_name]['P'].iloc[0]
            kr = df[df['Crop'] == crop_name]['K'].iloc[0]

            n = nr - N
            p = pr - P
            k = kr - K

            temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
            max_value = temp[max(temp.keys())]

            if max_value == "N":
                if n < 0:
                    key = 'NHigh'
                else:
                    key = "Nlow"
            elif max_value == "P":
                if p < 0:
                    key = 'PHigh'
                else:
                    key = "Plow"
            else:
                if k < 0:
                    key = 'KHigh'
                else:
                    key = "Klow"

            response = mark_safe(str(fertilizer_dic[key]))
            return render(request, 'fertilizerresult.html', {'recommendation': response, 'title': title})
    else:
        form = FertilizerForm()
    return render(request, 'fertilizer.html', {'form': form, 'title': title})

# views.py
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SoilTestRequestForm, TrackSoilTestForm
from .models import SoilTestRequest

def request_soil_test(request):
    if request.method == 'POST':
        form = SoilTestRequestForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            SoilTestRequest.objects.create(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode'],
            )
            messages.success(request, 'Your soil test request has been submitted successfully!')
            return redirect('request_soil_test')
    else:
        form = SoilTestRequestForm()

    context = {'form': form}
    return render(request, 'request_soil_test.html', context)

def track_soil_test(request):
    if request.method == 'POST':
        form = TrackSoilTestForm(request.POST)
        if form.is_valid():
            soil_tests = SoilTestRequest.objects.filter(full_name=form.cleaned_data['full_name'])
            context = {'soil_tests': soil_tests, 'form': form}
            return render(request, 'track_soil_test.html', context)
    else:
        form = TrackSoilTestForm()

    context = {'form': form}
    return render(request, 'track_soil_test.html', context)

def all_soil_tests(request):
    soil_tests = SoilTestRequest.objects.all()
    context = {'soil_tests': soil_tests}
    return render(request, 'all_soil_tests.html', context)
# views.py
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import SoilTestRequest

# views.py
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import SoilTestRequest

def generate_pdf(request, tracking_id):
    try:
        soil_test = SoilTestRequest.objects.get(tracking_id=tracking_id)
    except SoilTestRequest.DoesNotExist:
        return HttpResponse("Soil Test Request not found.", status=404)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="soil_test_report_{tracking_id}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    p.drawString(100, height - 100, f"Soil Test Report for {soil_test.full_name}")
    p.drawString(100, height - 120, f"Email: {soil_test.email}")
    p.drawString(100, height - 140, f"Phone Number: {soil_test.phone_number}")
    p.drawString(100, height - 160, f"Address: {soil_test.address}")
    p.drawString(100, height - 180, f"City: {soil_test.city}")
    p.drawString(100, height - 200, f"State: {soil_test.state}")
    p.drawString(100, height - 220, f"Pincode: {soil_test.pincode}")
    p.drawString(100, height - 240, f"Submitted At: {soil_test.submitted_at}")
    p.drawString(100, height - 260, f"Status: {soil_test.status}")
    p.drawString(100, height - 280, f"Tracking ID: {soil_test.tracking_id}")

    p.drawString(100, height - 320, "Soil Test Results:")
    p.drawString(100, height - 340, f"Nitrogen: {soil_test.nitrogen} ppm")
    p.drawString(100, height - 360, f"Phosphorus: {soil_test.phosphorus} ppm")
    p.drawString(100, height - 380, f"Potassium: {soil_test.potassium} ppm")
    p.drawString(100, height - 400, f"pH: {soil_test.pH}")
    p.drawString(100, height - 420, f"Copper: {soil_test.copper} ppm")
    p.drawString(100, height - 440, f"Boron: {soil_test.boron} ppm")
    p.drawString(100, height - 460, f"Sulfur: {soil_test.sulfur} ppm")
    p.drawString(100, height - 480, f"Iron: {soil_test.iron} ppm")
    p.drawString(100, height - 500, f"Zinc: {soil_test.zinc} ppm")

    p.showPage()
    p.save()
    return response

##Fertilizer Sugession List

fertilizer_dic = {
        'NHigh': """The N value of soil is high and might give rise to weeds.
        <br/> <b>Please consider the following suggestions:<b>

        <br/><br/> 1. <i> Manure </i> – adding manure is one of the simplest ways to amend your soil with nitrogen. Be careful as there are various types of manures with varying degrees of nitrogen.

        <br/> 2. <i>Coffee grinds </i> – use your morning addiction to feed your gardening habit! Coffee grinds are considered a green compost material which is rich in nitrogen. Once the grounds break down, your soil will be fed with delicious, delicious nitrogen. An added benefit to including coffee grounds to your soil is while it will compost, it will also help provide increased drainage to your soil.

        <br/>3. <i>Plant nitrogen fixing plants</i> – planting vegetables that are in Fabaceae family like peas, beans and soybeans have the ability to increase nitrogen in your soil

        <br/>4. Plant ‘green manure’ crops like cabbage, corn and brocolli

        <br/>5. <i>Use mulch (wet grass) while growing crops</i> - Mulch can also include sawdust and scrap soft woods""",

        'Nlow': """The N value of your soil is low.
        <br/> Please consider the following suggestions:
        <br/><br/> 1. <i>Add sawdust or fine woodchips to your soil</i> – the carbon in the sawdust/woodchips love nitrogen and will help absorb and soak up and excess nitrogen.

        <br/>2. <i>Plant heavy nitrogen feeding plants</i> – tomatoes, corn, broccoli, cabbage and spinach are examples of plants that thrive off nitrogen and will suck the nitrogen dry.

        <br/>3. <i>Water</i> – soaking your soil with water will help leach the nitrogen deeper into your soil, effectively leaving less for your plants to use.

        <br/>4. <i>Sugar</i> – In limited studies, it was shown that adding sugar to your soil can help potentially reduce the amount of nitrogen is your soil. Sugar is partially composed of carbon, an element which attracts and soaks up the nitrogen in the soil. This is similar concept to adding sawdust/woodchips which are high in carbon content.

        <br/>5. Add composted manure to the soil.

        <br/>6. Plant Nitrogen fixing plants like peas or beans.

        <br/>7. <i>Use NPK fertilizers with high N value.

        <br/>8. <i>Do nothing</i> – It may seem counter-intuitive, but if you already have plants that are producing lots of foliage, it may be best to let them continue to absorb all the nitrogen to amend the soil for your next crops.""",

        'PHigh': """The P value of your soil is high.
        <br/> Please consider the following suggestions:

        <br/><br/>1. <i>Avoid adding manure</i> – manure contains many key nutrients for your soil but typically including high levels of phosphorous. Limiting the addition of manure will help reduce phosphorus being added.

        <br/>2. <i>Use only phosphorus-free fertilizer</i> – if you can limit the amount of phosphorous added to your soil, you can let the plants use the existing phosphorus while still providing other key nutrients such as Nitrogen and Potassium. Find a fertilizer with numbers such as 10-0-10, where the zero represents no phosphorous.

        <br/>3. <i>Water your soil</i> – soaking your soil liberally will aid in driving phosphorous out of the soil. This is recommended as a last ditch effort.

        <br/>4. Plant nitrogen fixing vegetables to increase nitrogen without increasing phosphorous (like beans and peas).

        <br/>5. Use crop rotations to decrease high phosphorous levels""",

        'Plow': """The P value of your soil is low.
        <br/> Please consider the following suggestions:

        <br/><br/>1. <i>Bone meal</i> – a fast acting source that is made from ground animal bones which is rich in phosphorous.

        <br/>2. <i>Rock phosphate</i> – a slower acting source where the soil needs to convert the rock phosphate into phosphorous that the plants can use.

        <br/>3. <i>Phosphorus Fertilizers</i> – applying a fertilizer with a high phosphorous content in the NPK ratio (example: 10-20-10, 20 being phosphorous percentage).

        <br/>4. <i>Organic compost</i> – adding quality organic compost to your soil will help increase phosphorous content.

        <br/>5. <i>Manure</i> – as with compost, manure can be an excellent source of phosphorous for your plants.

        <br/>6. <i>Clay soil</i> – introducing clay particles into your soil can help retain & fix phosphorus deficiencies.

        <br/>7. <i>Ensure proper soil pH</i> – having a pH in the 6.0 to 7.0 range has been scientifically proven to have the optimal phosphorus uptake in plants.

        <br/>8. If soil pH is low, add lime or potassium carbonate to the soil as fertilizers. Pure calcium carbonate is very effective in increasing the pH value of the soil.

        <br/>9. If pH is high, addition of appreciable amount of organic matter will help acidify the soil. Application of acidifying fertilizers, such as ammonium sulfate, can help lower soil pH""",

        'KHigh': """The K value of your soil is high</b>.
        <br/> Please consider the following suggestions:

        <br/><br/>1. <i>Loosen the soil</i> deeply with a shovel, and water thoroughly to dissolve water-soluble potassium. Allow the soil to fully dry, and repeat digging and watering the soil two or three more times.

        <br/>2. <i>Sift through the soil</i>, and remove as many rocks as possible, using a soil sifter. Minerals occurring in rocks such as mica and feldspar slowly release potassium into the soil slowly through weathering.

        <br/>3. Stop applying potassium-rich commercial fertilizer. Apply only commercial fertilizer that has a '0' in the final number field. Commercial fertilizers use a three number system for measuring levels of nitrogen, phosphorous and potassium. The last number stands for potassium. Another option is to stop using commercial fertilizers all together and to begin using only organic matter to enrich the soil.

        <br/>4. Mix crushed eggshells, crushed seashells, wood ash or soft rock phosphate to the soil to add calcium. Mix in up to 10 percent of organic compost to help amend and balance the soil.

        <br/>5. Use NPK fertilizers with low K levels and organic fertilizers since they have low NPK values.

        <br/>6. Grow a cover crop of legumes that will fix nitrogen in the soil. This practice will meet the soil’s needs for nitrogen without increasing phosphorus or potassium.
        """,

        'Klow': """The K value of your soil is low.
        <br/>Please consider the following suggestions:

        <br/><br/>1. Mix in muricate of potash or sulphate of potash
        <br/>2. Try kelp meal or seaweed
        <br/>3. Try Sul-Po-Mag
        <br/>4. Bury banana peels an inch below the soils surface
        <br/>5. Use Potash fertilizers since they contain high values potassium
        """
}