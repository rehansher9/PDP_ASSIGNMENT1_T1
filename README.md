# PDP_ASSIGNMENT1_T1
Payment Analysis: Linear vs Parallel Processing
This repository contains Python scripts to analyze student payment data and compute the most frequent payment days for each student. It includes two implementations: Linear Processing and Parallel Processing. The goal is to demonstrate how multiprocessing can significantly reduce computation time for large datasets.

Features
Extracts payment day information from payment dates.
Computes the most frequent payment day for each student.
Merges the results with student information for a complete overview.
Demonstrates the efficiency of parallel processing over linear processing.
Implementation Details
1. Linear Processing
The linear implementation processes the entire dataset sequentially using pandas' built-in functions. It is simple and effective for smaller datasets but becomes inefficient as the dataset grows in size.

Execution Time: 28.8992 seconds
Steps:
Load datasets.
Extract day information from payment dates.
Group by Student ID and compute the mode (most frequent payment day).
Merge the results with student information.
2. Parallel Processing
The parallel implementation leverages Python's multiprocessing library to split the dataset into chunks and process them concurrently across multiple CPU cores. This significantly reduces computation time for large datasets.

Execution Time: 10.0915 seconds
Steps:
Load datasets.
Extract day information from payment dates.
Divide the dataset into chunks based on the number of CPU cores.
Process each chunk in parallel to compute the mode (most frequent payment day).
Combine the results from all processes and merge them with student information.
Datasets
students.csv: Contains student information, including Student ID, Name, and other attributes.
student_fees.csv: Contains fee payment records, including Student ID, Payment Date, and other details.
Results
**Execution Times:**
Linear Processing: 28.8992 seconds
Parallel Processing: 10.0915 seconds
Performance Improvement:
Parallel processing reduced the computation time by approximately 65%, demonstrating its effectiveness for large datasets.

How to Use
Clone the repository and install required dependencies (e.g., pandas, numpy).
Replace the file paths in the scripts with your dataset file paths (students.csv and student_fees.csv).
Run the scripts:
For linear processing: python linear_processing.py
For parallel processing: python parallel_processing.py
Compare execution times and results.
