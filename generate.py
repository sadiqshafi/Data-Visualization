import csv
import random
import calendar

# Function to generate random sales amount
def generate_sales():
    return round(random.uniform(1000, 10000), 2)

# Create and open the CSV file
with open('sales_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['label', 'data']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Generate data for each month and year
    for year in range(2020, 2025):
        for month_num in range(1, 13):
            month_name = calendar.month_name[month_num]
            label = f"{month_name[:3]}-{str(year)[-2:]}"  # Shortcut name for year
            data = generate_sales()
            writer.writerow({'label': label, 'data': data})

print("CSV file generated successfully.")
