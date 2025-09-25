"""
معرفی حلقه‌های while (Introduction to while Loops)
حلقه‌های while در پایتون یکی از عمومی‌ترین راه‌ها برای انجام تکرار است.
 دستور while به طور مکرر یک دستور یا گروهی از دستورات را اجرا می‌کند تا زمانی که شرط مربوطه درست (True) باشد.
 به این دلیل به آن "حلقه" گفته می‌شود که دستورات کد مجدداً و مجدداً تا زمانی که شرط برقرار نباشد، اجرا می‌شوند.
"""
# While loop acts as an iterator in Python (حلقه while در پایتون به عنوان ایتریتور عمل می‌کند)
# This example shows basic while loop concept (این مثال مفهوم پایه حلقه while را نشان می‌دهد)
x = 0
while x < 5:
    print(f"Current value of x: {x}")  # خروجی: مقدار فعلی x
    x += 1
# خروجی:
# Current value of x: 0
# Current value of x: 1
# Current value of x: 2
# Current value of x: 3
# Current value of x: 4

"""
نکته کلیدی:
حلقه‌های while تا زمانی که شرط مربوطه درست (True) باشد، ادامه می‌یابند.
وقتی شرط نادرست (False) شود، اجرای حلقه متوقف می‌شود.
برخلاف حلقه‌های for، حلقه‌های while نیازی به یک شیء ایتریبل ندارند و فقط به یک شرط بولین وابسته هستند.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
ساختار پایه حلقه while (Basic Structure of while Loops)
"""

"""
ساختار کلی یک حلقه while در پایتون به این صورت است
"""
# General format of while loop (ساختار کلی حلقه while)
# while test:
#     # code statements (دستورات کد)
# else:
#     # final code statements (دستورات نهایی کد)

"""
مثال ساده از ساختار حلقه while
"""
# Basic while loop example (مثال ساده حلقه while)
x = 0

while x < 10:
    print('x is currently:', x)  # خروجی: x در حال حاضر برابر است با
    print('x is still less than 10, adding 1 to x')  # خروجی: x هنوز کمتر از 10 است، 1 به x اضافه می‌شود
    x += 1
"""
خروجی کد بالا :
x is currently: 0
x is still less than 10, adding 1 to x
x is currently: 1
x is still less than 10, adding 1 to x
x is currently: 2
x is still less than 10, adding 1 to x
x is currently: 3
x is still less than 10, adding 1 to x
x is currently: 4
x is still less than 10, adding 1 to x
x is currently: 5
x is still less than 10, adding 1 to x
x is currently: 6
x is still less than 10, adding 1 to x
x is currently: 7
x is still less than 10, adding 1 to x
x is currently: 8
x is still less than 10, adding 1 to x
x is currently: 9
x is still less than 10, adding 1 to x
"""

"""
نکات مهم درباره ساختار حلقه while:
شرط تست: باید یک عبارت بولین باشد که تا زمانی که درست است، حلقه ادامه می‌یابد.
بدنه حلقه: کدهایی که باید در هر تکرار اجرا شوند (با تورفتگی مشخص می‌شوند).
بلوک else (اختیاری): کدهایی که پس از پایان حلقه (وقتی شرط نادرست شد) اجرا می‌شوند.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
استفاده از else با حلقه while (Using else with while Loops)
بلوک else در حلقه‌های while به صورت اختیاری است و
 فقط زمانی اجرا می‌شود که شرط حلقه while نادرست (False) شود.
"""

"""
مثال استفاده از else با حلقه while
"""
# While loop with else block (حلقه while با بلوک else)
x = 0

while x < 10:
    print('x is currently:', x)  # خروجی: x در حال حاضر برابر است با
    print('x is still less than 10, adding 1 to x')  # خروجی: x هنوز کمتر از 10 است، 1 به x اضافه می‌شود
    x += 1
else:
    print('All Done!')  # خروجی: همه چیز انجام شد!

"""
خروجی کد بالا:
x is currently: 0
x is still less than 10, adding 1 to x
x is currently: 1
x is still less than 10, adding 1 to x
x is currently: 2
x is still less than 10, adding 1 to x
x is currently: 3
x is still less than 10, adding 1 to x
x is currently: 4
x is still less than 10, adding 1 to x
x is currently: 5
x is still less than 10, adding 1 to x
x is currently: 6
x is still less than 10, adding 1 to x
x is currently: 7
x is still less than 10, adding 1 to x
x is currently: 8
x is still less than 10, adding 1 to x
x is currently: 9
x is still less than 10, adding 1 to x
All Done!
"""

"""
نکته مهم:
بلوک else فقط زمانی اجرا می‌شود که شرط حلقه while به طور طبیعی نادرست شود.
اگر از حلقه با استفاده از break خارج شوید، بلوک else اجرا نشده است.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
دستورات break، continue و pass (break, continue, and pass Statements)
ما می‌توانیم از دستورات break، continue و pass در حلقه‌های خود 
برای افزودن عملکردهای اضافی در موارد مختلف استفاده کنیم.
 این سه دستور به شرح زیر تعریف می‌شوند:

break: از حلقه بیرون می‌آید (حلقه را متوقف می‌کند).
continue: به ابتدای حلقه برمی‌گردد (تکرار فعلی را متوقف می‌کند و به تکرار بعدی می‌رود).
pass: هیچ کاری انجام نمی‌دهد (یک دستور خالی است).
"""

"""
ساختار کلی با استفاده از break و continue
"""
# # General format with break and continue (ساختار کلی با استفاده از break و continue)
# while test:
#     # code statement (دستور کد)
#     if test:
#         break  # Exits the loop (خارج از حلقه می‌شود)
#     if test:
#         continue  # Goes to the top of the loop (به ابتدای حلقه برمی‌گردد)
# else:
#     # final code statements (دستورات نهایی کد)

"""
نکات مهم درباره این دستورات:
دستورات break و continue می‌توانند 
در هر جایی از بدنه حلقه ظاهر شوند، اما معمولاً درون یک دستور if قرار می‌گیرند.
دستور pass معمولاً وقتی استفاده می‌شود که نیاز به یک
 دستور دارید اما نمی‌خواهید هیچ کاری انجام شود (مثلاً برای پیاده‌سازی آینده).
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
مثال‌های عملی (Practical Examples)
"""

# مثال استفاده از continue
# Example using continue statement (مثال استفاده از دستور continue)
x = 0

while x < 10:
    print('x is currently:', x)  # خروجی: x در حال حاضر برابر است با
    print('x is still less than 10, adding 1 to x')  # خروجی: x هنوز کمتر از 10 است، 1 به x اضافه می‌شود
    x += 1
    if x == 3:
        print('x==3')  # خروجی: x برابر با 3 است
    else:
        print('continuing...')  # خروجی: ادامه...
        continue

"""
خروجی کد بالا:
x is currently: 0
x is still less than 10, adding 1 to x
continuing...
x is currently: 1
x is still less than 10, adding 1 to x
continuing...
x is currently: 2
x is still less than 10, adding 1 to x
x==3
x is currently: 3
x is still less than 10, adding 1 to x
continuing...
x is currently: 4
x is still less than 10, adding 1 to x
continuing...
x is currently: 5
x is still less than 10, adding 1 to x
continuing...
x is currently: 6
x is still less than 10, adding 1 to x
continuing...
x is currently: 7
x is still less than 10, adding 1 to x
continuing...
x is currently: 8
x is still less than 10, adding 1 to x
continuing...
x is currently: 9
x is still less than 10, adding 1 to x
continuing...
"""

"""
مثال استفاده از break
"""
# Example using break statement (مثال استفاده از دستور break)
x = 0

while x < 10:
    print('x is currently:', x)  # خروجی: x در حال حاضر برابر است با
    print('x is still less than 10, adding 1 to x')  # خروجی: x هنوز کمتر از 10 است، 1 به x اضافه می‌شود
    x += 1
    if x == 3:
        print('Breaking because x==3')  # خروجی: متوقف می‌شود چون x برابر با 3 است
        break
    else:
        print('continuing...')  # خروجی: ادامه...
        continue

"""
خروجی کد بالا:
x is currently: 0
x is still less than 10, adding 1 to x
continuing...
x is currently: 1
x is still less than 10, adding 1 to x
continuing...
x is currently: 2
x is still less than 10, adding 1 to x
Breaking because x==3
"""

"""
نکته مهم:
در مثال break، بلوک else اجرا نمی‌شود و
 عبارت "continuing..." برای x=3 چاپ نمی‌شود، زیرا حلقه به طور کامل متوقف شده است.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
هشدار درباره حلقه‌های بی‌نهایت (Warning About Infinite Loops)
"""

"""
یک نکته مهم در استفاده از حلقه‌های while این است که ممکن است یک حلقه بی‌نهایت ایجاد کنید.
 این زمانی اتفاق می‌افتد که شرط همیشه درست (True) باشد و
 هیچ مکانیزمی برای خروج از حلقه وجود نداشته باشد.
"""

"""
مثال حلقه بی‌نهایت
"""
# WARNING: This will create an infinite loop (هشدار: این کد یک حلقه بی‌نهایت ایجاد می‌کند)
# DO NOT RUN THIS CODE UNLESS YOU KNOW HOW TO STOP IT (این کد را اجرا نکنید مگر اینکه بدانید چگونه آن را متوقف کنید)
try:
    # while True:
    #     print("I'm stuck in an infinite loop!")
    print("Warning: Infinite loop example is commented out to prevent accidental execution")
    # خروجی: Warning: Infinite loop example is commented out to prevent accidental execution (ترجمه: هشدار: مثال حلقه بی‌نهایت برای جلوگیری از اجرای تصادفی کامنت شده است)
except:
    pass

"""
راه‌های متوقف کردن حلقه بی‌نهایت:
در Jupyter Notebook: از منوی Kernel > Restart استفاده کنید.
در برنامه‌های عادی پایتون: کلیدهای Ctrl + C را فشار دهید.
"""
"""
چگونه از حلقه‌های بی‌نهایت جلوگیری کنیم:
مطمئن شوید که شرط حلقه در نهایت نادرست (False) می‌شود.
از متغیرهایی که در شرط استفاده می‌شوند، در بدنه حلقه تغییر دهید.
برای اطمینان، می‌توانید از یک متغیر شمارنده و یک حداکثر تعداد تکرار استفاده کنید.
"""
# Safe while loop with counter (حلقه while ایمن با شمارنده)
max_iterations = 100
counter = 0
x = 0

while x < 10 and counter < max_iterations :
    print ( 'x is currently:' , x )  # خروجی: x در حال حاضر برابر است با
    x += 1
    counter += 1

if counter == max_iterations :
    print ( "Stopped to prevent infinite loop" )  # خروجی: برای جلوگیری از حلقه بی‌نهایت متوقف شد

"""
نکته کلیدی:

حلقه‌های while زمانی مفید هستند که تعداد تکرارها از قبل مشخص نیست.
همیشه مطمئن شوید که شرط حلقه در نهایت نادرست (False) می‌شود تا از حلقه‌های بی‌نهایت جلوگیری کنید.
دستورات break و continue امکان کنترل پیشرفته‌تر جریان حلقه را فراهم می‌کنند.
بلوک else فقط در صورت پایان طبیعی حلقه (بدون استفاده از break) اجرا می‌شود.
"""
