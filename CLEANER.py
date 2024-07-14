import pandas as pd
import streamlit as st
import csv

def process_csv(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Drop rows with any empty cells
    df = df.dropna(how='any')

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Return the updated DataFrame
    return df

# Create a Streamlit app
st.title("Remove Empty Rows and Duplicates from CSV")

# Add a file uploader
uploaded_file = st.file_uploader("Select a CSV file", type=["csv"])

# Add a button to process the file
if st.button("Process CSV"):
    if uploaded_file is not None:
        # Process the file
        df = process_csv(uploaded_file)

        # Display the updated DataFrame
        st.write(df)

        # Add a button to download the processed CSV file
        st.markdown("#### Download Processed CSV")
        st.download_button(
            label="Download",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name="processed.csv",
            mime="text/csv"
        )
    else:
        st.error("Please select a CSV file")
