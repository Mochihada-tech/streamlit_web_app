import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/sample.csv', index_col='年月日')
st.dataframe(df)
st.bar_chart(df['平均気温(℃)'])

# matplotlib
fig, ax = plt.subplots()
ax.plot(df.index, df['平均気温(℃)'])
ax.set_title('matplotlib_graph')
st.pyplot(fig)
