import pandas as pd
import time

sheet_id = "1Y20ifXUI485_DVKZd6lwS7GxaHUpxI-NT5W64x23Xic"
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url)

# remove already selected books
unchosen = df[df['chosen'].isnull()]
short_list2 = unchosen[unchosen['short_list2'].isnull()]
short_list1 = unchosen[unchosen['short_list1'].isnull()]


len_short_list1 = len(short_list1)
len_short_list2 = len(short_list2)

pool = short_list1.append(short_list2)

option1 = pool.sample(1)
pool2 = pool[pool['Member Suggesting'] != option1['Member Suggesting'].item()]
option2 = pool2.sample(1)
pool3 = pool2[pool2['Member Suggesting'] != option2['Member Suggesting'].item()]
option3 = pool3.sample(1)

print("There are", len(unchosen), "unread books in the vault...")
time.sleep(1)
print('and', len_short_list2-len_short_list1, 'of them have been shortlisted once and will only go into the pool once...')
time.sleep(3)
print('whereas', len_short_list2, 'of them have never been shortlisted and will go into the pool twice...')
time.sleep(3)
print('for a total of', len(pool), 'in the pool!!!!')
time.sleep(3)
print('the first shortlisted book is...')
time.sleep(1.5)
print('***DRUMROLL***')
time.sleep(1.5)
print(option1['Title'].item(), 'by', option1['Author'].item(), '!!!!')
time.sleep(2)
print('the second shortlisted book is...')
time.sleep(1.5)
print('***DRUMROLL***')
print(option2['Title'].item(), 'by', option2['Author'].item(), '!!!!')
time.sleep(2)
print('and last but not least... ')
time.sleep(1.5)
print('***SUSPENSE***')
time.sleep(2)
print(option3['Title'].item(), 'by', option3['Author'].item(), '!!!!')
time.sleep(2)
print('Happy voting! :)')



## down weight previous shortlisted
