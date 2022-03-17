#!/usr/bin/env python
# coding: utf-8

# 

# # **자료형**

# In[ ]:





# ##Q1. 다음 수의 평균을 구하세요.
# 
# 80, 75, 55, 95

# In[6]:


(80+75+55+95)/4


# ##Q2. 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력하세요.
# 홍길동 씨의 주민등록번호는 881120-1068234이다.

# In[9]:


# 답을 작성해주세요
id_Hong = "881120-1068234"
print(id_Hong[:6])
print(id_Hong[7:])


# ##Q4. 주민등록번호에서 성별을 나타내는 숫자를 출력하세요.
# 주민등록번호 뒷자리의 첫 번째 숫자는 성별을 나타낸다. 

# In[10]:


# 답을 작성해주세요
id_pin = "881120-2153468"
id_pin[7]


# ##Q5. [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 정렬하세요

# In[13]:


# 답을 작성해주세요
rand_list = [1, 3, 5, 4, 2]
rand_list.sort()
rand_list.reverse()
print(rand_list)


# ##Q7. 다음 리스트를 Life is too short 문자열로 만들어 출력하세요

# In[15]:


# 답을 작성해주세요
string_list = ['Life', 'is', 'too', 'short'] 
" ".join(string_list)


# # **제어문**

# ## Q1. 다음 코드의 결과는?
# 
# a = "Life is too short, you need python"

# 
# if "wife" in a: print("wife")
# 
# elif "python" in a and "you" not in a: print("python")
# 
# elif "shirt" not in a: print("shirt")
# 
# elif "need" in a: print("need")
# 
# else: print("none")

# In[ ]:


shirt
need


# ##Q2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구하세요

# In[21]:


i=1
sum=0
while i<=1000:
    if i % 3==0:
        sum+=i
    i+=1
print(sum)


# ## Q3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성하세요

# In[ ]:


# 답을 작성해주세요


# ## Q4. for문을 사용해 1부터 100까지의 숫자를 출력하세요

# In[23]:


for i in range(1,101):
    print(i)


# ##Q5. for문을 사용하여 평균을 구하세요.
# 
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# 
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

# In[24]:


scores=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum=0
for score in scores:
    sum+=score
sum/len(scores)


# ##Q6. number list에서 홀수에만 2를 곱해 결과를 result에 저장한 후 출력하세요

# In[26]:


numbers = [1, 2, 3, 4, 5]
result = []
for number in numbers:
    if number%2!=0:
        result.append(number*2)
print(result)        


# # **함수와 입출력**

# ##Q1. 주어진 자연수가 홀수인지 짝수인지 판별하는 함수를 작성하세요

# In[27]:


# 답을 작성해주세요
def is_odd(a):
    if a%2==0:
        print("짝수")
    else:
        print("홀수")
is_odd(7)


# ##Q2. 입력으로 들어오는 모든 수의 평균을 계산해주는 함수를 작성하고 실행하세요
# (입력으로 들어오는 수의 개수는 랜덤입니다.)

# In[36]:


# 답을 작성해주세요
def average_rand(n):
    sum=0
    for i in n:
        sum+=i
    print(sum/len(n))

average_rand([1,2,3])


# ##Q3. 다음 프로그램의 오류를 수정하고 실행하세요

# In[29]:


input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)


# In[30]:


input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)


# ##Q4. 다음 중 출력 결과가 다른 것 하나를 고르세요
# 
# 1. print("you" "need" "python")
# 2. print("you"+"need"+"python")
# 3. print("you", "need", "python")
# 4. print("".join(["you", "need", "python"]))

# In[33]:


3. print("you", "need", "python")
