📊 Sales Prediction System

A machine learning-based Sales Prediction System that predicts product sales based on TV, Radio, and Newspaper advertising budgets. The project uses Multiple Linear Regression and provides an interactive Streamlit web application for data analysis, visualization, model evaluation, and sales prediction.

---

🚀 Project Overview

Advertising expenditure plays an important role in determining product sales. This project analyzes the relationship between advertising budgets across different media channels and sales.

The system uses historical advertising data to train a machine learning model and predict expected sales based on user-provided advertising budgets.

🎯 Objective

- Analyze advertising expenditure and its relationship with sales.
- Perform exploratory data analysis and visualization.
- Build a Multiple Linear Regression model.
- Evaluate model performance using standard regression metrics.
- Provide an interactive interface for making sales predictions.
- Help understand which advertising channels have stronger relationships with sales.

---

🛠️ Technologies Used

- Python
- Pandas – Data processing and analysis
- NumPy – Numerical computations
- Scikit-learn – Machine learning
- Matplotlib – Data visualization
- Seaborn – Statistical visualization
- Streamlit – Interactive web application

---

📂 Dataset

The project uses the Advertising dataset, containing 200 records with the following variables:

Feature| Description
TV| Advertising budget spent on TV
Radio| Advertising budget spent on Radio
Newspaper| Advertising budget spent on Newspaper
Sales| Product sales

The three advertising features are used as input variables, while Sales is the target variable.

---

🔄 Machine Learning Workflow

Advertising Dataset
        ↓
Data Cleaning & Validation
        ↓
Exploratory Data Analysis
        ↓
Correlation Analysis
        ↓
Train-Test Split (80:20)
        ↓
Multiple Linear Regression
        ↓
Model Evaluation
        ↓
Interactive Sales Prediction

---

🤖 Machine Learning Model

The project uses Multiple Linear Regression from Scikit-learn.

The model learns the relationship between advertising expenditure and sales using:

TV + Radio + Newspaper → Sales

Model Equation

The trained model produced approximately:

Sales = 2.9791
        + 0.04473 × TV
        + 0.18920 × Radio
        + 0.00276 × Newspaper

---

📈 Model Performance

The dataset was divided into 80% training data and 20% testing data using "random_state=42".

Evaluation Metric| Score
R² Score| 0.8994
MAE| 1.4608
MSE| 3.1741
RMSE| 1.7816

The model achieved an R² score of approximately 89.94% on the test set.

«Note: These results correspond to the specific train-test split used in this project and may vary if the dataset split or model configuration is changed.»

---

🔍 Exploratory Data Analysis

The application performs several analyses to understand the dataset and model behavior.

Dataset Analysis

- Dataset shape
- Data types
- Missing-value detection
- Duplicate-value detection
- Statistical summary
- Feature distributions

Correlation Analysis

The approximate correlations with Sales are:

Feature| Correlation with Sales
TV| 0.7822
Radio| 0.5762
Newspaper| 0.2283

These values describe the relationship observed in this dataset; correlation does not by itself establish causation.

---

📊 Visualizations

The project includes:

- 📌 Correlation Heatmap
- 📌 TV vs Sales Scatter Plot
- 📌 Radio vs Sales Scatter Plot
- 📌 Newspaper vs Sales Scatter Plot
- 📌 Sales Distribution Histogram
- 📌 Actual vs Predicted Sales Plot
- 📌 Residual Analysis Plot

---

💻 Streamlit Application

The project includes an interactive Streamlit interface with three major sections:

1. Dataset Overview

Displays:

- Dataset information
- Statistical summary
- Missing values
- Duplicate records
- Dataset structure

2. Visualizations

Provides interactive visual analysis of:

- Advertising channels
- Sales relationships
- Correlations
- Model predictions
- Residuals

3. Model & Prediction

Users can enter advertising budgets for:

TV
Radio
Newspaper

The trained machine learning model then generates the predicted sales value.

---

📁 Project Structure

sales-prediction-system/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── Advertising.csv
│
└── output/
    ├── actual_vs_predicted.png
    ├── correlation_heatmap.png
    ├── residual_plot.png
    ├── sales_histogram.png
    └── scatter_plots.png


---

⚙️ Installation & Setup

1. Clone the repository

git clone https://github.com/PrakharRai14/sales-prediction-system.git

2. Navigate to the project directory

cd sales-prediction-system

3. Create a virtual environment (Optional)

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Run the Streamlit application

streamlit run app.py

The application will open in your browser.

---

📦 Requirements

The main libraries used in the project are:

pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit

All dependencies are listed in "requirements.txt".

---

💡 Key Insights

- TV advertising has the strongest correlation with Sales among the three advertising channels in this dataset.
- Radio also shows a meaningful positive relationship with Sales.
- Newspaper has a comparatively weaker relationship with Sales.
- Multiple Linear Regression provides a strong baseline for this dataset.
- Visual and residual analysis helps evaluate how well the model fits the test data.

---

🔮 Future Improvements

Potential improvements include:

- Compare Linear Regression with Random Forest, Gradient Boosting, and other regression models.
- Perform cross-validation for more robust model evaluation.
- Add feature scaling and feature engineering where appropriate.
- Add hyperparameter tuning for alternative models.
- Deploy the application using Streamlit Community Cloud or another cloud platform.
- Add downloadable prediction reports.
- Add more recent or domain-specific advertising datasets.
- Monitor model performance when new data becomes available.

---

👨‍💻 Author

Prakhar Rai

B.Tech CSE (AI & ML) | Batch 2027

GitHub:
https://github.com/PrakharRai14

---

⭐ Project Highlights

✔ Machine Learning Regression
✔ Exploratory Data Analysis
✔ Data Visualization
✔ Model Evaluation
✔ Interactive Streamlit Application
✔ Real-time Sales Prediction
✔ Business-oriented ML Use Case

If you find this project useful, consider giving the repository a ⭐.
