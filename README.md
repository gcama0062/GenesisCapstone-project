# Hospital Database — Look Up Patients for Employees
Capstone Project

# Purpose / Problem Statement
This project simulates a simple hospital database system that allows hospital employees to look up patient information using a patient’s first name, last name, and date of birth. It addresses the need for quick patient verification in healthcare settings, especially when handling large volumes of patient data or when full records are not immediately available.

# Target Audience
-This program is ideal for:
<br>Aspiring healthcare technologists interested in how data systems might be used to organize and retrieve patient information.
<br>Entry-level Python programmers looking for real-world applications of APIs, conditional logic, and string formatting.


# Solution + Limitations
-Solutions:
<br>-Fetches a list of random users from the Random User API.
<br>-Simulates real-world patient lookup by requiring key identifying information 
<br>-Supports immediate feedback by displaying the results in a readable format

-Limitations:
<br>-The data is not connected to a real database; it uses mock data from the Random User API.
<br>-Does not store or update patient data.
<br>-Exact matching only: Slight misspellings or different date formats (e.g., "1/1/2001" vs "2001-01-01") will result in no match.




# Key Features/ Components
<br>-User Input Handling: Uses Python’s input() function and .strip() method to clean and collect data for first name, last name, and date of birth.

<br>-JSON Parsing: Extracts nested values like user['name']['first'] and user['dob']['date'] from the API's JSON response.

<br>-Conditional Matching: Compares lowercase versions of name strings and exact date strings using if and .lower statements for precise matches.

<br>-Display Logic: Uses Python’s random.choice() to select and display a random user if no match is found. (Adds gender, email, country, and nationality)

<br>-Formatted Output: Displays patient data using Python’s .format() method and string concatenation to create clean, readable print statements.

<br>-API Integration: Connects to the Random User API to pull simulated patient data.



# Technical Challenges + Future Plans
-Challenges
<br>Matching user input to randomly generated data (rare chance of finding a match).
<br>Saving the patient information into a CSV file. In a previous project, I successfully stored user inputs in a file, but I couldn’t implement that functionality in this version of the program.

-Future Plans
<br>Add search filters like gender, age range, or country.
<br>Include authentication for staff login before accessing patient data.



# Project Timeline
-Day one
<br>Define project idea and purpose.<br>
-Day two
<br>Learn how to add the data from Random User API.<br>
-Day three
<br>Started writing the code (how would they search the patient and what would come up)<br>
-Day four
<br>Finalizing last minute changes and errors<br>
-Day five
<br> Writing the README and prepare for submission<br>


# Tools and Resources Used
<br>[Unit 5 Project Rubric](https://docs.google.com/document/d/1jUnhqM03IApnXY_0myIYcisxFQtfx4LdcMpMpN-IfVM/edit?usp=sharing)
<br> -Requirements for projects<br>

<br>[API](https://randomuser.me/api/?results=50)
<br>-API used for info added to program<br>

<br>ChatGPT
<br>-Used to look up info on how to add and format some info in the program.
<br>-How to add points and organize the README.

<br>Techsmart
<br>Originally created using the TechSmart coding platform.

















