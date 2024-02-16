# import urllib.request

# u = urllib.request.urlopen("https://www.babson.edu")
# data = u.read()
# print(data)

# print("hello, world!")


name = "MSFT"
shares = 100
price = 317.92

# print(name, shares, price)
print(f"{name:>10s}: {shares:10d}, ${price:5.2f}")

print(f"Cost = ${shares*price:0.2f}")
# Cost = $31792.00
