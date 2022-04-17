import sqlite3


con = sqlite3.connect('dataBase.db')
cursor = con.cursor()


def add_anomaly(detector_id, anomaly_id, rate, x, y):
    cursor.execute('''INSERT INTO anomalies VALUES (?, ?, ?, ?, ?)''', (anomaly_id, detector_id, rate, x, y))
    con.commit()


def add_right_anomaly(anomaly_id, coord_x, coord_y, rate):
    cursor.execute('''INSERT INTO right_anomalies VALUES (?, ?, ?, ?)''', (anomaly_id, coord_x, coord_y, rate))
    con.commit()


def add_anomalies(data):
    for detector in data:
        for swan in detector['swans']:
            add_anomaly(detector['id'],
                        swan['id'],
                        swan['rate'],
                        detector['coords'][0],
                        detector['coords'][1])


def get_all_rates_of_anomaly(anomaly_id):
    line = cursor.execute('''SELECT * FROM anomalies WHERE anomaly_id=?''', (anomaly_id,)).fetchall()
    return line


def get_anomaly_table():
    line = cursor.execute('''SELECT * FROM anomalies''').fetchall()
    return line


def get_all_anomalies():
    line = cursor.execute('''SELECT DISTINCT anomaly_id FROM anomalies''').fetchall()
    return line


def clear_db():
    cursor.execute('DELETE FROM anomalies')
    con.commit()