

bike_price = 2000
def new_bike_price():
    bike_price = bike_price * 0.9
    print(bike_price)

new_bike_price()
while new_bike_price >= 1000:
    print(new_bike_price)
    new_bike_price = new_bike_price + 1


