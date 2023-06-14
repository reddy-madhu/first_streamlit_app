import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Mom's New healthy diner")

streamlit.header('Breakfast Favorites')

streamlit.text('🥣 Omega 3 and blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & rocket smoothie')
streamlit.text('🐔 Hard-Boiled free-range egg')
streamlit.text('🥑🍞 Avocado Toast ')
                
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
try:

fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit choice:
  streamlit.error("Please select a fruit to get the information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()

streamlit.stop()



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

streamlit.write('Thanks for adding', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
