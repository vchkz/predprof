import dataBase as db


for anomaly in [i[0] for i in db.get_all_anomalies()]:
    line = db.get_all_rates_of_anomaly(anomaly)
    sum_ = 0
    for i in line:
        sum_ += i[2]
    int0 = 0.9231
    int0_ans = 0
    diff = 1000
    x_ans = 0
    y_ans = 0
    while int0 <= 2.3:
        for x in range(0, 40):
            for y in range(0, 40):
                temp_sum = 0
                for i in line:
                    if i[3] == x and i[4] == y:
                        continue
                    int_r = int0 / ((i[3] - x) ** 2 + (i[4] - y) ** 2)
                    if abs(int_r - i[2]) < 0.01:
                        temp_sum += int_r
                if abs(temp_sum - sum_) < diff:
                    diff = abs(temp_sum - sum_)
                    int0_ans = int0
                    x_ans = x
                    y_ans = y
        int0 += 0.001
    print(anomaly, '-', int0_ans, x_ans, y_ans)
