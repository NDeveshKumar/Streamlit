import pandas as pd
import streamlit as st
#this is title
st.title("Employee Manager Relation")
df = pd.read_csv("App/Data/employee.csv",header =0).convert_dtypes()

st.dataframe(df)

edges = ""
for _, row in df.iterrows():
    if not pd.isna(row.iloc[1]):
        edges+=f'\t"{row.iloc[0]}" -> "{row.iloc[1]}";\n' 

d = f'digraph{{\n{edges}}}'

st.graphviz_chart(d)
