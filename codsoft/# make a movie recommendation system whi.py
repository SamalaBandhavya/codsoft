# make a movie recommendation system which take in user input of what kind of movie they want to watch
#1. anim
#2. romcom
#3. Action
#4. Thriller
#Also randomize output everytime
import random 

genreip = input("Hey ya! Give your choice and I will give you a great recommedation! \n1)anim\n2)romcom\n3)Action\n4)Thriller")

movieDict = { "anim" : ["frozen", "The lion king","shrek"],
            "romcom": ["call me by your name","la la land","titanic"],
            "action": ["the dark knight","the matrix","terminator2:the judgement day"],
            "Thriller": ["silence if lambs","shutter island","se7en"]
            }
print("\n\ni/p: "+genreip)
print("\no/p: "+movieDict[genreip][random.choice([0,1])]," , ",movieDict[genreip][random.choice([2,3])])