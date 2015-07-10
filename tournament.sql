-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

create database tournament;

create table players(int serial, name text, wins int, matches int);

create table matches(winner int, loser int);

create table already_played(name text, played text);




