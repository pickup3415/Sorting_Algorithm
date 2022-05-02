import time # 시간 측정 위해 time 모듈 추가
import random # 리스트를 무작위로 섞기위해 random 모듈 추가

m = int(input("데이터의 개수 : ")) # 데이터의 개수를 입력받음 
print("\n")

# 선택 정렬 
def selec_sort(a):
    n = len(a)
    
    for i in range(0, n-1): 
        max = i                      # 최대값을 저장할 변수 i에 초기화
        for j in range(i+1, n):     
            if a[max] < a[j]:        # 최대값이 다음 인덱스의 값보다 작으면
                max = j              # 최대값의 인덱스를 가져옴
        a[i], a[max] = a[max], a[i]  # a[i]와 a[max]의 자리 교환

# 버블 정렬
def bubble_sort(a):
    n = len(a)

    for i in range(0, n-1):                # 뒤에서 부터 정렬
        for j in range(n-i-1):             # 배열의 총 크기에서 i의 값과 1뺀 만큼 반복
            if a[j] > a[j+1]:              # 인근 값의 크기 비교
                a[j], a[j+1] = a[j+1], a[j]# a[j]와 a[j+1]의 자리 교환

#삽입 정렬
def inser_sort(a):
    n = len(a)
    
    for i in range(1, n):               # 1부터 n-1까지
        itme = a[i]                     # i번 위치의 값을 itme으로 저장
        j = i-1                         # j를 i 왼쪽에 저장
        while j >= 0 and a[j] > itme:   # j위치의 값과 비교 후 itme이 삽입될 위치 찾음
            a[j+1] = a[j]               # 오른쪽으로 한 칸 이동
            j -= 1                      # j를 하나씩 줄이며 비교
        a[j+1] = itme                   # a[j+1]자리에 itme 삽입


#병합정렬
def merge_sort(a):
     
    def sort(left, right):
        if right - left < 2:
            return
        mid = (left + right) // 2       
        sort(left, mid)               
        sort(mid, right)               
        merge(left, mid, right)         

    def merge(left, mid, right):
        tmp = []
        l, r = left, mid

        while l < mid and r < right:
            if a[l] < a[r]:             
                tmp.append(a[l])       
                l += 1
            else:
                tmp.append(a[r])        
                r += 1

        while l < mid:              
            tmp.append(a[l])       
            l += 1
        while r < right:           
            tmp.append(a[r])       
            r += 1

        for i in range(left, right):    
            a[i] = tmp[i - left]

    return sort(0, len(a))


        

ls = [x for x in range(m)] #  m개의 원소를 갖는 리스트
random.shuffle(ls) # 정렬하기 전 랜덤으로 섞기
ls2 = ls[:] # 버블 정렬에 사용하는 리스트
ls3 = ls[:] # 삽입 정렬에 사용하는리스트
ls4 = ls[:] # 병합 정렬에 사용하는 리스트


start = time.time()   
selec_sort(ls) # 선택 정렬 실행 시간
selec_time = time.time() - start 


start = time.time()
bubble_sort(ls2) # 버블 정렬 실행 시간
bubble_time = time.time() - start

star = time.time()
inser_sort(ls3) # 삽입 정렬 실행 시간
inser_time = time.time() - start

star = time.time()
merge_sort(ls4) # 병합 정렬 실행 시간
merge_time = time.time() - start

# 출력문 ㅎㅎ
print("<<<선택 정렬>>>")
print("실행시간 : ", selec_time,"\n")

print("<<<버블 정렬>>>")
print("실행시간 : ", bubble_time,"\n")

print("<<<삽입 정렬>>>")
print("실행시간 : ", inser_time,"\n")

print("<<<병합 정렬>>>")
print("실행시간 : ", merge_time)

