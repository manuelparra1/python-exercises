#  1. Define a function named is_two. It should accept 
#     one input and return True if the passed input 
#     is either the number or the string 2, False otherwise.

def is_two(num):
    if isinstance(num, int):
        return num == 2
    elif num.isdigit():
        return int(num) == 2
    else:
        return False
is_two("49")


# In[58]:


#  2. Define a function named is_vowel. 
#     It should return True if the passed string 
#     is a vowel, False otherwise.

def is_vowel(vow):
    if (0 < len(vow)< 2) and (isinstance(vow, str)):
        return vow in ['a','e','i','o','u']
    else:
        return False

input_word = input("Enter a vowel: ")
is_vowel(input_word)


# In[59]:


#  3. Define a function named is_consonant. 
#     It should return True if the passed string 
#     is a consonant, False otherwise. Use your 
#     is_vowel function to accomplish this.
def is_consonant(letter):
    if isinstance(letter, str) and (not any(i.isdigit() for i in letter )):
        return not is_vowel(letter)
    else:
        return False

input_word = input("Enter a consonant: ")
is_consonant(input_word)


# In[60]:


#  4. Define a function that accepts a 
#     string that is a word. The function 
#     should capitalize the first letter of 
#     the word if the word starts with a consonant.

def title_case(word):
    if is_consonant(word[0]):
        return word.capitalize()
word1="snapple"
word2="apple"
print(title_case(word1))
print(title_case(word2))


# In[61]:


#  5. Define a function named calculate_tip. 
#     It should accept a tip percentage 
#     (a number between 0 and 1) and the 
#     bill total, and return the amount to tip.

def calculate_tip(pcent,bill):
    if 1 >= pcent >= 0:
        return round((pcent*bill),2)

calculate_tip(.2, 36.15)


# In[ ]:


#  6. Define a function named apply_discount. 
#     It should accept a original price, and 
#     a discount percentage, and return the 
#     price after the discount is applied.

def apply_discount(price,percent):
    discount=(percent/100)*price
    
    return round((price - discount) , 2)

price=380.00
percentage=30
apply_discount(price, percentage)


# In[62]:


#  7. Define a function named handle_commas. 
#     It should accept a string that is a 
#     number that contains commas in it as 
#     input, and return a number as output.

def handle_commas(broken_number):
    fixed_number = ''.join([i for i in broken_number if i.isdigit()])
    
    return fixed_number

def add_numbers(num1,num2):
    return num1+num2

commas_number = "2,530,389"

#add_numbers(8,3)

handle_commas(commas_number)


# In[63]:


#  8. Define a function named get_letter_grade. 
#     It should accept a number and return the 
#     letter grade associated with that number (A-F).

def get_letter_grade(num_grd):
    if 90 <= num_grd <=100:
        return "A"
    elif 80 <= num_grd <=89:
        return "B"
    elif 70 <= num_grd <=79:
        return "C"
    elif 60 <= num_grd <=69:
        return "D"
    else:
        return "F"

get_letter_grade(87)


# In[64]:


#  9. Define a function named remove_vowels 
#     that accepts a string and returns a 
#     string with all the vowels removed.

def remove_vowels(word):
    return ''.join([i for i in word if i.lower() not in ['a','e','i','o','u']])

incoming_word="apple"
remove_vowels(incoming_word)


# In[ ]:


word = "8track 88track     "
fixed = ""

for i in word:
# Strips all numbers and symbols. Spaces stay. 1 Fell swoop lowercases.
    if (i.isalnum() or i == " ") and not i.isdigit():
        fixed+=i.lower()
    else:
        pass
# Strips leading & trailing spaces. Afterwards replaces middle spaces.

fixed = fixed.strip().replace(" ","_")
print(fixed)


# In[265]:


#  10. Define a function named normalize_name. 
#     It should accept a string and return a 
#     valid python identifier, that is:
#     - anything that is not a valid python 
#       identifier should be removed
#     - leading and trailing whitespace should be removed
#     - everything should be lowercase
#     - spaces should be replaced with underscores
#     
#     for example:
#     - Name will become name
#     - First Name will become first_name
#     - % Completed will become completed

def normalize_name(bad_line):
    fixed = ""

    for i in bad_line:
        if (i.isalnum() or i == " ") and not i.isdigit():
            fixed+=i.lower()
        else:
            pass

    fixed = fixed.strip().replace(" ","_")

    return fixed

normalize_name(" 88track 88Track.    ")


# In[8]:


#     11. Write a function named cumulative_sum 
#         that accepts a list of numbers and returns 
#         a list that is the cumulative sum of 
#         the numbers in the list.
#     
#         cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#         cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(inputs):
    from itertools import accumulate

    return list(accumulate(inputs))

cumulative_sum([1,1,1])

output=[]
sum=0
for loop
+=
append output
return ouput


# In[ ]:


#     B1. Create a function named twelveto24. 
#         It should accept a string in the 
#         format 10:45am or 4:30pm and return a 
#         string that is the representation of the time 
#         in a 24-hour format. Bonus write a function 
#         that does the opposite.

def thwelveto24(time_twelve):
    
    hour = time_twelve.split(':')[0]
    minutes = time_twelve.split(':')[1][0] + time_twelve.split(':')[1][1]
    am_pm = time_twelve.split(':')[-1][-2] + time_twelve.split(':')[-1][-1]
    
    if am_pm == 'am':
        if int(hour) < 10:
            return '0' + hour + minutes
        else:
            return hour + minutes
    else:
        return str(int(hour)+12) + minutes

thwelveto24("10:45am")

def twentyfour_to12(time_24):
    
    hour = time_24[0] + time_24[1]
    minutes = time_24[2] + time_24[3]
    
    if int(hour) > 12:
        return str(int(hour)-12) + ":" + minutes + "pm"
    elif hour == '12':
        return hour + ":" + minutes + "pm"
    else:
        return hour + ":" + minutes + "am"

print(thwelveto24("10:45pm"))
print(twentyfour_to12("1245"))


# In[54]:


#     B2. Create a function named col_index. 
#         It should accept a spreadsheet column 
#         name, and return the index number of the column.
#         col_index('A') returns 1
#         col_index('B') returns 2
#         col_index('AA') returns 27

def col_index(column_name_string):

    
    
    index = 'Test'
    return index

col_index('AB')

