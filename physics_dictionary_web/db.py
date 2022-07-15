import json
import requests
from difflib import get_close_matches as gcm

# Author: Casper van Veen
# Version v2

class Dictionary:
    def __init__(self):
        self.file_location = 'https://raw.githubusercontent.com/Cas1997/Physics-dictionary/main/PhysicsDictionary.json'
        self.data = requests.get(self.file_location).json()
        # self.data = json.load(open(self.json_file))
        self.tags = {"A":"Accelerator", "DE":"Detector & Experiments", "H":"Heavy Flavour", "P":"Photons", "L":"Leptons", "AM":"Anti-matter", "DM":"Dark Matter", "DC":"Detector Components", "CO":"CERN Office Terms", "I":"Institutes"}

    # Look for direct matches
    def direct_match(self, word):
        result = ""
        match = []
        close_match = False
        if(word in self.data):
            match.append(word)
        elif(word.lower() in self.data):
            match.append(word.lower())
        elif(word.title() in self.data):
            match.append(word.title())
        elif(word.upper() in self.data):
            match.append(word.upper())
        else:
            match = self.close_match(word)
            close_match = True

        return match, close_match

    # Look for close matches
    def close_match(self, word):
        thresh = 1.
        if(len(word) > 1):
            thresh = (len(word) - 1)/len(word) - 0.001

        match_found = False
        match = []
        # Close match attempt number 1
        match = gcm(word, self.data.keys(), cutoff = thresh)
        if(len(match) > 0):
            match_found = True
        # Close match attempt number 2
        if(not match_found):
            match = gcm(word.upper(), self.data.keys(), cutoff = thresh)
            if(len(match) > 0):
                match_found = True
        # Close match attempt number 3
        if(not match_found):
            match = gcm(word.title(), self.data.keys(), cutoff = thresh)
            if(len(match) > 0):
                match_found = True
        # Close match attempt number 4
        if(not match_found):
            match = gcm(word.lower(), self.data.keys(), cutoff = thresh)
            if(len(match) > 0):
                match_found = True

        return match

    # Print the result
    def find_result(self, word):
        match, close_match_bool = self.direct_match(word)
        return match, close_match_bool
    
    def description(self, acronym):
        return self.data[acronym]

    def get_tags(self):
        return self.tags
    
    # Merge your file with the data file
    def merge(self, file):
        return

    def add(self, word, meaning):
        return
