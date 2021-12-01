contents = []

A = open("musicrecplus.txt", "w+")


B = open("musicrecplus_ex2_a.txt")
   

def artists():
    Artist = []
    Artist1 = 1
    while Artist1 != "" :
        Artist1 = input("Enter an artist that you like (Enter to finish): ")
        if Artist1 in Artist:
            print("Your last input was a duplicate")
        else:
            Artist.append(Artist1)
    Artist.remove('')
    Artist.sort()
    contents = Artist
   

def Username():
    username = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private ): ")
    if username in A.read():
        pass
        #take to menu
    else:
        artists()
        pass
        #enter inicial prefrences

def main():
    Username()
    while menu != e:
    menu = input( """Enter a letter to choose an option :
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit""")

   
if __name__ == "__main__":
    main()
