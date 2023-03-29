# 백준 9012 괄호

"""
문제 : 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 
만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

입력 : 입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 
하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

출력 :출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 
한 줄에 하나씩 차례대로 출력해야 한다. 
"""

# 1. 스택을 이용한 문제 -> 괄호 쌍을 맺어야 정상 VPS이므로, 마지막 괄호와 그 바로전 괄호가 매칭이 되어야 하므로
# 선입 후출 방식의 스택을 이용한 문제이다.

# 입력
T = int(input()) # 입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 
                    # 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
for i in range(T): #첫째줄
    stk = []
    isVPS = True # vps가 맞는것들을 처리하기 위해서 boolean 값으로 처리
    for ch in input(): 
        if ch == '(': # ch는 무조건 여는 괄호 아니면 닫는괄호
            stk.append(ch) # 여는 괄호가 들어왔을 때에는 스택에 그대로 ch를 넣음
        else:
            if len(stk)>0: # 괄호가 모두 쌍이 맺어져서 리스트에 아무것도 안남게 되면 오류가 나므로 한번더
                           # 스택이 비어있는지 검사
                stk.pop() # 닫는 괄호는 직전 여는괄호랑 쌍을 맺어서 pop으로 꺼냄
            else: #닫는 괄호가 더 많이 들어오면 isVPS는 false 처리
                isVPS = False
                break
    if len(stk) >0:
        isVPS = False

    print('YES' if isVPS else 'NO') # isVPS면 YES, 아니면 NO 출력
        
               


