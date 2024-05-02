# Importing necessary libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read CSV file and return DataFrame
def read_csv_file(file_name):
    """
    Reads a CSV file and returns a pandas DataFrame.

    Parameters:
    file_name (str): The name of the CSV file.

    Returns:
    DataFrame: A DataFrame containing the student data.
    """
    df = pd.read_csv(file_name)
    return df

# Function to analyze student grades
def analyze_grades(df):
    """
    Performs basic analysis on student grades.

    Parameters:
    df (DataFrame): A DataFrame containing the student data.

    Returns:
    None
    """
    # Calculate the minimum, maximum, and average grades
    min_grade = df["Grade"].min()
    max_grade = df["Grade"].max()
    avg_grade = df["Grade"].mean()

    # Display the analysis results
    st.write("Grade Analysis:")
    st.write(f"Minimum Grade: {min_grade}")
    st.write(f"Maximum Grade: {max_grade}")
    st.write(f"Average Grade: {avg_grade:.2f}")

    # Plot a histogram of grades
    fig, ax = plt.subplots()
    sns.histplot(df["Grade"], kde=True, ax=ax)
    ax.set_title("Grade Distribution")
    ax.set_xlabel("Grade")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    # Plot a boxplot of grades
    fig, ax = plt.subplots()
    sns.boxplot(df["Grade"], ax=ax)
    ax.set_title("Grade Boxplot")
    ax.set_ylabel("Grade")
    st.pyplot(fig)

# Main function
def main():
    # Create a Streamlit title and header
    st.title("Student Grade Analyzer")
    st.header("Upload a CSV file containing student data")

    # Create a file uploader
    file_uploader = st.file_uploader("Select a CSV file", type=["csv"])

    # Read the uploaded CSV file
    if file_uploader is not None:
        df = read_csv_file(file_uploader)
        st.write("Student Data:")
        st.write(df)

        # Analyze grades
        analyze_grades(df)

# Call the main function
if __name__ == "__main__":
    main()