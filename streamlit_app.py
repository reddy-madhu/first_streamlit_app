import streamlit

streamlit.title("My Mom's New healthy diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 and blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & rocket smoothie')
streamlit.text('🐔 Hard-Boiled free-range egg')
streamlit.text('🥑🍞 Avocado Toast ')
                
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

Import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
