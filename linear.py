import pandas as pd
import time

student_fees = pd.read_csv('student_fees.csv')
students = pd.read_csv('students.csv')

start_time_linear = time.time()

merged_data = pd.merge(student_fees, students, on="Student ID")

most_frequent_dates = merged_data.groupby('Student ID')['Payment Date'].agg(
    lambda dates: dates.mode().iat[0] if not dates.mode().empty else None
).reset_index()

end_time_linear = time.time()
execution_time_linear = end_time_linear - start_time_linear

most_frequent_dates.columns = ['Student ID', 'Most Frequent Payment Date']
most_frequent_dates.to_csv('linear_results_updated.csv', index=False)
print(f"Execution Time (Linear): {execution_time_linear:.4f} seconds")
