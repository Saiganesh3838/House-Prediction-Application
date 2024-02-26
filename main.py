import pandas as pd
from flask import *
import pickle
import numpy as np

app = Flask(__name__)
data=pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open('RidgeModel.pkl', 'rb'))

@app.route('/')
def message():
    locations=sorted(data['location'].unique())
    return render_template('index.html',locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get("location")
    bhk = request.form.get("bhk")
    bath = request.form.get("bath")
    sqft = request.form.get("total_sqrt")
    print(location, bhk, bath, sqft)
    cinput = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
    prediction = pipe.predict(cinput)[0] * 1e5
    return str(np.round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)