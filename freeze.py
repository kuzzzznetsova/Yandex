# A. Кондиционер
# Яндекс. Тренировки по алгоритмам июнь 2021, занятие 1

def freeze(t_room, t_cond):
    if(t_room < t_cond):
        otv = t_room
    if(t_room >= t_cond):
        otv = t_cond
    print(otv)

def heat(t_room, t_cond):
    if(t_room > t_cond):
        otv = t_room
    if(t_room <= t_cond):
        otv = t_cond
    print(otv)

def auto(t_room, t_cond):
    print(t_cond)

def fan(t_room, t_cond):
    print(t_room)

def main():
    values = input()
    values_list = values.split()
    t_room = int(values_list[0])
    t_cond = int(values_list[1])
    make = input()
    if (make == 'freeze'):
        freeze(t_room,t_cond)
    if (make == 'heat'):
        heat(t_room,t_cond)
    if (make == 'auto'):
        auto(t_room,t_cond)
    if (make == 'fan'):
        fan(t_room,t_cond)
main()
