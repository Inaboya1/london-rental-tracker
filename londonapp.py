#import and page setup
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# st.set_page_config to configure page setting
st.set_page_config(
    page_title="London Rental Affordability Tracker",
    page_icon="🏠",
    layout="wide"
)
st.title("🏠 London Rental Affordability Tracker")

st.write(
    "Explore how rent compares to local wages across London boroughs."
)
# Data sources:
# kaggle_london_house_price_data.csv
# london_wages.csv

# load clean data with cache to avoid slow loading
@st.cache_data
def load_data():
    df = pd.read_csv(
        'data/clean/london_properties_with_borough.csv.gz', compression='gzip'
    )
    borough_afford = pd.read_csv(
        'data/clean/borough_affordability.csv'
    )
    return df, borough_afford
df, borough_afford = load_data()

# setup to select borough from dropdown
borough_list = sorted(borough_afford['borough'].unique())
# st.sidebar to put this dropdown in a sidebar on the left
selected_borough = st.sidebar.selectbox(
"Choose a London borough",
borough_list
)
# Filter the borough summary table to just the selected borough
borough_row = borough_afford[borough_afford['borough'] == selected_borough].iloc[0]
# .iloc[0] gets the first (and only) matching row as a simple object

# metric card statistics
st.header(f'🏠 {selected_borough}')

# Create 4 columns side by side
col1, col2, col3, col4 = st.columns(4)
col1.metric(
"Median Monthly Rent",
f"£{borough_row.median_rent:,.0f}"
)
col2.metric(
"Median Annual Wage",
f"£{borough_row.median_wage:,.0f}"
)
col3.metric(
"Rent-to-Income",
f"{borough_row.rent_to_income:.1f}%",
# delta shows red/green vs the 30% stress threshold
delta=f"{borough_row.rent_to_income - 30:.1f}pp vs 30% threshold",
delta_color="inverse"
)
col4.metric(
"Years of Salary to Buy",
f"{borough_row.years_to_buy:.1f} yrs"
)

# borough ranking chart, accessing live
st.subheader('How does this compare across London?')
# Sort all boroughs by affordability
ranked_borough = borough_afford.sort_values('rent_to_income', ascending=False)
fig, ax = plt.subplots(figsize=(10, 10))
# Highlight the selected borough in a different colour
colours = [
    '#0F6E56' if b == selected_borough else '#D3D1C7'
    for b in ranked_borough['borough']
]
ax.barh(ranked_borough['borough'][::-1], ranked_borough['rent_to_income'][::-1],
color=colours[::-1], edgecolor='white')
ax.axvline(30, color='#993C1D', linestyle='--', linewidth=2.0,
label='30% stress threshold')
ax.set_xlabel('Rent-to-income ratio (%)')
ax.set_title(f'{selected_borough} highlighted vs all London boroughs')
ax.legend()
# st.pyplot displays a matplotlib figure on the page
st.pyplot(fig)
st.subheader('Full borough data')
# st.dataframe shows an interactive table 
# users can click column headers to sort, and scroll
st.dataframe(
ranked_borough[['borough','median_rent','median_wage',
'rent_to_income','years_to_buy','property_count']]
.rename(columns={
'borough':'Borough',
'median_rent':'Median Rent (£)',
'median_wage':'Median Wage (£)',
'rent_to_income':'Rent-to-Income (%)',
'years_to_buy':'Years to Buy',
'property_count':'Sample Size',
}),
use_container_width=True,
hide_index=True
)
# Data sources
st.caption(
"Data: Kaggle London House Price Dataset (2025) | "
"ONS Annual Survey of Hours and Earnings (2023 estimates) | "
"Built as part of a self learning portfolio project."
)