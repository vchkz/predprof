import sqlite3


con = sqlite3.connect('dataBase.db')
cursor = con.cursor()


def add_anomaly(detector_id, anomaly_id, rate, x, y):
    cursor.execute('''INSERT INTO anomalies VALUES (?, ?, ?, ?, ?)''', (anomaly_id, detector_id, rate, x, y))
    con.commit()


def add_anomalies(data):
    for detector in data:
        for swan in detector['swans']:
            add_anomaly(detector['id'],
                        swan['id'],
                        swan['rate'],
                        detector['coords'][0],
                        detector['coords'][1])


def clear_db():
    cursor.execute('DELETE FROM anomalies')
    con.commit()
