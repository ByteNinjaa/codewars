#https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

def cakes(recipe, available):
    max_cakes = float('inf')
    
    for ingredient, amount in recipe.items():
        if ingredient not in available:
            return 0
        
        max_cakes = min(max_cakes, available[ingredient] // amount)
    
    return max_cakes
