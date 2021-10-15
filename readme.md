# py-getrfc (A Python script to fetch RFCs)

Thank you for taking the time to check out my first open-source
project!
## About the Application
This script uses the `requests` module to get RFCs from the
IETF website.
On running the application, currently, it will either:
- Output all the RFC data on the terminal
- Write it to a file specified by the user.
## What is IETF?
The Internet Engineering Task Force (IETF) is an open standards organization, which develops and promotes voluntary Internet standards, in particular the technical standards that comprise the Internet protocol suite (TCP/IP).
## What is RFC?
A Request for Comments (RFC) is an individually numbered publication in a series, from one of a small group of bodies, most prominently the Internet Engineering Task Force (IETF), the principal technical development and standards-setting bodies for the Internet.

 The RFC system was invented by Steve Crocker in 1969 to help record unofficial notes on the development of ARPANET. RFCs have since become official documents of Internet specifications, communications protocols, procedures, and events.[3] According to Crocker, the documents "shape the Internet's inner workings and have played a significant role in its success".

# Installation

- Clone the repo
- Make sure that the libraries mentioned in requirements.txt have been installed.(If not Please install using pip)
- Go to the terminal (Make sure you are in the application's folder)
- Enter ```python main.py -h ```
- You will get an output of the parameters required and their respective description

# Usage Instructions

This is the syntax of the instruction that must be entered in the terminal(Arguments enclose in [] brackets are optional):
```sh
python main.py [-h] [-notall] [-tofile] [-name NAME] RFCno
```
| Arguments | Description |
| ------ | ------ |
| -h | Shows a help message |
| -notall | Specify if you want only first page |
| -tofile | Specify if you want to write to a file or just display in shell(Default is false i.e. Display in shell) |
| -name NAME | Name of a file you want to write to |
| RFCno | RFC Number that you want to get |

# Example

To get the first page of RFC No.15 the command is:
```python main.py -notall 15 ```

Output:
```

call function - first page data to terminal






Network Working Group                                   C. Stephen Carr
Request for Comments: 15                                           UTAH
                                                      25 September 1969

                Network Subsystem for Time Sharing Hosts


Introduction

   A set of network primitives has been defined (Network Working Group
   Note 11) for inclusion in the monitor systems of the respective
   HOSTS.  These primitives are at the level of system calls: SPOP's or
   BRS's on the 940; UUO's on the PDP-10.  Presumably these UUO's are
   accessible to all user programs when executing for users whose status
   bits allow network access.

   In addition to user program access, a convenient means for direct
   network access from the terminal is desirable.  A sub-system called
   "Telnet" is proposed which is a shell program around the network
   system primitives, allowing a teletype or similar terminal at a
   remote host to function as a teletype at the serving host.

System Primitives

   G. Deloche of U.C.L.A. has documented a proposed set of basic network
   primitives for inclusion in the operating systems of the respective
   HOSTs (NWG Note:  11).  The primitives are:

      Open primary connection

      Open auxiliary connection

      Transmit over connection

      Close connection.

   The details  and terminology are defined by Deloche and others in
   previous memos.  The primitives are system calls, available to
   programmers, and are most likely a part of the resident monitor,
   rather than the swappable executive.

Basic Terminal Access

   In addition to user programming access, it is desirable to have a
   subsystem program at each HOST which makes the network immediately
   accessible from the teletype without special programming.  Subsystems
   are commonly used system components such as text editors, compilers
   and interpreters.  The first network-related subsystem should allow



Carr                                                            [Page 1]

```
Similarly the command to get all the pages would be:

```python main.py 15```
