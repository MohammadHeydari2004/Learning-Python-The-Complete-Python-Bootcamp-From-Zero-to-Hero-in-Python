"""
دستورات شرطی if در پایتون به ما امکان می‌دهند تا به کامپیوتر بگوییم بر اساس مجموعه‌ای از نتایج،
اقدامات جایگزینی را انجام دهد. به عبارت ساده، می‌توانیم به کامپیوتر بگوییم:

"اگر این شرط اتفاق افتاد، عمل خاصی را انجام بده"

سپس می‌توانیم این ایده را با دستورات elif و else گسترش دهیم که به ما امکان می‌دهد بگوییم:

"اگر این شرط اتفاق افتاد، عمل خاصی را انجام بده. در غیر این صورت، اگر شرط دیگری اتفاق افتاد،
 عمل دیگری را انجام بده. و اگر هیچ‌کدام از شرط‌های بالا اتفاق نیفتاد، این عمل را انجام بده."
"""

"""
ساختار پایه دستورات شرطی
"""
# Basic if-elif-else structure (ساختار پایه if-elif-else)
condition = True

if condition:
    print("Condition is True, this block will execute")  # خروجی: Condition is True, this block will execute (ترجمه: شرط درست است، این بلوک اجرا می‌شود)
else:
    print("Condition is False, this block will not execute")  # این خط اجرا نمی‌شود


# مثال ساده با مقدار True
# Simple if statement with True condition (دستور if ساده با شرط True)
if True:
    print("It was true!")  # خروجی: It was true! (ترجمه: شرط درست بود!)

"""
نکته کلیدی:
دستور if فقط زمانی بلوک کد مربوطه را اجرا می‌کند که شرط آن درست (True) باشد.
شرط‌ها معمولاً از عملگرهای مقایسه‌ای (مثل ==, >, < و غیره) تشکیل می‌شوند.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
دستورات if-else (if-else Statements)
وقتی نیاز به بررسی یک شرط و ارائه یک گزینه جایگزین داریم،
 از ساختار if-else استفاده می‌کنیم.
"""
# مثال if-else ساده
# Simple if-else example (مثال ساده if-else)
x = False

if x:
    print('x was True!')  # این خط اجرا نمی‌شود
else:
    print('I will be printed in any case where x is not true')
    # خروجی: I will be printed in any case where x is not true (ترجمه: در هر حالتی که x درست نباشد، این چاپ می‌شود)

# مثال عملی با مقایسه
# Practical example with comparison (مثال عملی با مقایسه)
age = 18

if age >= 18:
    print("You are eligible to vote")  # خروجی: You are eligible to vote (ترجمه: شما واجد شرایط رأی دادن هستید)
else:
    print("You are not eligible to vote yet")  # این خط اجرا نمی‌شود

"""
نکات مهم درباره if-else:
بلوک else هیچ شرطی نمی‌گیرد و فقط زمانی اجرا می‌شود که شرط if نادرست (False) باشد.
else اختیاری است - می‌توانید فقط از if بدون else استفاده کنید.
"""
# if without else (if بدون else)
temperature = 30

if temperature > 25:
    print("It's a hot day")  # خروجی: It's a hot day (ترجمه: روز گرمی است)
# No else block (بدون بلوک else)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
شاخه‌های متعدد با elif (Multiple Branches with elif)
وقتی نیاز به بررسی چندین شرط متفاوت داریم، از دستور elif (مخفف else if) استفاده می‌کنیم.
"""
# ساختار کلی با چندین شرط
# Multiple conditions with if-elif-else (چندین شرط با if-elif-else)
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # خروجی: Grade: B (ترجمه: نمره: B)
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# مثال مکان‌ها با elif
# Location example with if-elif-else (مثال مکان با if-elif-else)
loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the Auto Shop!')  # این خط اجرا نمی‌شود
elif loc == 'Bank':
    print('Welcome to the bank!')  # خروجی: Welcome to the bank! (ترجمه: به بانک خوش آمدید!)
else:
    print('Where are you?')  # این خط اجرا نمی‌شود

# مثال نام افراد با چندین شرط
# Person name example (مثال نام افراد)
person = 'George'

if person == 'Sammy':
    print('Welcome Sammy!')  # این خط اجرا نمی‌شود
elif person == 'George':
    print('Welcome George!')  # خروجی: Welcome George! (ترجمه: به جورج خوش آمدید!)
else:
    print("Welcome, what's your name?")  # این خط اجرا نمی‌شود

"""
نکات مهم درباره elif:
می‌توانید تعداد نامحدودی elif قبل از else اضافه کنید.
پایتون شرط‌ها را از بالا به پایین بررسی می‌کند و در اولین شرط درست،
 بلوک مربوطه را اجرا کرده و از بقیه شرط‌ها عبور می‌کند.
بلوک else در صورتی اجرا می‌شود که هیچ‌کدام از شرط‌های if و elif درست نباشند.
"""
# Multiple elif example (مثال چندین elif)
number = 7

if number == 5:
    print("Number is 5")
elif number == 6:
    print("Number is 6")
elif number == 7:
    print("Number is 7")  # خروجی: Number is 7 (ترجمه: عدد 7 است)
elif number == 8:
    print("Number is 8")  # این خط اجرا نمی‌شود
else:
    print("Number is not 5, 6, 7, or 8")  # این خط اجرا نمی‌شود

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
اهمیت تورفتگی (Importance of Indentation)
در پایتون، تورفتگی (Indentation) بخشی از سینتکس زبان است و تعیین می‌کند
 که کدام خطوط کد درون یک بلوک شرطی قرار می‌گیرند.
"""
# مثال‌های صحیح تورفتگی
# Correct indentation examples (مثال‌های تورفتگی صحیح)
x = 15

if x > 10:
    print("x is greater than 10")  # خروجی: x is greater than 10 (ترجمه: x بزرگتر از 10 است)
    if x > 12:
        print("x is also greater than 12")  # خروجی: x is also greater than 12 (ترجمه: x همچنین بزرگتر از 12 است)
    print("This is still inside the first if")  # خروجی: This is still inside the first if (ترجمه: این همچنان درون if اولیه است)
print("This is outside all ifs")  # خروجی: This is outside all ifs (ترجمه: این خارج از تمام ifها است)

# خطا در تورفتگی
# Example of indentation error (مثال خطا در تورفتگی)
# try:
#     x = 5
#     if x > 3:
#     print("x is greater than 3")  # خطا: فاصله‌گذاری اشتباه
# except IndentationError as e:
#     print("Indentation Error:", str(e))
#     # خروجی: Indentation Error: expected an indented block after 'if' statement on line X (ترجمه: خطا در تورفتگی)

"""
نکات مهم درباره تورفتگی:
همگونی تورفتگی بسیار مهم است - نمی‌توانید در یک بلوک از فضای خالی و در بلوک دیگر از تب استفاده کنید.
استاندارد پیشنهادی PEP 8 استفاده از 4 فضای خالی برای هر سطح تورفتگی است.
تورفتگی در پایتون یک انتخاب برای خوانایی نیست، بلکه بخشی از سینتکس زبان است.
"""
# Proper indentation with multiple conditions (تورفتگی صحیح با چندین شرط)
weather = "rainy"

if weather == "sunny":
    print("Wear sunglasses")
    print("It's a bright day")
elif weather == "rainy":
    print("Take an umbrella")  # خروجی: Take an umbrella (ترجمه: چتر بگیرید)
    print("Wear waterproof shoes")
    if True:
        print("This is nested inside rainy condition")  # خروجی: This is nested inside rainy condition (ترجمه: این درون شرط بارانی تو در تو است)
else:
    print("Check the weather forecast")

"""
نکته کلیدی:

دستورات شرطی به شما امکان می‌دهند برنامه‌های هوشمندتری بنویسید
 که بر اساس شرایط مختلف رفتار متفاوتی داشته باشند.
پایتون شرط‌ها را از بالا به پایین بررسی می‌کند و در اولین شرط درست، بلوک مربوطه را اجرا می‌کند.
تورفتگی در پایتون یک انتخاب نیست، بلکه بخشی ضروری از سینتکس زبان است.
می‌توانید از ترکیب if, elif و else برای پوشش تمام سناریوهای ممکن استفاده کنید.
"""
