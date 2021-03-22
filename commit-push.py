import os
import git
import random
import string
import datetime

def randomstring(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


count = random.randint(1,10)
for i in range(count):
    # branchの取得
    repo = git.Repo(os.getcwd())

    with open('bar.txt', 'wt', encoding='utf-8') as f:
        rand_str = randomstring(100)
        f.write(rand_str)
    
    now = datetime.datetime.now()
    repo.git.add('bar.txt')
    repo.git.commit('bar.txt', message='Commited by commit-push.py {}'.format(now.strftime('%Y-%m-%d %H:%M:%S')))
    repo.git.push('origin', 'master')