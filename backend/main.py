from scraper import get_price, check_size_available
import time

print("What do you want to track?")
print("1. Price")
print("2. Size")

choice = input("Enter 1 or 2: ")

url = input("Enter product URL: ")

# 🔥 PRICE TRACKER
if choice == "1":
    target_price = int(input("Enter target price: "))

    while True:
        print("\nChecking price...\n")

        price = get_price(url)

        if price:
            print("Current price:", price)

            if price <= target_price:
                print("🔥 PRICE DROP! BUY NOW!")
                break
            else:
                print("Waiting 60 sec...\n")
        else:
            print("Error fetching price")

        time.sleep(60)


# 🔥 SIZE TRACKER
elif choice == "2":
    size = input("Enter size (S/M/L): ")

    while True:
        print("\nChecking size...\n")

        result = check_size_available(url, size)

        if result == True:
            print(f"🔥 SIZE {size} AVAILABLE! GO BUY!")
            break
        elif result == False:
            print(f"Size {size} not available. Waiting 60 sec...\n")
        else:
            print("Size not found")

        time.sleep(60)


# ❌ INVALID INPUT
else:
    print("Invalid choice. Restart program.")
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
