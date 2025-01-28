# Web Scraping Introduction with Selenium

This repository serves as a brief introduction to the basics of web scraping using the Selenium library. It provides a simple example that helped me understand how Selenium works and how to set it up for future projects.

## Overview

Web scraping is a technique used to extract data from websites or do automated tasks on them.
Selenium is a powerful tool that allows to automate web browsers, making it ideal for scraping dynamic content that is not easily accessible through traditional methods.

The goal was to get comfortable with Python, understand how Selenium works, and use it to extract data from websites. I’m starting with simple tasks and gradually building up to more complex scripts.

## My Objectives

  1. Learn a Little Bit of Python:

     - Get familiar with Python syntax and basic concepts.

     - Learn how to use Python libraries like Selenium.

  2. Learn the Basics of Web Scraping Using Selenium:

     - Set up Selenium with a web driver (e.g., GeckoDriver for Firefox).

     - Use Selenium to interact with web pages, navigate through sites, and extract data.

      - Work with dynamic web pages where content is loaded asynchronously (e.g., via JavaScript).

  3. Build Incremental Scripts:

     - Started with a simple script that takes a screenshot of a webpage.

     - Moved to a script that navigates through a site and extracts specific data (e.g., the number of players on a server).

     - Finally, create a script that iterates through multiple servers, extracts the number of players from each, and logs the data into a file.


## Prerequisites

Before you begin, ensure you have the following installed:

 - Python3 

 - pip (Python package installer)

On Linux:

```
sudo apt update
sudo apt install python3
sudo apt install python3-pip
```

## Installation

  1. Clone the Repository and navigate into it

  ```
  git clone https://github.com/your-username/web-scraping-intro.git
  cd web-scraping-intro
  ```

  2. Install Dependencies

   - Install the required Python packages by running:
    
      ```
      pip install -r requirements.txt
      ```
    
  3. Set Up WebDriver

      This project uses GeckoDriver for Firefox. If you prefer to use a different browser (e.g., Chrome), you will need to download the corresponding WebDriver and adjust the code accordingly.
    
      Download GeckoDriver: You can download GeckoDriver from the official GitHub releases page.
    
      Set GeckoDriver Path: After downloading, ensure the path to the GeckoDriver executable is correctly set in the code. If you place the executable in a directory included in your system's PATH, you can skip this step.

  Example:
  
    ```
    from selenium import webdriver
  
    # Update the path to your GeckoDriver executable
    driver = webdriver.Firefox(executable_path='/path/to/geckodriver')
    ```

## Usage

To run the web scraping script, simply execute the following command:

```
python3 src/<scrit_you_want_to_see>
```

## Contact

For any questions or suggestions on what to try, please feel free to reach out:

  Artur Carvalho

  **Email:** arturcarvalho0507@gmail.com

  **GitHub:** Artur-2k
