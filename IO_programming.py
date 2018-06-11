
try:
    f=open('C:/Users/admin/Desktop/f_hello.txt','r')
    print(f.read())
finally:
    if f:
        f.close()

with open('C:/Users/admin/Desktop/f_hello.txt','r') as f:
    print(f.read())

with open('C:/Users/admin/Desktop/f_hello.txt','w') as f:
    f.write('Hello world')

from io import StringIO
f=StringIO()
f.write('hi')
f.write(' ')
f.write('Friends')
print(f.getvalue())

f=StringIO('Hi\nfriends')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())

import os
print(os.name)
#print(os.environ)
#print(os.environ.get('PATH'))

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

import pickle
d=dict(name='LJ',age=20)
print(pickle.dumps(d))


'''
f=open('C:/Users/admin/Desktop/f1_hello.txt','wb')
pickle.dump(d,f)
f=open('C:/Users/admin/Desktop/f1_hello.txt','rb')
d=pickle.load(f)
f.close()
'''
print(d)

import json
print(json.dumps(d))

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
s=Student('Bob',20,88)
def student2dict(std):
    return {'name':std.name,'age':std.age,'score':std.score}
print(json.dumps(s,default=student2dict))

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
json_str='{"age":20,"score":88,"name":"BOb"}'
print(json.loads(json_str,object_hook=dict2student))

from multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s (%s)' % os.getpid())
if __name__=='__main__':
    print('Parent process %s,' % os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')

from multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getip()))
    start=time.start()
    time.sleep(random.randint()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end-start)))
if __name__=='__main__':
    print('Parent process %s.'% os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

import time,threading
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s' %(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
print('thread %s is running...' % threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopTread')
t.start()
t.join()
print('thread %s ended'% threading.current_thread().name)

'''
import threading
local_school=theading,local()
def process_student():
    std=local_school.student
    print('Hello,% s (in %s)'%(std,threading.current_thread(),name))
def process_thread(name):
    local_school.student=name
    process_student()
t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2=threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
'''
import re
print(re.split(r'\s+','ab   c'))

