import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

df = pd.read_csv("data/generations/gen_data_updated.csv",index_col=0)

brackets = ["<=24", "25-34", "35-44", "45-54", "55-64", "65-74", ">=75"]

st.set_page_config(
    page_title="GEI 1.0",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")

with open('pages/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown('<p class="dashboard_title">Generational Economic Index (GEI 1.0)</p>', unsafe_allow_html=True)

st.markdown(
    "<p class=\"body_text\">GEI 1.0 is an attempt to categorize the relative financial performance of various age "
    "brackets in "
    "the U.S. "
    "through 3 sectors: "
    "income, public education, and housing. All raw data was pulled from the BLS.</p>", unsafe_allow_html=True)

st.sidebar.success('Select a year and age bracket to view the GEI.')

num_years = len(df.index.values)
year = st.sidebar.selectbox('Year', df.index.values,index=num_years-1,label_visibility='hidden')
bracket = st.sidebar.selectbox('Age Bracket', [i + " years" for i in brackets],index=1,label_visibility='hidden')[:-6]
pti_value = round(df.at[year, 'adj_income ' + bracket], 2)
pti_rank = round(df.at[year, 'RANK_adj_income ' + bracket])
apcp_value = round(df.at[year, 'apcp ' + bracket], 1)
apcp_rank = round(df.at[year, 'RANK_apcp ' + bracket])
housepi_price = round(df.at[year, 'h_pti ' + bracket], 1)
housepi_rank = round(df.at[year, 'RANK_h_pti ' + bracket])
index_val = round(df.at[year, 'INDEX ' + bracket], 2)
mean_val = round(df['INDEX ' + bracket].mean(), 2)

income_col, apcp_col, housepi_col = st.columns([1.5, 1.5, 1.5])

with income_col:
    with st.container():
        st.markdown(f'<p class="income_text">PRE-TAX ANNUAL INCOME (2022 $) <br></p><p class="price_details">'
                    f'${pti_value}</p>',
                    unsafe_allow_html=True)
        st.markdown(f'<p class="income_text">Rank<br></p><p class="price_details">'
                    f'#{pti_rank}/{num_years}</p>',
                    unsafe_allow_html=True)

with apcp_col:
    with st.container():
        st.markdown(f'<p class="apcp_text">PUBLIC HIGHER-ED COST (% INCOME)<br></p><p class="price_details">{apcp_value}%</p>',
                    unsafe_allow_html=True)
        st.markdown(f'<p class="apcp_text">Rank<br></p><p class="price_details">'
                    f'#{apcp_rank}/{num_years}</p>',
                    unsafe_allow_html=True)
with housepi_col:
    with st.container():
        st.markdown(f'<p class="housepi_text">HOUSE PRICE-INCOME RATIO<br></p><p class="price_details">{housepi_price}X</p>',
                    unsafe_allow_html=True)
        st.markdown(f'<p class="housepi_text">Rank<br></p><p class="price_details">'
                    f'#{housepi_rank}/{num_years}</p>',
                    unsafe_allow_html=True)

emp_col, index_col, emp2_col = st.columns([1.5, 1.5, 1.5])

with index_col:
    with st.container(border=2):
        st.markdown(
            f'<p class="gei_text">GEI 1.0<br></p><p class="gei_details">{index_val}</p>',
            unsafe_allow_html=True)


st.markdown(f'<p class="body_text2">In {year}, {bracket} year olds had a GEI of {index_val} (avg {mean_val}).</p>', unsafe_allow_html=True)

left_col, right_col = st.columns([3.0, 3.0])

with left_col:
    income_title = alt.TitleParams('Pre-Tax Annual Income', anchor='middle')
    income_chart = alt.Chart(df.reset_index(),title=income_title).mark_line(color='orange').encode(
        x=alt.X('year',title='Year',type='nominal'),
        y=alt.Y('adj_income ' + bracket,title='Income (2022 $)'),
    )
    st.altair_chart(income_chart, use_container_width=True)

    apcp_title = alt.TitleParams('Public Higher-Education Cost', anchor='middle')
    apcp_chart = alt.Chart(df.reset_index(),title=apcp_title).mark_line(color='gray').encode(
        x=alt.X('year',title='Year',type='nominal'),
        y=alt.Y('apcp ' + bracket,title='Cost (% of Annual Income)'),
    )
    st.altair_chart(apcp_chart, use_container_width=True)

with right_col:
    housepi_title = alt.TitleParams('House Price to Income Ratio', anchor='middle')
    housepi_chart = alt.Chart(df.reset_index(),title=housepi_title).mark_line(color='#ff6b08').encode(
        x=alt.X('year',title='Year',type='nominal'),
        y=alt.Y('h_pti ' + bracket,title='Amount (X of Annual Income)'),
    )
    st.altair_chart(housepi_chart, use_container_width=True)

    index_title = alt.TitleParams('Generational Economic Index', anchor='middle')
    index_chart = alt.Chart(df.reset_index(),title=index_title).mark_line(color='#807af4').encode(
        x=alt.X('year',title='Year',type='nominal'),
        y=alt.Y('INDEX ' + bracket,title='GEI 1.0 Value'),
    )
    st.altair_chart(index_chart, use_container_width=True)