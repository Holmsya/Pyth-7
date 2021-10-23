favoritSports = ["Footbal", "Tennis"]

userFavoritSport = input("Input favorite: ").capitalize()

favoritSports.append(userFavoritSport)

favoritSports.sort()

for sport in favoritSports:
    print(sport)
