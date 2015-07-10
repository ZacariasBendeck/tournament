#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    db = connect()
    c = db.cursor()
    query = 'delete from matches;'
    c.execute(query)
    db.commit()
    db.close()
    
    """Remove all the match records from the database."""


def deletePlayers():
    db = connect()
    c = db.cursor()
    query = 'delete from players;'
    c.execute(query)
    db.commit()
    db.close()
    """Remove all the player records from the database."""


def countPlayers():
    db = connect()
    c = db.cursor()
    query = 'select count(name) from players;'
    c.execute(query)
    count = c.fetchone()
    db.close()
    return count[0]
    """Returns the number of players currently registered."""


def registerPlayer(name):
    db = connect()
    c = db.cursor()
    query = 'insert into players(name,wins,matches) values(%s,0,0);'
    data = (name,)
    c.execute(query,data)
    db.commit()
    db.close()
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """


def playerStandings():
    db = connect()
    c = db.cursor()
    query = 'select * from players order by wins desc;'
    c.execute(query)
    standings = c.fetchall() 
    db.close()
    return standings
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):
    db = connect()
    c = db.cursor()
    query = 'insert into matches(winner,loser) values(%s,%s);'
    data = (winner,loser)
    c.execute(query,data)
    query = 'update players set wins = wins + 1 where int = ' +str(winner)+';'
    c.execute(query)
    query = 'update players set matches = matches + 1 where int = ' +str(loser)+';'
    c.execute(query)
    query = 'update players set matches = matches + 1 where int = ' +str(winner)+';'
    c.execute(query)
    db.commit()
    db.close()

       
    
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
def swissPairings():
    db = connect()
    c = db.cursor()
    query = 'select winner, loser from matches'
    c.execute(query)
    existing_players = c.fetchall()
    print existing_players




    standings = playerStandings()
    pairings = []

    i = 0
    while i < len(standings):

        pairings.append((standings[i][0],standings[i][1],standings[i+1][0],standings[i+1][1]))
        print 'We paired ' + standings[i][1] + ' with ' + standings[i+1][1]
        pair = (standings[i][0], standings[i+1][0])
        for e in existing_players:
            print e, pair
          
            if e == standings[i][0]:
                print e, standings[i][0]
                print 'these players already played together!!!'


        i+=2
    return pairings

    
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
'''
def updatePlayed(playerA, playerB):
    db = connect()
    c = db.cursor()
    query = 'select name from already_played'
    c.execute(query)
    existing_players = c.fetchall()
    print existing_players

    
    query = 'insert into already_played(name,played) values(%s,%s);'
    data = (playerA,playerB)
    c.execute(query,data)
    
    query = 'update players set wins = wins + 1 where int = ' +str(winner)+';'
    c.execute(query)
    query = 'update players set matches = matches + 1 where int = ' +str(loser)+';'
    c.execute(query)
    query = 'update players set matches = matches + 1 where int = ' +str(winner)+';'
    c.execute(query)
    db.commit()
    db.close()
'''



