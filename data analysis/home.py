import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


years=list(range(1980,2014))
cols_to_drop=['Type','Coverage','AREA','DEV','REG']ṭ
rename_dict={'OdName':'Country',
             'AreaName':'Continent',
             'RegName':'Region',
             'DevName':'Status'}

@st.cache_data()
def load_data(path):
    df=pd.read_excel('Canada.xlsx',sheet_name=1,skiprows=20,skipfooter=2)
    df.drop(columns=cols_to_drop,inplace=True)
    df.rename(columns=rename_dict,inplace=True)
    df['Total']=df[years].sum(axis=1)
    df.set_index('Country',inplace=True)
    return df

with st.spinner('Processing Immigration Data...'):
    df=load_data('Canada.xlsx')


    
st.image("https://blog.mbeforyou.com/wp-content/uploads/2020/01/CANADIAN-IMMIGRATION.jpg",
         use_column_width=True)
st.title("Immigration Analysis App")     


total_countries=df.shape[0]
duration="1980 - 2013"
total_immigration=df['Total'].sum()

#st.write(total_countries)
st.subheader("Data Summary")
c1 ,c2, c3, c4, c5, c6 =st.columns(6)
c1.metric("Total_countries", total_countries)
c2.metric("Years",duration)
c3.metric("total",total_immigration)

st.header('Immigration Visualixation')

fig=px.line(df,x=df.index,y='Total',height=500)
st.plotly_chart(fig,use_container_width=True)
top_countries=df.sort_values(by='Total',ascending=False).head(25)
c1 ,c2=st.columns([1,3])

limit=c2.slider("select number of countries",1,25,value=9)
countries=top_countries.index.tolist()[:limit]
countries_df=df.loc[countries,years].T
fig2=px.area(countries_df.T,x=countries_df.index,y=countries_df.columns)
#st.write(df.loc[countries,years]
c1.dataframe(top_countries)


c2.plotly_chart(fig2,use_container_width=True)
st.subheader('Trend Comparison')
c1 ,c2 =st.column(2)
countries_list=df.index.to_list()
countries=c2.multiselect('select countries',countries_list)

if countries:
    countries_df=df.loc[countries,years].T
    fig3=px.line(
        countries_df,
        x=countries_df.index,
        y=countries_df.columns )
    for country in countries:
        c1.info(f'{country}:{df.loc[country,Total]} Immigration')
        c2.plotly_chart(fig3,use_container_width=True)
        st.toast('your search has been loaded:',icon='😍')

