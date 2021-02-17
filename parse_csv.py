import csv

# Read csv
with open('Data/news_metropoles.csv', 'r') as news_metropoles_csv:
    csv_reader = csv.reader(news_metropoles_csv)

    for row in csv_reader:
        print(row)

# Parse csv

# Write new csv

