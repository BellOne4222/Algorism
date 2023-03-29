# 집합

s = set() # 집합
s.add(456)
s.add(12)
s.add(456)
s.add(7890)
s.add(7890)
s.add(456) # 중복 값은 안되므로 456, 12 ,7890 밖에 안들어가서 길이는 3이 나온다.

print("size : " , len(s))
for i in s:
    print(i)
