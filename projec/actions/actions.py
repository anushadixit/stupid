# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionLocation(Action):

    def name(self):
        return "action_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        user_message_entity = tracker.latest_message['entities']
        output = ""
        # now make a list of locations , and add markers for each
        
        for entitiy in user_message_entity:
            
            val = entitiy['value'].lower().replace("-" , " ")
            
            if(val == "lake"):
                output += "https://www.google.com/maps/place/SNU+Lake/@28.525674,77.5738558,17z/data=!4m8!1m2!2m1!1sshiv+nadar+university,+lake!3m4!1s0x0:0x96c4e051b8e0fe5d!8m2!3d28.5252391!4d77.5778029\n"
            if(val == "a-block" or val=="a block"):
                output += "https://www.google.com/maps/place/Block+A/@28.5271035,77.5764632,19z/data=!4m13!1m7!3m6!1s0x390c94dbba7e890b:0xd57d847587c2c1e4!2sGreater+Noida,+Uttar+Pradesh+203207!3b1!8m2!3d28.527105!4d77.5770053!3m4!1s0x390c94dbb996cad7:0xcf41dec069c94390!8m2!3d28.5268793!4d77.5771049\n"
            if(val == "b-block" or val=="b block"):
                output += "https://www.google.com/maps/place/Block+B/@28.526578,77.5760931,19z/data=!4m13!1m7!3m6!1s0x390c94dbba7e890b:0xd57d847587c2c1e4!2sGreater+Noida,+Uttar+Pradesh+203207!3b1!8m2!3d28.527105!4d77.5770053!3m4!1s0x390c94dbb547af09:0xaf25bf592e0dc2ba!8m2!3d28.5265965!4d77.5763243\n"
            if(val == "c-block" or val=="c block"):
                output += "https://www.google.com/maps/place/28%C2%B031'34.0%22N+77%C2%B034'32.2%22E/@28.5257932,77.5754467,19z/data=!4m13!1m7!3m6!1s0x390c94dbba7e890b:0xd57d847587c2c1e4!2sGreater+Noida,+Uttar+Pradesh+203207!3b1!8m2!3d28.527105!4d77.5770053!3m4!1s0x0:0x0!8m2!3d28.5260851!4d77.5757235\n"
            if(val == "d-block" or val=="d block" or val=="academic block"):
                output += "https://www.google.com/maps/place/28%C2%B031'31.5%22N+77%C2%B034'31.0%22E/@28.525402,77.5754467,19z/data=!4m13!1m7!3m6!1s0x390c94dbba7e890b:0xd57d847587c2c1e4!2sGreater+Noida,+Uttar+Pradesh+203207!3b1!8m2!3d28.527105!4d77.5770053!3m4!1s0x0:0x0!8m2!3d28.5253548!4d77.5751734\n"
            if(val == "student activity center" or val == "sac" or val == "gym"):
                output += "https://www.google.com/maps/place/SNU+Indoor+Sports+Complex/@28.5215387,77.5708196,18.04z/data=!4m13!1m7!3m6!1s0x390c94dbba7e890b:0xd57d847587c2c1e4!2sGreater+Noida,+Uttar+Pradesh+203207!3b1!8m2!3d28.527105!4d77.5770053!3m4!1s0x390c94d7a94b99e3:0x43336882518f9b3c!8m2!3d28.5213677!4d77.5709693\n"
            if(val == ""):
                output += "\n"
            
        output += "Please open this link in google maps , then press navigate to reach your destination \n"

        dispatcher.utter_message(text=output)

        return []

