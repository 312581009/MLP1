import csv

# Define the number of rows and the fixed price value
num_rows = 6485
price_value = 550088

# Create a list of data for the CSV file
data = [("id", "price")]  # Header row
for i in range(1, num_rows + 1):
    data.append((i, price_value))

# Define the CSV file path
csv_file_path = "output.csv"

# Write the data to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' has been generated with {num_rows} rows.")