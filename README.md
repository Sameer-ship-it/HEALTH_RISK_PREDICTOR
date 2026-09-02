# 🩺 Health Risk Predictor

A machine learning-based **Health Risk Prediction web application** built with **Python, Scikit-learn, and Streamlit**.

The application takes lifestyle and health-related inputs such as age, diet quality, exercise frequency, sleep duration, stress level, BMI, smoking, alcohol consumption, and family history, and predicts the user's overall **health risk level**.

> **Note:** This project is for educational and demonstration purposes only. It is not a medical diagnostic system.

---

## 🚀 Features

* Predicts health risk level using a Machine Learning model
* Interactive web interface built with Streamlit
* Takes multiple lifestyle and health-related inputs
* Converts categorical data using Label Encoding
* Uses a trained Random Forest Classifier
* Displays the predicted risk level
* Provides a visualization of selected health factors
* Saved trained model and encoders are loaded using Pickle

---

## 🧠 Machine Learning

### Algorithm Used

**Random Forest Classifier**

The model was trained using:

* `n_estimators = 100`
* `random_state = 42`

Random Forest was selected after experimenting with Logistic Regression and Random Forest.

The project notebook records approximately **96% accuracy for the Random Forest model**, while Logistic Regression was noted at approximately 85%.

> Accuracy should be independently verified using the final test set before treating these numbers as official benchmark results.

---

## 📊 Input Features

The model uses the following features:

| Feature             | Description                      |
| ------------------- | -------------------------------- |
| Age                 | User's age                       |
| Diet Quality        | Poor / Average / Good            |
| Exercise Days       | Number of exercise days per week |
| Sleep Hours         | Average sleep duration           |
| Stress Level        | Low / Medium / High              |
| BMI                 | Body Mass Index                  |
| Smoking             | Yes / No                         |
| Alcohol Consumption | Low / Medium / High              |
| Family History      | Yes / No                         |

The training dataset contains the same feature structure and a target column named `risk_level`.

---

## 🔄 Project Workflow

```text
                ┌─────────────────────┐
                │   Health Dataset    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Data Preprocessing  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Label Encoding      │
                │ Categorical Data    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Train/Test Split    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Random Forest       │
                │ Classifier          │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Save Model +        │
                │ Encoders using      │
                │ Pickle              │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Streamlit Web App   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Predicted Risk      │
                │ Level               │
                └─────────────────────┘
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**
* **Matplotlib**
* **Plotly**
* **Pickle**

---

## 📁 Project Structure

```text
Health-Risk-Predictor/
│
├── app.py
├── Health_RiskPredictor.pkl
├── label_encoder.pkl
├── synthetic_health_data.csv
├── requirements.txt
└── README.md
```

### File Description

| File                        | Purpose                     |
| --------------------------- | --------------------------- |
| `app.py`                    | Streamlit application       |
| `Health_RiskPredictor.pkl`  | Trained Random Forest model |
| `label_encoder.pkl`         | Saved LabelEncoder objects  |
| `synthetic_health_data.csv` | Dataset used for training   |
| `requirements.txt`          | Required Python packages    |
| `README.md`                 | Project documentation       |

The trained model and encoder dictionary were serialized using Pickle for use inside the Streamlit application.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/health-risk-predictor.git
```

### 2. Navigate to the project directory

```bash
cd health-risk-predictor
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💻 How It Works

The user enters their health and lifestyle information through the Streamlit interface.

The categorical inputs are converted into numerical values using the previously trained LabelEncoders.

The resulting feature vector is passed to the trained Random Forest model:

```python
prediction = model.predict([input_data])
```

The numerical prediction is then converted back into a human-readable risk level using the saved `risk_level` encoder.

---

## 📈 Visualization

The application also displays a pie chart representing selected health-related factors including:

* Diet
* Exercise
* Sleep
* Stress
* BMI

This provides a simple visual representation alongside the prediction.

---

## 🎯 Example

### Input

```text
Age: 25
Diet Quality: Good
Exercise Days: 5
Sleep Hours: 8
Stress Level: Low
BMI: 22
Smoking: No
Alcohol Consumption: Low
Family History: No
```

### Output

```text
Predicted Risk Level: Low
```

*The actual output depends on the trained model and encoded input values.*

---

## 🔬 Model Training

The dataset is divided into training and testing sets using an **80/20 split** with `random_state=42`.

Categorical columns are converted into numerical representations using Scikit-learn's `LabelEncoder`.

The target variable is:

```text
risk_level
```

Possible risk categories in the dataset include:

```text
Low
Medium
High
```

---

## ⚠️ Limitations

* The dataset used for this project is synthetic.
* The prediction should not be interpreted as a medical diagnosis.
* Model performance depends heavily on the quality and representativeness of the training dataset.
* The current application uses a relatively small set of health and lifestyle features.
* The recorded accuracy should not be considered evidence of clinical reliability.

---

## 🔮 Future Improvements

* Use a larger and clinically validated dataset
* Add additional health parameters
* Compare multiple ML algorithms
* Add proper model evaluation metrics
* Display prediction probabilities
* Add feature importance analysis
* Improve UI/UX
* Deploy the application online
* Add personalized health recommendations
* Implement cross-validation and hyperparameter tuning

---

## 👨‍💻 Author

**Sameer Raza**

Computer Science / AI & Machine Learning Project

---

## 📜 Disclaimer

This project was developed for **educational and demonstration purposes**.

The predictions generated by this application should **not be used for medical diagnosis, treatment, or healthcare decisions**. Always consult a qualified healthcare professional for medical advice.
