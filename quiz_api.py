#import neccesary module
#----------------------------------------------------
import requests
import json
import pprint
import random
#----------------------------------------------------
Marks=0#calculate the total score
count=0
end=True
while end:
    count+=1
    OP=[]#option stored array
    #--------------------------------------------------------------
    try:
        #connecting to an api
        r=requests.get("https://opentdb.com/api.php?amount=1&category=18&difficulty=easy&type=multiple")
        q=r.text
        res=json.loads(q)#converting json to dic type
    except:
        print("Error",r.status_code)

    #----------------------------------------------------
    question=res['results'][0]['question']
    print(count,question)#question display
    #-----------------------------------------------------

    #option are resupuled using random
    #------------------------------------------------------
    option=res['results'][0]['incorrect_answers']
    option.append(res['results'][0]['correct_answer'])
    stop=0
    while stop<4:
        index=random.randint(0,3)
        if index in OP:
            continue
        else:
            OP.append(index)
            stop=stop+1
    for j in range(1,5):
        print(j,">",option[OP[j-1]])
    #---------------------------------------------------------
    #taking input of answer
    error=True
    while error:
        Answer=input("Answer")
        try:
            a=int(Answer)
            if a>0 and a<5:
                error=False
            else:
                print("Enter an integer beween 1 to 4")       
        except:
            print("Please Enter a intiger value")
    #---------------------------------------------------------
    #Checking Answer and giving marks
    if(option[OP[a-1]]==res['results'][0]['correct_answer']):
        print('Correct Answer')
        Marks+=1
    else:
        print("Incorrect Answer")
        Marks-=1
    print("Your Total Score is %d out of %d"%(Marks,count))
    #-----------------------------------------------------------
    #mor playing
    e=True
    while e:
        play=input("Do you want to play again(y/n):")
        play.lower()
        if play=='y' or play=='n':
            e=False
        else:
            print("Plese Enter y/n")
    if play=='y':
        continue
    elif play=='n':
        #print("Your Total Score is %d out of %d"%(Marks,count))
        end=False
        
        
