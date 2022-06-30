# show cocktail recipe
# v2 - change to one function
# v3 - clean up
# v4 - update recipes
# v5 - update recipes

from tkinter import *

# holds all the recipes
recipes = {
        'martini' : """
    - 2 ounces - dry gin/vodka
    - 1 ounce  - dry vermouth
    - 1 dash   - orange bitters
    - olive    - 'bad'

    Mix - shaker
    Garnish - Lemon Peel
    """,

        'maragarita' : """
    - 2 ounces - white tequila
    - 1/2 ounce - orange liqueur
    - 1 ounce  - lime juice, freshly squeezed
    - 1/2 ounce - agave syrup

    Mix - shaker
    Garnish - Lime Wheel (kosher salt, chillies)
    """,

    'old_fashioned':"""
    - 2 ounces       -  bourbon
    - 1/2 teaspoon   -  sugar
    - 1 teaspoon     -  water
    - 3 dashes       -  angostura bitters
    
    Mix - sugar, water, bitters - rock glass
    Garnish - Orange Peel
    """,

    'manhattan':"""
    - 2 ounces - bourbon 
    - 1 ounce  - sweet vermouth
    - 2 dashes - angostura bitters
    - 1 dash   - orange bitters

    Mix - in glass
    Garnish - bradied cherry or lemon twist
    """,

    'cosmopolitan':"""
    - 1 1/2 ounces   - vodka
    - 3/4 ounces     - cointreau
    - 3/4 ounces     - lime juice freshly squeezed
    - 1/2 ounce      - cranberry juice

    Mix - shaker
    Garnish - lime wedge
    """,

    'negroni':"""
    - 1 ounce   - gin
    - 1 ounce   - campari
    - 1 ounce   - sweet vermouth

    Mix - glass
    Garnish  - orange peel
    """,

    'long island iced tea':"""
    - 3/4 ounce     - vodka
    - 3/4 ounce     - white rum
    - 3/4 ounce     - silver tequila
    - 3/4 ounce     - gin
    - 3/4 ounce     - triple sec
    - 3/4 ounce     - simple syrup
    - 3/4 ounce     - lemon juice, freshely squeezed
    - to top        - cola

    Mix  - glass
    Garnish - lemon wedge
    """,

    'tom collins':"""
    - 2 ounces     - dry gin
    - 1 ounce      - lemon juice, freshly squeezed
    - 1/2 ounce    - simple syrup
    - to top       - club soda

    Mix - glass
    Garnish - lemon wheel, maraschino cherry
    """,
    
    'moscow mule':"""
    - 2 ounces    - vodka
    - 1/2 ounces  - lime juice, freshly squeezed
    - 3 ounces    - ginger beer
    
    Mix - glass
    Garnish - lime wheel
    """,

    }

def recpLabel(name, text='Not Defined'):
    """
    Create the recipe label
    """
    win = Toplevel()
    win.title(name)
    Label(win, text=text).pack()

root = Tk()
root.title('Cocktail Recipes')
icon = PhotoImage(file='jk_icon.png')
root.iconphoto(False, icon)
for cocktail in recipes:
    """
    create one button for each item in the recipe
    """
    Button(root, text=cocktail, command=\
            lambda cock=cocktail: recpLabel(cock, recipes[cock])\
            ).pack(expand=YES, fill=BOTH)

#Button(root, text='margarita', command=margarita).pack()
Button(root, text='Quit', command=root.quit).pack()
root.mainloop()
