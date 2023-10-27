# MasterCard uses 16-digit numbers
#Multiply every other digit by 2, starting with the number’s second-to-last digit,
#and then add those products’ digits together.
#Add the sum to the sum of the digits that weren’t multiplied by 2.
#If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0),
#the number is valid!
#[4]0 [0]3 [6]0 [0]0 [0]0 [0]0 [0]0 [1]4
#4003600000000014
def card(x):
    cardnumber = []
    for number in x:
        new = int(number)
        cardnumber.append(new)
    odd_number = 0
    oddnumb = []
    string = '' #empty string
    #print(len(cardnumber)-1)
    if len(cardnumber) > 14:
        x = (len(cardnumber)-2)
        y = len(cardnumber)
    else:
        x = len(cardnumber)
        y = (len(cardnumber)-1)
    for i in cardnumber[x:None:-2]:
        #print(i)
        odd_number = i*2
        oddnumb.append(odd_number)
    string = ""
    for number2 in oddnumb:
        string = ''.join([str(number2) for number2 in oddnumb]) #[] the for loop #list comprehension 
    total_odd = 0
    for number in string: #uses string of all odd numbers *2
        int_of_sum = int(number)
        #print(int_of_sum)
        total_odd += int_of_sum #creates sum
   # print(total_odd)
    even_number = 0
    for x in cardnumber[y:None:-2]:
        even_number += x
    #print(even_number)
    total = 0
    total = (even_number + total_odd)
    #print(total)
    #print(total%10)
    if total % 10 == 0:
        print("The number is valid")
    else:
        print("The number is invalid")
cardnumb = str(input("Hi, please give me your credit card number to ensure its validity:"))
card(cardnumb)

