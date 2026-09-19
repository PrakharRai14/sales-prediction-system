import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

st.set_page_config(page_title="Sales Prediction", layout="wide")

st.title("📊 Sales Prediction Project")
st.markdown("Predict sales based on **TV**, **Radio**, and **Newspaper** advertising budget")

# data load kr rhe h
try:
    df = pd.read_csv('data/Advertising.csv')
except FileNotFoundError:
    st.error("Advertising.csv file not found in data/ folder!")
    st.stop()

# extra index column hata rhe h
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

# sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dataset Overview", "Visualizations", "Model & Prediction"])

# feature aur target
x = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

# model train kr rhe h
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
prediction = model.predict(x_test)

# metrics calculate
r2 = r2_score(y_test, prediction)
mae = mean_absolute_error(y_test, prediction)
mse = mean_squared_error(y_test, prediction)
rmse = np.sqrt(mse)


if page == "Dataset Overview":
    st.header("📋 Dataset Overview")

    st.subheader("First 5 Rows")
    st.dataframe(df.head())

    st.subheader("Last 5 Rows")
    st.dataframe(df.tail())

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Duplicates", df.duplicated().sum())

    st.subheader("Data Types")
    st.dataframe(df.dtypes.rename("Type"))

    # missing value check
    st.subheader("Missing Values")
    st.dataframe(df.isnull().sum().rename("Count"))

    st.subheader("Statistical Summary")
    st.dataframe(df.describe())


elif page == "Visualizations":
    st.header("📈 Visualizations")

    # correlation heatmap
    st.subheader("Correlation Heatmap")
    fig1, ax1 = plt.subplots(figsize=(7, 4))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax1)
    st.pyplot(fig1)

    # scatter plots
    st.subheader("Feature vs Sales")
    fig2, axes = plt.subplots(1, 3, figsize=(14, 4))

    axes[0].scatter(df['TV'], df['Sales'], color='blue', alpha=0.5)
    axes[0].set_xlabel('TV')
    axes[0].set_ylabel('Sales')
    axes[0].set_title('TV vs Sales')

    axes[1].scatter(df['Radio'], df['Sales'], color='green', alpha=0.5)
    axes[1].set_xlabel('Radio')
    axes[1].set_ylabel('Sales')
    axes[1].set_title('Radio vs Sales')

    axes[2].scatter(df['Newspaper'], df['Sales'], color='red', alpha=0.5)
    axes[2].set_xlabel('Newspaper')
    axes[2].set_ylabel('Sales')
    axes[2].set_title('Newspaper vs Sales')

    plt.tight_layout()
    st.pyplot(fig2)

    # sales histogram
    st.subheader("Sales Distribution")
    fig3, ax3 = plt.subplots(figsize=(7, 4))
    ax3.hist(df['Sales'], bins=15, color='skyblue', edgecolor='black')
    ax3.set_xlabel('Sales')
    ax3.set_ylabel('Frequency')
    ax3.set_title('Sales Distribution')
    st.pyplot(fig3)

    # actual vs predicted
    st.subheader("Actual vs Predicted")
    fig4, ax4 = plt.subplots(figsize=(6, 5))
    ax4.scatter(y_test, prediction, color='blue', alpha=0.6)
    ax4.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
    ax4.set_xlabel('Actual Sales')
    ax4.set_ylabel('Predicted Sales')
    ax4.set_title('Actual vs Predicted')
    st.pyplot(fig4)

    # residual plot
    st.subheader("Residual Analysis")
    residuals = y_test - prediction
    fig5, ax5 = plt.subplots(figsize=(6, 5))
    ax5.scatter(prediction, residuals, color='purple', alpha=0.6)
    ax5.axhline(y=0, color='red', linestyle='--')
    ax5.set_xlabel('Predicted Sales')
    ax5.set_ylabel('Residuals')
    ax5.set_title('Residual Analysis')
    st.pyplot(fig5)


elif page == "Model & Prediction":
    st.header("🤖 Model Performance")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("R² Score", f"{r2:.4f}")
    col2.metric("MAE", f"{mae:.4f}")
    col3.metric("MSE", f"{mse:.4f}")
    col4.metric("RMSE", f"{rmse:.4f}")

    st.markdown("---")

    # user input prediction
    st.header("🔮 Predict Sales")
    st.markdown("Enter advertising budget to predict sales")

    col1, col2, col3 = st.columns(3)
    tv = col1.number_input("TV Budget", min_value=0.0, max_value=500.0, value=150.0,step=5.0)
    radio = col2.number_input("Radio Budget", min_value=0.0, max_value=500.0, value=30.0,step=5.0)
    newspaper = col3.number_input("Newspaper Budget", min_value=0.0, max_value=500.0, value=20.0,step=5.0)

    if st.button("Predict Sales"):
        input_data = pd.DataFrame({'TV': [tv], 'Radio': [radio], 'Newspaper': [newspaper]})
        result = model.predict(input_data)
        st.success(f"📌 Predicted Sales: **{result[0]:.2f}** units")

    st.markdown("---")

    # business insights
    st.header("💡 Business Insights")
    st.info(f"📺 TV advertising ka Sales pe sabse zyada impact hai (correlation: {df['TV'].corr(df['Sales']):.2f})")
    st.info(f"📻 Radio bhi achha contributor hai (correlation: {df['Radio'].corr(df['Sales']):.2f})")
    st.warning(f"📰 Newspaper ka Sales pe bahut kam impact hai (correlation: {df['Newspaper'].corr(df['Sales']):.2f})")
    st.success(f"✅ Model {r2*100:.1f}% variance explain kr rha hai")
    st.markdown("**Conclusion:** TV aur Radio pe zyada invest karna chahiye, Newspaper pe kam")
