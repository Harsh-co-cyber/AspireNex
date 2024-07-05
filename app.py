from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__, static_url_path='/static')

# Load the trained model
clf = joblib.load('titanic_model.pkl')

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    input_data = {
        'Pclass': int(request.form['Pclass']),
        'Sex': request.form['Sex'],
        'Age': float(request.form['Age']),
        'Fare': float(request.form['Fare']),
        'Cabin': request.form['Cabin'],
    }
    
    # Preprocess input_data (create DataFrame and preprocess)
    input_df = pd.DataFrame([input_data])
    
    # Predict using the model
    prediction = clf.predict(input_df)
    
    # Prepare response
    if prediction[0] == 1:
        result = 'Survived'
    else:
        result = 'Did not survive'
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=False)
 