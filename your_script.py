import streamlit as st
import pandas as pd

# Create a DataFrame to store the data
df = pd.DataFrame(columns=['Site Name', 'Contract Amount', 'Date', 'Category', 'Amount'])

# Function to save data to CSV file
def save_data():
    site_name = st.session_state.site_name
    df_site = df[df['Site Name'] == site_name]
    df_site.to_csv(f'{site_name}.csv', index=False)

# Function to get data for a selected site
def get_data():
    site_name = st.session_state.site_name
    df_site = df[df['Site Name'] == site_name]
    st.write(df_site)

# Function to display total amounts for each category
def display_totals():
    st.subheader('Total Amounts Till Now:')
    totals = df.groupby('Category')['Amount'].sum()
    st.write(totals)

# Streamlit app
def main():
    st.title('Construction Site Tracker')

    # Input for Site Name and Contract Amount
    st.sidebar.header('Input')
    st.sidebar.text_input('Site Name', key='site_name')
    st.sidebar.number_input('Contract Amount', key='contract_amount')

    # Date input
    st.sidebar.header('Date Input')
    date_input = st.sidebar.date_input('Select Date', pd.to_datetime('today'))

    # Sub-inputer for categories
    st.sidebar.header('Category Input')
    category = st.sidebar.selectbox('Select Category', ['Bricks', 'Plumber', 'Murum', 'Sand', 'Aggregate',
                                                        'Steel', 'Electrical material', 'Plumbing material',
                                                        'Flooring material', 'Labor payment', 'Ducting', 'Rcc labor',
                                                        'Brick work and plaster work', 'Electric labor', 'Plumbing labor',
                                                        'Flooring labor', 'IPS labor'], key='category')

    amount = st.sidebar.number_input('Amount', key='amount')

    # Submit button to save data
    if st.sidebar.button('Submit'):
        site_name = st.session_state.site_name
        contract_amount = st.session_state.contract_amount
        df.loc[len(df)] = [site_name, contract_amount, date_input, category, amount]
        st.success('Data submitted successfully!')

    # Get Data button to display entries for a selected site
    if st.sidebar.button('Get Data'):
        get_data()

    # Save Data button to save data to CSV file
    if st.sidebar.button('Save Data'):
        save_data()

    # Display totals
    display_totals()

if __name__ == '__main__':
    main()