RICETTE  = "polenta_concia.txt"
FOODS = "foods.txt"
def main():
    food_info = dict()
    with open(FOODS) as f:
        for line in f:
            fields = line.split(";")
            food = fields[0]
            price = float(fields[1])
            calories = int(fields[2])
            food_info[food] = [price,calories]
    total_price = 0
    total_cals = 0
    number = 0
    with open(RICETTE) as f:
        for i,line in enumerate(f): #allows to have the lines index
            if i != 0 :
                fields = line.split(";")
                if len(fields) != 2:
                    break
                food = fields[0]
                quantity = int(fields[1])/1000
                total_price += quantity * food_info[food][0]
                total_cals += quantity * food_info[food][1]
                number += 1
                print(f'{food} - {quantity * 1000}')
    print()
    print(f'Recipe cost : {total_price}, \nRecipe calories : {total_cals},\nNumber of ingredients : {number}')


if __name__ == "__main__":
    main()
