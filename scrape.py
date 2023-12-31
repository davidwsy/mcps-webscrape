import requests
from bs4 import BeautifulSoup

URL = "https://ww2.montgomeryschoolsmd.org/directory/directory_Boxschool.aspx?processlevel=04757"
source = requests.get(URL)

soup = BeautifulSoup(source.content, 'html.parser')

names = list(soup.find_all("span", class_="dark-gray-border"))
pre_pos = soup.find_all("span", class_="icon-profile fs1")
positions = [element.parent.text for element in pre_pos]
emails = list(soup.find_all(string=lambda text: "@mcpsmd.org" in text))

names.pop(0) # remove "Maryland's Largest School District"
def name_format(name):
    name = name.text.split(",")
    name[1] = name[1][5:].split()  # ['Sanchez', ['Beth', 'S']]
    name = " ".join(name[1]) + " " + name[0] # Beth S Sanchez
    return name
names = list(map(name_format, names)) # len 302

# positions is already list of text

emails = emails[:len(emails)-2] # remove ASKMCPS@mcpsmd.org and ersc@mcpsmd.org

rows = zip(names, positions, emails)


# import csv

# fields = ["names", "positions", "emails"]

# with open("data.csv", "w") as f:
#     write = csv.writer(f)

#     write.writerow(fields)
#     write.writerows(rows)
