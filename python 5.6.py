import numpy as np


rates = eval(input())
prob = eval(input())
hltime = eval(input())

temp_1 = 0
washing_t = 0
washing_turn = 0           # for the second car
waiting_t = 0
total_wash = 0
waiting_avg = np.array([])
washing_avg = np.array([])
waiting_avg_2 = np.array([])
washing_avg_2 = np.array([])
total_t = np.array([])

for m in range(500):
    for i in range(len(rates)):
        for minute in range(i * 60, (i + 1) * 60):
            each_rate = np.random.binomial(n=1, p=list(rates.values())[i] / 60)
            if each_rate == 1:
                if minute < temp_1 + total_wash:
                    waiting_t = total_wash - (minute - temp_1)
                    waiting_avg = np.append(waiting_avg, waiting_t)
                else:
                    waiting_avg = np.append(waiting_avg, 0)
                each_prob = np.random.choice(list(prob.keys()), p=list(prob.values()))
                washing_t = np.random.choice(hltime[each_prob])
                washing_avg = np.append(washing_avg, washing_t)
                total_wash = washing_t + waiting_t
                temp_1 = minute
    washing_avg_2 = np.append(washing_avg_2, washing_avg)
    waiting_avg_2 = np.append(waiting_avg_2, waiting_avg)
    total = washing_avg + waiting_avg
    total_t = np.append(total_t, total)
    total_wash = 0
    waiting_t = 0
    temp_1 = 0
    washing_avg = np.array([])
    waiting_avg = np.array([])


print('total: ', round(np.mean(total_t), 1), sep='')
print('waiting time: ', round(np.mean(waiting_avg_2), 1), sep='')
print('washing time: ', round(np.mean(washing_avg_2), 1), sep='')

# second part of the question

temp_3 = round(np.mean(waiting_avg_2), 1)
total_t = np.array([])
waiting_avg_2 = np.array([])
washing_avg_2 = np.array([])
washing_t_2_1 = 0
washing_t_2_2 = 0
temp_1 = 0
temp_2 = 0


for m in range(500):
    for i in range(len(rates)):
        for minute in range(i * 60, (i + 1) * 60):
            each_rate = np.random.binomial(n=1, p=list(rates.values())[i] / 60)
            if each_rate == 1:
                if minute < min((temp_1 + washing_t_2_1), (temp_2 + washing_t_2_2)):
                    if temp_1 + washing_t_2_1 < temp_2 + washing_t_2_2:
                        waiting_t = washing_t_2_1 - (minute - temp_1)
                        waiting_avg = np.append(waiting_avg, waiting_t)
                        washing_turn = 1
                    else:
                        waiting_t = washing_t_2_2 - (minute - temp_2)
                        waiting_avg = np.append(waiting_avg, waiting_t)
                        washing_turn = 2
                else:
                    waiting_t = 0
                    waiting_avg = np.append(waiting_avg, waiting_t)
                    if minute >= temp_1 + washing_t_2_1:
                        washing_turn = 1
                    else:
                        washing_turn = 2
                each_prob = np.random.choice(list(prob.keys()), p=list(prob.values()))
                if washing_turn == 1:
                    temp_1 = minute
                    washing_t_1 = np.random.choice(hltime[each_prob])
                    washing_avg = np.append(washing_avg, washing_t_2_1)
                    washing_t_2_1 = waiting_t + washing_t_1
                else:
                    temp_2 = minute
                    washing_t_2 = np.random.choice(hltime[each_prob])
                    washing_avg = np.append(washing_avg, washing_t_2)
                    washing_t_2_2 = waiting_t + washing_t_2
    washing_avg_2 = np.append(washing_avg_2, washing_avg)
    waiting_avg_2 = np.append(waiting_avg_2, waiting_avg)
    total = washing_avg + waiting_avg
    total_t = np.append(total_t, total)
    washing_t_2_1 = washing_t_2_2 = waiting_t = temp_1 = temp_2 = 0
    washing_avg = waiting_avg = np.array([])

print('waiting time is lowered by: ', round(((round(np.mean(waiting_avg_2), 1) - temp_3) / temp_3) * 100, 2), 'percent')


# third part of the question

waiting_line = temp_1 = total_wash = 0
waiting_line_list = []
waiting_line_temp_2 = np.array([])
waiting_line_washing = np.array([])
waiting_line_waiting_avg = []
temp_3 = np.array([])


for m in range(10):
    for i in range(len(rates)):
        for minute in range(i * 60, (i + 1) * 60):
            each_rate = np.random.binomial(n=1, p=list(rates.values())[i] / 60)
            if each_rate == 1:
                if minute < temp_1 + total_wash:
                    waiting_t = total_wash - (minute - temp_1)
                    waiting_avg = np.append(waiting_avg, waiting_t)
                    waiting_line += 1
                else:
                    waiting_avg = np.append(waiting_avg, 0)
                    waiting_line = 0
                each_prob = np.random.choice(list(prob.keys()), p=list(prob.values()))
                washing_t = np.random.choice(hltime[each_prob])
                washing_avg = np.append(washing_avg, washing_t)
                total_wash = washing_t + waiting_t
                temp_1 = minute
                waiting_line_temp_2 = np.append(waiting_line_temp_2, temp_1)
                waiting_line_washing = np.append(waiting_line_list, total_wash)
                waiting_line_list.append(waiting_line)
            else:
                for q in range(len(waiting_line_temp_2)):
                    temp_3 = np.append(temp_3, list(waiting_line_temp_2)[q] + list(waiting_line_washing)[q])
                if minute in temp_3:
                    waiting_line -= 1
                waiting_line_list.append(waiting_line)
    waiting_line_waiting_avg.append(max(waiting_line_list))
    waiting_line_list = []
    waiting_line = 0
    waiting_line_temp_2 = np.array([])
    waiting_line_washing = np.array([])
    washing_avg_2 = np.append(washing_avg_2, washing_avg)
    waiting_avg_2 = np.append(waiting_avg_2, waiting_avg)
    total_wash = 0
    waiting_t = 0
    temp_1 = 0
    waiting_avg = np.array([])
    washing_avg = np.array([])
    temp_3 = np.array([])



print('the maximum line of the car wash (with only one line) in this day is: ', max(waiting_line_waiting_avg))

# and for the second part of the third question


carwash_1 = []
carwash_1_t = []
carwash_1_avg = []
carwash_2 = []
carwash_2_t = []
carwash_2_avg = []
temp_1 = 0
temp_2 = 0
washing_t_2_1 = 0
washing_t_2_2 = 0
washing_t_1 = 0
washing_t_2 = 0

for m in range(500):
    for i in range(len(rates)):
        for minute in range(i * 60, (i + 1) * 60):
            each_rate = np.random.binomial(n=1, p=list(rates.values())[i] / 60)
            if each_rate == 1:
                if minute < min((temp_1 + washing_t_2_1), (temp_2 + washing_t_2_2)):
                    if temp_1 + washing_t_2_1 < temp_2 + washing_t_2_2:
                        waiting_t = washing_t_2_1 - (minute - temp_1)
                        waiting_avg = np.append(waiting_avg, waiting_t)
                        washing_turn = 1
                    else:
                        waiting_t = washing_t_2_2 - (minute - temp_2)
                        waiting_avg = np.append(waiting_avg, waiting_t)
                        washing_turn = 2
                else:
                    waiting_t = 0
                    waiting_avg = np.append(waiting_avg, waiting_t)
                    if minute >= temp_1 + washing_t_2_1:
                        washing_turn = 1
                    else:
                        washing_turn = 2
                each_prob = np.random.choice(list(prob.keys()), p=list(prob.values()))
                temp_1_spair = temp_1
                washing_t_2_1_spair = washing_t_2_1
                if washing_turn == 1:
                    temp_1 = minute
                    washing_t_1 = np.random.choice(hltime[each_prob])
                    washing_avg = np.append(washing_avg, washing_t_1)
                    washing_t_2_1 = waiting_t + washing_t_1
                    carwash_1.append(1)
                    if minute < temp_2 + washing_t_2_2:
                        carwash_2.append(1)
                    else:
                        carwash_2.append(0)
                else:
                    temp_2 = minute
                    washing_t_2 = np.random.choice(hltime[each_prob])
                    washing_avg = np.append(washing_avg, washing_t_2)
                    washing_t_2_2 = waiting_t + washing_t_2
                    carwash_2.append(1)
                    if minute < temp_1_spair + washing_t_2_1_spair:
                        carwash_1.append(1)
                    else:
                        carwash_1.append(0)
            else:
                if len(carwash_1) != 0:
                    if minute < temp_1 + washing_t_2_1 and carwash_1[-1] == 1:
                        carwash_1.append(1)
                    else:
                        carwash_1.append(0)
                if len(carwash_2) != 0:
                    if minute < washing_t_2_2 + temp_2 and carwash_2[-1] == 1:
                        carwash_2.append(1)
                    else:
                        carwash_2.append(0)
        carwash_1_t.append(60 - sum(carwash_1))
        carwash_2_t.append(60 - sum(carwash_2))
        carwash_1 = []
        carwash_2 = []
    carwash_1_avg.append(carwash_1_t)
    carwash_2_avg.append(carwash_2_t)
    carwash_1_t = []
    carwash_2_t = []
    washing_t_2_1 = 0
    washing_t_2_2 = 0
    temp_1 = 0
    temp_2 = 0
    waiting_t = 0

# and for the output:
print('\n')
for i in range(len(rates)):
    print('for the ', str(i + 1), 'th hour')
    print('first car wash hs been empty for an average of: ', end='')
    print(round(np.mean(np.array(carwash_1_avg), axis=1)[i], 2), end='')
    print(' minutes in the hour ', str(list(rates.keys())[i]), sep='')
    print('second car wash hs been empty for an average of: ', end='')
    print(round(np.mean(np.array(carwash_2_avg), axis=1)[i], 2), end='')
    print(' minutes in the hour ', str(list(rates.keys())[i]), sep='')
    print('\n')











