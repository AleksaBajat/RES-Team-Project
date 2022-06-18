# Development of Electroenergetic Systems - Cache Memory

Project created for a class in the Faculty of Technical Sciences. 

## Table of Contents
* [General](#general)
* [Technologies](#technologies)
* [How to Run](#how-to-run?)
* [Team Members](#team-members)

## General

Used to create and retrieve meter readings using micro-service architecture.

## Technologies
* Python 3.10.5
* SQLite

## How to run?
1. Use git to pull the whole repository `git clone https://github.com/AleksaBajat/RES-Team-Project.git`
2. Change directory to `../RES-Team-Project/Database/` and using terminal use `python main.py` this runs a one time script that will generate SQLite database
3. Run services by going to `../RES-Team-Project/Client/`, `../RES-Team-Project/Writer`, `../RES-Team-Project/Reader`, `../RES-Team-Project/DumpBuffer`, `../RES-Team-Project/Historical` and in each of them run the `python main.py` (This will require multiple terminals, Powershell 7.2.4 is a very good tool for this if you don't use IDE)
4. Go to the Client terminal and start using the application

## Team members
    Anja Puškaš 
    Dragan Stančević 
    Jovan Peškanov 
    Аleksa Bajat
