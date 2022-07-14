import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime,timedelta,date
from db import BotDB
import config

BotDB = BotDB(config.DB_NAME,config.DB_USER,config.DB_PASSWORD,config.DB_HOST,config.DB_PORT)
#7
def generate_stats(interval):
    users,mailings = dict(),dict()
    users_last,mailings_last = 0,0

    for i in range(interval):
        request_date = date.today() - timedelta(days=i)
        #users
        users[request_date] = BotDB.count_where('users',request_date)
        users_last = users_last + int(BotDB.count_where('users',request_date))
        #mailings
        mailings[request_date] = BotDB.count_where('mailings',request_date)
        mailings_last = mailings_last + int(BotDB.count_where('mailings',request_date))

    #generate users table
    t = users.keys()
    s = users.values()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, s)

    ax.set(xlabel='Date', ylabel='User count',title='User stats')
    ax.grid()
    
    fig.savefig("media/users_plot.png")

    plt.clf()

    #generate mailings

    t = mailings.keys()
    s = mailings.values()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, s)

    ax.set(xlabel='Date', ylabel='User count',title='Mailing stats')
    ax.grid()
    
    fig.savefig("media/mailings_plot.png")

    return(f"||Статистика за последние {interval} дней||\n\nТекущих пользователей {BotDB.get_records_len('users')} (+{users_last})\nПодключило подписку {BotDB.get_records_len('mailings')} (+{mailings_last})")

print(generate_stats(21))