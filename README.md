# RECIPES
Write a program in Python language for reading the ingredients needed to make a recipe, and the calculation of the cost and calories of the recipe.

The program must:

read the necessary ingredients from a recipe file. In particular, each recipe is described in the following format:

Ingredients:
Ingredient name 1; needed ingredient 1 grams
Ingredient name 2; necessary ingredient 2 grams
...
Ingredient name n; grams needed ingredient n
Method:
Description of the procedure for making the recipe
...
Note that the ingredient list is preceded by the keyword "Ingredients", which the ingredients are reported one per line, together with the required quantity (in grams), and that after the list of ingredients is the procedure is shown, highlighted by the keyword "Procedure".

read from a second file foods.txt the detailed data on the cost and calories of each food that can be used as ingredient of recipes. In particular, this file contains, for each line, the food, the cost per kg, and the calories per kg, separated by a semicolon.

manage any exceptions in reading from file

1)print the list of ingredients of the recipe, reporting them one per line and separating the ingredient name and quantity from a " - "

2)print the number of ingredients needed to make the recipe

3)print the total cost of the recipe

4)print the total calories of the recipe

Example of Execution
Example of program output, based on the polenta_concia.txt file:

Ingredients:
Corn flour - 500.0
Toma - 200.0
Fontina - 200.0
Butter - 200.0

Number of ingredients: 4
Recipe cost: 7.52
Recipe calories: 2928.0
