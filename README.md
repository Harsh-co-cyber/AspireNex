# AspireNex



# Machine Learning Model Prediction using Flask

This repository contains two projects: Titanic Survival Prediction and Iris Species Classification. Both projects use machine learning models integrated into a Flask web application for predictions.

## Titanic Survival Prediction

The Titanic Survival Prediction project predicts whether a passenger would survive the Titanic disaster based on features like passenger class, sex, age, fare, and cabin.

### Features

- Predict survival chances based on input features.
- Simple web interface for input and prediction.

### How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/repositoryname.git
   cd repositoryname
   ```

2. **Set up the virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open a web browser and go to `http://127.0.0.1:5000/`

### Files
You have to save files like index1 and index2 in the templates folder.
Style1 ,style2 and all the images in the static folder.
- `app.py`: The main Flask application file.
- `templates/`: Contains the HTML templates for the web interface.
  - `index1.html`: The main page for input features.
  - `result.html`: The result page displaying the prediction.
- `static/`: Contains static files like CSS.
  - `Style1.css`: The stylesheet for the web interface.
- `titanic_model.pkl`: The trained machine learning model for Titanic survival prediction.
- `preprocessor.pkl`: The preprocessing pipeline used for transforming input data.

## Iris Species Classification

The Iris Species Classification project predicts the species of an iris flower based on features like sepal length, sepal width, petal length, and petal width.

### Features

- Predict iris species based on input features.
- Simple web interface for input and prediction.

### How to Run

1. **Set up the virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**
   ```bash
   python app2.py
   ```

4. **Access the application:**
   Open a web browser and go to `http://127.0.0.1:5000/`

### Files

- `app2.py`: The main Flask application file for the Iris project.
- `templates/`: Contains the HTML templates for the web interface.
  - `index2.html`: The main page for input features.
  - `result2.html`: The result page displaying the prediction.
- `static/`: Contains static files like CSS.
  - `style2.css`: The stylesheet for the web interface.
- `iris_model.pkl`: The trained machine learning model for Iris species classification.
- `preprocessor_iris.pkl`: The preprocessing pipeline used for transforming input data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This template provides an overview of the repository, how to set up and run the applications, and what files are included. Adjust the file names and details as necessary to match your actual repository structure.
