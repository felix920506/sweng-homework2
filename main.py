import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Reservations(timestamp DATETIME, name TEXT, email TEXT, cartype TEXT, starttime DATETIME, endtime DATETIME)')

CARTYPES = ['sedan', 'suv', 'pickup', 'van']

def printReservations():
    global con, cur
    res = cur.execute('SELECT * FROM Reservations;')
    res = res.fetchall()
    print('Reservations:')
    print('Timestamp (UTC)\t\tName\tEmail\t\tCar Type\tStart Time (UTC)\tEnd Time (UTC)')
    for i in res:
        print(*i, sep='\t')


def inputReservation():
    global con, cur
    name = input('Enter Your Name: ')
    email = input('Enter Your Email: ')
    cartype = input(f'Enter Car Type [{", ".join(CARTYPES)}]: ')
    starttime = input('Enter Start Time (UTC) [YYYY-MM-DD HH:MM:SS]: ')
    endtime = input('Enter End Time (UTC) [YYYY-MM-DD HH:MM:SS]: ')
    data = [name, email, cartype, starttime, endtime]
    cur.execute('INSERT INTO Reservations VALUES(CURRENT_TIME, ?, ?, ?, ?, ?)', data)
    con.commit()

while True:
    func = input(
        "Select Function:\n \
        1 - Print Reservations\n \
        2 - Create Reservation\n \
        q - Exit Program\n \
        Your Selection [1, 2, q]: "
    )

    if func == '1':
        printReservations()
    elif func == '2':
        inputReservation()
    elif func == 'q':
        break
    else:
        print('Unknown Function')
    
    print()
