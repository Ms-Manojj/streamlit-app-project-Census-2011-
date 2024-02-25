import pandas as pd
import plotly.graph_objects as go
import plotly.express as ex
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px


st.set_page_config(layout='wide')


df=pd.read_csv('final_df.csv')

st.sidebar.title('Census 2011 Data Analysis')


option=st.sidebar.selectbox('Select Box',['Overall Analysis','State Wise'])
# option = 'Overall Analysis'  # Replace this with your actual logic for option selection

if option == 'Overall Analysis':
    st.title('Overall Analysis')

    col01, col02, col03, col04 = st.columns(4)

    with col01:
        st.metric('Total Population', str(round(df['Population'].sum() / 10000000)) + ' Cr')
        st.markdown("<style>div#centered_col01 { text-align: center; }</style>", unsafe_allow_html=True)

    with col02:
        st.metric('Total Male Population', str(round(df['Male'].sum() / 10000000)) + ' Cr')
        st.markdown("<style>div#centered_col02 { text-align: center; }</style>", unsafe_allow_html=True)

    with col03:
        st.metric('Total Female Population', str(round(df['Female'].sum() / 10000000)) + ' Cr')
        st.markdown("<style>div#centered_col03 { text-align: center; }</style>", unsafe_allow_html=True)

    with col04:
        st.metric('Sex Ratio', round((df['Male'].sum() / df['Female'].sum()) * 1000))
        st.markdown("<style>div#centered_col04 { text-align: center; }</style>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        final_df = df.groupby('Zone')['Population'].sum().sort_values()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(final_df.index, final_df.values, width=0.8)
        ax.set_title('Population by Zone')
        st.pyplot(fig)

    with col2:
        final_df = df.groupby('Zone')['Population'].sum().sort_values()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.pie(final_df, labels=final_df.index, autopct='%1.1f%%', startangle=90)
        ax.set_title('Population Distribution by Zone')
        st.pyplot(fig)

    col05, col06 = st.columns(2)

    with col05:
        final_df_male = df.groupby('Zone')['Male'].sum().sort_values()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(final_df_male.index, final_df_male.values, width=0.8)
        ax.set_title('Male Population')
        st.pyplot(fig)

    with col06:
        final_df_female = df.groupby('Zone')['Female'].sum().sort_values()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(final_df_female.index, final_df_female.values, width=0.8)
        ax.set_title('Female Population')
        st.pyplot(fig)

    gp = df.groupby('Vehicle')['Male'].sum().sort_values().reset_index()
    gp['Male'] = gp['Male'] / 10000000
    st.title('State wise Male Population')
    st.line_chart(gp.set_index('Vehicle'))

    gp = df.groupby('Vehicle')['Female'].sum().sort_values().reset_index()
    gp['Female'] = gp['Female'] / 10000000
    st.title('State wise Female Population ')
    st.line_chart(gp.set_index('Vehicle'))


     # plot for india Male population

    fig = px.scatter_mapbox(df, 
                        lat="Latitude", 
                        lon="Longitude",
                        size=df['Population'],
                        color=df['Male'],  # or df['Female'] based on your preference
                        zoom=4,
                        size_max=35,
                        mapbox_style="carto-positron",
                        width=1200,
                        height=700,
                        hover_name='District',
                        title='Geographical Distribution of Male Population')

    st.plotly_chart(fig, use_container_width=True)

         # plot for india Female population

    fig = px.scatter_mapbox(df, 
                        lat="Latitude", 
                        lon="Longitude",
                        size=df['Population'],
                        color=df['Female'],  # or df['Female'] based on your preference
                        zoom=4,
                        size_max=35,
                        mapbox_style="carto-positron",
                        width=1200,
                        height=700,
                        hover_name='District',
                        title='Geographical Distribution of Female Population')

    st.plotly_chart(fig, use_container_width=True)



    fig = px.scatter_mapbox(df, 
                        lat="Latitude", 
                        lon="Longitude",
                        size=df['Population'],
                        color=df['Vehicle'],
                        zoom=4,
                        size_max=35,
                        mapbox_style="carto-positron",
                        width=1200,
                        height=700,
                        hover_name='District',
                        title='Geographical Population of State ')

    st.plotly_chart(fig, use_container_width=True)


elif option=='State Wise':
    st.title('State Wise Analysis')
    selected=st.sidebar.selectbox('Select State',df['State name'].unique().tolist())
    st.subheader(selected.capitalize())

    col01, col02, col03, col04 ,col05= st.columns(5)

    with col01:
        st.metric('Total Population', str(round(df[df['State name']==selected]['Population'].sum()/10000000)) + ' Cr')
        st.markdown("<style>div#centered_col01 { text-align: center; }</style>", unsafe_allow_html=True)

    with col02:
        st.metric('Total Male Population', str(round(df[df['State name']==selected]['Male'].sum()/10000000,2)) + ' Cr')
        st.markdown("<style>div#centered_col02 { text-align: center; }</style>", unsafe_allow_html=True)

    with col03:
        st.metric('Total Female Population', str(round(df[df['State name']==selected]['Female'].sum()/10000000,2)) + ' Cr')
        st.markdown("<style>div#centered_col03 { text-align: center; }</style>", unsafe_allow_html=True)

    with col04:
        st.metric('Sex Ratio', round((df[df['State name']==selected]['Male'].sum() / df[df['State name']==selected]['Female'].sum()) * 100))
        st.markdown("<style>div#centered_col04 { text-align: center; }</style>", unsafe_allow_html=True)

    with col05:
        st.metric('Total District', df[df['State name']==selected]['District name'].nunique())
        st.markdown("<style>div#centered_col03 { text-align: cent er; }</style>", unsafe_allow_html=True)


    col001,col002,col003=st.columns(3)

    with col003:
        male_literacy_rate = (df[df['State name'] == selected]['Literate'].sum() / df[df['State name'] == selected]['Population'].sum()) * 100
        formatted_rate = round(male_literacy_rate, 2)  # Rounding to two decimal places
        st.metric('Literacy Rate', f"{formatted_rate}%")
        st.markdown("<style>div#centered_col04 { text-align: center; }</style>", unsafe_allow_html=True)
    
    with col001:
        male_literacy_rate = (df[df['State name'] == selected]['Male_Literate'].sum() / df[df['State name'] == selected]['Male'].sum()) * 100
        formatted_rate = round(male_literacy_rate, 2)  # Rounding to two decimal places
        st.metric('Male Literacy Rate', f"{formatted_rate}%")
        st.markdown("<style>div#centered_col04 { text-align: center; }</style>", unsafe_allow_html=True)
    
    with col002:
        male_literacy_rate = (df[df['State name'] == selected]['Female_Literate'].sum() / df[df['State name'] == selected]['Female'].sum()) * 100
        formatted_rate = round(male_literacy_rate, 2)  # Rounding to two decimal places
        st.metric('Female Literacy Rate', f"{formatted_rate}%")
        st.markdown("<style>div#centered_col04 { text-align: center; }</style>", unsafe_allow_html=True)


    # Filter data for the selected state
    dist = df[df['State name'] == selected].groupby('District name')['Population'].sum().reset_index()
    dist['Population'] = dist['Population'] / 10000000
    dist = dist.sort_values(by='Population')
    st.subheader(f"Population of Districts in {selected}")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(dist['District name'], dist['Population'], width=0.8)
    ax.set_xticklabels(dist['District name'], rotation=45, ha='right')
    st.pyplot(fig)


    # Filter data for the selected state- Male population
    dist = df[df['State name'] == selected].groupby('District name')['Male'].sum().reset_index()
    dist['Population'] = dist['Male'] / 10000000
    dist = dist.sort_values(by='Male')
    st.subheader(f"Male-Population of Districts in {selected}")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(dist['District name'], dist['Population'], width=0.8)
    ax.set_xticklabels(dist['District name'], rotation=45, ha='right')
    st.pyplot(fig)

    dist = df[df['State name'] == selected].groupby('District name')['Female'].sum().reset_index()
    dist['Population'] = dist['Female'] / 10000000
    dist = dist.sort_values(by='Female')
    st.subheader(f"Female-Population of Districts in {selected}")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(dist['District name'], dist['Population'], width=0.8)
    ax.set_xticklabels(dist['District name'], rotation=45, ha='right')
    st.pyplot(fig)



else:
    pass
