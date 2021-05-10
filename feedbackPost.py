#! /usr/bin/env python3
import os, requests

# Process directory of text files
for file in os.listdir("/data/feedback"):
        with open(file) as file:
                lines = file.readlines()
                feedback_entry = {}
                
# Create dictionary with data from each file
                feedback_entry["title"] = lines[0].strip()
                feedback_entry["name"] = lines[1].strip()
                feedback_entry["date"] = lines[2].strip()
                feedback_entry["feedback"] = " ".join(lines[3:]).strip()
                #print(feedback_entry)

# Post content to web service api using requests.
                response = requests.post("https://example.com/path/to/api", data=feedback_entry)