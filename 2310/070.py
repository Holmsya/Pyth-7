countries = ("Belgia", "Moldova", "Japan", "Romania", "Serbia")

for country in countries:
    print(country)

countryID = int(input("Input country id plz: "))
try:
    print(countries[countryID])
except IndexError:
    print("Not found")
