from typing import Dict, Text, Any, List, Union, Optional
from sendotp import sendotp ##to install "pip install sendotp"

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
import re
from rasa_sdk import Action
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
#import pandas as pd
from typing import Any, Text, Dict, List
from pymongo.database import Database
from pymongo import MongoClient
from rasa_sdk import Action, Tracker 
from rasa_sdk.executor import CollectingDispatcher
import pymongo
#######otp func imports######
import json
import requests
from random import randint

class sendotp:

    def __init__(self, key, msg):

        self.baseUrl = "http://control.msg91.com"
        self.authkey = key

        try:
            msg
        except NameError:
            self.msg = "Your otp is {{otp}}. Please do not share it with anybody"
        else:
            self.msg = msg

    def actionURLBuilder(self, actionurl):
        # print self.baseUrl + '/api/' +str(actionurl)
        #print (actionurl)
        return self.baseUrl + '/api/' + str(actionurl)

    def generateOtp(self):
        return randint(1000, 9999)

    def send(self, contactNumber, senderId, otp):
        values = {
            'authkey': self.authkey,
            'mobile': contactNumber,
            'message': self.msg.replace("{{otp}}", str(otp)),
            'sender': senderId,
            'otp': otp
        }
        print (self.call('sendotp.php', values))
        return otp

    def retry(self, contactNumber, retrytype='text'):
        values = {
            'authkey': self.authkey,
            'mobile': contactNumber,
            'retrytype': retrytype
        }
        print (values)
        response = self.call('retryotp.php', values)
        return;

    def verify(self, contactNumber, otp):
        values = {
            'authkey': self.authkey,
            'mobile': contactNumber,
            'otp': otp
        }
        response = self.call('verifyRequestOTP.php', values)
        return response

    def call(self, actionurl, args):
        url = self.actionURLBuilder(actionurl)
        #print (url)
        payload = (args)

        response = requests.post(url, data=payload, verify=False)
        #print (response.text)
        return response.text#status_code
otpobj=sendotp('293971AJNhj1bUMHcC5e3bd0d9P1','Your OTP code is {{otp}} keep otp with you. \nFrom CareerLabs PVT LTD.')
###############################################
class QuestionsForm(FormAction):
    def name(self):
        return "questions_form"

    def required_slots(self,tracker) -> List[Text]:
        return ["question_1","question_2","question_3","question_4","question_5","question_6"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "question_1": [
                self.from_text(),
            ],
            "question_2": [
                self.from_text(),
            ],
            "question_3": [
                self.from_text(),
            ],
            "question_4": [
                self.from_text(),
            ],
            "question_5": [
                self.from_text(),
            ],
            "question_6": [
                self.from_text(),
            ],
            
        }
    def validate(self, dispatcher, tracker, domain):
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
        q1=["My Coding Ability","My Ability  to Get Things done","My Creative Work","My Ability to Play with Data and Get Insights","My Engineering Mastermind"]
        q4=["How AI can save the world","The evolution of Animation Films since Toy Story","The New Age Marketing","The beauty of Analytics and Visualization","Engineers beyond engineering -- The Art of being an Engineer"]
        q2=["Architect, Design, Develop,Software Products","Plan and Get things Done","Work on animated movies","Analyse Information & Execute Projects","Engineer solutions to real world problems"]
        q5=["The art of computer programming","The One Minute Manager","Pixar Storytelling: Rules for Effective Storytelling Based on Pixar’s Greatest Films","Business Analytics for Managers: Taking Business Intelligence Beyond Reporting","The essential pleasures of engineering"]
        q3=["Software Engineer","Product Manager","Character Animator","Business Analyst","Work in my Core Technical field"]
        q6=["Youtube Recommendation Algorithms","Making Policy Changes that Help Employees","Google Creative Team's Projects","Google Analytics Team's Projects","Any Engineering Team in my Domain"]
        myclient = pymongo.MongoClient("localhost", 27017)
        #mydb=myclient["rasa"]#database name
        #mycol=mydb["user_details"] #it is a collection name in the db rasa .
        for slot, value in slot_values.items():
                if slot == 'question_1':
                    if value not in q1:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
                elif slot == 'question_2':
                    if value not in q2:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
                elif slot == 'question_3':
                    if value not in q3:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
                elif slot == 'question_4':
                    if value not in q4:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
                elif slot == 'question_5':
                    if value not in q5:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
                elif slot == 'question_6':
                    if value not in q6:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        optA = ['How AI can save the world','Architect, Design, Develop,Software Products','The art of computer programming','Software Engineer','Youtube Recommendation Algorithms','My Coding Ability']
        optB = ['My Abilty to Get Things done','The New Age Marketing','Plan and Get things Done','The One Minute Manager','Product Manager','Making Policy Changes that Help Employees']
        optC = ['My Creative Work','The evolution of Animation Films since Toy Story','Work on animated movies','Pixar Storytelling: Rules for Effective Storytelling Based on Pixar’s Greatest Films','Character Animator','Google Creative Team\'s Projects']
        optD = ['My Ability to Play with Data and Get Insights','The beauty of Analytics and Visualization','Analyse Information & Execute Projects','Business Analytics for Managers: Taking Business Intelligence Beyond Reporting','Business Analyst','Google Analytics Team\'s Projects']
        optE = ['My Engineering Mastermind','Engineers beyond engineering -- The Art of being an Engineer','Engineer solutions to real world problems','The essential pleasures of engineering','Work in my Core Technical field','Any Engineering Team in my Domain']
    
        ent1 = tracker.get_slot("question_1")
        ent2 = tracker.get_slot("question_2")
        ent3 = tracker.get_slot("question_3")
        ent4 = tracker.get_slot("question_4")
        ent5 = tracker.get_slot("question_5")
        ent6 = tracker.get_slot("question_6")
        countA = 0
        countB = 0
        countC = 0
        countD = 0
        countE = 0
        print(ent1)
    
        #for question 1 
        if ent1 in optA:
            countA += 1
        elif ent1 in optB:
            countB += 1
            
        elif ent1 in optC:
            countC += 1
          
        elif ent1 in optD:
            countD += 1
           
        elif ent1 in optE:
            countE += 1
                
        #for question 2 
        if ent2 in optA:
            countA += 1
        elif ent2 in optB:
            countB += 1
        elif ent2 in optC:
            countC += 1
        elif ent2 in optD:
            countD += 1
        elif ent2 in optE:
            countE += 1  
                
        #for question 3 
        if ent3 in optA:
            countA += 1
        elif ent3 in optB:
            countB += 1
        elif ent3 in optC:
            countC += 1
        elif ent3 in optD:
            countD += 1
        elif ent3 in optE:
            countE += 1
                
        #for question 4 
        if ent4 in optA:
            countA += 1
        elif ent4 in optB:
            countB += 1
        elif ent4 in optC:
            countC += 1
        elif ent4 in optD:
            countD += 1
        elif ent4 in optE:
            countE += 1  
                
        #for question5 
        if ent5 in optA:
            countA += 1
        elif ent5 in optB:
            countB += 1
        elif ent5 in optC:
            countC += 1
        elif ent5 in optD:
            countD += 1
        elif ent5 in optE:
            countE += 1 
                
        #for question6 
        if ent6 in optA:
            countA += 1
        elif ent6 in optB:
            countB += 1
        elif ent6 in optC:
            countC += 1
        elif ent6 in optD:
            countD += 1
        elif ent6 in optE:
            countE += 1  
        l=[countA,countB,countC,countD,countE]
        print(l)
        nl=sorted(l)
        print(nl)
        top1=nl[-1]
        top2=nl[-2]
        top3=nl[-3]
        top4=nl[-4]
        top5=nl[-5]
        
        rcomd1=""
        rcomd2=""
        print(countA)
        print(countE)
        print(top1)
        print(top2)
        ###########################recomd 1
        if countA == top1:
            if countA == countB or countA == countC or countA == countD or countA == countE:
                rcomd1="CODING Career Tracks"
                countA += 10
            elif countA != countB or countA != countC or countA != countD or countA != countE:
                rcomd1="CODING Career Tracks"
        elif countB == top1:
            if countB == countA or countB == countC or countB == countD or countB == countE:
                rcomd1="MANAGEMENT Career Tracks"
                countB += 10
            elif countB != countA or countB != countC or countB != countD or countB != countE:
                rcomd1="MANAGEMENT Career Tracks"
        elif countC == top1:
            if countC == countB or countC == countD or countC == countA or countC == countE:
                rcomd1="CREATIVE Career Tracks"
                countC += 10
            elif countC != countB or countC != countD or countC != countA or countC != countE:
                rcomd1="CREATIVE Career Tracks"
        elif countD == top1:
            if countD == countA or countD == countB or countD == countC or countD == countE:
                rcomd1="TECHNO-MANAGERIAL Career Tracks"
                countD += 10
            elif countD != countA or countD != countB or countD != countC or countD != countE:
                rcomd1="TECHNO-MANAGERIAL Career Tracks"
        elif countE == top1:
            if countE == countD or countE == countA or countE == countC or countE == countB:
                rcomd1="CORE ENGINEERING Career Tracks"
                countE += 10
            elif countE != countD or countE != countA or countE != countC or countE != countB:
                rcomd1="CORE ENGINEERING Career Tracks"
        #########################recomd 2       
        if countA == top2:
            if countA == countB or countA == countC or countA == countD or countA == countE:
                rcomd2="CODING Career Tracks"
                countA += 9
            else:# countA != countB or countA != countC or countA != countD or countA != countE:
                rcomd2="CODING Career Tracks"
        elif countB == top2:
            if countB == countA or countB == countC or countB == countD or countB == countE:
                rcomd2="MANAGEMENT Career Tracks"
                countB += 9
            else:# countB != countA or countB != countC or countB != countD or countB != countE:
                rcomd2="MANAGEMENT Career Tracks"
        elif countC == top2:
            if countC == countB or countC == countD or countC == countA or countC == countE:
                rcomd2="CREATIVE Career Tracks"
                countC += 9
            else:# countC != countB or countC != countD or countC != countA or countC != countE:
                rcomd2="CREATIVE Career Tracks"
        elif countD == top2:
            if countD == countA or countD == countB or countD == countC or countD == countE:
                rcomd2="TECHNO-MANAGERIAL Career Tracks"
                countD += 9
            else:# countD != countA or countD != countB or countD != countC or countD != countE:
                rcomd2="TECHNO-MANAGERIAL Career Tracks"
        elif countE == top2:
            if countE == countD or countE == countA or countE == countC or countE == countB:
                rcomd2="CORE ENGINEERING Career Tracks"
                countE += 9
            else:# countE != countD or countE != countA or countE != countC or countE != countB:
                rcomd2="CORE ENGINEERING Career Tracks"    
        print(rcomd2)
        print(rcomd1)
        dispatcher.utter_message("CONGRATS ! You Have Selected Some Interesting Answers !\n Based On The Answers You Selected, \nTop recommanded Domain For You")
        if rcomd1== "CODING Career Tracks":
            dispatcher.utter_template("utter_domain_coding",tracker)
        elif rcomd1== "MANAGEMENT Career Tracks":
            dispatcher.utter_template("utter_domian_mgt",tracker)
        elif rcomd1== "CREATIVE Career Tracks":
            dispatcher.utter_template("utter_domain_creative",tracker)
        elif rcomd1== "TECHNO-MANAGERIAL Career Tracks":
            dispatcher.utter_template("utter_domain_techno_mgt",tracker)
        elif rcomd1== "CORE ENGINEERING Career Tracks":
            dispatcher.utter_template("utter_domain_core",tracker)
        dispatcher.utter_message("This may also suits your Profile:\n"+(rcomd2))     
        dispatcher.utter_template("utter_ask_retake_test",tracker)
        return []
        
########################
class QuestionsForm2(FormAction):
    def name(self):
        return "questions_form2"

    def required_slots(self,tracker) -> List[Text]:
        return ["2question_1","2question_2","2question_3","2question_4","2question_5","2question_6"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "2question_1": [
                self.from_text(),
            ],
            "2question_2": [
                self.from_text(),
            ],
            "2question_3": [
                self.from_text(),
            ],
            "2question_4": [
                self.from_text(),
            ],
            "2question_5": [
                self.from_text(),
            ],
            "2question_6": [
                self.from_text(),
            ],
            
        }
    def validate(self, dispatcher, tracker, domain):
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
        q1=["My Coding Ability","My Ability  to Get Things done","My Creative Work","My Ability to Play with Data and Get Insights","My Engineering Mastermind"]
        q4=["How AI can save the world","The evolution of Animation Films since Toy Story","The New Age Marketing","The beauty of Analytics and Visualization","Engineers beyond engineering -- The Art of being an Engineer"]
        q2=["Architect, Design, Develop,Software Products","Plan and Get things Done","Work on animated movies","Analyse Information & Execute Projects","Engineer solutions to real world problems"]
        q5=["The art of computer programming","The One Minute Manager","Pixar Storytelling: Rules for Effective Storytelling Based on Pixar’s Greatest Films","Business Analytics for Managers: Taking Business Intelligence Beyond Reporting","The essential pleasures of engineering"]
        q3=["Software Engineer","Product Manager","Character Animator","Business Analyst","Work in my Core Technical field"]
        q6=["Youtube Recommendation Algorithms","Making Policy Changes that Help Employees","Google Creative Team's Projects","Google Analytics Team's Projects","Any Engineering Team in my Domain"]
        myclient = pymongo.MongoClient("localhost", 27017)
        #mydb=myclient["rasa"]#database name
        #mycol=mydb["user_details"] #it is a collection name in the db rasa .
        for slot, value in slot_values.items():
                if slot == '2question_1':
                    if value not in q1:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
                elif slot == '2question_2':
                    if value not in q2:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
                elif slot == '2question_3':
                    if value not in q3:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
                elif slot == '2question_4':
                    if value not in q4:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
                elif slot == '2question_5':
                    if value not in q5:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
                elif slot == '2question_6':
                    if value not in q6:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
        return [SlotSet(slot, value) for slot, value in slot_values.items()]
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        optA = ['How AI can save the world','Architect, Design, Develop,Software Products','The art of computer programming','Software Engineer','Youtube Recommendation Algorithms','My Coding Ability']
        optB = ['My Abilty to Get Things done','The New Age Marketing','Plan and Get things Done','The One Minute Manager','Product Manager','Making Policy Changes that Help Employees']
        optC = ['My Creative Work','The evolution of Animation Films since Toy Story','Work on animated movies','Pixar Storytelling: Rules for Effective Storytelling Based on Pixar’s Greatest Films','Character Animator','Google Creative Team\'s Projects']
        optD = ['My Ability to Play with Data and Get Insights','The beauty of Analytics and Visualization','Analyse Information & Execute Projects','Business Analytics for Managers: Taking Business Intelligence Beyond Reporting','Business Analyst','Google Analytics Team\'s Projects']
        optE = ['My Engineering Mastermind','Engineers beyond engineering -- The Art of being an Engineer','Engineer solutions to real world problems','The essential pleasures of engineering','Work in my Core Technical field','Any Engineering Team in my Domain']
    
        ent1 = tracker.get_slot("2question_1")
        ent2 = tracker.get_slot("2question_2")
        ent3 = tracker.get_slot("2question_3")
        ent4 = tracker.get_slot("2question_4")
        ent5 = tracker.get_slot("2question_5")
        ent6 = tracker.get_slot("2question_6")
        countA = 0
        countB = 0
        countC = 0
        countD = 0
        countE = 0
        print(ent1)
    
        #for question 1 
        if ent1 in optA:
            countA += 1
        elif ent1 in optB:
            countB += 1
            
        elif ent1 in optC:
            countC += 1
          
        elif ent1 in optD:
            countD += 1
           
        elif ent1 in optE:
            countE += 1
                
        #for question 2 
        if ent2 in optA:
            countA += 1
        elif ent2 in optB:
            countB += 1
        elif ent2 in optC:
            countC += 1
        elif ent2 in optD:
            countD += 1
        elif ent2 in optE:
            countE += 1  
                
        #for question 3 
        if ent3 in optA:
            countA += 1
        elif ent3 in optB:
            countB += 1
        elif ent3 in optC:
            countC += 1
        elif ent3 in optD:
            countD += 1
        elif ent3 in optE:
            countE += 1
                
        #for question 4 
        if ent4 in optA:
            countA += 1
        elif ent4 in optB:
            countB += 1
        elif ent4 in optC:
            countC += 1
        elif ent4 in optD:
            countD += 1
        elif ent4 in optE:
            countE += 1  
                
        #for question5 
        if ent5 in optA:
            countA += 1
        elif ent5 in optB:
            countB += 1
        elif ent5 in optC:
            countC += 1
        elif ent5 in optD:
            countD += 1
        elif ent5 in optE:
            countE += 1 
                
        #for question6 
        if ent6 in optA:
            countA += 1
        elif ent6 in optB:
            countB += 1
        elif ent6 in optC:
            countC += 1
        elif ent6 in optD:
            countD += 1
        elif ent6 in optE:
            countE += 1  
        l=[countA,countB,countC,countD,countE]
        print(l)
        nl=sorted(l)
        print(nl)
        top1=nl[-1]
        top2=nl[-2]
        top3=nl[-3]
        top4=nl[-4]
        top5=nl[-5]
        
        rcomd1=""
        rcomd2=""
        print(countA)
        print(countE)
        print(top1)
        print(top2)
        ###########################recomd 1
        if countA == top1:
            if countA == countB or countA == countC or countA == countD or countA == countE:
                rcomd1="CODING Career Tracks"
                countA += 10
            elif countA != countB or countA != countC or countA != countD or countA != countE:
                rcomd1="CODING Career Tracks"
        elif countB == top1:
            if countB == countA or countB == countC or countB == countD or countB == countE:
                rcomd1="MANAGEMENT Career Tracks"
                countB += 10
            elif countB != countA or countB != countC or countB != countD or countB != countE:
                rcomd1="MANAGEMENT Career Tracks"
        elif countC == top1:
            if countC == countB or countC == countD or countC == countA or countC == countE:
                rcomd1="CREATIVE Career Tracks"
                countC += 10
            elif countC != countB or countC != countD or countC != countA or countC != countE:
                rcomd1="CREATIVE Career Tracks"
        elif countD == top1:
            if countD == countA or countD == countB or countD == countC or countD == countE:
                rcomd1="TECHNO-MANAGERIAL Career Tracks"
                countD += 10
            elif countD != countA or countD != countB or countD != countC or countD != countE:
                rcomd1="TECHNO-MANAGERIAL Career Tracks"
        elif countE == top1:
            if countE == countD or countE == countA or countE == countC or countE == countB:
                rcomd1="CORE ENGINEERING Career Tracks"
                countE += 10
            elif countE != countD or countE != countA or countE != countC or countE != countB:
                rcomd1="CORE ENGINEERING Career Tracks"
        #########################recomd 2       
        if countA == top2:
            if countA == countB or countA == countC or countA == countD or countA == countE:
                rcomd2="CODING Career Tracks"
                countA += 9
            else:# countA != countB or countA != countC or countA != countD or countA != countE:
                rcomd2="CODING Career Tracks"
        elif countB == top2:
            if countB == countA or countB == countC or countB == countD or countB == countE:
                rcomd2="MANAGEMENT Career Tracks"
                countB += 9
            else:# countB != countA or countB != countC or countB != countD or countB != countE:
                rcomd2="MANAGEMENT Career Tracks"
        elif countC == top2:
            if countC == countB or countC == countD or countC == countA or countC == countE:
                rcomd2="CREATIVE Career Tracks"
                countC += 9
            else:# countC != countB or countC != countD or countC != countA or countC != countE:
                rcomd2="CREATIVE Career Tracks"
        elif countD == top2:
            if countD == countA or countD == countB or countD == countC or countD == countE:
                rcomd2="TECHNO-MANAGERIAL Career Tracks"
                countD += 9
            else:# countD != countA or countD != countB or countD != countC or countD != countE:
                rcomd2="TECHNO-MANAGERIAL Career Tracks"
        elif countE == top2:
            if countE == countD or countE == countA or countE == countC or countE == countB:
                rcomd2="CORE ENGINEERING Career Tracks"
                countE += 9
            else:# countE != countD or countE != countA or countE != countC or countE != countB:
                rcomd2="CORE ENGINEERING Career Tracks"    
        print(rcomd2)
        print(rcomd1)
        dispatcher.utter_message("CONGRATS ! You Have Selected Some Interesting Answers !\n Based On The Answers You Selected, \nTop recommanded Domain For You")
        if rcomd1== "CODING Career Tracks":
            dispatcher.utter_template("utter_domain_coding",tracker)
        elif rcomd1== "MANAGEMENT Career Tracks":
            dispatcher.utter_template("utter_domian_mgt",tracker)
        elif rcomd1== "CREATIVE Career Tracks":
            dispatcher.utter_template("utter_domain_creative",tracker)
        elif rcomd1== "TECHNO-MANAGERIAL Career Tracks":
            dispatcher.utter_template("utter_domain_techno_mgt",tracker)
        elif rcomd1== "CORE ENGINEERING Career Tracks":
            dispatcher.utter_template("utter_domain_core",tracker)
        dispatcher.utter_message("This may also suits your Profile:\n"+(rcomd2))   
        
        dispatcher.utter_message("Thank You for Taking the Career Track Test.")
        dispatcher.utter_template("utter_goodbye_message",tracker)
        return []
########################


#########################
#####for getting user details
class SignUpForm(FormAction):

    def name(self):
            return 'sign_up_form'
    @staticmethod
    def required_slots(tracker):
            return ["full_name","password","email","phno","collegeName","stream","hereAbout"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "full_name": [
                self.from_text(),
            ],
            "password": [
                self.from_text(),
            ],
            "email": [
                self.from_text(),
            ],
            "phno": [
                self.from_text(),
            ],
            "collegeName": [
                self.from_text(),
            ],
            "stream": [
                self.from_text(),
            ],
            "hereAbout": [
                self.from_text(),],
        }
    def validate(self, dispatcher, tracker, domain):
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
        hearAbout=["College Seminar","Online","Friend","Others"]
        #myclient = pymongo.MongoClient("localhost", 27017)
        #mydb=myclient["rasa"]#database name
        #mycol=mydb["user_details"] #it is a collection name in the db rasa .
        for slot, value in slot_values.items():
                if slot == 'full_name':
                    #x = mycol.insert_one({"Name":value})
                    #print(x)
                    dispatcher.utter_message("Hi {} Wellcome to CareerLabs ".format(value))
                    #dispatcher.utter_message("Please Enter username ")
                    dispatcher.utter_message("Please type The Password")
                elif slot == 'password':
                    SpecialSym =['$', '@', '#', '%']
                    if len(value) < 6:
                        dispatcher.utter_message("length should be at least 6")
                        slot_values[slot] = None
                    elif len(value) > 20: 
                        dispatcher.utter_message('length should be not be greater than 20') 
                        slot_values[slot] = None
                         
                    elif not any(char.isdigit() for char in value): 
                        dispatcher.utter_message('Password should have at least one numeral') 
                        slot_values[slot] = None
                          
                    elif not any(char.isupper() for char in value): 
                        dispatcher.utter_message('Password should have at least one uppercase letter') 
                        slot_values[slot] = None
                          
                    elif not any(char.islower() for char in value): 
                        dispatcher.utter_message('Password should have at least one lowercase letter') 
                        slot_values[slot] = None
                          
                    elif not any(char in SpecialSym for char in value): 
                        dispatcher.utter_message('Password should have at least one of the symbols $@#') 
                        slot_values[slot] = None
                    else:
                        print("give password")
                elif slot == 'email':
                    email = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
                    mo = email.search(value)
                    if mo == None:
                        dispatcher.utter_message("Please Enter valid email Address! ")
                        slot_values[slot] = None
                    else:
                        #x = mycol.insert_one({"Email_Address":value})
                        print("x")
                        #dispatcher.utter_message("Please Enter Working Mobile Number")         
                elif slot == 'phno':
                    if len(value) == 12 and value.isdigit() == True:
                        if value.startswith('91'):
                            #dispatcher.utter_message("Please Enter The Varfication OTP")
                            print(value)
                            #print("above")
                        else:
                            dispatcher.utter_message("Please include country code 91")
                            slot_values[slot] = None
                    else:
                        dispatcher.utter_message("Please provide valid mobile number including country code 91")
                        slot_values[slot] = None               
                elif slot == 'collegeName':
                    if value.replace(" ","").isalpha() == False:
                        dispatcher.utter_message("Please Enter valid College Name! ")
                        slot_values[slot] = None
                    else:
                        #x = mycol.insert_one({"College_Name":value})
                        print("x")
                        #dispatcher.utter_message("Which Stream are You From?")         
                elif slot == 'stream':
                    if value.replace(" ","").isalpha() == False:
                        dispatcher.utter_message("Please Enter valid Stream! ")
                        slot_values[slot] = None
                    else:
                        #x = mycol.insert_one({"Stream":value})
                        print("x")
                          
                elif slot == 'hereAbout':
                    if value not in hearAbout:
                        dispatcher.utter_message("Please Choose from Options! ")
                        slot_values[slot] = None
                    else:
                        #x = mycol.insert_one({"Hear_About":value})
                        print("x")
                        
                '''
                elif slot == 'gender':
                    if value.lower() not in ["male","female"]:
                        dispatcher.utter_template('utter_ask_question', tracker)
                        slot_values[slot] = None
                elif slot == 'dob':
                    try:
                        datetime.strptime(value, '%d-%m-%Y')
                    except ValueError:
                        dispatcher.utter_template('utter_ask_question', tracker)
                        slot_values[slot] = None'''
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict]:
        firstname=tracker.get_slot("full_name")
        
        #gender=tracker.get_slot("gender")
        #dob=tracker.get_slot("dob")
        email=tracker.get_slot("email")
        contact=tracker.get_slot("phno")
        collegeName=tracker.get_slot("collegeName")
        stream=tracker.get_slot("stream")
        hereAbout=tracker.get_slot("hereAbout")
        #state=tracker.get_slot("state")
        #zipcode=tracker.get_slot("zipcode")
        #ssn=tracker.get_slot("ssn")
        #SlotSet('zipcode', None)
        #SlotSet('zipcode', "11111")
        dispatcher.utter_message("Here is the details you have entered.Please review")
        dispatcher.utter_message("Name : {}                      \nemail : {}                \ncontact : {}                \nCollege Name : {}                  \nStream : {}                  \nHear About : {} ".format(firstname,email,contact,collegeName,stream,hereAbout))
        dispatcher.utter_message("Thank You for Sign Up @careerLabs")
        dispatcher.utter_template("utter_ask_start_test",tracker)
        return []

#############################################
class ActionCheckOtp(Action):
    def name(self) -> Text:
        return "action_check_otp"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("OTP Successfully Send")
        otpobj.retry(tracker.get_slot("phno"))
        return []
class SignInForm(FormAction):#sign in form
    
    def name(self):
            return 'sign_in_form'
    @staticmethod
    def required_slots(tracker):
            return ["phno","otp"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "phno": [
                self.from_text(),
            ],
           "otp": [
                self.from_text(),
            ]
        }
    def validate(self, dispatcher, tracker, domain):
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
        #db connection
        #myclient = pymongo.MongoClient("localhost", 27017)
        #mydb=myclient["rasa"]#database name
        #mycol=mydb["conversations"] #it is a collection name in the db rasa .
           
       
        for slot, value in slot_values.items():
                if slot == 'phno':
                    if len(value) == 12 and value.isdigit() == True:
                        if value.startswith('91'):
                            print(otpobj.send(value,'msgind',sendotp.generateOtp(4)))
                            #dispatcher.utter_message("Please Enter The Varfication OTP")
                            print(value)
                            #print("above")
                        else:
                            dispatcher.utter_message("Please include country code 91")
                            slot_values[slot] = None
                    else:
                        dispatcher.utter_message("Please provide valid mobile number including country code 91")
                        slot_values[slot] = None        
                

        return [SlotSet(slot, value) for slot, value in slot_values.items()]
    
    def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict]:
        mob=tracker.get_slot("phno")
        otp=tracker.get_slot("otp")
        '''def retryOTP(mob):
            print(otpobj.retry(mob))
            dispatcher.utter_message("OTP successfully Send")'''
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
        
        print("strated")
        print(mob)
        verfiyotp = otpobj.verify(mob,otp)
        out0 = str(verfiyotp)
        only_alpha = ""
        for char in out0:
            if ord(char) >= 65 and ord(char) <= 90:
                only_alpha += char
                ## checking for lower case
            elif ord(char) >= 97 and ord(char) <= 122:
                only_alpha += char
                ## printing the string which contains only alphabets
        print(only_alpha)
        str1=only_alpha.replace("message","")
        str2=str1.replace("typesuccess","")
        str3=str2.replace("typeerror","")
        outputdata=str3
        print(outputdata)
        for slot, value in slot_values.items():
            if slot == 'otp':
                if value.isdigit() == True and len(value) == 4:
                    #print( tracker.latest_message.get('text')) to take last indent value
                    
                    if "otpverified" == outputdata:
                            dispatcher.utter_message("Successfully Logged In")
                            dispatcher.utter_message("Welcome To The CareerLabs")
                            dispatcher.utter_template("utter_ask_start_test",tracker)
                    if "alreadyverified" == outputdata:
                            dispatcher.utter_message("Successfully Log In")
                            dispatcher.utter_message("welcome To CareerLabs")
                            dispatcher.utter_template("utter_ask_start_test",tracker)
                    elif "otpnotverified" == outputdata:  
                            print("otp_not_verified or error")
                            slot_values[slot] = None
                            dispatcher.utter_template("utter_ask_retry",tracker)
                            
                    elif "otpoutoflimit" == outputdata:  
                            print("otp out of limit or error")
                            slot_values[slot] = None
                            dispatcher.utter_template("utter_ask_retry",tracker)
                            
                    elif "invalidotp" == outputdata:  
                            print("invalid otp or error")
                            slot_values[slot] = None
                            dispatcher.utter_template("utter_ask_retry",tracker)
                    elif "otpexpired" == outputdata:  
                            print("otp expired or error")
                            slot_values[slot] = None
                            dispatcher.utter_template("utter_ask_retry",tracker)
                    elif "maxlimitreachedforthisotpverification" == outputdata:  
                            print("maxlimitreachedforthisotpverification or error")
                            slot_values[slot] = None
                            dispatcher.utter_template("utter_ask_retry",tracker)
                            
                    
                else:
                    slot_values[slot] = None
                    dispatcher.utter_message(text="Please Type 4 Digit Valid OTP!")
                    dispatcher.utter_message(text="You Can Choose Resend OTP!",buttons=[{"title": "Resend OTP", "payload": "Resending OTP"}])
                
                
        return [SlotSet(slot, value) for slot, value in slot_values.items()]
