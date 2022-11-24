"""
Timmy & Sarah think they are in love, but around where they live, 
they will only know once they pick a flower each. 
If one of the flowers has an even number of petals and the other has an odd number 
of petals it means they are in love.
Write a function that will take the number of petals of each flower and return 
true if they are in love and false if they aren't.
"""

def lovefunc( flower1, flower2 ):
    # ...
    test1 = 'odd'
    test2 = 'odd'
    if flower1%2 == 0:
        test1 = 'even'
    if flower2%2 == 0:
        test2 = 'even'
    if test1 == test2:
        return False
    else:
        return True