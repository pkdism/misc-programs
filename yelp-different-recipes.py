class Recipe():
    def __init__(self, item_name, ingredients):
        self.item_name = item_name
        self.ingredients = ingredients


def n_recipes(recipes):
    s = set()
    for recipe in recipes:
        s.add(tuple(sorted(recipe.ingredients)))
    return len(s)

r = []
r.append(Recipe('Sandwich', tuple(['Bread', 'Butter', 'Cheese', 'Tomato', 'Spinach'])))
r.append(Recipe('Pizza', tuple(['Loaf', 'Butter', 'Cheese', 'Ketchup', 'Corn'])))
r.append(Recipe('Burger', tuple(['Butter', 'Cheese', 'Bread', 'Tomato', 'Spinach'])))

print(n_recipes(r))
