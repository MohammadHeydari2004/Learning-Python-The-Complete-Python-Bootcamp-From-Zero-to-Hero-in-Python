"""
فهم لیست‌ها (List Comprehensions)
 یک عملیات پیشرفته در پایتون است که علاوه بر عملیات‌های دنباله‌ای و متدهای لیست، به ما امکان می‌دهد لیست‌ها را با نمادگذاری متفاوتی بسازیم.
 می‌توانید آن را به عنوان یک حلقه for در یک خط که داخل براکت قرار گرفته است، در نظر بگیرید.
"""
# Basic list comprehension example (مثال پایه فهم لیست)
lst = [x for x in 'word']
print("List comprehension result:", lst)
# خروجی: List comprehension result: ['w', 'o', 'r', 'd'] (ترجمه: نتیجه فهم لیست)

"""
نکته کلیدی:
فهم لیست‌ها راهی خوانا و کارآمد برای ساخت لیست‌ها هستند.
این ساختار برای کسانی که با نمادگذاری ریاضی آشنا هستند، بسیار آشنا خواهد بود (مثل: x^2 : x در {0,1,2...10}).
فهم لیست‌ها معادل یک حلقه for در یک خط هستند اما خواناتر و مختصرتر از آن.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
ساختار کلی فهم لیست‌ها به این صورت است:
"""
# Basic structure of list comprehension (ساختار پایه فهم لیست)
# [expression for item in iterable]
squares = [x**2 for x in range(5)]
print("Squares using list comprehension:", squares)
# خروجی: Squares using list comprehension: [0, 1, 4, 9, 16] (ترجمه: مربع‌ها با استفاده از فهم لیست)

"""
اجزای ساختار فهم لیست:
expression: عبارتی که برای هر آیتم ارزیابی می‌شود (مثل x, x**2, x.upper() و غیره).
for item in iterable: حلقه‌ای که روی یک شیء ایتریبل (iterable) پیمایش می‌کند.
"""
# Grab every letter in string (گرفتن هر حرف در رشته)
letters = [letter for letter in 'python']
print("Letters in 'python':", letters)
# خروجی: Letters in 'python': ['p', 'y', 't', 'h', 'o', 'n'] (ترجمه: حروف در 'python')

# Create list of numbers (ایجاد لیست اعداد)
numbers = [num for num in range(5, 10)]
print("Numbers from 5 to 9:", numbers)
# خروجی: Numbers from 5 to 9: [5, 6, 7, 8, 9] (ترجمه: اعداد از 5 تا 9)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
فهم لیست‌ها می‌توانند برای انجام عملیات ساده روی داده‌ها استفاده شوند.
"""
# Square numbers in range (ساخت مربع اعداد در محدوده)
squares = [x**2 for x in range(0, 11)]
print("Squares of numbers 0-10:", squares)
# خروجی: Squares of numbers 0-10: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100] (ترجمه: مربع اعداد 0 تا 10)

# Convert letters to uppercase (تبدیل حروف به بزرگ)
uppercase_letters = [letter.upper() for letter in 'hello']
print("Uppercase letters:", uppercase_letters)
# خروجی: Uppercase letters: ['H', 'E', 'L', 'L', 'O'] (ترجمه: حروف بزرگ)

# Generate even numbers (تولید اعداد زوج)
even_numbers = [x for x in range(20) if x % 2 == 0]
print("Even numbers up to 20:", even_numbers)
# خروجی: Even numbers up to 20: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] (ترجمه: اعداد زوج تا 20)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
می‌توانیم از دستورات شرطی در فهم لیست‌ها استفاده کنیم تا فیلترهای پیچیده‌تری ایجاد کنیم.
"""
# Check for even numbers in a range (بررسی اعداد زوج در محدوده)
even_numbers = [x for x in range(11) if x % 2 == 0]
print("Even numbers 0-10:", even_numbers)
# خروجی: Even numbers 0-10: [0, 2, 4, 6, 8, 10] (ترجمه: اعداد زوج 0 تا 10)

# Multiple conditions in list comprehension (چندین شرط در فهم لیست)
filtered_numbers = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
print("Numbers divisible by 2 and 3:", filtered_numbers)
# خروجی: Numbers divisible by 2 and 3: [0, 6, 12, 18] (ترجمه: اعداد قابل تقسیم بر 2 و 3)

# Using if-else in list comprehension (استفاده از if-else در فهم لیست)
even_odd = ['Even' if x % 2 == 0 else 'Odd' for x in range(10)]
print("Even/Odd classification:", even_odd)
# خروجی: Even/Odd classification: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd'] (ترجمه: طبقه‌بندی زوج/فرد)

"""
نکته مهم:
در فهم لیست‌ها، بخش if بعد از for قرار می‌گیرد.
برای استفاده از if-else، باید قبل از for قرار بگیرد.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
فهم لیست‌ها می‌توانند برای انجام عملیات پیچیده‌تر مانند تبدیل واحد‌ها استفاده شوند.
"""
# Convert Celsius to Fahrenheit (تبدیل سلسیوس به فارنهایت)
celsius = [0, 10, 20.1, 34.5]
fahrenheit = [((9/5) * temp + 32) for temp in celsius]
print("Celsius temperatures:", celsius)
# خروجی: Celsius temperatures: [0, 10, 20.1, 34.5] (ترجمه: دمای سلسیوس)
print("Fahrenheit temperatures:", fahrenheit)
# خروجی: Fahrenheit temperatures: [32.0, 50.0, 68.18, 94.1] (ترجمه: دمای فارنهایت)

# Combine strings (ترکیب رشته‌ها)
names = ['Ali', 'Reza', 'Sara']
greetings = [f"Hello, {name}!" for name in names]
print("Personalized greetings:", greetings)
# خروجی: Personalized greetings: ['Hello, Ali!', 'Hello, Reza!', 'Hello, Sara!'] (ترجمه: سلام‌های شخصی‌سازی شده)

# Complex mathematical operations (عملیات‌های ریاضی پیچیده‌تر)
results = [x**2 + 2*x + 1 for x in range(-5, 6)]
print("Results of x^2 + 2x + 1:", results)
# خروجی: Results of x^2 + 2x + 1: [16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36] (ترجمه: نتایج x^2 + 2x + 1)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
می‌توانیم فهم لیست‌ها را در داخل یکدیگر قرار دهیم تا ساختارهای پیچیده‌تری ایجاد کنیم.
"""
# Nested list comprehension example (مثال فهم لیست تو در تو)
nested_comp = [x**2 for x in [x**2 for x in range(11)]]
print("Nested list comprehension result:", nested_comp)
# خروجی: Nested list comprehension result: [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000] (ترجمه: نتیجه فهم لیست تو در تو)

# Create multiplication table (ساخت جدول ضرب)
multiplication_table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print("First row of multiplication table:", multiplication_table[0])
# خروجی: First row of multiplication table: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (ترجمه: اولین سطر جدول ضرب)
print("Last row of multiplication table:", multiplication_table[-1])
# خروجی: Last row of multiplication table: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] (ترجمه: آخرین سطر جدول ضرب)

# Filtering in nested list comprehension (فیلتر کردن در فهم لیست تو در تو)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_elements = [num for row in matrix for num in row if num % 2 == 0]
print("Even elements in matrix:", even_elements)
# خروجی: Even elements in matrix: [2, 4, 6, 8] (ترجمه: عناصر زوج در ماتریس)

"""
نکته مهم:
در فهم لیست‌های تو در تو، ترتیب حلقه‌ها از چپ به راست است.
فهم لیست‌های پیچیده می‌توانند خوانایی کد را کاهش دهند، بنابراین برای خوانایی بهتر، گاهی استفاده از حلقه‌های معمولی ترجیح داده می‌شود.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
نکته کلیدی:

فهم لیست‌ها راهی کوتاه‌تر و خواناتر برای ساخت لیست‌ها هستند.
آن‌ها معادل حلقه‌های for هستند اما خلاصه‌تر و تمیزتر از آن‌ها هستند.
برای فیلتر کردن داده‌ها و انجام تبدیلات سریع بسیار مفید هستند.
در موارد پیچیده، ممکن است خوانایی کد کاهش یابد، بنابراین باید با احتیاط استفاده شوند.
"""
