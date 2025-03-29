import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('HR-Employee-Attrition.csv')

# Set up Streamlit page
st.set_page_config(page_title="HR Attrition EDA", layout="wide")
st.title("📊 HR Attrition EDA Dashboard 🚀")
st.sidebar.header("🔍 Navigation")

# Theme Toggle 🎨
theme = st.sidebar.radio("🎨 Select Theme:", ["🌞 Light Mode", "🌙 Dark Mode"])

# Apply Theme
if theme == "🌙 Dark Mode":
    dark_style = {
        "backgroundColor": "#1E1E1E",
        "textColor": "#FFFFFF",
        "gridColor": "#666666"
    }
    plt.style.use("dark_background")
    sns.set_style("darkgrid")
else:
    dark_style = {
        "backgroundColor": "#FFFFFF",
        "textColor": "#000000",
        "gridColor": "#DDDDDD"
    }
    plt.style.use("default")
    sns.set_style("whitegrid")

# Select visualization 📊
viz_option = st.sidebar.selectbox("📊 Choose a visualization", [
    "📌 Count Plot - Categorical Features",
    "📌 Box Plot - Numerical Features",
    "📌 Histogram - Numerical Distribution",
    "📌 Correlation Heatmap"
])

# Count Plot - Categorical Features 🏷️
if viz_option == "📌 Count Plot - Categorical Features":
    st.header("🏷️ Count Plot for Categorical Features")
    categorical_features = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime']
    selected_feature = st.selectbox("🔍 Select a categorical feature:", categorical_features)

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.countplot(data=df, x=selected_feature, palette='viridis', ax=ax)
    
    # Apply Theme
    ax.set_facecolor(dark_style["backgroundColor"])
    ax.xaxis.label.set_color(dark_style["textColor"])
    ax.yaxis.label.set_color(dark_style["textColor"])
    ax.tick_params(colors=dark_style["textColor"])
    
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Box Plot - Numerical Features 📦
elif viz_option == "📌 Box Plot - Numerical Features":
    st.header("📦 Box Plots for Numerical Features")
    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
    selected_feature = st.selectbox("🔍 Select a numerical feature:", numerical_features)

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxplot(data=df, x=selected_feature, palette='coolwarm', ax=ax)
    
    # Apply Theme
    ax.set_facecolor(dark_style["backgroundColor"])
    ax.xaxis.label.set_color(dark_style["textColor"])
    ax.yaxis.label.set_color(dark_style["textColor"])
    ax.tick_params(colors=dark_style["textColor"])
    
    st.pyplot(fig)

# Histogram - Numerical Distribution 📊
elif viz_option == "📌 Histogram - Numerical Distribution":
    st.header("📊 Histograms for Numerical Features")
    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
    selected_feature = st.selectbox("🔍 Select a numerical feature:", numerical_features)

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df[selected_feature], bins=30, kde=True, color='blue', ax=ax)
    
    # Apply Theme
    ax.set_facecolor(dark_style["backgroundColor"])
    ax.xaxis.label.set_color(dark_style["textColor"])
    ax.yaxis.label.set_color(dark_style["textColor"])
    ax.tick_params(colors=dark_style["textColor"])
    
    st.pyplot(fig)

# Correlation Heatmap 🔥
elif viz_option == "📌 Correlation Heatmap":
    st.header("🔥 Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)

    # Apply Theme
    ax.set_facecolor(dark_style["backgroundColor"])
    ax.xaxis.label.set_color(dark_style["textColor"])
    ax.yaxis.label.set_color(dark_style["textColor"])
    ax.tick_params(colors=dark_style["textColor"])
    
    st.pyplot(fig)

st.sidebar.text("🚀 EDA Dashboard for HR Attrition Analysis")