import streamlit as st
import plotly as plt
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json
import numpy as np

st.title("LEVANA BOUNTY 2 - Meteor Shower Participants")
st.text('')

st.text("""
For those who bought and participated in the Levana Meteor Shower, is there a 
relationship between their participation and their LUNATIC degen score?
    """)
st.markdown("""---""")

st.text('')
st.text("""
Taking a look at the data there is some relationship between Lunatic score and
Meteor Shower event participation. Unfortunately due to the nature of the
Lunatic score data, the analysis in this dashboard is static, and scores are
up to date only as of 11/16/2021.
    """)
st.text('')
st.text("""
The table below shows the very basic breakdown of the Meteor Shower event.
    """)
st.text('')

st.write('**_Address_ - refers to each unique Terra wallet address which received a meteor**')
st.write('**_Number of meteors obtained_ - refers to total meteors distributed to addreses**')
st.write('**_Number of tx_ - refers to an instance where a wallet deposited ust**')

meteor_receivers = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/62f6cf60-0824-432e-8811-f378306a14a2/data/latest')
meteor_receivers

st.text('And here is the table of addresses and their total UST deposits')

basic_table = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/9d9532d5-9e1c-49a4-bf6e-ee61919dd54f/data/latest')
basic_table

st.text('')
st.markdown("""---""")





address_merged_table = pd.read_csv('scores_1_to_30_2021-11-16.csv')
address_score = address_merged_table[['address', 'Total Score']]
score_to_ust = address_merged_table[['Total Score', 'UST_DEPOSITED']]

st.markdown("""### Lunatic Score Distribution""")
st.text("""
The table below displays the count of scores among the addresses which
participated in the meteor shower event. It skews slightly to the right
with the largest portion of addresses holding a Lunatic score of 27.
    """)
st.bar_chart(address_score['Total Score'].value_counts())
st.text('')

st.markdown("""### SUM of UST deposits by Lunatic score""")
st.text("""
This graph skews much more to the right. Addresses with a score of 27
deposited the most out of all the addresses at a sum total of $556,720.
    """)
st.bar_chart(score_to_ust.groupby(['Total Score']).sum())
st.text('')

st.markdown("""### MEAN of UST deposits by Lunatic score""")
st.text("""
This graph skews again to the right, but this time 27 is not the winner.
Scores 29 and 18 most notably make the biggest average deposit when they
deposit.
    """)
st.bar_chart(score_to_ust.groupby(['Total Score']).mean())
st.text('')

st.markdown("""### Percent distribution of contribution sizes""")
st.text("""
This graph is less intuitive but displays the binning of deposits.
That is, deposits are split into 4 quartiles depending on their size
with the smallest 25 percent being in 25, 25 to 50 is 50, 50 to 75 is
75, and 75 to 100 is 100. For the most part, it does not seem deposit
frequency being a major factor in this event, as the size of the deposit
contributes much more to the likelihood of meteors gained. This is
reflected in the fact that the graphs above display a right skew, but
the percent distribution is mostly even, with there only being slightly
fewer deposits in the 50 to 75 percent quartile than the rest.
    """)
st.bar_chart(pd.qcut(score_to_ust['UST_DEPOSITED'], 4, [25, 50, 75, 100]).value_counts())