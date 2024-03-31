from db_work import add_day, add_info_day

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