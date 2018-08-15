# 02_UD_Portfolio
My portfolio of work - 2017 and 2018
>Stay tuned for more apps.

1) Presentation: BART delay analysis
   https://docs.google.com/presentation/d/1TtxBkK_1ycEkZEMcZ7vQ9ChIyhvvPe13v18e2xERlTQ/edit?usp=sharing 
   - description: Used Twitter data from @SFBARTalert to analyze delay metrics for the past two years
   - Tools/Libraries: csv, pandas, matplotlib.pyplot, seaborn, datetime, numpy, plotly  

2) Presentation: Data engineering experiment 
    https://docs.google.com/presentation/d/1_YzgOiKi_mDTA2ZA-337RQc9RMSzSYbIX39nPaqlXSw/edit?usp=sharing
	- description: comparison of the processing time between Pandas versus Python data structure for a base case ETL process
	- Tools/Libraries: pandas, datetime, sqlalchemy, pymysql, csv

3) App8_TwitterAnalyzeBot: Generates a sentiment plot with the request of another Twitter user.
	- How to use: Example of a request to do Sentiment analysis on CNN: "@LenaCorredor Analyze: @CNN".  
		      The result will be a Sentiment Analysis of CNN tweeted to the requested user.
	   	      This Script will also output a log file.
	- Tools: Matplotlib, pandas, tweepy  
	- Status: turned off
	
4) App7_FinancialGraph: Candle stick stock price graph deployed on Heroku.
	- How to view: https://lenafgraph.herokuapp.com/plot/
	- Features: plot can be saved in png format. Plot can zoom and pan.
	- Tools used: Bokeh(plots), pandas datareader(to get stock prices), flask

5) App6_webscrapper: An app that scraps century21 property information for Rock Springs, WY
	- How to run: jupyter notbook
	- Features: The scrapped data can be viewed in file: Output_allpages.csv
	- Tools used: Pandas, Requests, BeautifulSoup, Jupyter notebook(installation can be done through mini conda)

6) App5_BookStore: A bookstore standalone application that stores book information.
	- Main file: app5_script1_tkinter_store.py
	- Features: View books, search book entries, add book entries, update book entries, delete entries.
	- Tools used: Tkinter, sqlite3
	- youtube demo:https://youtu.be/dmOcUb9QPUk

7) App3_website_blocker: A website blocker that blocks users from accessing certain website between 8am and 4pm.
	- Tools in the app: time, datetime, host file

8) App2_webmap: A map showing the valcano locations and population of each country.
	- How to run: 
	  a. Execute the program by: python3 app2_webmap.py
	  b. Open up file created in browser: Map1.html
	-youtube demo:https://youtu.be/WPgKAm14Bj0
	- Features: 
	  1) There are markers showing valcano locations. The color indicates the height of the valcano. 			  
	     Green for less than 1000m; orange for between 1000 and 3000m; red for greater than 3000m.
	  2) The color for each country represents the population of the country. Green for less than 
	     10 millions; Orange for between 10 million and 20 millions; Red for greater than 20 millions.
	  3) There is layer-country so the user can hide/show the 'Valcano layer' or the 'Population layer'.
	- Tools in the app: folium, pandas

9) app_physiology_card_game: This is a beta version. A buzzfeed game that helps the player learn human physiology.
	- How to run: Execute the main file Game1_v2.py, then follow instructions
	- Features: This app helps player learn by showing facts and checks if player remember them until a correct 
		    answer is selected.
	- How to play: The player have 4 cards to play with. Each card will have three facts to browse through.
                     After the player have browsed through all the cards. The player will be asked to answer one random
                     question. The player will get 1 jewel for each card answered correctly.
	- Tools in the app: random library, dictionary of cards

10) App_weather_api: Connects to a weather website api and checks the weather to see if an umbrella is needed today.
	- How to run: Install flask. Start up the Flask server in a virtual environment and apply the requirement.txt file. 
		      Make sure there is connection to the internet.
	- Features: Works for most US cities and zip codes, and possibility some international cities.
	- Tools in the app: Flask, API

11) App1_Dictionary: a python command line app that outputs the definition of a word entered.
	- How to run: Execute the program by: python3 app1_Ditionary.py
	- Features: If a word is mistyped. For example: rainn instead of rain, the program will suggest the closest matching word.
	- Tools in the app: JSON file, difflib
	- youtube demo: https://youtu.be/2_JH0JhCag0














