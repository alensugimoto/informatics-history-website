#!/usr/bin/python

from bs4 import BeautifulSoup
import os
from natsort import natsorted
import sys


# Written by Bonus Group 2

team1 = ['\\section{1986-1980}']
team2 = ['\\section{1981-1990}']
team3 = ['\\section{1991-2000}']
team4 = ['\\section{2001-2010}']
team5 = ['\\section{2011-2020}']

html_struct = [
	['michele_andrea','1986-1980', team1],
	['laurenz_ebi','1981-1990', team2],
	['paola_guma','1991-2000', team3],
	['francesco_casarella','2001-2010', team4],
	['daniela_gjorgjieva','2011-2020', team5]
]
all_top_dirs = []

for topic_leader in html_struct:
	path = '../../html/'+topic_leader[0]
	for root, dirs, files in os.walk(path, topdown=False):
		for name in dirs:
			if name != 'fazlic_mak':
				all_top_dirs.append(os.path.join(root, name))


all_files = []
for person in all_top_dirs:
	for root, dirs, files in os.walk(person, topdown=False):
		for name in natsorted(files):
			all_files.append(os.path.join(root, name))


def get_in_latex(one_file):
	if one_file[-6:] == '1.html':
		page_1(one_file)
	elif one_file[-6:] == '2.html':
		page_2(one_file)
	elif one_file[-6:] == '3.html':
		page_3(one_file)
	elif one_file[-6:] == '4.html':
		page_4(one_file)
	else:
		pass

def page_1(link):
	with open(link, 'r') as f:
	    contents = f.read()

	    soup = BeautifulSoup(contents, 'lxml')

	    if "../../html/michele_andrea/sugimoto_georgi/georgi1.html" == link:
	        print('\\section{1968-1980}')
	    elif "../../html/laurenz_ebi/horler_linus/linus1.html" == link:
	        print('\\section{1981-1990}')
	    elif "../../html/paola_guma/paola/paola1.html" == link:
	        print('\\section{1991-2000}')
	    elif "../../html/francesco_casarella/prato_andrea/andrea1.html" == link:
	        print('\\section{2001-2010}')
	    elif "../../html/daniela_gjorgjieva/sugimoto_alen/alen1.html" == link:
	        print('\\section{2011-2020}')

	try:
	    nameOfProject = soup.find("div", {"class": "nameOfProject"})
	    imageContainerPageOne = soup.find("div", {"class": "imageContainerPageOne"})
	    name_str = nameOfProject.text

	    name_ltx = "\\paragraph*{}"+str(name_str)

	    img_str = imageContainerPageOne.img['src'][3:]
		

	    img_ltx = "\\begin{figure}[H]\\centering{\\includegraphics[width=0.7\\linewidth]{"+img_str+"}}\end{figure}"
	    print(name_ltx)
	    print(img_ltx)
	except:
		pass

def page_2(link):
	with open(link, 'r') as f:

	    contents = f.read()

	    soup = BeautifulSoup(contents, 'lxml')

	try:
		    nameOfCreator = soup.find("div", {"class": "nameOfCreator"})

		    columnOfContentPageTwo = soup.find("div", {"class": "columnOfContentPageTwo"})

		    blockquote = soup.find("div", {"class": "blockquote"})

		    name_str = nameOfCreator.text

		    img_str = columnOfContentPageTwo.img['src'][3:]

		    quote_str = blockquote.text

		    name_ltx = "\\paragraph*{}"+str(name_str)

		    img_ltx = "\\begin{figure}[H]\\centering{\\includegraphics[width=0.7\\linewidth]{"+img_str+"}}\end{figure}"

		    quote_ltx = "\\paragraph*{}"+str(quote_str)

		    print(name_ltx)

		    print(img_ltx)

		    print(quote_ltx)
	except:
		pass


def page_3(link):
	with open(link, 'r') as f:

	    contents = f.read()

	    soup = BeautifulSoup(contents, 'lxml')

	    why = soup.find("div", {"class": "why"})


	    title_ltx = "\\paragraph*{}"+str(why)

	    all_images = []

	    columnOfContentPageThree = soup.findAll("div", {"class": "columnOfContentPageThree"})
	    for image in columnOfContentPageThree:
		    img_str = image.img['src'][3:]
		    img_ltx = "\\begin{figure}[H]\\centering{\\includegraphics[width=0.7\\linewidth]{"+img_str+"}}\end{figure}"
		    all_images.append(img_ltx)


	    all_text = []
	    columnOfContentPageThreeText = soup.findAll("div", {"class": "columnOfContentPageThreeText"})
	    for text_lines in columnOfContentPageThreeText:
		    lns_str = text_lines.text
		    lns_str = lns_str.replace("\\","\\\^")
		    lns_str = lns_str.replace("&","\&")
		    lns_str = lns_str.replace("$","\$")
		    lns_str = lns_str.replace("%","\%")
		    lns_str = lns_str.replace("_","\_")			
		    lns_str = lns_str.replace("{","\}")
		    lns_str = lns_str.replace("~","\~")
		    lns_str = lns_str.replace("}","\}")
		    lns_str = lns_str.replace("^","\^")


		    lns_ltx = "\\paragraph*{}"+lns_str
		    all_text.append(lns_ltx)

	    cont = all_images + all_text

	    for x in cont:
	    	print(x)

def page_4(link):
	with open(link, 'r') as f:

	    contents = f.read()

	    soup = BeautifulSoup(contents, 'lxml')
	    try:
	        interestingThings = soup.find("div", {"class": "interestingThings"})
	        print(str(interestingThings.text))
	    except:
	        pass


	    all_images = []
	    card = soup.findAll("div", {"class": "card"})
	    for image in card:
		    img_str = image.img['src'][3:]
		    img_ltx = "\\begin{figure}[H]\\centering{\\includegraphics[width=0.7\\linewidth]{"+img_str+"}}\end{figure}"
		    all_images.append(img_ltx)

	    all_text = []
	    description = soup.findAll("div", {"class": "description"})
	    for text_lines in description:
		    lns_str = text_lines.text
		    lns_str = lns_str.replace("\\","\\\^")
		    lns_str = lns_str.replace("&","\&")
		    lns_str = lns_str.replace("$","\$")
		    lns_str = lns_str.replace("%","\%")
		    lns_str = lns_str.replace("_","\_")			
		    lns_str = lns_str.replace("{","\}")
		    lns_str = lns_str.replace("~","\~")
		    lns_str = lns_str.replace("}","\}")
		    lns_str = lns_str.replace("^","\^")


		    lns_ltx = "\\paragraph*{}"+ lns_str
		    all_text.append(lns_ltx)

	    cont = all_images + all_text

	    for x in cont:
	    	print(x)


print(
'''
\\documentclass[11pt,letterpage]{article}
\\usepackage{geometry}
\\geometry{margin=3cm}
\\usepackage{graphicx}
\\usepackage{multicol}
\\usepackage{float}



\\begin{document}

\\begin{titlepage}
   \\begin{center}
       \\vspace*{1cm}

       \\textbf{\\Large{Recent Informatics History}}

       \\vspace{0.5cm}
        Group Project 2
        
            
       \\vspace{1.8cm}

        \\textbf{Bonus Question Latex}

       \\vspace{10cm}
            
       This project was approved by Gabriele Bavota\\\
       prof. at Software Atelier 1
            
       \\vspace{0.8cm}
       
        October 19 - November 19 2020\\\
        Universita della Svizzera italiana\\\
        Faculty of Informatics\\\
        Switzerland\\\

   \\end{center}
\\end{titlepage}

\\begin{centering}

'''
)
for f in all_files:
    get_in_latex(f)
#	break
print(
'''
\\end{centering}
\\end{document}
'''
)
#for x in all_files:
#    print(x)