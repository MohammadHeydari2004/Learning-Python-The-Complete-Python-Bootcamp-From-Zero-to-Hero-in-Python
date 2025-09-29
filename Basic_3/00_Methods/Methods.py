"""
متدها (Methods) در پایتون در واقع توابع داخلی ساخته شده در اشیاء هستند.
 متدها عملکردهای خاصی را روی یک شیء انجام می‌دهند و می‌توانند پارامترهایی را دریافت کنند، دقیقاً مانند یک تابع معمولی.
"""
# Methods are functions built into objects (متدها توابعی هستند که درون اشیاء ساخته شده‌اند)
# Example of method usage (مثال استفاده از متد)
my_string = "hello world"
print("Uppercase string:", my_string.upper())
# خروجی: Uppercase string: HELLO WORLD (ترجمه: رشته با حروف بزرگ)

# Another example with list (مثال دیگر با لیست)
my_list = [1, 2, 3]
print("List after append:", my_list.append(4))
# خروجی: List after append: None (توجه: append تغییرات را مستقیماً روی لیست اعمال می‌کند و None برمی‌گرداند)
print("Modified list:", my_list)  # خروجی: Modified list: [1, 2, 3, 4] (ترجمه: لیست تغییر یافته)

"""
نکته کلیدی:
متدها به شیء خاصی متعلق هستند و فقط روی آن نوع شیء کار می‌کنند.
ساختار کلی متدها به این صورت است: شیء.نام_متد(آرگومان‌ها).
در پس‌زمینه، پایتون یک آرگومان مخفی به نام self را که به خود شیء ارجاع می‌دهد، به متدها اضافه می‌کند (این آرگومان را نمی‌بینیم اما در برنامه‌نویسی شیءگرا از آن استفاده می‌کنیم).
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
برای استفاده از متدها، ابتدا باید یک شیء از نوع مورد نظر ایجاد کنید، سپس متد مربوطه را روی آن فراخوانی کنید.
"""
# General format of method calling (ساختار کلی فراخوانی متدها)
# object.method(arg1, arg2, etc...)
result = "example".upper()
print("Result of upper() method:", result)
# خروجی: Result of upper() method: EXAMPLE (ترجمه: نتیجه متد upper())

# String methods examples (مثال‌های متدهای رشته)
text = "python programming"

# Convert to uppercase (تبدیل به حروف بزرگ)
print("Uppercase:", text.upper())  # خروجی: Uppercase: PYTHON PROGRAMMING (ترجمه: حروف بزرگ)

# Capitalize first letter (کپیتال کردن اولین حرف)
print("Capitalize:", text.capitalize())  # خروجی: Capitalize: Python programming (ترجمه: کپیتال اولین حرف)

# Find substring position (یافتن موقعیت زیررشته)
print("Position of 'prog':", text.find("prog"))  # خروجی: Position of 'prog': 7 (ترجمه: موقعیت 'prog')

# Replace substring (جایگزینی زیررشته)
print("Replace 'python' with 'java':", text.replace("python", "java"))
# خروجی: Replace 'python' with 'java': java programming (ترجمه: جایگزینی 'python' با 'java')

"""
نکات مهم درباره متدها:
هر نوع شیء (رشته، لیست، دیکشنری و غیره) مجموعه‌ای از متدهای خاص خود را دارد.
برخی متدها مقداری برمی‌گردانند (مثل upper()) و برخی دیگر تغییرات را مستقیماً روی شیء اعمال می‌کنند و None برمی‌گردانند (مثل append()).
برای مشاهده متدهای یک شیء در Jupyter Notebook می‌توانید بعد از نقطه (.) کلید Tab را فشار دهید.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
لیست‌ها در پایتون مجموعه‌ای از متدهای مفید دارند که به شما امکان می‌دهند به راحتی لیست‌ها را مدیریت کنید.
"""
# Create a sample list (ایجاد یک لیست نمونه)
lst = [1, 2, 3, 4, 5]
print("Original list:", lst)  # خروجی: Original list: [1, 2, 3, 4, 5] (ترجمه: لیست اصلی)

# append() - Add element to the end (افزودن عنصر به انتهای لیست)
lst.append(6)
print("After append(6):", lst)  # خروجی: After append(6): [1, 2, 3, 4, 5, 6] (ترجمه: پس از append(6))

# count() - Count occurrences of an element (شمارش تکرار یک عنصر)
print("Count of 2:", lst.count(2))  # خروجی: Count of 2: 1 (ترجمه: تعداد تکرار 2)

# extend() - Add elements from another iterable (افزودن عناصر از یک ایتریبل دیگر)
lst.extend([7, 8])
print("After extend([7, 8]):", lst)  # خروجی: After extend([7, 8]): [1, 2, 3, 4, 5, 6, 7, 8] (ترجمه: پس از extend)

# insert() - Insert element at specific position (درج عنصر در موقعیت خاص)
lst.insert(2, 99)  # Insert 99 at index 2 (درج 99 در ایندکس 2)
print("After insert(2, 99):", lst)  # خروجی: After insert(2, 99): [1, 2, 99, 3, 4, 5, 6, 7, 8] (ترجمه: پس از insert)

# pop() - Remove and return element at index (حذف و بازگرداندن عنصر در ایندکس)
popped = lst.pop(2)
print(f"After pop(2)={popped}:", lst)  # خروجی: After pop(2)=99: [1, 2, 3, 4, 5, 6, 7, 8] (ترجمه: پس از pop)

# remove() - Remove first occurrence of value (حذف اولین تکرار مقدار)
lst.remove(3)
print("After remove(3):", lst)  # خروجی: After remove(3): [1, 2, 4, 5, 6, 7, 8] (ترجمه: پس از remove)

# reverse() - Reverse the list (معکوس کردن لیست)
lst.reverse()
print("After reverse():", lst)  # خروجی: After reverse(): [8, 7, 6, 5, 4, 2, 1] (ترجمه: پس از reverse)

# sort() - Sort the list (مرتب‌سازی لیست)
lst.sort()
print("After sort():", lst)  # خروجی: After sort(): [1, 2, 4, 5, 6, 7, 8] (ترجمه: پس از sort)

"""
نکات مهم درباره متدهای لیست:
برخی متدها مانند append()، extend()، insert()، pop()، remove()، reverse() و sort() تغییرات را مستقیماً روی لیست اعمال می‌کنند و None برمی‌گردانند.
برخی دیگر مانند count() مقداری را برمی‌گردانند اما لیست اصلی را تغییر نمی‌دهند.
برای دریافت لیست مرتب‌شده جدید بدون تغییر لیست اصلی می‌توانید از sorted(lst) استفاده کنید.
"""
# Important note about methods that modify in-place (نکته مهم درباره متدهای تغییردهنده در جا)
original_list = [3, 1, 2]

# sort() modifies the list in-place and returns None (sort() لیست را در جا تغییر می‌دهد و None برمی‌گرداند)
sort_result = original_list.sort()
print("Sort result:", sort_result)  # خروجی: Sort result: None (ترجمه: نتیجه sort)
print("Modified list:", original_list)  # خروجی: Modified list: [1, 2, 3] (ترجمه: لیست تغییر یافته)

# sorted() returns a new sorted list without modifying the original (sorted() لیست جدید مرتب شده برمی‌گرداند بدون تغییر لیست اصلی)
new_list = sorted(original_list, reverse=True)
print("New sorted list:", new_list)  # خروجی: New sorted list: [3, 2, 1] (ترجمه: لیست جدید مرتب شده)
print("Original list remains unchanged:", original_list)  # خروجی: Original list remains unchanged: [1, 2, 3] (ترجمه: لیست اصلی بدون تغییر می‌ماند)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
تابع help() به شما امکان می‌دهد اطلاعات بیشتری درباره متدها و توابع پایتون دریافت کنید.
"""
# Using help() function (استفاده از تابع help)
# Note: In actual code, help() would display documentation in console (نکته: در کد واقعی، help() مستندات را در کنسول نمایش می‌دهد)
print("To get help on list.count method, use: help(list.count)")
# خروجی: To get help on list.count method, use: help(list.count) (ترجمه: برای دریافت راهنما درباره متد list.count، از help(list.count) استفاده کنید)

# Simulating help output for list.count (شبیه‌سازی خروجی help برای list.count)
print("\nSimulated help for list.count:")
print("count(...) method of builtins.list instance")
print("    L.count(value) -> integer -- return number of occurrences of value")
# خروجی:
# Simulated help for list.count:
# count(...) method of builtins.list instance
#     L.count(value) -> integer -- return number of occurrences of value
# (ترجمه: شبیه‌سازی راهنمای list.count)

"""
نکات مهم درباره تابع help:
در محیط‌های توسعه مانند Jupyter Notebook، می‌توانید با فشردن کلید Tab بعد از نقطه (.) لیست تمام متدهای یک شیء را مشاهده کنید.
با فشردن Shift+Tab می‌توانید راهنمای کوتاهی درباره متد فعلی دریافت کنید.
برای اطلاعات کامل‌تر می‌توانید از تابع help() استفاده کنید.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
در این بخش چند مثال ترکیبی از استفاده از متدها را بررسی می‌کنیم.
"""
# Task management example (مثال مدیریت کارها)
tasks = []

# Add tasks (افزودن کارها)
tasks.append("Complete Python course")
tasks.append("Learn data structures")
tasks.append("Practice coding daily")
print("Initial tasks:", tasks)
# خروجی: Initial tasks: ['Complete Python course', 'Learn data structures', 'Practice coding daily'] (ترجمه: کارهای اولیه)

# Mark first task as completed (علامت‌گذاری اولین کار به عنوان تکمیل شده)
completed_task = tasks.pop(0)
print(f"Completed: {completed_task}")
print("Remaining tasks:", tasks)
# خروجی: Remaining tasks: ['Learn data structures', 'Practice coding daily'] (ترجمه: کارهای باقی‌مانده)

# Add a higher priority task (افزودن کار با اولویت بالاتر)
tasks.insert(0, "Urgent: Fix critical bug")
print("After adding urgent task:", tasks)
# خروجی: After adding urgent task: ['Urgent: Fix critical bug', 'Learn data structures', 'Practice coding daily'] (ترجمه: پس از افزودن کار فوری)

# Count occurrences of a keyword (شمارش تکرار یک کلیدواژه)
keyword_count = str(tasks).count("Learn")
print(f"Tasks containing 'Learn': {keyword_count}")  # خروجی: Tasks containing 'Learn': 1 (ترجمه: کارهای حاوی 'Learn')


# String processing example (مثال پردازش رشته‌ها)
text = "Python is powerful and Python is versatile"

# Convert to lowercase (تبدیل به حروف کوچک)
lower_text = text.lower()
print("Lowercase text:", lower_text)
# خروجی: Lowercase text: python is powerful and python is versatile (ترجمه: متن با حروف کوچک)

# Count occurrences of a word (شمارش تکرار یک کلمه)
word_count = lower_text.count("python")
print(f"'python' appears {word_count} times")  # خروجی: 'python' appears 2 times (ترجمه: 'python' 2 بار ظاهر شده است)

# Replace a word (جایگزینی یک کلمه)
replaced_text = text.replace("Python", "Java")
print("After replacement:", replaced_text)
# خروجی: After replacement: Java is powerful and Java is versatile (ترجمه: پس از جایگزینی)

# Split text into words (تقسیم متن به کلمات)
words = text.split()
print("Words list:", words)
# خروجی: Words list: ['Python', 'is', 'powerful', 'and', 'Python', 'is', 'versatile'] (ترجمه: لیست کلمات)

# Join words with custom separator (ادغام کلمات با جداکننده سفارشی)
joined_text = "-".join(words)
print("Joined with hyphens:", joined_text)
# خروجی: Joined with hyphens: Python-is-powerful-and-Python-is-versatile (ترجمه: ادغام با خط تیره)

"""
 نکته کلیدی:

متدها توابعی هستند که به شیء خاصی متعلق هستند و فقط روی آن نوع شیء کار می‌کنند.
برای استفاده از متدها، ابتدا یک شیء ایجاد کنید، سپس متد مربوطه را با فرمت شیء.متد() فراخوانی کنید.
برخی متدها مقداری برمی‌گردانند و برخی دیگر تغییرات را مستقیماً روی شیء اعمال می‌کنند.
از تابع help() یا کلیدهای میانبر در Jupyter Notebook (Tab و Shift+Tab) برای دریافت راهنمایی درباره متدها استفاده کنید.
برای یادگیری متدهای جدید، حتماً از Google و مستندات پایتون کمک بگیرید.
"""
