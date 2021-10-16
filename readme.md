# py-getrfc (A Python script to fetch RFCs)

Thank you for taking the time to check out my first open-source
project!


# WORKING:
```
+ This script uses the `requests` module to get RFCs from the
  IETF website.
+ On running the application, currently, it will input the rfc number and display all the pages regarding the same in the terminal.
```

# USAGE:
```
+ main.py [-h] [-notall] [-tofile] [-name NAME] RFCno

+ Get RFC data from command line (input)
```

# POSITIONAL ARGUEMENTS:
```
+ These are the arguements that dont have a default value. The program cannot be further executed if this arguement is not entered by the user.
+ In this case, the positional arguement is the rfc number whose information you want to display.

  RFCno       RFC Number that you want to get
```

# OPTIONAL ARGUEMENTS:
```
+ These are the arguements the user does not necessarily have to enter. 
+ The program will continue running normally, even when these arguements are not inputed. 

  -h, --help  show this help message and exit
  -notall     specify if you want only first page
  -tofile     Specify if you want to write to a file or just display in shell
              (default - false)
  -name NAME  Name of a file you want to write to
```
  
  
# HOW TO RUN THE PROGRAM:
 
```
+ The first step to leave the directory you are currently working in like this:
 
  C:\Hacknight_getfrc\py-getrfc-master (1)\py-getrfc-master>cd..\..
  C:\Hacknight_getfrc>cd..

+ The next step is to enter the appropriate directory as depicted:
 
  C:\>cd "\Hacknight_getfrc\py-getrfc-master (1)\py-getrfc-master"\
  C:\Hacknight_getfrc\py-getrfc-master (1)\py-getrfc-master>

+ Next, we need to run the program in command prompt while also giving in the necessary input.
+ In this case, the input is the rfc number. Since this is a positional arguement, the program will throw an error if this arguement is not entered.
  
  C:\Hacknight_getfrc\py-getrfc-master (1)\py-getrfc-master>python main.py 2306

+ Here, 2306 is the rfc number
```

# EXAMPLE:
```
+ If the above steps are followed and the code is run, the output will be as follows:


Parsons & Rafferty           Informational                     [Page 23]
♀
RFC 2306                     TIFF-F Profile                   March 1998


   [REQ] Bradner, S., "Key words for use in RFCs to Indicate
        Requirement Levels", RFC 2119, March 1997.
   [T.30] ITU-T Recommendation T.30 - "Procedures for Document
        Facsimile Transmission in the General Switched Telephone
        Network", June, 1996
   [T.4] ITU-T Recommendation T.4 - "Standardization of Group 3
        Facsimile Apparatus for Document Transmission", June, 1996
   [T.6] ITU-T Recommendation T.6 - "Facsimile Coding Schemes and
        Coding Control Functions for Group 4 Facsimile Apparatus",
        March, 1993
   [TIFF] Adobe Developers Association, TIFF (TM) Revision 6.0 -
        Final, June 3, 1992.
   [TIFFREG] Parsons, G., Rafferty, J. and S. Zilles, "Tag Image File
        Format (TIFF) - image/tiff:  MIME Sub-type Registration ", RFC
        2302, March 1998.
   [VPIM2] G. Vaudreuil and G. Parsons, "Voice Profile for Internet
        Mail - version 2", Work In Progress, <draft-ema-vpim-06.txt>,
        November 1997.
        
        
+ It will display all 25 pages describing the rfc, this is just one of the pages for sample.
```
