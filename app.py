#Import Libraries
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

#Heading
st.title('Research Project on Stock Market Analysis and Prediction')
st.caption('All data is taken from BSE and was last updated on 10th March, 2023')
st.write("#")

#TCS Data Taken
tcsdaily = pd.read_csv('data/tcs-daily.csv')
tcsdaily = tcsdaily.iloc[::-1] #Daily data to be reversed ordered
tcsmonthly= pd.read_csv('data/tcs-monthly.csv')
tcsyearly = pd.read_csv('data/tcs-yearly.csv')

#Reliance Data Taken
reldaily = pd.read_csv('data/relianceind-daily.csv')
reldaily = reldaily.iloc[::-1] #Daily data to be reversed ordered
relmonthly= pd.read_csv('data/relianceind-monthly.csv')
relyearly = pd.read_csv('data/relianceind-yearly.csv')

#Infosys Data Taken
infdaily = pd.read_csv('data/infosys-daily.csv')
infdaily = infdaily.iloc[::-1] #Daily data to be reversed ordered
infmonthly= pd.read_csv('data/infosys-monthly.csv')
infyearly = pd.read_csv('data/infosys-yearly.csv')

#Select Box
comp = st.selectbox('Select a Company from the below options :', ('Tata Consultancy Services', 'Reliance Industries', 'Infosys'))

if comp == 'Tata Consultancy Services':
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Market Price", value="3,331.05", delta="-6.40")
    col2.metric(label="52 Week Low", value="2,867.90")
    col2.metric(label='P/E Ratio', value='30.04')
    col3.metric(label="52 Week High", value="3,759.34")
    col3.metric(label='Return on Equity', value='43.66%')
    col4.metric(label="Market Cap", value="12.18L Cr")
    col4.metric(label='Dividend Yeild', value='1.38%')

if comp == 'Reliance Industries':
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Market Price", value="2,323.15", delta="-37.00")
    col2.metric(label="52 Week Low", value="2,181.00")
    col2.metric(label='P/E Ratio', value='24.72')
    col3.metric(label="52 Week High", value="2,855.00")
    col3.metric(label='Return on Equity', value='8.21%')
    col4.metric(label="Market Cap", value="15.28L Cr")
    col4.metric(label='Dividend Yeild', value='0.34%')

if comp == 'Infosys':
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Market Price", value="1,471.35", delta="-9.40")
    col2.metric(label="52 Week Low", value="1,355.50")
    col2.metric(label='P/E Ratio', value='26.13')
    col3.metric(label="52 Week High", value="1,924.00")
    col3.metric(label='Return on Equity', value='29.15%')
    col4.metric(label="Market Cap", value="6.08L Cr")
    col4.metric(label='Dividend Yeild', value='2.21%')

#Tab for Hist Data
st.write("#")
st.subheader('Historic data : ')
option1, option2, option3 = st.tabs(["Daily", "Monthly", "Yearly"])

with option1:
    if comp == 'Tata Consultancy Services':
        fig = px.line(tcsdaily, x='Date', y='Close Price',markers=False, title='Tata Consultancy Services Daily Data from Jan 2019')
        st.plotly_chart(fig, use_container_width=True)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=tcsdaily['Date'], y=tcsdaily['Close Price'], name='Closing Price', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=tcsdaily['Date'], y=tcsdaily['Open Price'], name = 'Opening Price', line=dict(color='yellow')))
        fig.add_trace(go.Scatter(x=tcsdaily['Date'], y=tcsdaily['High Price'], name = 'High', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=tcsdaily['Date'], y=tcsdaily['Low Price'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Date', yaxis_title='Price', title='Comparing other relevant parameters along close price')
        st.plotly_chart(fig, use_container_width=True, title='Comparing other relevant parameters')

    if comp == 'Infosys':
        fig = px.line(infdaily, x='Date', y='Close Price',markers=False, title='Infosys Daily Data from Jan 2019')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()   
        fig.add_trace(go.Scatter(x=infdaily['Date'], y=infdaily['Close Price'], name='Closing Price', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=infdaily['Date'], y=infdaily['Open Price'], name = 'Opening Price', line=dict(color='yellow')))
        fig.add_trace(go.Scatter(x=infdaily['Date'], y=infdaily['High Price'], name = 'High', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=infdaily['Date'], y=infdaily['Low Price'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Date', yaxis_title='Price', title='Comparing other relevant parameters')
        st.plotly_chart(fig, use_container_width=True)

    if comp == 'Reliance Industries':
        fig = px.line(reldaily, x='Date', y='Close Price',markers=False, title='Reliance Industries Daily Data from Jan 2019')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=reldaily['Date'], y=reldaily['Close Price'], name='Closing Price', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=reldaily['Date'], y=reldaily['Open Price'], name = 'Opening Price', line=dict(color='yellow')))
        fig.add_trace(go.Scatter(x=reldaily['Date'], y=reldaily['High Price'], name = 'High', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=reldaily['Date'], y=reldaily['Low Price'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Date', yaxis_title='Price', title='Comparing other relevant parameters along close price')
        st.plotly_chart(fig, use_container_width=True)

with option2:
    if comp == 'Tata Consultancy Services':
        fig = px.line(tcsmonthly, x='Month', y='Close Price',markers=False, title='Tata Consultancy Services Monthly Data from 2004')
        st.plotly_chart(fig, use_container_width=True)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=tcsmonthly['Month'], y=tcsmonthly['Close Price'], name='Closing Price', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=tcsmonthly['Month'], y=tcsmonthly['Open Price'], name = 'Opening Price', line=dict(color='yellow')))
        fig.add_trace(go.Scatter(x=tcsmonthly['Month'], y=tcsmonthly['High Price'], name = 'High', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=tcsmonthly['Month'], y=tcsmonthly['Low Price'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Month', yaxis_title='Price', title='Comparing other relevant parameters')
        st.plotly_chart(fig, use_container_width=True)

    if comp == 'Infosys':
        fig = px.line(infmonthly, x='Month', y='Close Price',markers=False, title='Infosys Monthly Data from 2004')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=infmonthly['Month'], y=infmonthly['Close Price'], name='Closing Price', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=infmonthly['Month'], y=infmonthly['Open Price'], name = 'Opening Price', line=dict(color='yellow')))
        fig.add_trace(go.Scatter(x=infmonthly['Month'], y=infmonthly['High Price'], name = 'High', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=infmonthly['Month'], y=infmonthly['Low Price'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Month', yaxis_title='Price', title='Comparing other relevant parameters')
        st.plotly_chart(fig, use_container_width=True)

    if comp == 'Reliance Industries':
        fig = px.line(relmonthly, x='Month', y='Close Price',markers=False, title='Reliance Industries Monthly Data from 2004')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=relmonthly['Month'], y=relmonthly['Close Price'], name='Closing Price', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=relmonthly['Month'], y=relmonthly['Open Price'], name = 'Opening Price', line=dict(color='yellow')))
        fig.add_trace(go.Scatter(x=relmonthly['Month'], y=relmonthly['High Price'], name = 'High', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=relmonthly['Month'], y=relmonthly['Low Price'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Month', yaxis_title='Price', title='Comparing other relevant parameters')
        st.plotly_chart(fig, use_container_width=True)

with option3:
    if comp == 'Tata Consultancy Services':
        fig = px.line(tcsyearly, x='Year', y='Close Price',markers=False, title='Tata Consultancy Services Yearly Data from 2004')
        st.plotly_chart(fig, use_container_width=True)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=tcsyearly['Year'], y=tcsyearly['Close Price'], name='Closing Price', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=tcsyearly['Year'], y=tcsyearly['Open Price'], name = 'Opening Price', line=dict(color='yellow')))
        fig.add_trace(go.Scatter(x=tcsyearly['Year'], y=tcsyearly['High Price'], name = 'High', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=tcsyearly['Year'], y=tcsyearly['Low Price'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Year', yaxis_title='Price', title='Comparing other relevant parameters along close price')
        st.plotly_chart(fig, use_container_width=True, title='Comparing other relevant parameters')

    if comp == 'Infosys':
        fig = px.line(infyearly, x='Year', y='Close Price',markers=True, title='Infosys Yearly Data from 2004')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=infyearly['Year'], y=infyearly['Close Price'], name='Closing Price', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=infyearly['Year'], y=infyearly['Open Price'], name = 'Opening Price', line=dict(color='yellow')))
        fig.add_trace(go.Scatter(x=infyearly['Year'], y=infyearly['High Price'], name = 'High', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=infyearly['Year'], y=infyearly['Low Price'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Year', yaxis_title='Price', title='Comparing other relevant parameters')
        st.plotly_chart(fig, use_container_width=True)

    if comp == 'Reliance Industries':
        fig = px.line(relyearly, x='Year', y='Close Price',markers=True, title='Reliance Industries Yearly Data from 2004')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=relyearly['Year'], y=relyearly['Close Price'], name='Closing Price', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=relyearly['Year'], y=relyearly['Open Price'], name = 'Opening Price', line=dict(color='yellow')))
        fig.add_trace(go.Scatter(x=relyearly['Year'], y=relyearly['High Price'], name = 'High', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=relyearly['Year'], y=relyearly['Low Price'], name = 'Low', line=dict(color='red')))
        fig.update_layout(xaxis_title='Year', yaxis_title='Price', title='Comparing other relevant parameters')
        st.plotly_chart(fig, use_container_width=True)

#Tab for Hist Data
st.write("#")
st.subheader('Financial data : ')
a1, a2, a3 = st.tabs(["Revenue & Profit", "Net Worth", "Shareholding Pattern"])

tier=['Promoters', 'Mutual Funds', 'Retail', 'Foreign Institutions','Others'] 
y=['2018', '2019', '2020', '2021', '2022']

with a1:
    st.caption('All values in Crs')
    if comp == 'Infosys':
        chart_data = pd.DataFrame([[70522,16029], [82675,15404], [90791,16594], [100472,19351], [121641,22110]],
        index=y, columns=["Revenue", "Profit"])
        st.bar_chart(chart_data, height=350)

    if comp == 'Tata Consultancy Services':
        chart_data = pd.DataFrame([[123104,25826], [146463,31472], [156949,32430], [164177,32430], [191754,38327]],
        index=y, columns=["Revenue", "Profit"])
        st.bar_chart(chart_data, height=350)

    if comp == 'Reliance Industries':
        chart_data = pd.DataFrame([[408265,36075], [583094,39588], [611645,39354], [486326,49128], [721634,60705]],
        index=y, columns=["Revenue", "Profit"])
        st.bar_chart(chart_data, height=350)

    
with a2:
    st.caption('All values in Crs')
    if comp == 'Infosys':
        chart_data = pd.DataFrame([64923, 64948, 65450, 76351, 75350], index=y, columns=['Net Worth'])
        st.bar_chart(chart_data, height=350)

    if comp == 'Tata Consultancy Services':
        chart_data = pd.DataFrame([85128, 89446, 84126, 86433, 89139], index=y, columns=['Net Worth'])
        st.bar_chart(chart_data, height=350)

    if comp == 'Reliance Industries':
        chart_data = pd.DataFrame([293506, 387112, 453331, 700172, 779485], index=y, columns=['Net Worth'])
        st.bar_chart(chart_data, height=350)

with a3:
    if comp == 'Infosys':
        x = [15.11, 17.71, 18.22, 36.28, 12.68]
        fig = px.pie(values=x, names=tier)
        st.plotly_chart(fig, use_container_width=True, height=350)

    if comp == 'Tata Consultancy Services':
        x = [72.30, 3.31, 5.96, 12.94, 5.49]
        fig = px.pie(values=x, names=tier)
        st.plotly_chart(fig, use_container_width=True, height=350)

    if comp == 'Reliance Industries':
        x = [50.49, 5.81, 11.64, 23.43, 8.63]
        fig = px.pie(values=x, names=tier)
        st.plotly_chart(fig, use_container_width=True, height=350)

st.caption('App was made by Anand Soni and Deepak Rathore')
