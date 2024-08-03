import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_tags import st_tags

# matplotlib colours
# 1d5dec
# 247afd

# seaborn colours
#hls
# mako


st.set_page_config(
    page_title='BECL'
)

@st.cache_data
def load_becl(url):
    # Running load_becl(...)
    df = pd.read_excel(url)
    df['lemma'].replace({None: 'null'}, inplace=True)
    return df

image_link = 'https://ldsl.rub.de/assets/images/brand/logo.svg'
st.logo(image=image_link, link='https://ldsl.rub.de/study-linguistic-data-science')

st.image(image=image_link, width=128)

df = load_becl(r"C:\Users\Anna\Desktop\RP1\BECL_prep.xlsx")

st.title('Bochum English Countability Lexicon')
st.write('Explore the lexicon and utilize our data manipulation tools to analyze and visualize the countability classes of English noun-sense pairs.')


def plot_lemmas_minor(df, division=' (Whole Lexicon)'):
    st.subheader('Number of lemmas per minor countability class')
    count_df = df['minor_class'].value_counts().reset_index()
    count_df.columns = ['minor_class', 'count']
    st.bar_chart(data=count_df, x='minor_class', y='count', x_label='Minor Countability Class', y_label='Count', color='minor_class')


def plot_lemmas_major(df, division=' (Whole Lexicon)'):
    count_df = df['major_class'].value_counts().reset_index()
    count_df.columns = ['major_class', 'count']
    st.subheader('Percentage of lemmas per major countability class')
    fig = px.pie(count_df, values='count', names='major_class')
    st.plotly_chart(fig)



col_hints = {'senseindex': st.column_config.NumberColumn(help='sense number in WordNet'), 
                                'sense_synset': st.column_config.Column(help='a synset is identified with a 3-part name of the form: word.pos.sense number'),
                                'oanc_total': st.column_config.NumberColumn(help='total number of occurrences in the Open American National Corpus')}

filtered_df = df.copy()

#word_search = st.text_input('Type comma-separated word(s) to search')

word_search = st_tags(
    label='Word Search',
    text='Type the word and press "enter"',
    value=[]
)



column_options = st.multiselect('Select column(s) to display', options=df.columns.values.tolist())
output_length = st.number_input('Enter the number of rows to display', min_value=1, max_value=len(df), value=len(df))

if word_search:
    filtered_df = filtered_df[filtered_df['lemma'].isin(word_search)]

filter_cols = []
for col in column_options:
    if st.checkbox(f'Filter {col}'):
        filter_values = st.multiselect(f'Select values for {col}', options=filtered_df[col].unique())
        filtered_df = filtered_df[filtered_df[col].isin(filter_values)]
        filter_cols.append(col)


if column_options:
    filtered_df = filtered_df[column_options]

if output_length:
    filtered_df = filtered_df[:output_length]

st.dataframe(filtered_df, column_config=col_hints)


if 'minor_class' in filtered_df.columns:
    st.divider()
    plot_lemmas_minor(filtered_df)
if 'major_class' in filtered_df.columns:
    st.divider()
    plot_lemmas_major(filtered_df)
    
st.divider()



@st.cache_data
def convert_csv(df):
    return df.to_csv().encode('utf-8')

csv = convert_csv(df)

st.download_button(
    label="Download as CSV",
    data=csv,
    file_name='BECL.csv',
    mime='text/csv')

st.link_button(
    label='Go to BECL GitHub Repository',
    url='https://github.com/Linguistic-Data-Science-Lab/BECL'
)

st.divider()

st.markdown('Created by Anna Buzmakova. For feedback or issues, please contact anna.buzmakova@ruhr-uni-bochum.de. Click the button below to access source code on GitHub:')
st.link_button(
    label='Go to Source Code',
    url='https://github.com/sonnayaanya/BECL_Visualiser'
    )