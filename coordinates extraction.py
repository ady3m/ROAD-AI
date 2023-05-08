import csv

# Open the input file
with open('input_data.txt', 'r') as f:
    lines = f.readlines()

# Initialize the list of rows for the CSV file
rows = []

# Parse the input data and add rows to the list
for i in range(0, len(lines), 4):
    time_interval = lines[i].strip()
    speed = lines[i+1].split()[0]
    date_time = lines[i+1].split()[2] + ' ' + lines[i+1].split()[3]
    altitude = lines[i+2].split()[3]
    direction = lines[i+2].split()[4]
    latitude = lines[i+2].split()[1]
    longitude = lines[i+2].split()[3]
    app = lines[i+3].strip()

    row = [time_interval, speed, date_time, altitude, direction, latitude, longitude, app]
    rows.append(row)

# Write the rows to a CSV file
with open('output_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Time Interval', 'Speed (km/h)', 'Date and Time', 'Altitude (m)', 'Direction', 'Latitude', 'Longitude', 'App'])
    writer.writerows(rows)
