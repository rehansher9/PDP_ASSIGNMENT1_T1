import pandas as pd
import time

students_file_path = "students_info.csv"
fees_file_path = "student_fees.csv"

students_df = pd.read_csv(students_file_path)
fees_df = pd.read_csv(fees_file_path)

fees_df['Day'] = pd.to_numeric(fees_df['Payment Date'].str.extract(r'(\d+)$')[0], errors='coerce')

start_time = time.time()

fees_df = fees_df.dropna(subset=['Day'])

# Calculate consistent payment days
consistent_payment_days = (
    fees_df.groupby('Student ID')['Day']
    .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
    .reset_index()
)

# Merge the consistent payment data with the student information
merged_df = pd.merge(students_df, consistent_payment_days, on='Student ID', how='inner')

# Measure the end time
end_time = time.time()
execution_time = end_time - start_time

# Display runtime and a preview of the merged dataset
print(f"Execution Time (Linear): {execution_time:.4f} seconds")
print(merged_df.head(10))
