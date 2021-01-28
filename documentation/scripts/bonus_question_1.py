import requests
import sys
import os
from bs4 import BeautifulSoup


# Written by Bonus Group 1


WEBSITE_DIRECTORY = r'../../html/'
BadLinks = []

def extract_href(element):
    return element['href']

def verify_html(filepath):
    with open(filepath, 'rb') as target_html:

        #print("Verifiying file : ", filepath)

        soup = BeautifulSoup(target_html, features="html.parser")

        #select all a tags with an HREF 
        a_refs = soup.select("a[href]")

        #functional programming :)
        links = list(map(extract_href, a_refs))
        bad_links = []
        duplicates = set()

        for link in links: 
            #Not a relative path

            if "mailto" in link:
                continue

            if "http" in link:
                #Send a request and see if we get a 200
                response = requests.get(link)

                if response.status_code != 200:
                    bad_links.append(link)
                    #print(" Bad-Link : ", link)

            else: #Relative Path
                #Check if the file exists 

                #if it starts with '/' it's relative to base
                if link[0] == '/':
                    start_path = os.path.abspath(WEBSITE_DIRECTORY)
                else:
                    start_path = os.path.abspath(os.path.dirname(filepath))

                #print("start_path : ", start_path)
                #print("link : ", link)
                link = link.split("#")[0]

                if link in duplicates:
                    continue

                duplicates.add(link)

                target_path = os.path.normpath(os.path.join(start_path, link))

                if not os.path.isfile(target_path):
                    bad_links.append(link)
                    #print(" Bad-Link : ", target_path)
        
        BadLinks.append((filepath, bad_links))


def walk_over_directories():
    for subdir, dirs, files in os.walk(WEBSITE_DIRECTORY):
        for filename in files:
            #print(filename)
            filepath = subdir + os.sep + filename

            if not filepath.endswith("html"):
                continue

            verify_html(filepath)


walk_over_directories()

print("BAD LINKS: ")
for file_path, bad_links in BadLinks:
    print(" File : ", file_path)
    if len(bad_links) == 0:
        print("  All Good!")
        continue
    for link in bad_links:
        print("  Bad-Link : ", link)
