"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from MachineLeaningService import app
from keras.models import load_model
from MachineLeaningService.collectdata import CollectTraningData
import json
from MachineLeaningService.dataset import CreateTestSet

# Build Model
# Input1 Forcast

# Load Model
model = load_model("E:/Works/2018B/LinearRegressionTechnicalAnalyService/Service/LinearRegressionTecnicalService/MachineLeaningService/MachineLeaningService/Model/model_ep0")

# Prepeare Data





@app.route('/')
@app.route('/home')
def home():

    
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    labels = []
    # trainingset = CollectTraningData("trainingset",labels)
    
    testset = CreateTestSet(labels, 20)
    
    investorLog = testset[6]
    
    # Evaluate
    result = model.predict([testset[0], testset[1], testset[2], testset[3], testset[4],testset[5]])

    MakedecisionbyEvaluateValue(result, investorLog, 20)

    with open("Data09112018/testresult.csv","w+") as my_csv:   
        csvWriter = csv.writer(my_csv, delimiter=',')  # using the csv module to write the file
        csvWriter.writerows(investorLog)

    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/foo', methods=['POST']) 
def foo():

    if not request.json:
        abort(400)
    print (request.json)
    data = json.load(request.json)

    return json.dumps(request.json)