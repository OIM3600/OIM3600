import webbrowser


search_query = input("What do you want to search? ")

url = "https://www.google.com/search?q=" + search_query

webbrowser.open(url)
