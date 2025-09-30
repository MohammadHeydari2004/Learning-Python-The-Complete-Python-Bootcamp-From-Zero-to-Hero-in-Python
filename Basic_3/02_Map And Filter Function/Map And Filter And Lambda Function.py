"""
تابع map به شما امکان می‌دهد یک تابع را روی هر آیتم در یک شیء ایتریبل (مثل لیست) اعمال کنید.
 به عبارت دیگر، می‌توانید به سرعت همان تابع را برای هر آیتم در یک دنباله فراخوانی کنید.
"""
# General format of map function (ساختار کلی تابع map)
# map(function, iterable)
# To get results, convert to list: list(map(function, iterable))
# (برای دریافت نتایج، تبدیل به لیست: list(map(function, iterable)))

# Define a function to square numbers (تعریف تابع برای مربع کردن اعداد)
def square(num):
    """Returns the square of a number.
    (بازگرداندن مربع یک عدد)"""
    return num ** 2

# Create a list of numbers (ایجاد لیست اعداد)
my_nums = [1, 2, 3, 4, 5]

# Apply square function to each element using map (اعمال تابع مربع به هر عنصر با استفاده از map)
squared_nums = map(square, my_nums)
print("Map object:", squared_nums)
# خروجی: Map object: <map object at 0x...> (ترجمه: شیء map)

# Convert map result to list to see values (تبدیل نتیجه map به لیست برای مشاهده مقادیر)
print("Squared numbers:", list(map(square, my_nums)))
# خروجی: Squared numbers: [1, 4, 9, 16, 25] (ترجمه: اعداد مربع شده)


# Function to process strings based on length (تابع برای پردازش رشته‌ها بر اساس طول)
def splicer(mystring):
    """Returns 'even' if string length is even, otherwise returns first character.
    (اگر طول رشته زوج باشد 'even' را برمی‌گرداند، در غیر این صورت اولین کاراکتر را برمی‌گرداند)"""
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]

# List of names (لیست نام‌ها)
mynames = ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike']

# Apply splicer function to each name (اعمال تابع splicer به هر نام)
print("Processed names:", list(map(splicer, mynames)))
# خروجی: Processed names: ['even', 'C', 'S', 'K', 'even'] (ترجمه: نام‌های پردازش شده)

"""
نکات مهم درباره تابع map:
map یک ژنراتور است، بنابراین برای مشاهده نتایج باید آن را به لیست تبدیل کنید یا از آن عبور کنید.
تابع ارسالی به map باید یک تابع قابل فراخوانی باشد.
map برای اعمال یک تابع خاص به تمام عناصر یک ایتریبل بسیار مفید است.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
تابع filter یک ایتریتور برمی‌گرداند که آیتم‌هایی
 از یک ایتریبل را ارائه می‌دهد که تابع ارسالی برای آن‌ها مقدار True برمی‌گرداند.
 به عبارت دیگر، شما باید یک تابع فیلتر را تعریف کنید که مقدار True یا False برگرداند،
 سپس آن را به همراه ایتریبل خود به filter ارسال کنید.
"""
# Function to check if a number is even (تابع برای بررسی اینکه آیا یک عدد زوج است)
def check_even(num):
    """Returns True if number is even, False otherwise.
    (اگر عدد زوج باشد True را برمی‌گرداند، در غیر این صورت False را برمی‌گرداند)"""
    return num % 2 == 0

# List of numbers (لیست اعداد)
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Apply filter to get even numbers (اعمال فیلتر برای دریافت اعداد زوج)
even_nums = filter(check_even, nums)
print("Filter object:", even_nums)
# خروجی: Filter object: <filter object at 0x...> (ترجمه: شیء filter)

# Convert filter result to list to see values (تبدیل نتیجه filter به لیست برای مشاهده مقادیر)
print("Even numbers:", list(filter(check_even, nums)))
# خروجی: Even numbers: [0, 2, 4, 6, 8, 10] (ترجمه: اعداد زوج)

"""
نکات مهم درباره تابع filter:
تابع ارسالی به filter حتماً باید مقدار بولین (True یا False) برگرداند.
filter فقط آیتم‌هایی را برمی‌گرداند که تابع برای آن‌ها مقدار True برمی‌گرداند.
مانند map، filter نیز یک ژنراتور است و برای مشاهده نتایج باید آن را به لیست تبدیل کنید.
"""
# Another example: filter numbers greater than 5 (مثال دیگر: فیلتر اعداد بزرگتر از 5)
def greater_than_five(num):
    return num > 5

print("Numbers > 5:", list(filter(greater_than_five, nums)))
# خروجی: Numbers > 5: [6, 7, 8, 9, 10] (ترجمه: اعداد بزرگتر از 5)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
یکی از مفیدترین (و برای مبتدیان، گیج‌کننده‌ترین) ابزارهای پایتون،
 عبارت‌های لامبدا (lambda expressions) هستند. عبارت‌های لامبدا به شما امکان می‌دهند تا توابع "ناشناس" (anonymous) ایجاد کنید.
 این بدان معناست که می‌توانید به سرعت توابع موقت را بدون نیاز به تعریف رسمی آن‌ها با استفاده از def ایجاد کنید.
"""
# Regular function definition (تعریف تابع معمولی)
def square(num):
    return num ** 2

print("Regular function result:", square(2))  # خروجی: Regular function result: 4 (ترجمه: نتیجه تابع معمولی)

# Lambda expression equivalent (معادل عبارت لامبدا)
square_lambda = lambda num: num ** 2
print("Lambda function result:", square_lambda(2))  # خروجی: Lambda function result: 4 (ترجمه: نتیجه تابع لامبدا)

# General format of lambda expression (ساختار کلی عبارت لامبدا)
# lambda arguments: expression
# Example: lambda x, y: x + y (مثال: lambda x, y: x + y)

# Lambda for getting first character of a string (لامبدا برای گرفتن اولین کاراکتر رشته)
first_char = lambda s: s[0]
print("First character of 'hello':", first_char('hello'))  # خروجی: First character of 'hello': h (ترجمه: اولین کاراکتر 'hello')

# Lambda for reversing a string (لامبدا برای معکوس کردن رشته)
reverse_str = lambda s: s[::-1]
print("Reversed 'python':", reverse_str('python'))  # خروجی: Reversed 'python': nohtyp (ترجمه: معکوس 'python')

# Lambda with multiple arguments (لامبدا با چندین آرگومان)
add_nums = lambda x, y: x + y
print("3 + 5 =", add_nums(3, 5))  # خروجی: 3 + 5 = 8 (ترجمه: جمع دو عدد)

# Lambda with conditional expression (لامبدا با عبارت شرطی)
is_even = lambda num: 'even' if num % 2 == 0 else 'odd'
print("4 is", is_even(4))  # خروجی: 4 is even (ترجمه: 4 زوج است)
print("7 is", is_even(7))  # خروجی: 7 is odd (ترجمه: 7 فرد است)

"""
نکات مهم درباره عبارت‌های لامبدا:
بدنه لامبدا یک عبارت واحد است، نه یک بلوک دستورات.
لامبدا‌ها برای توابع ساده و کوتاه طراحی شده‌اند.
برای توابع پیچیده، استفاده از def مناسب‌تر است.
لامبدا‌ها اغلب هنگامی استفاده می‌شوند که نیاز به ارسال یک تابع ساده به توابع دیگر (مثل map و filter) دارید.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
یکی از موارد رایج استفاده از لامبدا، استفاده آن با توابع map و filter است. این کار زمانی مفید است که
 تنها یک بار نیاز به استفاده از تابع دارید و نیازی به تعریف رسمی آن نیست.
"""
# List of numbers (لیست اعداد)
my_nums = [1, 2, 3, 4, 5]

# Using lambda with map to square numbers (استفاده از لامبدا با map برای مربع کردن اعداد)
print("Squared with lambda map:", list(map(lambda num: num ** 2, my_nums)))
# خروجی: Squared with lambda map: [1, 4, 9, 16, 25] (ترجمه: مربع شده با lambda map)

# Using lambda with map for string processing (استفاده از لامبدا با map برای پردازش رشته)
names = ['Ali', 'Reza', 'Sara']
print("Uppercase names:", list(map(lambda name: name.upper(), names)))
# خروجی: Uppercase names: ['ALI', 'REZA', 'SARA'] (ترجمه: نام‌ها با حروف بزرگ)


# List of numbers (لیست اعداد)
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using lambda with filter to get even numbers (استفاده از لامبدا با filter برای دریافت اعداد زوج)
print("Even numbers with lambda filter:", list(filter(lambda n: n % 2 == 0, nums)))
# خروجی: Even numbers with lambda filter: [0, 2, 4, 6, 8, 10] (ترجمه: اعداد زوج با lambda filter)

# Using lambda with filter for more complex condition (استفاده از لامبدا با filter برای شرط پیچیده‌تر)
print("Numbers > 5 with lambda filter:", list(filter(lambda n: n > 5, nums)))
# خروجی: Numbers > 5 with lambda filter: [6, 7, 8, 9, 10] (ترجمه: اعداد بزرگتر از 5 با lambda filter)

# Filter strings with specific length (فیلتر رشته‌های با طول خاص)
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Words with length > 5:", list(filter(lambda word: len(word) > 5, words)))
# خروجی: Words with length > 5: ['banana', 'cherry', 'elderberry'] (ترجمه: کلمات با طول بیشتر از 5)

"""
نکات مهم درباره ترکیب لامبدا با map و filter:
لامبدا‌ها کد را مختصرتر و خواناتر می‌کنند، به خصوص برای توابع ساده.
برای توابع پیچیده، استفاده از def بهتر است چون خوانایی کد را افزایش می‌دهد.
لامبدا‌ها اغلو در کتابخانه‌هایی مانند pandas برای پردازش داده‌ها استفاده می‌شوند.
"""


"""
نکته کلیدی:

تابع map برای اعمال یک تابع به تمام عناصر یک ایتریبل استفاده می‌شود.
تابع filter برای فیلتر کردن عناصر بر اساس یک شرط استفاده می‌شود.
عبارت‌های لامبدا برای ایجاد توابع کوتاه و موقت بدون نیاز به تعریف رسمی با def استفاده می‌شوند.
ترکیب لامبدا با map و filter کد را مختصرتر و خواناتر می‌کند، اما برای توابع پیچیده از def استفاده کنید.
لامبدا‌ها اغلب در کتابخانه‌های پردازش داده مانند pandas استفاده می‌شوند.
"""