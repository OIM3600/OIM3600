import webbrowser

url = 'http://www.pythonchallenge.com/pc/def/0.html'

res = 2 ** 38

new_url = url.replace('0', str(res))

print(new_url)

webbrowser.open(new_url)