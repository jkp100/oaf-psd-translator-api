# oaf-psd-translator-api

Initial Repository for Translator API 

About the project:

The goal of this project is to translate communications and provide insights within conversations using open-source natural language processing libraries and production-level data structure. Specifically, this project features text translation cross-functionality from multiple languages using an open-source translator API (https://libretranslate.de.) 

Motivation:

I plan to use this project to provide better communication between conversations.  Effective communication requires a shared understanding between the sender and receiver of information and is essential for the success of any business.

  As of 2023:

  
    •	86% of employees and executives state the lack of effective collaboration and communication as the main cause of workplace failures. 
    •	Teams that communicate effectively may increase productivity by 25%.
    •	68% of consumers say they’ve personally wasted time as a result of communication issues in businesses.


Summary of Approach:


 ![image](https://github.com/jkp100/oaf-psd-translator-api/assets/137459213/ac955b98-9821-4a06-a4e6-e35496c0536d)


  Libre Translate API: Provides translation services through the Libre Translate API.
    
    •	https://libretranslate.de
    •	Translates text from a source language to a target language.
    •	Supports auto-detection of the source language.
    •	Handles errors and returns translation results.


  Translator Main: Acts as the main script to orchestrate the translation process.
    
    •	Takes user input with a given prompt.
    •	Resets the conversation database based on user input.
    •	The main function that executes the translation process using other classes.
    •	Manages user interactions and coordinates translation using Translator Service.
    •	Implements sentiment analysis using Translator Sentiment


  Translator Service: Interacts with the Libre Translate API to translate text.


    •	Initializes the service with the API URL.
    •	Translates text using the Libre Translate API.
    •	Initializes the handler with a Translator Service instance.
    •	Takes user input with a given prompt to auto-detect a source language.
    •	Prompts the user to choose a target language and validates the input.
    •	Calls Translator Service to translate text.


  Translator Database: Manages the SQLite database for storing translations.


    •	Initializes the database with a given path.
    •	Creates the SQLite table for translations.
    •	Adds a translation to the database.
    •	Retrieves all past translations from the database.
    •	Closes the connection to the database.
    •	Serves as an entry point for resetting the database through the command line.


  Translator Sentiment: Performs sentiment analysis on the provided text.


    •	Initializes the Translator Sentiment instance.
    •	Uses Text Blob for sentiment analysis, returning a sentiment score and label.

Future Direction:

  My future aspirations for this project are to expand convenience and functionality.  One concept is to add the ability to pass in an audio file, or even translate in real-time with voice dictation. Focusing on the ability to expand on the sentiment score, and reading education level, and suggest the appropriate things to say across multiple languages.


A Reflection of What I Learned

  The most important part of the project I realized is Dependency Injection.  Implementing this concept, allowed flexibility in changing the structure of each function as I added or modified each class. By setting the Translation Handler to take an instance of the Translator Service as a dependency I was able to modify the main crucial part of the application Translator Service, without affecting code in the Translation Handler which manages the user inputs and prompts.

  When I first created this project the database operations were printed to display functionality but made the results cluttered. I used the concept of Encapsulation, in the database operations, to hide behind methods, promoting cleaner and modular code.  Having hidden methods made the significant functions stand out even better and with more esthetics for the user.

  The project uses SQLite as a local database for storing translations. Each translation is stored as a record in the translations table, maintaining a structured format. An SQL query can be passed in to refer to and create data tables for future processing.  By establishing a database, I was able to hide methods and reduce the amount of API requests and load on the application. Super lightweight, easy to integrate, and low resource requirements.


How is the Data used?

The utilization of data requires the user to input text, specify their target language, and the ability to automatically detect the language they are typing. By utilizing the user input, it is stored locally in an SQLite database. The main script then utilizes the data by displaying past conversations when prompted by the user.  Furthermore, spaCy and Textblob libraries were utilized for sentiment analysis. Both are open-source pre-trained models, with high efficiency in production environments with various Natural Language Processing tasks. It was a game changer to learn how these models work in NLP and have future aspirations for this project.  Understanding, the confidence level and result sentiment could influence a user’s understanding in conversations.




