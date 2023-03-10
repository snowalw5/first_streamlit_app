import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🧃 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍓🍌 Build Your Own Fruit Smoothie 🍉🍊')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Choosing fruit name column as index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# This line filters the table data and prepopulates the list for the customer
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# put the list of selected fruits into a variable called fruits_selected
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])


# change the fruit in the pick list
# fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Grapes'])


# remove fruit in the pick list - results in an error
# fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),[''])


#use the fruits in our fruits_selected list to pull rows from the full data set (and assign that data to a variable called fruits_to_show)
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
#streamlit.dataframe(my_fruit_list)

# Use the data in fruits_to_show in the dataframe it displays on the page. 
streamlit.dataframe(fruits_to_show)

#new section to display fruityvice response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Apple')
streamlit.write('The user entered ', fruit_choice)



import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


#writes the data to screen
#streamlit.text(fruityvice_response.json()) 

# normalize json version of the response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output to scren as table
streamlit.dataframe(fruityvice_normalized)



