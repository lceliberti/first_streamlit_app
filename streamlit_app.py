import streamlit
import pandas

streamlit.title('My parents own a diner')
streamlit.header('Breakfast Menu')
streamlit.text ('🐔 western omelets')
streamlit.text('🥑🍞hardboiled eggs')
streamlit.text('🥣 oatmeal with fruit')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
