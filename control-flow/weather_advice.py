# clothing advice for a weather condition
weather = input("what's the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print("Wear a t-shirt and sun glasses.")

elif weather == "rainy":
    print("Don't forget your umbrella and rain coat.")

elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")

else:
    print("Sorry, I don't have recommendation for this weather.")
