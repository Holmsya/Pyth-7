countries = ("Belgia", "Moldova", "Japan", "Romania", "Serbia")

for country in countries:
    print(country)

userCountry = input("Input country plz: ").capitalize()
try:
    print(countries.index(userCountry))
except ValueError:
    print("Not found")
