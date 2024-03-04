#`set()` : 함수 비어있는 새로운 set 객체를 생성
my_set1 = set()
print(my_set1)

#`set(iterable)` : 매개변수로 주어진 이터러블 iterable(리스트, 튜플)의 원소들을 가지고 새로운 set 객체를 생성, 중복된 원소는 제거
my_set = set([1, 2, 3, 3, 4])
print(my_set)

#`.add(element)` : 매개변수로 주어진 요소를 set에 추가, set 에 존재하는 요소라면 아무런 작업도 하지 않는다
my_set.add(5)
print(my_set)

#`.update(*others)` : 다른 하나 이상의 이터러블 객체의 모든 요소들을 set 에 추가, 중복값은 빠지고 추가된다.
my_set.update([6, 7])
print(my_set)

#`.remove(element)` : 주어진 요소를 set 에서 제거, 해당 요소가 set 에 존재하지 않으면 KeyError 발생
my_set.remove(7)
print(my_set)

#`.discard(element)` : 주어진 요소를 set 에서 제거, 해당 요소가 set 에 존재하지 않아도 예외를 발생시키지 않음
my_set.discard(7)
print(my_set)

#`.pop()` : set 에서 임의의 요소를 제거하고 반환, 만약 set 이 비어있다면 KeyError 발생, 앞에서부터 제거
pop_element = my_set.pop()
print(pop_element)
print(my_set)

pop_element = my_set.pop()
print(pop_element)
print(my_set)

#`.clear()` : set 의 모든 요소를 제거
my_set.clear()
print(my_set)
print('--')

# 교집합 합집합
set1 = {'apple', 'banana', 'orange'}
set1.add('mango')
print('set1 :', set1)
set2 = set()
set2 = {'apple', 'naver', 'gogle'}
print('set2 :', set2)

print()
print(set1 & set2) # & 교집합
print(set1 | set2) # | 합집합
print()

list_set = [set1, set2] # 여러 세트를 리스트에 담음
print(set.intersection(*list_set)) # .intersection(*list) 교집합
print(set.union(*list_set)) # .union(*list_set) 합집합
print('--')

# 리스트 -> 세트, 중복 원소가 없고 원소 순서가 유지되지 않음
chlist = list('google')
print('chlist :', chlist)
print('set:', set(chlist))
print('--')

# 집합끼리 뺄셈
s1 = {1,2,3,4,5,6,7}
s2 = {3,6,9}
print('s1 :', s1,'\ns2 :', s2)
print('s1-s2 :', s1 - s2)

# 출력
#set()
#{1, 2, 3, 4}
#{1, 2, 3, 4, 5}
#{1, 2, 3, 4, 5, 6, 7}
#{1, 2, 3, 4, 5, 6}
#{1, 2, 3, 4, 5, 6}
#1
#{2, 3, 4, 5, 6}
#2
#{3, 4, 5, 6}
#set()
# --
# set1 : {'orange', 'mango', 'apple', 'banana'}
# set2 : {'gogle', 'apple', 'naver'}
#
# {'apple'}
# {'orange', 'mango', 'apple', 'banana', 'gogle', 'naver'}
#
# {'apple'}
# {'orange', 'mango', 'apple', 'banana', 'gogle', 'naver'}
# --
# chlist : ['g', 'o', 'o', 'g', 'l', 'e']
# set: {'g', 'l', 'o', 'e'}
# --
# s1 : {1, 2, 3, 4, 5, 6, 7}
# s2 : {9, 3, 6}
# s1-s2 : {1, 2, 4, 5, 7}