import pandas as pd
import streamlit as st

def remove_empty_rows(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Drop rows with any empty cells
    df = df.dropna(how='any')

    # Return the updated DataFrame
    return df

# Create a Streamlit app
st.title("Remove Empty Rows from CSV")

# Add a file uploader
uploaded_file = st.file_uploader("Select a CSV file", type=["csv"])

# Add a button to process the file
if st.button("Remove Empty Rows"):
    if uploaded_file is not None:
        # Process the file
        df = remove_empty_rows(uploaded_file)

        # Display the updated DataFrame
        st.write(df)
    else:
        st.error("Please select a CSV file")
