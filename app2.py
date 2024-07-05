from flask import Flask, render_template, request
import joblib
import pandas as pd
app2 = Flask(__name__, static_url_path='/static')
clf = joblib.load('titanic_model.pkl')
@app2.route('/')
def home():
    return render_template('index2.html')
@app2.route('/predict', methods=['POST'])
def predict():
    # Get form data
    input_data = {
        'sepal_length' : float(request.form['sepal_length']),
        'sepal_width': float(request.form['sepal_width']), 
        'petal_length': float(request.form['petal_length']), 
        'petal_width': float(request.form['petal_width'])
    }
    
    # Preprocess input_data (create DataFrame and preprocess)
    input_df = pd.DataFrame([input_data])
    
    
    # Predict using the model
    prediction = clf.predict(input_df)
    
    # Prepare response
    if prediction[0] == 1:
        result = 'Iris-versicolor'
    elif prediction[0]== 2:
        result = 'Iris-virginica'
    else:
        result = 'Iris-setosa'
    
    return render_template('result2.html', result=result)

if __name__ == '__main__':
    app2.run(debug=False)