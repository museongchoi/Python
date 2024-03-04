my_dict = {'a':1, 'b':2, 'c':3}

# dict.keys() 딕셔너리 모든 키 값 반환
keys = my_dict.keys()
print(keys) # 출력 : dict_keys(['a', 'b', 'c'])

# dict.values() 딕셔너리 모든 값 반환
values = my_dict.values()
print(values) # 출력 : dict_values([1, 2, 3])

# dict.items() 딕셔너리 모든 키-값 반환
items = my_dict.items()
print(items) # 출력 : dict_items([('a', 1), ('b', 2), ('c', 3)])

# dict.get(key[, default]) 주어진 키의 값을 반환, 없으면 default 갑 반환
value = my_dict.get('b')
print(value) # 출력 : 2
value = my_dict.get('d', 'Not Found')
print(value) # 출력 : Not Found

# dict.pop(key[, default]) 주어진 키의 값을 반환하고 딕셔너리에서 해당 키-값 쌍 삭제
value = my_dict.pop('b')
print(value) # 출력 : 2
print(my_dict) # 출력 : {'a': 1, 'c': 3}

# dict.popitem() 딕셔너리의 임의의 키-값 쌍을 반환하고 삭제
key, value = my_dict.popitem()
print(key, value) # 임의의 (키, 값) 쌍을 출력
print(my_dict) # 출력 : 임의의 (키, 값) 쌍을 삭제한 딕셔너리

# dict[key] = value 새로운 키-값 쌍을 추가
my_dict['b'] = 2
print(my_dict) # 출력 : {'a': 1, 'b': 2}

# dict.update(iterable) 딕셔너리 확장, 키-값 쌍 추가, 동일 키-값 값을 업데이트
my_dict.update({'b': 3, 'c': 4})
print(my_dict) # 출력 : {'a': 1, 'b': 3, 'c': 4}

# dict.clear() 딕셔너리 모든 요소 제거
my_dict.clear()
print(my_dict) # 출력 : {}

my_dict.update({'a':1, 'b':2, 'c':3})
print(my_dict)

# len(dict) 딕셔너리 길이 반환
length = len(my_dict)
print(length) # 출력 : 3

# key in dict 키가 딕셔너리에 있는지 여부를 확인 True & False
is_key_present = 'b' in my_dict
print(is_key_present)