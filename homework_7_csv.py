import csv
import random
from datetime import datetime
import sys
import os
import Functions_Homework
import re
import string

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
            file1.write("\n" + category+" ----------\n")
            file1.write(content + "\n")
            file1.write(dateline + "\n")
            file1.close()
        except IOError:
            print("IOError raised")

class WordCount: #class for wordcount and letter count
    def __init__(self):
        pass
    def count_words(self): #function for word count
        #read the news feed output file
        with open(r"C:\Users\Nikil_Ajarekar\PycharmProjects\epam_python\newsfeed.txt","r") as f1:
            reader_result = csv.reader(f1,delimiter=" ")
            w_count = {}
            for row in reader_result:
                for word in row:
                    if re.match('[a-zA-Z]+',word): #only to match the words not the numbers
                        if word.lower() in w_count:
                            w_count[word.lower()] += 1
                        else :
                            w_count[word.lower()] = 1
            return w_count
    def count_letters(self): #function for letter counting
        with open(r"C:\Users\Nikil_Ajarekar\PycharmProjects\epam_python\newsfeed.txt","r") as f1:
            reader_result = csv.reader(f1,delimiter=" ")
            list_a_z = list(string.ascii_lowercase) #initialization
            l_count={} #total_count
            upper_count={} #upper_count
            for x in list_a_z:
                l_count[x] = 0
                upper_count[x] = 0
            for row in reader_result:
                for word in row:
                    for i in range(len(word)):
                        if re.match('[a-z]',word[i]): #for matching lower case letters
                                l_count[word[i]] += 1
                        elif re.match('[A-Z]',word[i]): #upper case matching
                                l_count[word[i].lower()] += 1
                                upper_count[word[i].lower()] += 1
            return l_count,upper_count
    def write_wordcount_csv(self,name,wc_dict): #writing to word count csv
        with open(name+".csv","w",newline='') as w1:
            test_writer = csv.writer(w1,dialect='excel')
            for key,value in wc_dict.items():
                test_writer.writerow([str(key) + " : " + str(value)])


    def write_lettercount_csv(self,name,l_count,upper_count): #writing to letter count csv
        headers = ['letter','Total_count','UpperCase_count','Percentage']
        with open(name+".csv","w",newline='') as w1:
            test_writer = csv.DictWriter(w1,fieldnames=headers)
            test_writer.writeheader()
            for key,value in l_count.items():
                if l_count[key] != 0:
                    test_writer.writerow({'letter':str(key),'Total_count':value,'UpperCase_count':str(upper_count[key]),'Percentage': (upper_count[key] / value ) * 100})
                else:
                    test_writer.writerow({'letter': str(key), 'Total_count': value, 'UpperCase_count': str(upper_count[key]), 'Percentage': "N/A"})


#class to get the News data from user
class InputNews:
    def __init__(self,category):
        self.category = category

    def enterData(self,category):#Polymorphic method
        self.category = category
        self.content = input("Please tell us the News Headlines\n")
        city = input("Enter City")
        self.dateline = city + ' , ' + str(datetime.now())  + "\n"
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

class ImportFromTxtFile:
    def __init__(self,path):
        try :
            with open(path+ "\\" + "NewsFeed1.txt","r") as file1:
                lines = file1.readlines()
                print(lines)
                file2 = open("newsfeed.txt","a")
                for line in lines:
                    liness = Functions_Homework.normalize(line)
                    file2.writelines(liness)
            file2.close()
            #os.remove(path+"NewsFeed1.txt")
        except FileNotFoundError:
            print("File Not Found")

class ChoiceError(Exception):
    print("In Choice Error Exception class")


try :
    category = int(input("Enter Category. 1. News 2. Private Advertisement 3.Opinion Poll "
                         "4.Import Directly from .txt file\n"))

    if category == 1:
        InNews = InputNews("News")
        category,content,dateline = InNews.enterData("News")
        WriteNews = WriteToTxt(category,content,dateline)
        wc = WordCount() #object to calculate wordcount
        wc_dict = wc.count_words() #function to count words
        wc.write_wordcount_csv("word_count",wc_dict)
        lc_dict,upper_count = wc.count_letters() #function to count letters
        wc.write_lettercount_csv("letter_count",lc_dict,upper_count)
    elif category == 2:
        InAd = InputAd("Private Ad")
        category,content,dateline = InAd.enterData("Advertisement")
        WriteAd = WriteToTxt(category,content,dateline)
        wc = WordCount()
        wc_dict = wc.count_words()
        wc.write_wordcount_csv("word_count",wc_dict)
        lc_dict,upper_count = wc.count_letters()
        wc.write_lettercount_csv("letter_count",lc_dict,upper_count)
    elif category == 3:
        InOp = OpinionPoll("Opinion Poll")
        InOp.readOpinion("Opinion Poll")
        wc = WordCount()
        wc_dict = wc.count_words()
        wc.write_wordcount_csv("word_count",wc_dict)
        lc_dict,upper_count = wc.count_letters()
        wc.write_lettercount_csv("letter_count",lc_dict,upper_count)
    elif category == 4 :
        try :
            if sys.argv[1] != '':
                print(sys.argv[1])
                imp = ImportFromTxtFile(sys.argv[1])
        except IndexError:
            default_path = 'C:\\Users\\Nikil_Ajarekar\\Downloads\\'
            imp = ImportFromTxtFile(default_path)
        wc = WordCount()
        wc_dict = wc.count_words()
        wc.write_wordcount_csv("word_count", wc_dict)
        lc_dict, upper_count = wc.count_letters()
        wc.write_lettercount_csv("letter_count", lc_dict, upper_count)
    else :
        raise ChoiceError("Invalid Category")

except ChoiceError:
        print("Exception raised by Code for invalid Choice")
        raise

