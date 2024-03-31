import requests
from db_work import add_day, add_info_day, get_info_day


def get_dates():
    headers = {'X-Auth-Token': 'ppo_11_14610'}
    a = requests.get(f'https://olimp.miet.ru/ppo_it_final/date', headers=headers)
    return a.json()['message']


def get_info_about_date(date):
    headers = {'X-Auth-Token': 'ppo_11_14610'}
    date = date.split('-')
    a = requests.get(f'https://olimp.miet.ru/ppo_it_final?day={date[0]}&month={date[1]}&year={date[2]}',
                     headers=headers)
    b = a.json()['message']
    lst = [len(b['windows']['data'].keys()), len(b['windows']['data']['floor_1'])]
    win = []
    for i in b['windows']['data'].keys():
        win = win + b['windows']['data'][i]
    lst.append(win)
    flat_count = b['windows_for_flat']['data']
    lst.append(flat_count)
    return lst


def raschet(lst):
    cnt_room = len(lst[-2])
    rooms_with_light = []
    rooms = []
    i = 0
    j = 0
    pr = lst[-2][j]
    b = []
    while i != len(lst[4]):
        if i != pr:
            b.append(lst[4][i])
            i += 1
        else:
            rooms.append(b.copy())
            b = []
            j += 1
            if j == len(lst[-2]):
                j = 0
            pr += lst[-2][j]
    rooms.append(b.copy())
    for i in range(len(rooms)):
        if True in rooms[i]:
            rooms_with_light.append(i + 1)
    ans = [cnt_room, lst[-2], len(rooms_with_light), rooms_with_light, rooms]

    return ans


def first_run():
    dates = get_dates()
    for i in range(len(dates)):
        date = dates[i]
        add_day(date)
        sp = [date]
        i = 0
        for elem in get_info_about_date(date):
            if i == 2:
                need_elem = []
                for el in elem:
                    if el:
                        need_elem.append('True')
                    else:
                        need_elem.append('False')
                sp.append(need_elem)
            elif i == 3:
                need_elem = []
                for el in elem:
                    need_elem.append(str(el))
                sp.append(need_elem)
            else:
                sp.append(elem)
            i += 1
        add_info_day(sp)
