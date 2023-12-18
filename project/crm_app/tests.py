from crm_app.models import *

fname = 'Liuba'
lname = 'Kovaleva'

#задаю формат переменный: 25 и 10, и выравниваю их по правому краю
sent = 'I am {:>25} {:>10}!'.format(fname, lname)
print(sent)

#задаю формат переменный: 25 и 10, и выравниваю их по левому краю
sent2 = 'I am {:<25} {:<10}!'.format(fname, lname)
print(sent2)

sent3 = f'I am {fname:>25} {lname.lower()}!!!!'
print(sent3)

