# cybersecurity-projects
My few cybersecurity projects

Project 1: Password strength checker 

It takes a password and calculates a score from 0 to 7, taking into account length, uppercase and lowercase, special symbols and digits and whether the password is in the evidently small list of the most common passwords in the world. 
The current state of the project lacks real functionality like case sensitivity or efficient pattern recognition. It can be used to check a password's strength, but its definition of a strong password should not be taken seriously when testing a password for a real site. 

Project 2: File Integrity Monitor

A small program which consists of 2 functions and one main menu from which a user can choose between a file hash generator and a file integrity monitor. Currently, the program is primitive and is capable of calculating a hash and comparing it to the current state of the file, but only when the path to the file and the previously hashed file are entered manually. The program lacks any automation and relies entirely on the user to perform operations. The generated hash by the program also lacks any meaningful protection from malicious modification and the program is currently only able to compare two hashed files and print a message whether they are the same or not, which is obviously not close to real-world functionality. 

I intend to update these projects in time, as my knowledge of Python grows, to make them more usable in real-world conditions, but for now they remain a mere demonstration, not actual tools. 
