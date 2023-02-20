import os
import csv
import openpyxl

# Get the current working directory and join with the CSV file to create a path
current_dir = os.getcwd()
csv_file_path = os.path.join(current_dir, 'Quiz 1.download - Cleaned (1) .csv')

# Create a workbook and select the active worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Open the CSV file using 'with' keyword
with open(csv_file_path, newline='') as csvfile:
    # Read the contents of the CSV file
    data = csv.reader(csvfile, delimiter=',')

    # Create an empty list to store the cleaned data
    cleaned_data = []

    # Process each row of the CSV file
    for index, row in enumerate(data):
        # Skip the first row (column names)
        if index == 0:
            continue

        # Extract the columns from the row
        username = row[0]
        last_name = row[1].strip().upper()
        first_name = row[2].strip().capitalize()
        full_name = ' '.join([name.strip().capitalize() for name in row[3].split()])
        auto_scores = [float(score) for score in row[4:15]]
        total = sum(auto_scores)

        # Create a new row with cleaned data
        cleaned_row = [username, last_name, first_name, full_name] + auto_scores + [total]

        # Append the cleaned row to the list of cleaned data
        cleaned_data.append(cleaned_row)

    # Write the cleaned data to the worksheet
    worksheet.append(["Username", "Last Name", "First Name", "Full Name", "Auto Score 1", "Auto Score 2",
                      "Auto Score 3", "Auto Score 4", "Auto Score 5", "Auto Score 6", "Auto Score 7", "Auto Score 8",
                      "Auto Score 9", "Auto Score 10", "Total"])
    for row in cleaned_data:
        worksheet.append(row)

    # Save the workbook to an Excel file
    excel_file_path = os.path.join(current_dir, 'Quiz 1 - Cleaned.xlsx')
    workbook.save(excel_file_path)

    # Print the cleaned data in equally spaced columns
    print("{:<15}{:<15}{:<15}{:<25}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(
    "Username", "Last Name", "First Name", "Full Name", "Auto Score 1", "Auto Score 2", "Auto Score 3",
    "Auto Score 4", "Auto Score 5", "Auto Score 6", "Auto Score 7", "Auto Score 8", "Auto Score 9", "Auto Score 10",
    "Total"))
for row in cleaned_data:
    print("{:<15}{:<15}{:<15}{:<25}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
        row[12], row[13], row[14]))