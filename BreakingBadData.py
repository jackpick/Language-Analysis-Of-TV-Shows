# importing the required module 
import matplotlib.pyplot as plt
# open the txt file containing the words you are searching for
words = open ("Words.txt", encoding="utf-8")
# open the txt file containing the titles you are looking for
titles = open ("Titles.txt", encoding="utf-8")
# set up lists
WordCount=[]
WordsList = []
TitlesList =[]
y=[]
x=[]

# add all words to a list
for g in words:
    # remove trailing new line
    g = g.rstrip("\n")
    # add element to list
    WordsList.append(g)
# remove duplicates
WordsList = list(dict.fromkeys(WordsList))
# close txt file
words.close()
# add all titles to a list
for q in titles:
    # remove trailing new line
    q = q.rstrip("\n")
    # add element to list
    TitlesList.append(q)
# close txt file
titles.close()

# set up n as a variable
n=0
# loop through every title in list
for title in TitlesList:
    a=0
    # add 1 to n for the episode number
    n=n+1
    # separate out lines
    print ("")
    # remove txt from title when it is shown
    ShowTitle = title.rstrip(".txt")
    # show title
    print (ShowTitle)
    # open the txt file for the corresponding title
    script = open(title, encoding="utf-8")
    # loop through every line in the txt file
    for line in script:
        # loops through every word in each line
        for everyword in line:
            # finds how many words their are in each txt file
            a=a+1
        # loop through every word in the word list you are checking for
        for word in WordsList:
            # check if word you are looking for is in that line
            if word in line:
                # add the word to a list
                WordCount.append(word)
    # show the proportion of swearwords there are in this episode
    print ((len(WordCount))/a)
    # add this to a list to be plotted later
    y.append((len(WordCount))/a)
    # add the episode number to a list to be plotted later
    x.append(n)
    # empty list
    WordCount = []



# plotting the points
plt.plot(x, y)

# could have used this instead but didnt look as good:
#plt.scatter(x, y, label= "stars", color= "green", marker= "*", s=30)
  
# naming the x axis 
plt.xlabel('Episode Number') 
# naming the y axis 
plt.ylabel('Number Of Swear Words')   
# giving a title to my graph 
plt.title('Number of Swearwords in Each Breaking bad episode')   
# function to show the plot 
plt.show() 
