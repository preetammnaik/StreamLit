import pandas as pd
import streamlit as st
import plotly.express as px
import plotly

st.set_page_config(page_title="Twitter Data Analysis",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )

df = pd.read_csv("Final_Users_File.csv")

st.sidebar.header("Please Filter Here:")
country = st.sidebar.multiselect(
    "Select the Country:",
    options=df['location_country'].unique(),
    default="Germany"
)
city = st.sidebar.multiselect(
    "Select the City:",
    options=df['location_city'].unique()
)
state = st.sidebar.multiselect(
    "Select the State:",
    options=df['location_state'].unique()
)

category = st.sidebar.multiselect(
    "Select the Category:",
    options=df['user_category'].unique(),
    default=df['user_category'].unique()
)

df_selection = df.query(
    "location_country == @country & user_category == @category "
)

df_selection1 = df.query(
    'location_city == @city '
)

df_selection2 = df.query(
    'location_state == @state '
)

st.title(":bar_chart: Twitter Data Dashboard")
st.markdown("___")

total_users = df_selection['username'].count()
user_categories = df_selection['user_category'].nunique()

left_column, middle_column = st.columns(2)
with left_column:
    st.subheader("Total Users:")
    st.subheader(f"{total_users}")
with middle_column:
    st.subheader("Number of Categories:")
    st.subheader(f"{user_categories}")

st.markdown("___")

# Plotting Graph
df_selection = df_selection["user_category"].value_counts().rename_axis('user_categories').reset_index(name='counts')
category_labels = df_selection.user_categories
category_values = df_selection.counts

fig = px.pie(df_selection,
             values=category_values,
             names=category_labels,
             title=" Different User Groups Present "
             )
st.plotly_chart(fig)

df_selection1 = df_selection1["user_category"].value_counts().rename_axis('user_categories').reset_index(name='counts')
category_labels = df_selection1.user_categories
category_values = df_selection1.counts

fig1 = px.pie(df_selection1,
              values=category_values,
              names=category_labels,
              title=" Different User Groups Present based on City "
              )
st.plotly_chart(fig1)


df_selection1 = df_selection2["user_category"].value_counts().rename_axis('user_categories').reset_index(name='counts')
category_labels = df_selection1.user_categories
category_values = df_selection1.counts

fig2 = px.pie(df_selection2,
              values=category_values,
              names=category_labels,
              title=f" Different User Groups present in {state} state "
              )
st.plotly_chart(fig2)
