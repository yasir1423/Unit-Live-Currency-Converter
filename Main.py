import requests
def meters_to_kilometers(value):
    return value/1000
def grams_to_kilograms(value):
    return value/1000
def hours_to_minutes(value):
    return value*60
def currency_convertor(amount,from_currency,to_currency):
    url=f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    try:
        response=requests.get(url)
        data=response.json()
        if "rates" not in data:
            return "Error!!! API problem or currency not found."
        rate=data["rates"].get(to_currency.upper())
        if rate is None:
            return "Error: Target Currrency not found."
        return amount*rate
    except Exception as e:
        return "Error:Could not connect to currency API"
#function dictionaries
Conversion_functions={1:("meters=>kilometers",meters_to_kilometers),2:("grams=>kilograms",grams_to_kilograms),3:("hours=>minutes",hours_to_minutes)}
#main program
def main():
    while True:
        print("==UNIT & CURRENCY CONVERTOR==")
        print("1.Meters to Kilometers:")
        print("2.Grams to Kilograms:")
        print("3.Hours to minutes:")
        print("4.Currency Convertor:")
        print("5.Exit")
        choice=int(input("Enter your choice(1-5):"))
        if choice in Conversion_functions:
            label, func=Conversion_functions[choice]
            #label receives text(e.g:meters=>kilometers) and func receives functions(meters_to_kilometers)
            value=float(input(f"Enter value to convert({label}):"))
            result=func(value)#e.g:func=meters_to_kilometers
            print(f"Converted value:{result}")
        elif choice==4:
            print("Currency Convertor")
            amount=float(input("Enter your amount:"))
            from_currency=input("From currency(e.g:USDT):")
            to_currency=input("To currency(e.g:PKR):")
            result=currency_convertor(amount,from_currency,to_currency) 
            print(f"Converted amount:{result}")
        elif choice==5:
            print("Exiting the Program....God Bye.")
            break
        else:
            print("Invalid Choice.Try again later.")
main()           