
# E x 1

# coding: utf-8

#####################################################################################
##############################  Basic python syntax  ################################
#####################################################################################


my_basket = ['clover', 'pansy', 'clover', 'rose', 'ivy', 'daisy']


# Q1. Show `my_basket` contents.
print(my_basket)

# Q2. How many flowers in `my_basket`?
print(len(my_basket))

# Q3. Are there any `pansy` in `my_basket`? <br/>
# (hint: use `in`)
if 'pansy' in my_basket:
    print("Yes! 'pansy' is in my_basket")

# Q4. Are there any rose or daisy in `my_basket`? <br/>
#  (hint: use `or`, `in`)
if 'rose' or 'daisy' in my_basket:
    print("Yes! There are any rose or daisy in my_basket")

# Q5. How many `clover` are in `my_basket`?
print(my_basket.count('clover'))

# Q6. What kinds of flowers are in `my_basket`?
print(len(set(my_basket)))

# Q7. Put a `violet` into `my_basket` if it is not in the `my_basket`?
if 'violet' not in my_basket:
    my_basket.append('violet')
print(my_basket)

# Q8. Show the name of flowers in `my_basket` ending with `y`.
yflower = []
for flowers in my_basket:
    if flowers[-1] == 'y':
        yflower.append(flowers)
print(yflower)

# Q9. Count the number for each kind of flowers in `my_basket`. (You may represent them as a dict name = `counter`)<br/>
#    ex) counter = {'clover': 2, 'daisy'  :1,  ..}
counter = {}
for flowers in my_basket:
    counter[flowers] = my_basket.count(flowers)
print(counter)

price = {'clover': 1500,
          'pansy': 1000,
          'rose': 2000,
          'ivy' : 500,
          'daisy' : 3000}

# Q10. update `violet` data at `price` dictionary. (`violet` price is 2500)
price['violet']=2500
print(price)

# Q11. How much do I pay for flowers in `my_basket`.
total = 0
for money in price.values():
    total += money
print(total)

# Q12. Add any flower in `my_basket` and update `price` dictionary. (flower name and price choose your own)
my_basket.append('lily')
price['lily'] = 4500
print(my_basket)
print(price)



#####################################################################################
##################################  Loop & Function  ################################
#####################################################################################

# ## 스스로 tester 작성하기: 예제
# 다음과 같이 test function이 주어져 있다:

# In[2]:

import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


# #### Q1. 절대값을 구하는 function `ablsolute_value`를 작성해서 다음과 같이 test해 보자.
# 모든 test case가 통과될 때 까지 code를 수정한다.

# In[3]:

def absolute_value(n):  # Buggy version
    """ Compute the absolute value of n """
    if n < 0:
        return n*(-1)
    elif n >= 0:
        return n


test(absolute_value(17) == 17)
test(absolute_value(-17) == 17)
test(absolute_value(0) == 0)
test(absolute_value(3.14) == 3.14)
test(absolute_value(-3.14) == 3.14)


# ## 다음 물음에 답하여 code를 작성하고, 함께 test case들도 작성한다.

# #### Q2. 정수를 매개 변수로 받아 각 자리를 제곱한 뒤 모두 더하는 `sum_of_digit_square` function을 작성하라.
# Parameter: 789 -> Output: 49+64+81=194

# In[4]:


def sum_of_digit_square(n):
    total = 0
    if n<0:
        n*=(-1)
    for num in str(n):
        total += int(num)**2
    return total

test(sum_of_digit_square(789) == 7 ** 2 + 8 ** 2 + 9 ** 2)
test(sum_of_digit_square(-123) == 1 ** 2 + 2 ** 2 + 3 ** 2)


# #### Q3. 2이상의 자연수를 매개 변수로 받아 소수인지 검사하는 `is_prime` function을 작성하라.

# In[5]:


def is_prime(n):
    for num in range(2, n):
        if n%num==0:
            return False
        num+=1
    return True

test(is_prime(2) == True)
test(is_prime(5) == True)
test(is_prime(12) == False)
test(is_prime(13) == True)
test(is_prime(1033) == True)


# #### Q4. 2이상의 자연수를 인자로 받아, 아래와 같은 문양을 출력하는 `star_pattern` void function을 작성하라.

# input: 5일 떄, 다음을 출력
# ```python
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# ```

# In[6]:


def star_pattern(n):
    for star in range(n):
        print('*'*(star+1))
    for star in range(n,1,-1):
        print('*'*(star-1))
star_pattern(5)
star_pattern(6)


# #### Q5. 자연수를 매개 변수로 받아 가장 가까운 완전 제곱수를 출력하는 `perfect_square` function을 작성하라.

# In[7]:


def perfect_square(n):
    root = int(n**0.5)
    up = root+1
    a = root**2
    b = up**2
    if n-a>b-n:
        return up
    else:
        return root

test(perfect_square(15) == 4)
test(perfect_square(31) == 6)
test(perfect_square(41) == 6)
test(perfect_square(99) == 10)


# #### Q6. 자연수를 매개 변수로 받아 각 자리의 수를 더하여 새로운 수를 구하고, 이를 반복하여 한 자리 수를 만들어 출력하는 `unit_place_value` function을 작성하라.
# (e.g., 75 -> 7+5=12 -> 1+2=3).

# In[8]:


def unit_place_value(n):
    while n>9:
        total = 0
        for num in str(n):
            total += int(num)
        n = total
    return n


test(unit_place_value(75) == 3)
test(unit_place_value(3942) == 9)
test(unit_place_value(32) == 5)
test(unit_place_value(9) == 9)


# #### Q7. 자연수를 매개 변수로 받아 해당 숫자까지의 팩토리얼을 계산하는 `recursive_factorial` recursive function을 작성하라.

# In[9]:


def recursive_factorial(n):
    if n==1: return 1
    else: return (n*recursive_factorial(n-1))

import math

test(recursive_factorial(5) == math.factorial(5))
test(recursive_factorial(8) == math.factorial(8))
test(recursive_factorial(2) == math.factorial(2))
test(recursive_factorial(10) == math.factorial(10))


# #### Q8. 자연수를 매개 변수로 받아 해당 숫자까지의 팩토리얼을 계산하는 `non_recursive_factorial` non recursive function을 작성하라.

# In[10]:


def non_recursive_factorial(n):
    value = 1
    if n<=1:
        return 1
    elif n>1:
        for i in range(n):
            if i>0:
                value *= i
        value*=n
        return value

import math

test(non_recursive_factorial(5) == math.factorial(5))
test(non_recursive_factorial(8) == math.factorial(8))
test(non_recursive_factorial(2) == math.factorial(2))
test(non_recursive_factorial(10) == math.factorial(10))


# #### Q9. 두 자연수를 매개 변수로 받아 최대공약수를 구하는 `my_gcd` function을 작성하라.

# In[11]:


def my_gcd(a, b):
    if a>0 and b>0:
        small = min(a,b)
        for num in range(1, small):
            if max(a,b)%small==0 and min(a,b)%small==0:
                return small
            if small>0:
                small -= 1
    else:
        big = max(a,b)
        for num in range(big, -1):
            if max(a,b)%big==0 and min(a,b)%big==0:
                return big*(-1)
            if big<0:
                big += 1


import math

test(my_gcd(12, 16) == math.gcd(12, 16))
test(my_gcd(16, 12) == math.gcd(16, 12))
test(my_gcd(9, 6) == math.gcd(9, 6))
test(my_gcd(-12, -38) == math.gcd(-12, -38))


# #### Q10. 임의의 정수가 들어있는 set을 input으로 입력받아, 가장 큰 세 숫자만을 가지고 있는 set을 반환하는 `max_of_three` function을 작성하라.

# In[12]:


def max_of_three(numset):
    numset=input("임의의 집합을 입력하시오(집합의 괄호는 작성하지 않고 집합의 요소들은 ,로 구분한다): ").split(',')
    numlist = []
    for i in numset:
      if i is not ',':
        numlist.append(int(i))
    numlist.sort()
    answer = set()
    for i in range(-3, 0):
        answer.add(numlist[i])
    return answer

test(max_of_three({1, 2, 3, 4, 5}) == {3, 4, 5})
test(max_of_three({-100, 42, 32, -4, -1}) == {42, 32, -1})


# #### Q11. 임의의 정수가 들어있는 리스트를 input으로 입력받아, 전부 곱한 결과를 반환하는 `mult_of_list` function을 작성하라.

# In[13]:


def mult_of_list(numlist):
    numlist = input("임의의 정수들을 입력하시오(리스트의 괄호는 작성하지 않고 요소들은 ,로 구분한다): ").split(',')
    total = 1
    for num in numlist:
        total *= int(num)
    return total


test(mult_of_list([1, 2, 3, 4]) == 24)
test(mult_of_list([1, 20, -3, 4]) == -240)
test(mult_of_list([1, 0, -33, 9999]) == 0)


# #### Q12. 임의의 정수가 들어있는 리스트를 input으로 입력받아, 그 중 짝수만을 가진 리스트를 반환하는 `even_filter` function을 작성하라.

# In[14]:


def even_filter(nlist):
    nlist = input("임의의 정수들을 입력하시오(리스트의 괄호는 작성하지 않고 요소들은 ,로 구분한다): ").split(',')
    evenlist=[]
    for num in nlist:
        if int(num)%2==0:
            evenlist.append(int(num))
    return evenlist

test(even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8])
test(even_filter([1, 3, 5, 7, 9]) == [])