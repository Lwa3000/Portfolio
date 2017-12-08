# 02_UD_Portfolio
My portfolio of work 2017
>Stay tuned for more apps.

1) App1_Dictionary: a python command line app that outputs the definition of a word you enter.
	- How to run: Execute the program by: python3 app1_Ditionary.py
	- Features: If you mistype the word: e.g. rainn instead of rain, the program will suggest to you the closest matching word.
	- Tools in the app: JSON file, difflib
	- youtube demo: https://youtu.be/2_JH0JhCag0

2) App_weather_api: Connects to a weather website api and checks the weather to see if you need to bring an umbrella out today.
	- How to run: Install flask. Start up the Flask server in a virtual environment and apply the requirement.txt file. Make sure you are connected to the internet.
	- Features: Works for most US cities and zip codes, and possibility some international cities.
	- Tools in the app: Flask, API


3) app_physiology_card_game: This is a beta version. A buzzfeed game that helps you learn human physiology.
	- How to run: Execute the program by: python3 Game1_v2.py, then follow instructions
	- Features: This app helps you learn by showing you facts and checks if you remember them until you get it right.
	- How to play: You have 4 cards to play with. Each card will have three facts to browse through.
                     After you have browsed through all the cards. You will be asked to answer one random
                     question. You will get 1 jewel for each card you answer correctly.
	- Tools in the app: random library, dictionary of cards

4) App2_webmap: A map showing the valcano locations and population of each country.
	- How to run: 
	  a. Execute the program by: python3 app2_webmap.py
	  b. Open up file created in browser: Map1.html
	-youtube demo:https://youtu.be/WPgKAm14Bj0
	- Features: 
	  1) There are markets showing valcano locations. The color indicates the height of the valcano. 			  Green for less than 1000m; orange for between 1000 and 3000m; red for greater than 3000m.
	  2) The color for each country represents the population of the country. Green for less than 10 millions; Orange for between 10 million and 20 millions; Red for greater than 20 millions.
	  3) There is layer country so you can hide/show the 'Valcano layer' or the 'Population layer'.
	- Tools in the app: folium, pandas

5) App3_website_blocker: A website blocker that blocks users from accessing certain website between 8am and 4pm.
	- Tools in the app: time, datetime, host file

6) App5_BookStore: bookstore app: a standalone application that stores book information
	- How to run: python3 app5_script1_tkinter_store.py
	- Features: View books, search book entries, add book entries, update book entries, delete entries.
	- Tools used: Tkinter, sqlite3
	- youtube demo:https://youtu.be/dmOcUb9QPUk

7) App6_webscrapper: An app that scraps century21 property information for Rock Springs, WY
	- How to run: jupyter notbook
	- Features: You can see all the data scrapped in file: Output_allpages.csv
	- Tools used: Pandas, Requests, BeautifulSoup, Jupyter notebook(installation can be done through mini conda)
