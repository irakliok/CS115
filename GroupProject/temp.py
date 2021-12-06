contents = []

A = open("musicrecplus.txt", "w+")


#B = open("musicrecplus_ex2_a.txt")
   
def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        # Read and parse a single line
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict

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
    
def ListConverter(n):
    '''List to Dict'''
    Dic = {}
    for i in n:
        Dic[i] = 0
    return artistDict

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
    while menu != "e":
        menu = input( """Enter a letter to choose an option :



e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit""")




def preferences(username, i):
    ''' Creates a list of user's preference.
        If the user is new, then it will ask for their
        preference. If the user isnt then it will return
        the user's prefered artist'''
    musicpre = ""
    if username in i:
        user = i[username]
        print("you already have a list of preferences")
        print("your top music choices are ")
        for a in m:
            print(a)
        musicpre = input("Enter an artist that you like or enter the return key")
    else:
        preference = []
        print("I see that you are a new user.")