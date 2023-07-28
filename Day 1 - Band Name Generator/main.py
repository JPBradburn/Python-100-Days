import random

print("Welcome to the band name gen!")

questionList=["whats the best sport? ", "what yo fav colour? ", "Whats ur pets name? ", "What city u grew up in? "]

one=random.randint(0,3)
ansOne=input(str(questionList[one]))
questionList.pop(one)
two=random.randint(0,2)
ansTwo=input(str(questionList[two]))
questionList.pop(two)
three=random.randint(0,1)
ansThree=input(str(questionList[three]))
questionList.pop(three)
print(f'Your band name be: {ansOne}-{ansTwo}-{ansThree}')