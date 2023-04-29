import argparse
import requests
from requests.exceptions import HTTPError
from rich.console import Console
from rich.prompt import Prompt
from tkinter import *
import sys
import time
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring

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
    
def getContentFromRFCNo(number, option, tofile, isgui, filename=''):

    out = ''

    if option == 'full':

        try:
            data = runRequest(getURL(number))

        except Error404:
            print("Sorry! The resource you are looking for does not exist!")
            return 0

        except ForbiddenError:
            print("Sorry! It appears that you do not have access to the above URL")
            return 0

        out = data.text


    else:

        try:
            data = runRequest(getURL(number))

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
            if '[Page {}]'.format(option.strip()) not in line:
                buf += line + '\n'
            else:
                buf += line + '\n'
                break

        out = buf


    if tofile:

        # we have been asked to write the output data to the file
        if isgui:
            with open(filename, 'w+') as current_file:
                current_file.write(out)

        else:
            
            with open(filename, 'w+') as current_file:
                current_file.write(out)

            print(f"Successfully written to file {filename} !")
    else:
        if isgui:
            showinfo(out)
        else:
            print(out)

def handler(RFC, pages, write_file):
    if write_file:
        filename = askstring("File name", "Enter name of file:")
        getContentFromRFCNo(RFC, pages, True, True, filename)
    else:
        getContentFromRFCNo(RFC, pages, False, True)


if len(sys.argv)==2 and sys.argv[1]=="gui":
    
    root = Tk()
    root.geometry("1200x800")
    root.title("py-getrfc")
    welcome_frame = Frame(root)
    input_frame = Frame(root)
    welcome_label = Label(welcome_frame, text='Welcome to py-getrfc!')
    welcome_label.pack()
    time.sleep(2)
    welcome_frame.pack_forget()

    rfc_label = Label(input_frame, text="Enter the RFC number:")
    rfc_input = Entry(input_frame)
    num_pages_label = Label(input_frame, text="Enter the number of pages:")
    num_pages_input = Entry(input_frame)
    rfc_label.pack()
    rfc_input.pack()
    num_pages_label.pack()
    num_pages_input.pack()
    var1=IntVar()
    write_file = Checkbutton(input_frame, text="Write it to a file?", variable=var1, onvalue=1, offvalue=0)
    write_file.var=BooleanVar(value=False)
    write_file.pack()
    submit_button = Button(input_frame, text="Submit", width = 10, height = 2, command=lambda:handler(rfc_input.get(), num_pages_input.get(), var1))
    submit_button.pack()

    input_frame.pack()
    root.mainloop()

else:
    console = Console()
    console.print("Hello, Welcome to GetRFC", style="green on black")
    RFC = Prompt.ask("Enter the RFC Number", default="15")
    console.log(RFC)
    page=Prompt.ask("Do you want just the first page?", default="Y or number")
    if page == 'y' or page == 'Y':
        page='fpage'

    tofile=Prompt.ask("Do you want to write the output to a file", default="Y")
    if tofile.lower() == 'y':
        tofile=True
    else:
        tofile=False
    if tofile:
        filename = input("Please enter the file name to store RFC at: ")
    else:
        filename = None

    runRequest((getURL(RFC)))
    getContentFromRFCNo(RFC, page,tofile, 0, filename) 
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




