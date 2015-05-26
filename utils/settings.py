PGS_TOKEN = 'C888EE7F420841CF92D0B0063EDDFC7D'
PGS_EMAIL = 'pagseguro@panfleteria.com.br'

# from datetime import datetime
# from datetime import date
# from datetime import timedelta



# dates = [d0]
# dates_two = list()

# def date_paginator(x, y):
#     print x, y

# if pages == 1 and pages_mods == 0:
#     _date = d0 + timedelta(days=30)
#     date_paginator(d0, _date)
# else:
#     for i in range(pages):
#         _date = d0 + timedelta(days=30 * (i + 1))
#         dates.append(_date)

# if pages_mods > 0 and pages_mods < 30:
#     new_date = dates[-1:][0] + timedelta(days=pages_mods)
#     dates.append(new_date)

# if dates:
#     for i in range(len(dates) - 1):
#         date_paginator(dates[i], dates[i + 1])


# class DateRangePagination:
#     """docstring for DateRangePagination"""

#     def __init__(self, initial_date):
#         self.initial_date = datetime.strptime(initial_date, "%Y-%m-%d").date()
#         self.dates = [self.initial_date]
#         self.date_limit = datetime.now().date()


#     def get_ranges(self):
#         print self.initial_date

#     def set_ranges():
#         d0 = date(2008, 8, 18)
#         d1 = date(2008, 11, 18)
#         delta = d1 - d0
#         pages = delta.days / 30
#         pages_mods = delta.days % 30
#         pass

#     def get_days(self,):
#         pass