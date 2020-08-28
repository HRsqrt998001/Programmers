import multiprocessing as mp

def mulpro():
  if __name__ == '__main__':
    num_list = [0,0,0]#함수에 들어갈 인자 리스트
    p = mp.Pool(3)#멀티 프로세싱을 수행할 갯수
    p.map_async(function,num_list).get()#실행할 함수, 들어갈 인자 리스트
    mp.freeze_support()