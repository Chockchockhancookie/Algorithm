from sys import stdin
n = int(stdin.readline())
#채널
# m = int(stdin.readline())
# #고장난 버튼 개수
# if m != 0: b = list(map(int, stdin.readline().split())) #고장난 버튼 else: b = [] only_ud = abs(100 - n) #+-만 써서 이동했을 때 up_c = None down_c = None #n 이상인 수 중에서 고장x인 버튼으로 만들 수 있는 가장 작은 수 #고장난게 없는 경우도 포함 if m != 10: #다 고장난게 아니면 temp = n while True: check = True for i in str(temp): if int(i) in b: check = False break if check: up_c = temp break if len(str(temp))+temp-n>only_ud: #너무 커지면 그냥 끝내기 up_c = temp break temp+=1 if m > 0: #n 미만인 수 중에서 고장x인 버튼으로 만들 수 있는 가장 큰 수 temp = n-1 while temp>=0: check = True for i in str(temp): if int(i) in b: check = False break if check: down_c = temp break if len(str(temp))+n-temp>only_ud: down_c = temp break temp-=1 if up_c==None and down_c==None: print(only_ud) elif up_c!=None and down_c==None: print(min(only_ud, len(str(up_c))+up_c-n)) elif up_c==None and down_c!=None: print(min(only_ud, len(str(down_c))+n-down_c)) else: print(min(only_ud, len(str(up_c))+up_c-n, len(str(down_c))+n-down_c))