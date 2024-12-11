import pandas as pd
import multiprocessing as mp
import numpy as np
import time

# File paths
students_file_path = "students_info.csv"
fees_file_path = "student_fees.csv"

# Load the datasets
students_df = pd.read_csv(students_file_path)
fees_df = pd.read_csv(fees_file_path)

# Extract the day from the Payment Date in the fees dataset
fees_df['Day'] = pd.to_numeric(fees_df['Payment Date'].str.extract(r'(\d+)$')[0], errors='coerce')

# Drop rows with invalid Day values early to reduce processing time
fees_df = fees_df.dropna(subset=['Day'])

# Function to calculate consistent payment days for a chunk
def calculate_consistent_payment_days(chunk):
    return (
        chunk.groupby('Student ID')['Day']
        .agg(lambda x: np.bincount(x.astype(int)).argmax())  # Faster mode calculation
        .reset_index()
    )

if __name__ == "__main__":
    # Measure the start time
    start_time = time.time()

    # Split the fees dataset into chunks
    num_partitions = min(mp.cpu_count(), len(fees_df))  # Use fewer partitions for small datasets
    chunk_size = max(1, len(fees_df) // num_partitions)
    chunks = np.array_split(fees_df, num_partitions)

    # Use multiprocessing to process chunks in parallel
    with mp.Pool(num_partitions) as pool:
        results = pool.map(calculate_consistent_payment_days, chunks)

    # Combine results from all processes
    consistent_payment_days = pd.concat(results).drop_duplicates(subset='Student ID')

    # Merge the consistent payment data with the student information
    merged_df = pd.merge(students_df, consistent_payment_days, on='Student ID', how='inner')

    # Measure the end time
    end_time = time.time()
    execution_time = end_time - start_time

    # Display runtime and a preview of the merged dataset
    print(f"Execution Time: {execution_time:.4f} seconds")
    print(merged_df.head(10))
