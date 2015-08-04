# tournament
full stack second project tournament 

Tournament Results Readme.
Date: July 18, 2015

Contact Information:
Programmer: Zacarias Bendeck, zbendeck@gmail.com
Githhub repository: https://github.com/ZacariasBendeck/tournament.git
Commit version: fcbcc44751958e518d9d350590f8db196f0e46f8


Purpose:
The purpose of this program is to keep track of players and matches in a game tournament. It will produce pairing for the next round of games using a Swiss pairing system. 


How to use the program. 
1.  First you must have psql and python installed in your virtual machine.  
2.  On the command line of the virtual machine type:
\i tournament.sql
	** This will import the tournament.sql file and run the sql commands to create the database and tables.  It will drop the database named tournament if it already exists.  
3.   This program will support a single tournament at a time, in the future it will be upgraded to support simultaneous tournaments.  
4.  Now you can run all the functions defined in the the tournaments. py program.  Including: reportMatch(), deleteMatches() etc... 
All of the functions to run the tournament are described in the tournament.py file. 
5.  To run a tournament you can type python tournament.py in the command line. 
6.  Then you can use the functions in the program from the command line.
