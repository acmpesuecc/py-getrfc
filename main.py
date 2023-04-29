import argparse
import requests
from requests.exceptions import HTTPError
from rich.console import Console
from rich.prompt import Prompt
import urllib.request
import re
import keyboard
import time
console = Console()
console.print("Hello, Welcome to GetRFC", style="green on black")

title = Prompt.ask("Enter the RFC title")
console.log(title)
page=Prompt.ask("Do you want just the first page?", default="Y")
if page.lower() == 'y':
    page='fpage'
else:
    page='full'
tofile=Prompt.ask("Do you want to write the output to a file", default="Y")
if tofile.lower() == 'y':
    tofile=True
else:
    tofile=False
if tofile:
    filename = input("Please enter the file name to store RFC at: ")
else:
    filename = None


'''
Python script to fetch RFC data from IETF's website using the requests
library and perform one of two actions -
1) Display it in stdout (terminal)
2) Write it to a file specified by this user

Open to collaboration.
'''



class Error(Exception):
    ''' base class for all errors '''
    pass

class Error404(Error):
    ''' exception class for resources not being found '''
    pass

class ForbiddenError(Error):
    ''' exception class for Forbidden resources '''
    pass



def getURL(rfc_no):

    # reuturn access URL for a specific RFC no
    return f'https://www.ietf.org/rfc/rfc{rfc_no}.txt'

def getURL_title(title):
    webUrl=urllib.request.urlopen('https://www.ietf.org/rfc/rfc-index.txt')
    # print("result:"+str(webUrl.getcode()))
    data = webUrl.read().decode('utf-8')
    matches = [i.start() for i in re.finditer(title, data)]
    
    if len(matches) == 0 : print("nothing")
    
    def get_RFC_id(match):
        for i in range(match, 1, -1):
            if data[i] == '\n' and data[i-1] == '\n':
                return data[i+1:i+5]

    ids = []
    for match in matches:
        ids.append(get_RFC_id(match))
        # yield runRequest(getURL((get_RFC_id(match))))

    def get_RFC_title(match):
        for i in range(match, 1, -1):
            if data[i] == '\n' and data[i-1] == '\n':
                for j in range(i+1, len(data)):
                    if data[j:j+8] == '(Format:':
                        return data[i+1:j].strip()

    title = []
    for match in matches:
        title.append(get_RFC_title(match))
    i = 0
    while True:
        if not title:
            break
        keyboard.wait('enter')
        for j in range(i, i + 5):
            if j < len(title):
                print(title[j])
        i += 5

    for i, id in enumerate(ids):
        print(f"{i+1}. {id}")

    choice = Prompt.ask("Enter your choice", default="1")
    return getURL(ids[int(choice)-1])
    # return f'https://www.ietf.org/rfc/rfc{ids[int(choice)-1]}.txt'


def runRequest(url):

    # function to run a request with the requests library
    # and return data with the appropriate HTTP codes

    try:
        response = requests.get(url)

    except requests.ConnectionError:
        print("Please connect to the internet and try again.")
        return 0

    if response.status_code == 200:
        print('200')
        return response

    elif response.status_code == 404:
        raise Error404

    elif response.status_code == 403:
        raise ForbiddenError

runRequest(getURL_title(title))
#Title
def getContentFromRFCTitle(title, option, tofile, filename):
    out = ''

    if option == 'full':

        try:
            data = runRequest(getURL_title(title))

        except Error404:
            print("Sorry! The resource you are looking for does not exist!")
            return 0

        except ForbiddenError:
            print("Sorry! It appears that you do not have access to the above URL")
            return 0

        out = data.text


    elif option == 'fpage':

        try:
            data = runRequest(getURL_title(title))

        except Error404:
            print("Sorry! The resource you are looking for does not exist!")
            return 0

        except ForbiddenError:
            print("Sorry! It appears that you do not have access to the above URL")
            return 0

        iterable_content = data.iter_lines()

        buf = ""

        for line in iterable_content:
            line = line.decode('utf-8')
            if '[Page 1]' not in line:
                buf += line + '\n'
            else:
                buf += line + '\n'
                break

        out = buf


    if tofile:

        # we have been asked to write the output data to the file

        if filename == '' or filename == None:
            filename = input("Please enter the file name to store RFC at: ")
            
        with open(filename, 'w+') as current_file:
            current_file.write(out)

        print(f"Successfully written to file {filename} !")

    else:

        print(out)


getContentFromRFCTitle(title,page,tofile,filename) 
# if __name__ == '__main__':

#     # setup ArgParse for ease of use
#     parser = argparse.ArgumentParser(description='Get RFC data from command line ')
#     parser.add_argument('rfc', type=int, metavar='RFCno', help='RFC Number that you want to get')
#     parser.add_argument('-notall', action="store_true", help='specify if you want only first page')
#     parser.add_argument('-tofile', action="store_true", help='Specify if you want to write to a file or just display in shell (default - false)')
#     parser.add_argument('-name', help='Name of a file you want to write to')

#     args = parser.parse_args()

#     #simplifying the last part
#     if args.notall == False:
#         para = 'full'
#     else:
#         para = 'fpage'

#     getContentFromRFCNo(args.rfc, para, args.tofile, args.name)




