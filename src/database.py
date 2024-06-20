import pyodbc
from config import SQL_SERVER, SQL_DATABASE, SQL_USER, SQL_PASSWORD

# Establish database connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER=tcp:{SQL_SERVER};'
    f'DATABASE={SQL_DATABASE};'
    f'UID={SQL_USER};'
    f'PWD={SQL_PASSWORD};'
    'Encrypt=yes;'
    'TrustServerCertificate=no;'
    'Connection Timeout=30;'
)
cursor = conn.cursor()

# Function to query data within a time range
def query_time_range(start_time, end_time):
    cursor.execute('SELECT * FROM EarthquakeData WHERE time BETWEEN ? AND ?', (start_time, end_time))
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

# Function to query specific time, net value, and count
def query_specific_time_net_value(time, net_value, count):
    cursor.execute('SELECT * FROM EarthquakeData WHERE time >= ? AND net = ? ORDER BY time OFFSET 0 ROWS FETCH NEXT ? ROWS ONLY', (time, net_value, int(count)))
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

# Function to modify attributes based on time
def modify_attribute(time, new_values):
    cursor.execute('UPDATE EarthquakeData SET latitude = ?, longitude = ?, depth = ?, mag = ?, net = ?, id = ? WHERE time = ?', (*new_values, time))
    conn.commit()

# Example usage of the functions
if __name__ == "__main__":
    # Example: Query data within a time range
    results = query_time_range(16000, 17000)
    for row in results:
        print(row)

    # Example: Query specific time, net value, and count
    results = query_specific_time_net_value(15560, 'ak', 3)
    for row in results:
        print(row)

    # Example: Modify attributes based on time
    new_values = (34.05, -118.25, 10.0, 5.0, 'ci', 'ci0000001')
    modify_attribute(15560, new_values)

    # Close cursor and connection
    cursor.close()
    conn.close()
