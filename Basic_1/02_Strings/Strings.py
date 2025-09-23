"""
رشته‌ها (Strings) برای ذخیره اطلاعات متنی مانند نام‌ها استفاده می‌شوند. در پایتون از گیومه تکی (') یا گیومه دوتایی (") برای ایجاد رشته استفاده می‌کنیم
"""
# Single word string (رشته یک کلمه‌ای)
print("Single word:", 'hello')  # خروجی: Single word: hello (ترجمه: رشته یک کلمه‌ای)

# Phrase with space (رشته با فاصله)
print("Phrase:", 'This is also a string')  # خروجی: Phrase: This is also a string (ترجمه: عبارت متنی)

# Using double quotes to avoid error (استفاده از گیومه دوتایی برای جلوگیری از خطا)
print("Correct quote handling:", "Now I'm ready to use single quotes!")
# خروجی: Correct quote handling: Now I'm ready to use single quotes! (ترجمه: مدیریت صحیح گیومه‌ها)

"""
اگر از گیومه تکی برای رشته‌ای با علامت ' استفاده کنید، خطای نحوی رخ می‌دهد
"""
# INVALID - Causes syntax error (نامعتبر - باعث خطای نحوی می‌شود)
# print('I'm using single quotes')  # ❌ این خط خطا می‌دهد

# ----------------------------------------------------------------------------------------------------------
print("-" * 80)
"""
برای نمایش رشته‌ها در خروجی از تابع print() استفاده کنید
"""
# Basic print (چاپ پایه)
print('Hello World')  # خروجی: Hello World (ترجمه: سلام دنیا)

# Newline character \n (استفاده از \n برای خط جدید)
print('Use \n to print a new line')
# خروجی:
# Use
#  to print a new line (ترجمه: استفاده از \n برای ایجاد خط جدید)

"""
تابع len() تمام کاراکترها (حتی فاصله و نمادها) را می‌شمارد
"""
text = "Hello World"
print("Length of 'Hello World':", len(text))  # خروجی: Length of 'Hello World': 11 (ترجمه: طول رشته)

# ----------------------------------------------------------------------------------------------------------
print("-" * 80)
"""
رشته‌ها دنباله‌ای از کاراکترها هستند که از ایندکس صفر شروع می‌شوند
"""
s = "Hello World"

# Access first character (دسترسی به اولین کاراکتر)
print("First character (index 0):", s[0])  # خروجی: First character (index 0): H (ترجمه: کاراکتر اول)

# Slicing: [start:stop:step] (برش با فرمت [شروع:پایان:گام])
print("Characters from index 1 to end:", s[1:])    # خروجی: Characters from index 1 to end: ello World (ترجمه: از ایندکس ۱ تا انتها)
print("Characters up to index 3:", s[:3])         # خروجی: Characters up to index 3: Hel (ترجمه: تا ایندکس ۳ - بدون شامل شدن ایندکس ۳)
print("Every other character:", s[::2])           # خروجی: Every other character: HloWrd (ترجمه: هر دو کاراکتر یکی)
print("Reverse string:", s[::-1])                 # خروجی: Reverse string: dlroW olleH (ترجمه: معکوس کردن رشته)

"""
برای شمارش از انتهای رشته از ایندکس منفی استفاده می‌شود
"""
print("Last character (index -1):", s[-1])       # خروجی: Last character (index -1): d (ترجمه: آخرین کاراکتر)
print("All except last character:", s[:-1])      # خروجی: All except last character: Hello Worl (ترجمه: همه به جز آخرین کاراکتر)

# ----------------------------------------------------------------------------------------------------------
print("-" * 80)

"""
رشته‌ها تغییرناپذیر هستند. نمی‌توانید کاراکترهای آن‌ها را مستقیماً تغییر دهید
"""
s = "Hello"
# s[0] = "J"  # ❌ خطای TypeError می‌دهد (رشته‌ها قابل تغییر مستقیم نیستند)

"""
برای "تغییر" رشته، از الحاق (+) استفاده کنید
"""
s = "Hello"
s = s + " World"  # الحاق رشته جدید
print("After concatenation:", s)  # خروجی: After concatenation: Hello World (ترجمه: پس از الحاق)

# تکرار رشته با *
letter = "z"
print("Repeated letter:", letter * 10)  # خروجی: Repeated letter: zzzzzzzzzz (ترجمه: تکرار کاراکتر)

# ----------------------------------------------------------------------------------------------------------
print("-" * 80)
"""
متدهای داخلی رشته‌ها با فرمت رشته.متد() فراخوانی می‌شوند
"""
s = "Hello World"

# تبدیل به حروف بزرگ
print("Uppercase:", s.upper())  # خروجی: Uppercase: HELLO WORLD (ترجمه: حروف بزرگ)

# تبدیل به حروف کوچک
print("Lowercase:", s.lower())  # خروجی: Lowercase: hello world (ترجمه: حروف کوچک)

# تقسیم رشته بر اساس فاصله (پیش‌فرض)
print("Split by space:", s.split())
# خروجی: Split by space: ['Hello', 'World'] (ترجمه: تقسیم بر اساس فاصله)

# تقسیم رشته بر اساس کاراکتر خاص
print("Split by 'o':", s.split("o"))
# خروجی: Split by 'o': ['Hell', ' W', 'rld'] (ترجمه: تقسیم بر اساس کاراکتر o)

# ----------------------------------------------------------------------------------------------------------
print("-" * 80)
"""
برای جایگزینی پویک در رشته‌ها از .format() استفاده کنید
"""
# Basic formatting (قالب‌بندی پایه)
template = "Insert another string with curly brackets: {}"
print(template.format("The inserted string"))
# خروجی: Insert another string with curly brackets: The inserted string (ترجمه: جایگزینی متن در قالب)

# Multiple placeholders (چندین جایگزین)
print("Name: {}, Age: {}".format("Ali", 25))
# خروجی: Name: Ali, Age: 25 (ترجمه: نمایش نام و سن)
