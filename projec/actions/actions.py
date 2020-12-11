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
                output += "https://goo.gl/maps/KY7NjK9FVkbw14yG9\n"
            if(val == "a-block" or val=="a block"):
                output += "https://goo.gl/maps/swM6BEicCe6GT2oAA\n"
            if(val == "b-block" or val=="b block"):
                output += "https://goo.gl/maps/9quNFYr2gC9X7JeZA\n"
            if(val == "c-block" or val=="c block"):
                output += "https://goo.gl/maps/bvbbZb1tNGQw2hyF6\n"
            if(val == "d-block" or val=="d block" or val=="academic block"):
                output += "https://goo.gl/maps/7oFDqrL79JjYg9fg8\n"
            if(val == "student activity center" or val == "sac" or val == "gym"):
                output += "https://goo.gl/maps/YYkpfdFaNR78kaok8\n"
            if (val == "towers" or val == "faculty housing" or val == "t2" or val=="t9" or val=="t10" or val == "t1"  or val == "t 2" or val=="t 9" or val=="t 10" or val == "t 1"):
                output += "https://goo.gl/maps/V53MkSN8XVCGm4Dg9\n"
            if (val == "r-block" or val== "research block"):
                output += "https://goo.gl/maps/84XgydELLohuukCT9"
            if (val == "management block"):
                output += "https://goo.gl/maps/uaAGGapJSKsfPoKa8"
            if (val == "biodiversity park" or val == "cactus park" or val=="bio-diversity park"):
                output += "https://goo.gl/maps/iS8Lejwzp3iUfQkL9\n"
            if (val == "library"):
                output += "https://goo.gl/maps/WazwEBPEEjCVuh219\n"
            if(val == ""):
                output += "\n"
            
        output += "Please open this link in google maps , then press navigate to reach your destination \n"

        dispatcher.utter_message(text = output)

        return []

