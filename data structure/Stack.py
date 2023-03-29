# 스택 (리스트 이용)

s= [] #[123, 456, 789]
s.append(123) # 1
s.append(456) # 2
s.append(789) # 3
print("size : ", len(s))
while len(s) > 0:
    print(s[-1]) #-1 -> -2 -> -3
    s.pop(-1) # Last In First Out