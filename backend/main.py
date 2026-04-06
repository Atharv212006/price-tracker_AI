from scraper import get_price

url = input("Enter product URL: ")
target_price = int(input("Enter your target price: "))

price = get_price(url)

if price:
    print("Current price:", price)

    if price <= target_price:
        print("🔥 BUY NOW! Price dropped!")
    else:
        print("Not yet. Keep waiting...")
else:
    print("Couldn't fetch price.")