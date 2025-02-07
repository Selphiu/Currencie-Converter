import requests, json

API_KEY = "INSERT HERE YOUR API KEY FROM EXCHANGERATE-API" #https://app.exchangerate-api.com/dashboard  - its free for 1500 requests
def get_valutes():
    global API_KEY
    print("Hello, User! Please, enter 1 Valute: ")
    valute1s = str(input())

    if len(valute1s) != 3 or not valute1s.isalpha():
        print("Invalid input. Please enter a valid 3-letter currency code.")
        return get_valutes()
    
    valute1 = valute1s.upper()
    print("Enter 2 Valute: ")
    valute2s = str(input())

    if len(valute2s) != 3 or not valute2s.isalpha():
        print("Invalid input. Please enter a valid 3-letter currency code.")
        return get_valutes()
    
    valute2 = valute2s.upper()

    while True:
        try:
            value = float(input("Enter value: "))
            break 
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue  
    
    get_curse(valute1, valute2, value)

def get_curse(valute1, valute2, value):
    check = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{valute1}")
    data = check.json()
    
    rates = data["conversion_rates"]
    if valute1 not in rates or valute2 not in rates:
        print("Invalid Valute")
        get_valutes()
        return 
    
    if valute1 == valute2:
        print(f"1 {valute1} = 1 {valute2}")
    else:
        converted_valute = value * rates[valute2]
        print(f"{value} {valute1} = {converted_valute} {valute2}")

get_valutes()