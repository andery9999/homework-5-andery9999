if __name__ == "__main__":

    pokemon = ("picachu", "charmander", "bulbasaur")
    
    print(pokemon[1])

    starter1, starter2, starter3 = pokemon

    my_name = tuple("Bo Wang")

    print("i" in my_name)

    for x in range(2, 11) :
        print(x)
    
    y = 2
    while y < 11 :
        print(y)
        y += 1
    
    for z in "This is a simple string" :
        print(z)
    
    set = ("This", "is", "a", "simple", "set")
    for a in range(3):
        for b in set:
            print(b)

    for c in ("this", "is", "a", "simple", "set"):
        for d in range(0,3):
            print(c)
