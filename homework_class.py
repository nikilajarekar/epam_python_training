import random
from datetime import datetime


#Class to write to Txt File
class WriteToTxt:
    #constructor which takes Data as input arguements
    def __init__(self, category,content,dateline):
        print("Initialising File Writer")
        self.category = category #News,Ad or Opinion Poll
        self.content = content #The news headline or Ad line or Opinion poll Question
        self.dateline = dateline #The Dateline to be written
        self.writer(category,content,dateline)

    def writer(self,category,content,dateline):
        #append mode file open
        try:
            file1 = open(r"C:\Users\Nikil_Ajarekar\PycharmProjects\epam_python\newsfeed.txt","a")
            file1.write(category+" ----------\n")
            file1.write(content + "\n")
            file1.write(dateline + "\n")
            file1.close()
        except IOError:
            print("IOError raised")

#class to get the News data from user
class InputNews:
    def __init__(self,category):
        self.category = category

    def enterData(self,category):#Polymorphic method
        self.category = category
        self.content = input("Please tell us the News Headlines\n")
        city = input("Enter City")
        self.dateline = city + ',' + str(datetime.now())  + "\n"
        return self.category,self.content,self.dateline #return the object data


#class to input the Ad data from user
class InputAd:
    def __init__(self,category):
        self.category = category

    def enterData(self,category):#Polymorphic method
        self.category = category
        try :
            self.content = input("Please tell us your Ad Headline\n")
            date_components = input("Enter Expiration Date in DD/MM/YYYY format\n")
            diff_date = (datetime.strptime(date_components,"%d/%m/%Y")-datetime.strptime(str(datetime.today().strftime('%d/%m/%Y')),"%d/%m/%Y")).days
            self.dateline = "Actual untill " + str(date_components) + ',' + str(diff_date) + " days left" + "\n"
            return self.category, self.content, self.dateline
        except ValueError:
            print("Exception raised : Please enter correct format")
        except AttributeError:
            print("Attribute Not found due to wrong Date format")


#class to input and write Opinion poll Questions and answers
#Inherits the super class
class OpinionPoll(WriteToTxt):
    def __init__(self,category):
        self.category = category

    #function to read the user opinion
    def readOpinion(self,category):
        questions = {1 : "Who will win 2024 Bharat Elections?\n",
                     2 : "Who will win the Premier League?\n" }
        answers = {1 : ["1.Narendra Modi", "2.Pappu"],
                   2 : ["1.Liverpool","2.Others"]}
        QNo = int(random.randint(1,2)) #randomly selects one question
        print(questions[QNo])
        print(answers[QNo])
        choice = int(input("Enter your Opinion : "))
        print("Your Opinion is : ",answers[QNo][choice-1])
        content = str(questions[QNo]) + str(answers[QNo])
        dateline = "Your Opinion is : "  + str(answers[QNo][choice-1]) + "\n"
        self.category = category
        super().writer(category,content,dateline) #uses the parent class' writer method to write to txt file



class ChoiceError(Exception):
    print("In ChoiceError Exception class")


try :
    category = int(input("Enter Category. 1. News 2. Private Advertisement 3.Opinion Poll\n"))

    if category == 1:
        InNews = InputNews("News")
        category,content,dateline = InNews.enterData("News")
        WriteNews = WriteToTxt(category,content,dateline)
    elif category == 2:
        InAd = InputAd("Private Ad")
        category,content,dateline = InAd.enterData("Advertisement")
        WriteAd = WriteToTxt(category,content,dateline)
    elif category == 3:
        InOp = OpinionPoll("Opinion Poll")
        InOp.readOpinion("Opinion Poll")
    else :
        raise ChoiceError("Invalid Category")
except ChoiceError:
        print("Exception raised by Code for invalid Choice")
        raise

