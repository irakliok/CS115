contents = []

#A = open("musicrecplus.txt", "w+")
#A = open("musicrecplus_ex2_a.txt")
#A = "musicrecplus_ex2_a.txt"
A = "musicrecplus.txt"

def main():
    '''Main function, initiates the program'''
    userDict = loadUsers(A)
    userName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
    if userName == '':
        while userName == '':
            print('You cannot enter a blank username. Please enter a username.')
            userName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
    if userName not in userDict:
        preferences(userDict, userName)
    options = ['e', 'r', 'p', 'h', 'm', 'q']
    while True:
        print("Enter a letter to choose an option :")
        print("e - Enter preferences")
        print("r - Get recommendations")
        print("p - Show most popular artists")
        print("h - How popular is the most popular")
        print("m - Which user has the most likes")
        print("q - Save and quit")
        choice = input();
        while choice not in options:
            print("Enter a letter to choose an option :")
            print("e - Enter preferences")
            print("r - Get recommendations")
            print("p - Show most popular artists")
            print("h - How popular is the most popular")
            print("m - Which user has the most likes")
            print("q - Save and quit")
            choice = input();
        if choice == 'e':
            preferences(userDict, userName)
        if choice == 'r':
            recs = Recommendation(userName,userDict,filtermap(userDict))
            print(recs)
        if choice == 'p':
            popular(filtermap(userDict))
        if choice == 'h':
            likes(filtermap(userDict))
        if choice == 'm':
            bestUser(filtermap(userDict))
        if choice == 'q':
            saveAndQuit(userDict,A,userName,userDict[userName])

def menu():
    pass

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
    return Dic


def preferences(userDict, userName):
    '''allows users to enter their preferences and updates, if necessary'''
    artistlist = []
    preference = input("Enter an artist that you like (Enter to finish):\n")
    if preference == '':
        while preference == '':
            print('You must enter at least 1 artist before you can proceed')
            preference = input("Enter an artist that you like (Enter to finish):\n")
    else:
        while preference != '':
            artistlist.append(preference)
            preference = input("Enter an artist that you like (Enter to finish):\n")
            userDict[userName] = list(set(artistlist))

def Recommendation(currUser, preference, i):
    '''
    Gets recommendations for currUser based on the users in i
    (a dictionary) and the current user's preferences in prefs (a list)
    '''
    bestuser = None
    bestscore = -1
    rec = []
    for user in i.keys():
        score = numMatches(preference, i[user])
        if score > bestscore and currUser != user:
            bestscore = score
            bestuser = user
            bestuser
        for j in i[bestuser]:
            if j in preference:
                []
            else:
               rec = rec + [j]
    rec.sort()
    if rec == []:
        return "No recommendations available at this time ."
    else:
        return rec

def numMatches(n,m):
    ''' gives the amount of elements that are shared among two lists '''
    result = 0
    for i in n:
        if i in m:
            result += 1
    return result
def filtermap(dictionary):
    ''' returns a new dictionary with public users only'''
    newdict = {}
    for key, value in dictionary.items():
        if key[-1] != '$':
            newdict[key] = value
    return newdict
 
def popular(userDict):
    '''Option p: returns the most popular artists'''
    userlist = userDict.keys()
    likes = {}
    mostPopular = []
    maxLikes = 0
    for user in userlist:
        for artist in userDict[user]:
            if artist in likes:
                likes[artist] += 1
            else:
                likes[artist] = 1
    for artists in likes:
        if likes[artists] > maxLikes:
            maxLikes = likes[artists]
    for artists in likes:
        if likes[artists] == maxLikes:
            mostPopular.append(artists)
    if mostPopular == []:
        print("Sorry, no artists found")
    else:
        for artist in mostPopular:
            print(artist)
   

def likes(userDict):
    '''returns the number of likes that the most popular artist has'''
    userlist = list(userDict.keys())
    if userlist == []:
        print("Sorry, no artists found")
    else:
        likes = {}
        mostPopular = []
        maxLikes = 0
        for user in userlist:
            for artist in userDict[user]:
                if artist in likes:
                    likes[artist] += 1
                else:
                    likes[artist] = 1
        for artists in likes:
            if likes[artists] > maxLikes:
                maxLikes = likes[artists]
        for artists in likes:
            if likes[artists] == maxLikes:
                mostPopular.append(artists)
        print(maxLikes)

def bestUser(userDict):
    '''returns the user with the most likes'''
    users = list(userDict.keys())
    if users == []:
        print("Sorry, no user found")
    else:
        maximum = 0
        bestUser = []
        for x in range(len(users)):
            if len(userDict[users[x]]) >= maximum:
                maximum = len(userDict[users[x]])
                bestUser.append(users[x])
        for x in range(len(bestUser)):
            print(bestUser[x])

def saveAndQuit(dict,fileName,user,preferences):
    '''Option q: Saves preferences and ends program'''
    dict[user] = preferences
    file = open(fileName, 'w')
    for user in dict:
        newline = str(user)+":"+",".join(dict[user])+ \
                  "\n"
        file.write(newline)
    file.close()


if __name__ == "__main__": main()