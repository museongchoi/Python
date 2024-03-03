my_list = [1,4,11]

# .append(x) 리스트 끝에 추가
my_list.append(5)
print('append 5추가 :', my_list) # [1, 3, 11, 5]

# .extend(iterable) 리스트 확장
f_elements = [7,6]
my_list.extend(f_elements)
print('extend 리스트 확장 :', my_list)

# .insert(i, x) idx에 x 요소 추가
my_list.insert(1,10)
print('insert idx 1에 10 :', my_list)

# .remove(x) 리스트의 첫번째로 나타나는 x 요소 삭제
my_list.remove(11)
print('remove 11 제거 :', my_list)

# .pop([i]) idx i 의 요소를 리스트에서 제거 후 반환
tmp = my_list.pop(3)
print('pop 값 :', tmp)
print('pop 이후 list :', my_list)

# .clear() 리스트 모든 요소 제거
my_list1 = [1,2,3,4]
print()
print('my_list1 :', my_list1)
my_list1.clear()
print('my_list1 :', my_list1)
print()

# .index(x[, start[, end]]) 값이 x인 첫번째 요소의 idx 를 반환
n = 7
index = my_list.index(n)
print(f'my_list[{n}] idx :', index)

# list.count(x) 값이 x인 요소 개수를 반환
count_list = [1,2,2,3,4]
cnt = count_list.count(2)
print('count 2 :', cnt)

# list.sort(key=None, reverse=False) 리스트 정렬
print('my_list :', my_list)
my_list.sort()
print('오름차순 정렬 :', my_list)
my_list.sort(reverse=True)
print('내림차순 정렬 :', my_list)

# list.reverse() 리스트의 요소를 역순으로 재배열
my_list.reverse()
print('역순으로 재배열 :', my_list)

# .copy() 리스트의 복사본
cop_list = my_list.copy()
print('cop_list :', cop_list)

