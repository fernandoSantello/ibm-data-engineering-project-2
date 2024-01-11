# Project Overview

This project was developed as a part of IBM Data Engineering Professional Certificate course. In this practice project,the student demonstrates their Python skills to extract, transform and load real-world data about the world's largest banks into a database for further processing and querying.

## Project Scenario

From IBM's project description:
"You have been hired as a data engineer by research organization. Your boss has asked you to create a code that can be used to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, the data needs to be transformed and stored in GBP, EUR and INR as well, in accordance with the exchange rate information that has been made available to you as a CSV file. The processed information table is to be saved locally in a CSV format and as a database table.

Your job is to create an automated system to generate this information so that the same can be executed in every financial quarter to prepare the report.

You have to complete the following tasks for this project:

1. Write a function `log_progress()` to log the progress of the code at different stages in a file code_log.txt. Use the list of log points provided to create log entries as every stage of the code.

2. Extract the tabular information from the given URL under the heading 'By market capitalization' and save it to a dataframe.
   a. Inspect the webpage and identify the position and pattern of the tabular information in the HTML code
   b. Write the code for a function `extract()` to perform the required data extraction.
   c. Execute a function call to `extract()` to verify the output.

3. Transform the dataframe by adding columns for Market Capitalization in GBP, EUR and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.
   a. Write the code for a function `transform()` to perform the said task.
   b. Execute a function call to `transform()` and verify the output.

4. Load the transformed dataframe to an output CSV file. Write a function `load_to_csv()`, execute a function call and verify the output.

5. Load the transformed dataframe to an SQL database server as a table. Write a function `load_to_db()`, execute a function call and verify the output.

6. Run queries on the database table. Write a function `load_to_db()`, execute a given set of queries and verify the output.

7. Verify that the log entries have been completed at all stages by checking the contents of the file code_log.txt.
   "

## Project Structure

The repository is organized into the following files and folders:

- `/python/main.py`: Main python file, used for executing functions from imported modules
- `/python/etl_modules/`: Contain all modules for the whole ETL process
- `/files/`: Contains the logging report, input .csv and output .csv and .db
- `/notebooks/banks_project.ipynb`: Jupyter Notebook for the project

## Technologies

This project uses the following technologies:

- Python
- Pandas
- SQLite3

## Getting Started

To get a local copy up and running, follow the following steps:

1. Clone the repo
   ```sh
   git clone https://github.com/fernandoSantello/ibm-data-engineering-project-2.git
   ```
2. Navigate to the project directory.
3. Run `main.py` to execute the ETL process or view `banks_project.ipynb` for a step by step guide

## License

Distributed under the MIT License. See `LICENSE` for more information.
