# importing the required modules

from sklearn import linear_model
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
# open the txt file containing the words you are searching for
words = open ("Words.txt", encoding="utf-8")
# open the txt file containing the writers
writers = open ("Writers.txt", encoding="utf-8")
# open the txt file containing the titles you are looking for
titles = open ("Titles.txt", encoding="utf-8")
# set up lists
WritersList = []
WordCount=[]
WordsList = []
TitlesList =[]
EpisodeSwearWordNumber = []
ElementNumberList = []

WriterTitlesList = []

#y=[]
x=[]

# writers we are looking for as they wrote enough episodes for the graphs to show something

print ("Choose from these writers:")
print ("")
print ("Vince Gilligan")
print ("George Mastras")
print ("Sam Catlin")
print ("Peter Gould")
print ("Moira Walley-Beckett")
print ("Thomas Schnauz")

WriterInput = input()
WriterInput = str(WriterInput)
# writers we aren't looking for as they didnt write many episodes

##Gennifer Hutchison
##John Shiban
##Patty Lin
##J. Roberts

# add all writers to a list
for b in writers:
    # remove trailing new line
    b = b.rstrip("\n")
    # add element to list
    WritersList.append(b)
# close txt file
writers.close()
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
# sets up the element number so you can get the episode number of the episodes written by vince
ElementNumber = 0
#loop through the wrter for each episode
for d in WritersList:
    if WriterInput in d:
        # had to use a try statement here, as for some reason the program got all the episodes correct that were written by vince but then stopped working as it used the number 63 which is outside of the idex range, if anyone knows how to fix this, please help
        try:
            # add the episode name to the list containing episodes just written by Vince Gilligan by using their corresponding episode number
            WriterTitlesList.append(TitlesList[ElementNumber])
            ElementNumberList.append(ElementNumber+1)
        except:
            print # if you want to see what the error is, put (ElementNumber) after this print
            #count the epsodes
    ElementNumber = ElementNumber+1
# loop through every title in list
for title in WriterTitlesList:
    a=0
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
    EpisodeSwearWordNumber.append((len(WordCount))/a)
    # empty list
    WordCount = []
    
# find the correlation of the points    
correlation, p_value = stats.pearsonr(ElementNumberList, EpisodeSwearWordNumber)
# show the correlation
print ("correlation:",correlation)

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


# plotting the points of swearword graph
#plt.plot(IMDBRankingList, y)

# seaparating the gaph with seasons
plt.plot(x1, y1, label = "Season 1 Finale")
plt.plot(x2, y2, label = "Season 2 Finale")
plt.plot(x3, y3, label = "Season 3 Finale")
plt.plot(x4, y4, label = "Season 4 Finale")
plt.plot(x5, y5, label = "Season 5 Finale")

coef = np.polyfit(ElementNumberList, EpisodeSwearWordNumber,1)
poly1d_fn = np.poly1d(coef) 
# poly1d_fn is now a function which takes in x and returns an estimate for y

plt.plot(ElementNumberList, EpisodeSwearWordNumber, 'yo', ElementNumberList, poly1d_fn(ElementNumberList), '--k', color= "green")
plt.xlim(0, 63)
plt.ylim(0, 0.0037)

# could have used this instead but didnt look as good:
#plt.scatter(IMDBRankingList, EpisodeSwearWordNumber, color= "green", marker= "x", s=10)
# naming the x axis 
plt.xlabel('Episode Number') 
# naming the y axis 
plt.ylabel('Proportion Of Swear Words')   
# giving a title to my graph 
plt.title('Proportion of Swear Words in each Breaking Bad episode written by ' + WriterInput)
# show a legend on the plot 
plt.legend() 
# function to show the plot 
plt.show()
