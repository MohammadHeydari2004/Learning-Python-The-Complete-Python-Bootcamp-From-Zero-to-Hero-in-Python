"""
تابع range در پایتون به شما امکان می‌دهد به سرعت یک لیست از اعداد صحیح ایجاد کنید. این تابع سه پارامتر دارد:

start: عدد شروع (پیش‌فرض 0)
stop: عدد پایان (این عدد در لیست گنجانده نمی‌شود)
step: اندازه گام (پیش‌فرض 1)
"""
# Generate numbers from 0 to 10 (0 تا 10 را ایجاد کن)
print("range(0,11) as list:", list(range(0, 11)))
# خروجی: range(0,11) as list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (ترجمه: لیست اعداد 0 تا 10)

# Note: 11 is not included (نکته: عدد 11 شامل نمی‌شود)
print("range(0,12) as list:", list(range(0, 12)))
# خروجی: range(0,12) as list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] (ترجمه: لیست اعداد 0 تا 11)

# Using step parameter (استفاده از پارامتر گام)
print("Even numbers with step 2:", list(range(0, 11, 2)))
# خروجی: Even numbers with step 2: [0, 2, 4, 6, 8, 10] (ترجمه: اعداد زوج با گام 2)

# Larger step example (مثال گام بزرگ‌تر)
print("Multiples of 10:", list(range(0, 101, 10)))
# خروجی: Multiples of 10: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] (ترجمه: مضارب 10)

"""
نکات مهم درباره تابع range:
range یک ژنراتور (Generator) است، نه یک لیست واقعی.
برای تبدیل آن به لیست باید از list(range(...)) استفاده کنید.
ژنراتورها اطلاعات را تولید می‌کنند اما نیازی به ذخیره‌سازی آن‌ها در حافظه ندارند.
عدد stop در لیست نهایی گنجانده نمی‌شود (مثل سایت نوتیشن در لیست‌ها).
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
تابع enumerate برای ردیابی ایندکس در حین استفاده از حلقه‌های for بسیار مفید است. به جای ایجاد و به‌روزرسانی دستی یک شمارنده، می‌توانید از این تابع استفاده کنید.
"""
# مثال بدون استفاده از enumerate
# Manual index tracking (ردیابی دستی ایندکس)
index_count = 0
for letter in 'abcde':
    print(f"At index {index_count} the letter is {letter}")
    index_count += 1
# خروجی:
# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e
# (ترجمه: در ایندکس X حرف Y است)

# مثال با استفاده از enumerate
# Using enumerate with tuple unpacking (استفاده از enumerate با بسته‌گشایی تاپل)
for i, letter in enumerate('abcde'):
    print(f"At index {i} the letter is {letter}")
# خروجی:
# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e
# (ترجمه: در ایندکس X حرف Y است)

"""
نکات مهم درباره enumerate:
enumerate یک ژنراتور است که تاپل‌هایی از (index, value) تولید می‌کند.
می‌توانید نتیجه را به لیست تبدیل کنید تا ساختار آن را ببینید:
# View enumerate as list (مشاهده enumerate به صورت لیست)
print("Enumerate as list:", list(enumerate('abcde')))  
# خروجی: Enumerate as list: [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')] (ترجمه: enumerate به صورت لیست)
این تابع به ویژه هنگام کار با کتابخانه‌های خارجی بسیار رایج است.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
تابع zip به شما امکان می‌دهد دو یا چند لیست را با هم "سنجش" کنید و یک لیست از تاپل‌ها ایجاد کنید.
"""
# Create two lists (ایجاد دو لیست)
mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c', 'd', 'e']

# Zip the lists together (سنجش لیست‌ها با هم)
zipped = zip(mylist1, mylist2)
print("Zipped object:", zipped)  # خروجی: Zipped object: <zip object at 0x...> (ترجمه: شیء zipped)

# Convert to list to see the result (تبدیل به لیست برای مشاهده نتیجه)
print("Zipped as list:", list(zipped))
# خروجی: Zipped as list: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')] (ترجمه: zipped به صورت لیست)

# Using zip in for loop (استفاده از zip در حلقه for)
for item1, item2 in zip(mylist1, mylist2):
    print(f"For this tuple, first item was {item1} and second item was {item2}")
# خروجی:
# For this tuple, first item was 1 and second item was a
# For this tuple, first item was 2 and second item was b
# For this tuple, first item was 3 and second item was c
# For this tuple, first item was 4 and second item was d
# For this tuple, first item was 5 and second item was e
# (ترجمه: برای این تاپل، آیتم اول X و آیتم دوم Y بود)

"""
نکات مهم درباره zip:
zip نیز یک ژنراتور است.
طول لیست نهایی برابر با کوتاه‌ترین لیست ورودی است.
اگر لیست‌ها طول‌های متفاوتی داشته باشند، zip تا طول کوتاه‌ترین لیست ادامه می‌یابد.
"""
# Different length lists (لیست‌های با طول متفاوت)
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']
print("Zip with different lengths:", list(zip(list1, list2)))
# خروجی: Zip with different lengths: [(1, 'a'), (2, 'b'), (3, 'c')] (ترجمه: zip با طول‌های متفاوت)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
عملگر in برای بررسی وجود یک شیء در یک لیست (یا هر شیء ایتریبل دیگر) استفاده می‌شود.
"""
# Check if 'x' is in list (بررسی وجود 'x' در لیست)
print("'x' in ['x','y','z']:", 'x' in ['x', 'y', 'z'])  # خروجی: 'x' in ['x','y','z']: True (ترجمه: 'x' در لیست وجود دارد)

# Check if 'x' is in numbers list (بررسی وجود 'x' در لیست اعداد)
print("'x' in [1,2,3]:", 'x' in [1, 2, 3])  # خروجی: 'x' in [1,2,3]: False (ترجمه: 'x' در لیست اعداد وجود ندارد)

# Check in string (بررسی در رشته)
print("'a' in 'apple':", 'a' in 'apple')  # خروجی: 'a' in 'apple': True (ترجمه: 'a' در رشته 'apple' وجود دارد)

# Check in dictionary keys (بررسی در کلیدهای دیکشنری)
print("'k1' in {'k1':1, 'k2':2}:", 'k1' in {'k1': 1, 'k2': 2})  # خروجی: 'k1' in {'k1':1, 'k2':2}: True (ترجمه: 'k1' در کلیدهای دیکشنری وجود دارد)

"""
نکات مهم درباره عملگر in:
در دیکشنری‌ها، in به طور پیش‌فرض کلیدها را بررسی می‌کند.
می‌توانید از .values() برای بررسی مقادیر دیکشنری استفاده کنید.
این عملگر برای بررسی سریع وجود یک مقدار در یک مجموعه داده بسیار مفید است.
"""
# Check in dictionary values (بررسی در مقادیر دیکشنری)
d = {'k1': 1, 'k2': 2}
print("1 in dictionary values:", 1 in d.values())  # خروجی: 1 in dictionary values: True (ترجمه: 1 در مقادیر دیکشنری وجود دارد)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
عملگر not in معکوس عملگر in است و بررسی می‌کند که آیا یک شیء در یک لیست (یا هر شیء ایتریبل دیگر) وجود ندارد.
"""
# Check if 'x' is not in list (بررسی عدم وجود 'x' در لیست)
print("'x' not in ['x','y','z']:", 'x' not in ['x', 'y', 'z'])  # خروجی: 'x' not in ['x','y','z']: False (ترجمه: 'x' در لیست وجود دارد)

# Check if 'x' is not in numbers list (بررسی عدم وجود 'x' در لیست اعداد)
print("'x' not in [1,2,3]:", 'x' not in [1, 2, 3])  # خروجی: 'x' not in [1,2,3]: True (ترجمه: 'x' در لیست اعداد وجود ندارد)

# Practical example (مثال عملی)
user_input = 'admin'
allowed_users = ['user1', 'user2', 'user3']
if user_input not in allowed_users:
    print("Access denied")  # خروجی: Access denied (ترجمه: دسترسی رد شد)

"""
نکات مهم درباره عملگر not in:
این عملگر برای بررسی عدم وجود یک مقدار بسیار مفید است.
می‌توانید از آن برای فیلتر کردن داده‌ها یا بررسی محدودیت‌ها استفاده کنید.
ترکیب not in با دستورات شرطی می‌تواند منطق برنامه‌نویسی شما را ساده‌تر کند.
"""
# Combined with if statement (ترکیب با دستور if)
fruits = ['apple', 'banana', 'cherry']
if 'orange' not in fruits:
    print("Adding orange to the list")
    fruits.append('orange')
print("Updated fruits list:", fruits)
# خروجی: Updated fruits list: ['apple', 'banana', 'cherry', 'orange'] (ترجمه: لیست به‌روزرسانی شده میوه‌ها)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
توابع min() و max() به شما امکان می‌دهند به سرعت کمترین و بیشترین مقدار را در یک لیست پیدا کنید.
"""
# Create a list of numbers (ایجاد لیست اعداد)
mylist = [10, 20, 30, 40, 100]

# Find minimum value (یافتن مقدار کمینه)
print("Minimum value:", min(mylist))  # خروجی: Minimum value: 10 (ترجمه: مقدار کمینه)

# Find maximum value (یافتن مقدار بیشینه)
print("Maximum value:", max(mylist))  # خروجی: Maximum value: 100 (ترجمه: مقدار بیشینه)

# Works with other data types (کار با انواع داده‌های دیگر)
letters = ['a', 'b', 'c', 'd', 'e']
print("Min letter:", min(letters))  # خروجی: Min letter: a (ترجمه: کمینه حروف)
print("Max letter:", max(letters))  # خروجی: Max letter: e (ترجمه: بیشینه حروف)

# Works with strings (کار با رشته‌ها)
words = ['apple', 'banana', 'cherry']
print("Min word:", min(words))  # خروجی: Min word: apple (ترجمه: کمینه کلمات)
print("Max word:", max(words))  # خروجی: Max word: cherry (ترجمه: بیشینه کلمات)

"""
نکات مهم درباره min و max:
این توابع برای لیست‌هایی از اعداد، رشته‌ها و سایر اشیاء قابل مقایسه کار می‌کنند.
در رشته‌ها، min و max بر اساس ترتیب الفبایی (ASCII) عمل می‌کنند.
اگر لیست خالی باشد، خطای ValueError رخ می‌دهد.
"""
# Error with empty list (خطا با لیست خالی)
try:
    min([])
except ValueError as e:
    print("Error with empty list:", str(e))
    # خروجی: Error with empty list: min() arg is an empty sequence (ترجمه: خطا با لیست خالی)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
پایتون یک کتابخانه داخلی به نام random دارد که شامل توابع مختلفی برای کار با اعداد تصادفی است. در اینجا دو تابع مفید را بررسی می‌کنیم:
"""
# Import shuffle function (وارد کردن تابع shuffle)
from random import shuffle

# Create a list (ایجاد لیست)
mylist = [10, 20, 30, 40, 100]
print("Original list:", mylist)  # خروجی: Original list: [10, 20, 30, 40, 100] (ترجمه: لیست اصلی)

# Shuffle the list (섞نده لیست)
shuffle(mylist)
print("Shuffled list:", mylist)  # خروجی: Shuffled list: [40, 10, 100, 30, 20] (معمولاً ترتیب متفاوت) (ترجمه: لیست شافل شده)

# Note: shuffle works in-place (نکته: shuffle در جای خود کار می‌کند)
result = shuffle([1, 2, 3])
print("Shuffle return value:", result)  # خروجی: Shuffle return value: None (ترجمه: مقدار بازگشتی shuffle)

# Import randint function (وارد کردن تابع randint)
from random import randint

# Generate random integer (تولید عدد تصادفی صحیح)
random_number = randint(0, 100)
print("Random integer between 0 and 100:", random_number)
# خروجی: Random integer between 0 and 100: 25 (معمولاً عدد متفاوت) (ترجمه: عدد تصادفی بین 0 و 100)

# Another random number (عدد تصادفی دیگر)
print("Another random integer:", randint(0, 100))
# خروجی: Another random integer: 91 (معمولاً عدد متفاوت) (ترجمه: عدد تصادفی دیگر)

"""
نکات مهم درباره کتابخانه random:
shuffle لیست را در جای خود (in-place) می‌چیند و هیچ چیزی را برنمی‌گرداند (مقدار بازگشتی None است).
randint(a, b) یک عدد تصادفی صحیح بین a و b (شامل خود a و b) تولید می‌کند.
این توابع برای شبیه‌سازی‌ها، بازی‌ها و هر جایی که نیاز به رفتار تصادفی دارید مفید هستند.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
تابع input() به شما امکان می‌دهد از کاربر ورودی دریافت کنید.
"""
# Get user input (دریافت ورودی کاربر)
user_input = input('Enter Something into this box: ')
print("You entered:", user_input)
# خروجی: You entered: great job! (ترجمه: شما وارد کردید: great job!)

"""
نکات مهم درباره تابع input:
ورودی همیشه به صورت رشته (string) دریافت می‌شود، حتی اگر کاربر اعداد وارد کند.
برای تبدیل ورودی به نوع داده‌ای دیگر (مثل عدد)، باید از توابع تبدیل استفاده کنید.
"""
# Convert input to integer (تبدیل ورودی به عدد صحیح)
age_input = input("Please enter your age: ")
age = int(age_input)
print(f"You are {age} years old")
# خروجی: You are 25 years old (ترجمه: شما 25 ساله هستید)

# Convert input to float (تبدیل ورودی به عدد اعشاری)
height_input = input("Please enter your height in meters: ")
height = float(height_input)
print(f"Your height is {height} meters")
# خروجی: Your height is 1.75 meters (ترجمه: قد شما 1.75 متر است)

# Advanced input example (مثال پیشرفته با input)
name = input("What is your name? ")
print(f"Hello, {name}!")

try:
    age = int(input("How old are you? "))
    print(f"Next year you will be {age + 1} years old.")
except ValueError:
    print("That's not a valid number!")

"""
نکات ایمنی درباره input:
همیشه ورودی کاربر را اعتبارسنجی کنید.
برای تبدیل به انواع داده‌های خاص (مثل عدد)، از بلاک‌های try/except استفاده کنید.
در برنامه‌های واقعی، ورودی کاربر ممکن است حاوی داده‌های مخرب باشد، بنابراین آن را همیشه با احتیاط پردازش کنید.
"""
