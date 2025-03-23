import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/exchange_rate_usd_eur_aud.csv")

df['Date']=pd.to_datetime(df['Date'])
# Page Config
st.set_page_config(
    page_title="Exchange Rate Dashboard",
    page_icon=":chart_with_upwards_trend:",
    #layout="wide",
)

cur = st.selectbox("Select Currency", ['USD', 'EUR', 'AUD'])
years = df['Date'].dt.year.unique()
#df.set_index('Date', inplace=True)

year = st.selectbox("Select Year", years)

strat_date = str(year) + "-01-01"
end_date = str(year) + "-12-31"

date_range = pd.date_range(strat_date, end_date)

plt.figure(figsize=(12,6))
plt.plot(df[df.index.isin(date_range)][cur])
plt.xlabel("Year")
plt.ylabel("Exchange Rate")
plt.title("Exchange Rate Trends Over 10 Years")
plt.legend()

st.pyplot(plt)

cur1 = st.selectbox("Select Currency 1", ['USD', 'EUR', 'AUD'])

years = list(df['Date'].dt.year.unique())

year1 = st.selectbox("Select Year 1", years)

strat_date1 = str(year1) + "-01-01"
end_date1 = str(year1) + "-12-31"

date_range1 = pd.date_range(strat_date1, end_date1)

year2 = st.selectbox("Select Year 2", years)

strat_date2 = str(year2) + "-01-01"
end_date2 = str(year2) + "-12-31"

date_range2 = pd.date_range(strat_date2, end_date2)


df = df.sort_values('Date')
df.set_index('Date', inplace=True)

df1 = df[df.index.isin(date_range1)].reset_index()[cur1]
df2 = df[df.index.isin(date_range2)].reset_index()[cur1]



plt.plot(df1, label = year1)
plt.plot(df2, label= year2)
plt.legend()

st.pyplot(plt)