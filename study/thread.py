from threading import Thread
a=4
b=5
def add(a, b):
 return print(a+b)

t = Thread(target=add, args=(1,2)) #실행할 함수 이름, 함수 인자
t.start()#스레드 시작