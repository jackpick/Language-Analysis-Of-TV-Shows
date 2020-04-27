# importing the required modules 
import matplotlib.pyplot as plt
import numpy as np
# open the txt file containing the words you are searching for
words = open ("Words.txt", encoding="utf-8")
# open the txt file containing the titles you are looking for
titles = open ("Titles.txt", encoding="utf-8")
# open the txt file containing the IMDB Rankings you are searching for
IMDBRankings = open ("IMDBRanking.txt", encoding="utf-8")
# set up lists
WordCount=[]
WordsList = []
TitlesList =[]
IMDBRankingList = []
y=[]
x=[]

# add all IMDB rankings to a list
for t in IMDBRankings:
    # remove trailing new line
    t = t.rstrip("\n")    
    # add element to list
    IMDBRankingList.append(t)
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
# set up BiggestWordCount as a variable so the checks can be started from here
BiggestWordCount = 0
# set up n as a variable
n=0
# loop through every title in list
for title in TitlesList:
    a=0
    # add 1 to n for the episode number
    n=n+1
    x.append(n)
    # open the txt file for the corresponding title
    script = open(title, encoding="utf-8")
    # loop through every line in the txt file
    for line in script:
        line = line.lower()
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
    # set the proportion of swearwords there are to a variable
    WordCountLength=(len(WordCount))/a
    # check if this is the biggest word count yet
    if BiggestWordCount<WordCountLength:
        # if it is, set its word count to the biggest word count
        BiggestWordCount = WordCountLength
    # add this to a list to be plotted later
    y.append((len(WordCount))/a)
    # add the episode number to a list to be plotted later
    #x.append(n)
    # empty list
    WordCount = []
    

# points so seasons lines can be plotted
x1 = [7,7] 
y1 = [0,BiggestWordCount]
x2 = [20, 20] 
y2 = [0,BiggestWordCount]
x3 = [33, 33] 
y3 = [0,BiggestWordCount]
x4 = [46, 46] 
y4 = [0,BiggestWordCount]
x5 = [62, 62] 
y5 = [0,BiggestWordCount] 

k = np.array([IMDBRankingList, y,])
l = k [ :, k[0].argsort()]
print(l[0])

# could have used this instead but didnt look as good:
plt.scatter(l[0], l[1], label= "stars", color= "green", marker= "*", s=3)
  
# naming the x axis 
plt.xlabel('IMDB Ranking') 
# naming the y axis 
plt.ylabel('Proportion Of Swear Words in an episode')   
# giving a title to my graph 
plt.title('Proportion of Swear Words in each episode compared to the IMDB ranking')
# show a legend on the plot 
#plt.legend() 
# function to show the plot 
plt.show() 
