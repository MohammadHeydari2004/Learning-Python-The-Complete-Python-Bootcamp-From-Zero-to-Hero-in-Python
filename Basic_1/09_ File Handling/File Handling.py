"""
در پایتون از شیء فایل (File Objects) برای تعامل با فایل‌های خارجی روی کامپیوتر استفاده می‌شود.
این فایل‌ها می‌توانند انواع مختلفی از فایل‌ها باشند (فایل‌های متنی، صوتی، ایمیل‌ها، اسناد اکسل و غیره).
 توجه داشته باشید که برای کار با برخی انواع فایل‌ها ممکن است نیاز
 به نصب کتابخانه‌های خاصی داشته باشید که در این بخش فقط به کار با فایل‌های متنی ساده می‌پردازیم.
"""
# Create a test file using IPython magic (ایجاد یک فایل تست با استفاده از IPython magic)
# Note: This works only in Jupyter notebooks (نکته: این کد فقط در Jupyter notebooks کار می‌کند)
# %%writefile test.txt
# Hello, this is a quick test file.

"""
باز کردن فایل‌ها (Opening Files)
پایتون یک تابع داخلی به نام open() دارد که امکان باز کردن و کار با فایل‌ها را فراهم می‌کند.
"""
# Open a file in the same directory (باز کردن فایل در همان دایرکتوری)
my_file = open('test.txt')
print("File opened successfully")  # خروجی: File opened successfully (ترجمه: فایل با موفقیت باز شد)

# Check current working directory (بررسی دایرکتوری فعلی)
# Note: This works only in Jupyter notebooks (نکته: این کد فقط در Jupyter notebooks کار می‌کند)
# print("Current directory:", pwd)


"""
خطاهای رایج در باز کردن فایل
اگر فایل مورد نظر در دایرکتوری موجود نباشد، خطای FileNotFoundError رخ می‌دهد
"""
try:
    # Attempt to open non-existent file (تلاش برای باز کردن فایل موجود نیست)
    myfile = open('whoops.txt')
except FileNotFoundError as e:
    print("Error when opening file:", str(e))
    # خروجی: Error when opening file: [Errno 2] No such file or directory: 'whoops.txt' (ترجمه: خطا هنگام باز کردن فایل)


"""
مسیرهای فایل در سیستم‌های مختلف
ویندوز: از دو بک‌اسلش \\ استفاده کنید تا پایتون آن را به عنوان کاراکتر خاص تفسیر نکند.
مک و لینوکس: از اسلش معکوس / استفاده کنید.
"""
# Windows file path example (مثال مسیر فایل ویندوز)
# windows_file = open("C:\\Users\\YourUserName\\test.txt")

# Mac/Linux file path example (مثال مسیر فایل مک/لینوکس)
# mac_linux_file = open("/Users/YourUserName/test.txt")

"""
خواندن از فایل‌ها (Reading Files)
پس از باز کردن یک فایل، می‌توانید از آن بخوانید:

متد read()
کل محتوای فایل را به صورت یک رشته برمی‌گرداند
"""
# Open and read a file (باز کردن و خواندن فایل)
my_file = open('test.txt')
content = my_file.read()
print("File content:", content)
# خروجی: File content: Hello, this is a quick test file. (ترجمه: محتوای فایل)

# Important: After reading, the cursor is at the end of the file (نکته مهم: پس از خواندن، نشانگر در انتهای فایل قرار می‌گیرد)
print("Trying to read again:", my_file.read())
# خروجی: Trying to read again:  (ترجمه: تلاش برای خواندن مجدد - خالی است)

# Reset the cursor to the beginning with seek(0) (بازنشانی نشانگر به ابتدا با seek(0))
my_file.seek(0)
print("After seek, read again:", my_file.read())
# خروجی: After seek, read again: Hello, this is a quick test file. (ترجمه: پس از seek، مجدد خواندن)


"""
متد readlines()
لیستی از تمام خطوط فایل را برمی‌گرداند
"""
# Reset cursor and read lines (بازنشانی نشانگر و خواندن خطوط)
my_file.seek(0)
lines = my_file.readlines()
print("File lines as list:", lines)
# خروجی: File lines as list: ['Hello, this is a quick test file.'] (ترجمه: خطوط فایل به صورت لیست)

# Close the file when done (بستن فایل پس از اتمام کار)
my_file.close()
print("File closed successfully")  # خروجی: File closed successfully (ترجمه: فایل با موفقیت بسته شد)

"""
نکته مهم:
همیشه پس از اتمام کار با فایل، آن را با متد close() ببندید تا منابع سیستم آزاد شوند.
برای فایل‌های بزرگ، استفاده از readlines() ممکن است حافظه زیادی مصرف کند چون کل فایل را در حافظه نگه می‌دارد.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
نوشتن در فایل‌ها (Writing to Files)
برای نوشتن در فایل، باید فایل را با حالت نوشتن ('w') باز کنید:

حالت نوشتن ('w')
اگر فایل وجود داشته باشد، محتوای قبلی آن پاک می‌شود.
اگر فایل وجود نداشته باشد، یک فایل جدید ایجاد می‌شود.
"""
# Open file in write mode (باز کردن فایل در حالت نوشتن)
write_file = open('test.txt', 'w')

# Write to the file (نوشتن در فایل)
chars_written = write_file.write('This is a new line')
print("Characters written:", chars_written)  # خروجی: Characters written: 18 (ترجمه: تعداد کاراکترهای نوشته شده)

# Always close the file (همیشه فایل را ببندید)
write_file.close()

# Verify the content (بررسی محتوا)
verify_file = open('test.txt')
print("File content after writing:", verify_file.read())
# خروجی: File content after writing: This is a new line (ترجمه: محتوای فایل پس از نوشتن)
verify_file.close()

"""
حالت نوشتن و خواندن ('w+')
امکان هم نوشتن و هم خواندن فایل را فراهم می‌کند
"""
# Open file in write and read mode (باز کردن فایل در حالت نوشتن و خواندن)
write_read_file = open('test.txt', 'w+')

# Write content (نوشتن محتوا)
write_read_file.write('First line\nSecond line')

# Reset cursor to beginning (بازنشانی نشانگر به ابتدا)
write_read_file.seek(0)

# Read the content (خواندن محتوا)
print("Content after write+read:", write_read_file.read())
# خروجی: Content after write+read: First line\nSecond line (ترجمه: محتوا پس از نوشتن و خواندن)
write_read_file.close()

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
 اضافه کردن به فایل‌ها (Appending to Files)
برای اضافه کردن محتوا به انتهای فایل بدون پاک کردن محتوای قبلی، از حالت اضافه کردن ('a') استفاده کنید:

حالت اضافه کردن ('a')
نشانگر در انتهای فایل قرار می‌گیرد.
اگر فایل وجود نداشته باشد، یک فایل جدید ایجاد می‌شود.
"""
# Open file in append mode (باز کردن فایل در حالت اضافه کردن)
append_file = open('test.txt', 'a')

# Append text (اضافه کردن متن)
append_file.write('\nThis is text being appended to test.txt')
append_file.write('\nAnd another line here.')

# Close the file (بستن فایل)
append_file.close()

# Verify the appended content (بررسی محتوای اضافه شده)
verify_append = open('test.txt')
print("File content after appending:")
print(verify_append.read())
# خروجی:
# File content after appending:
# First line
# Second line
# This is text being appended to test.txt
# And another line here.
# (ترجمه: محتوای فایل پس از اضافه کردن)
verify_append.close()

"""
حالت اضافه کردن و خواندن ('a+')
امکان هم اضافه کردن و هم خواندن فایل را فراهم می‌کند
"""
# Open file in append and read mode (باز کردن فایل در حالت اضافه کردن و خواندن)
append_read_file = open('test.txt', 'a+')

# Append more content (اضافه کردن محتوای بیشتر)
append_read_file.write('\nAdditional line with a+ mode')

# Reset cursor to beginning to read all content (بازنشانی نشانگر به ابتدا برای خواندن کل محتوا)
append_read_file.seek(0)
print("\nFull content after a+ mode:")
print(append_read_file.read())
# خروجی: Full content after a+ mode: (محتوای کامل فایل پس از حالت a+)
append_read_file.close()

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
تکرار روی خطوط فایل (Iterating Through Files)
یکی از روش‌های کارآمد برای کار با فایل‌های بزرگ، تکرار روی خطوط فایل بدون بارگیری کل فایل در حافظه است
"""
# Create a test file with multiple lines (ایجاد یک فایل تست با چند خط)
# %%writefile test.txt
# First Line
# Second Line

# Iterate through file line by line (تکرار روی فایل خط به خط)
for line in open('test.txt'):
    # Note: print automatically adds a newline (نکته: print به طور خودکار یک خط جدید اضافه می‌کند)
    print("Line:", line, end='')
    # خروجی:
    # Line: First Line
    # Line: Second Line
    # (ترجمه: خط:)

# Alternative variable name (نام متغیر جایگزین)
for custom_name in open('test.txt'):
    print("Custom name:", custom_name, end='')
    # خروجی:
    # Custom name: First Line
    # Custom name: Second Line
    # (ترجمه: نام سفارشی:)

"""
نکات مهم در تکرار روی فایل‌ها
می‌توانید نام متغیر را هر چیزی قرار دهید (مثل line, asdf, custom_name و غیره).
با این روش کل فایل در حافظه ذخیره نمی‌شود، فقط یک خط در هر زمان خوانده می‌شود.
تورفتگی (Indentation) بعد از حلقه for الزامی است چون در پایتون برای تعریف بلوک کد استفاده می‌شود.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
روش‌های توصیه‌شده برای کار با فایل‌ها (Recommended Practices)
استفاده از with برای مدیریت خودکار فایل‌ها
روش توصیه‌شده برای کار با فایل‌ها استفاده از بلاک with است که به طور خودکار فایل را بسته و از نشت منابع جلوگیری می‌کند
"""
# Recommended way to handle files (روش توصیه‌شده برای کار با فایل‌ها)
with open('test.txt', 'r') as file:
    content = file.read()
    print("\nContent using with statement:", content)
    # خروجی: Content using with statement: (محتوا با استفاده از دستور with)
# File is automatically closed here (فایل در اینجا به طور خودکار بسته می‌شود)

# Write using with statement (نوشتن با استفاده از دستور with)
with open('test.txt', 'w') as file:
    file.write('Content written with "with" statement')

# Read to verify (خواندن برای تأیید)
with open('test.txt', 'r') as file:
    print("After with write:", file.read())
    # خروجی: After with write: Content written with "with" statement (ترجمه: پس از نوشتن با with)

"""
مزایای استفاده از with
فایل به طور خودکار بسته می‌شود حتی اگر خطایی رخ دهد.
نیازی به فراخوانی دستی close() نیست.
کد تمیزتر و خواناتر است.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
حالت	   توضیحات	  مثال   
`'r'`	حالت پیش‌فرض - فقط برای خواندن (فایل باید وجود داشته باشد)	  open('file.txt', 'r')
`'w'`	حالت نوشتن - محتوای قبلی پاک می‌شود، اگر فایل نباشد ایجاد می‌شود	  open('file.txt', 'w')
`'a'`	حالت اضافه کردن - محتوا به انتهای فایل اضافه می‌شود	   open('file.txt', 'a')
`'r+'`	خواندن و نوشتن - نشانگر در ابتدا قرار می‌گیرد	   open('file.txt', 'r+')
`'w+'`	نوشتن و خواندن - محتوای قبلی پاک می‌شود	   open('file.txt', 'w+')
`'a+'`	اضافه کردن و خواندن - نشانگر در انتهای فایل قرار می‌گیرد	    open('file.txt', 'a+')
"""

"""
نکته کلیدی:

همیشه پس از اتمام کار با فایل، آن را با close() ببندید یا از بلاک with استفاده کنید.
برای خواندن فایل‌های بزرگ از تکرار خط به خط استفاده کنید تا حافظه کمتری مصرف شود.
در حالت 'w' مراقب باشید چون محتوای قبلی فایل پاک می‌شود.
برای اطمینان از وجود فایل در مسیر صحیح، از pwd در Jupyter یا بررسی مسیر کامل استفاده کنید.
"""
