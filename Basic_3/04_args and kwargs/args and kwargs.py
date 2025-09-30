"""
در پایتون، با گذشت زمان، حتماً با عبارت‌های عجیب *args و **kwargs مواجه خواهید شد.
 این اصطلاحات به عنوان پارامترهایی در تعریف توابع ظاهر می‌شوند. آن‌ها چه کاری انجام می‌دهند؟
"""
# Simple function with positional arguments (تابع ساده با پارامترهای موقعیتی)
def myfunc(a, b):
    """Returns 5% of the sum of a and b.
    (بازگرداندن 5% مجموع a و b)"""
    return sum((a, b)) * 0.05

print("Result of myfunc(40,60):", myfunc(40, 60))
# خروجی: Result of myfunc(40,60): 5.0 (ترجمه: نتیجه myfunc(40,60))

"""
تحلیل مثال:
در این تابع، a و b پارامترهای موقعیتی (Positional Arguments) هستند.
عدد 40 به a تخصیص می‌یابد چون اولین آرگومان است و 60 به b تخصیص می‌یابد.
برای کار با چندین پارامتر موقعیتی در تابع sum()، باید آن‌ها را به صورت یک تاپل ارسال کنیم.
نکته کلیدی:
وقتی نیاز به کار با بیش از دو عدد داریم، راه‌حل‌های بهتری نسبت به تعریف پارامترهای زیاد با مقادیر پیش‌فرض وجود دارد. در اینجا *args و **kwargs مفید خواهند بود.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
وقتی پارامتر تابع با یک ستاره (*) شروع می‌شود، این امکان را فراهم می‌کند
 که تعداد دلخواهی آرگومان موقعیتی دریافت کند و آن‌ها را به صورت یک تاپل از مقادیر بگیرد.
"""
# Function using *args (تابع با استفاده از *args)
def myfunc(*args):
    """Returns 5% of the sum of all positional arguments.
    (بازگرداندن 5% مجموع تمام آرگومان‌های موقعیتی)"""
    return sum(args) * 0.05

print("Result with three numbers:", myfunc(40, 60, 20))
# خروجی: Result with three numbers: 6.0 (ترجمه: نتیجه با سه عدد)

"""
نکات مهم درباره *args:
کلمه "args" دلخواه است و می‌توانید هر نام دیگری استفاده کنید (البته باید با یک ستاره شروع شود).
*args تمام آرگومان‌های موقعیتی را در یک تاپل جمع‌آوری می‌کند.
این روش برای توابعی که نمی‌دانید چند آرگومان موقعیتی دریافت خواهند کرد، بسیار مفید است.
"""

# Using different name for *args (استفاده از نام دیگر برای *args)
def myfunc(*spam):
    """Demonstrates that the name after * is arbitrary.
    (نشان می‌دهد که نام بعد از * دلخواه است)"""
    return sum(spam) * 0.05

print("Result with different *args name:", myfunc(40, 60, 20))
# خروجی: Result with different *args name: 6.0 (ترجمه: نتیجه با نام متفاوت برای *args)

# More examples with *args (مثال‌های بیشتر با *args)
def print_args(*args):
    """Prints all positional arguments.
    (چاپ تمام آرگومان‌های موقعیتی)"""
    print("Number of arguments:", len(args))  # خروجی: Number of arguments: X (ترجمه: تعداد آرگومان‌ها)
    for i, arg in enumerate(args):
        print(f"Argument {i}: {arg}")  # خروجی: Argument X: Y (ترجمه: آرگومان X)

print_args(1, "hello", True, [1, 2, 3])
# خروجی:
# Number of arguments: 4
# Argument 0: 1
# Argument 1: hello
# Argument 2: True
# Argument 3: [1, 2, 3]
# (ترجمه: مثال‌های بیشتر با *args)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
به طور مشابه، 
پایتون راهی برای مدیریت تعداد دلخواهی از آرگومان‌های کلیدواژه‌ای (Keyword Arguments) ارائه می‌دهد. 
به جای ایجاد یک تاپل از مقادیر، **kwargs یک دیکشنری از جفت‌های کلید/مقدار ایجاد می‌کند.
"""
# Function using **kwargs (تابع با استفاده از **kwargs)
def myfunc(**kwargs):
    """Checks for 'fruit' key in keyword arguments.
    (بررسی وجود کلید 'fruit' در آرگومان‌های کلیدواژه‌ای)"""
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")
        # خروجی: My favorite fruit is X (ترجمه: میوه مورد علاقه من X است)
    else:
        print("I don't like fruit")  # خروجی: I don't like fruit (ترجمه: من میوه دوست ندارم)

myfunc(fruit='pineapple')  # خروجی: My favorite fruit is pineapple (ترجمه: میوه مورد علاقه من pineapple است)
myfunc()  # خروجی: I don't like fruit (ترجمه: من میوه دوست ندارم)

"""
نکات مهم درباره **kwargs:
کلمه "kwargs" نیز دلخواه است و می‌توانید نام دیگری استفاده کنید (البته باید با دو ستاره شروع شود).
**kwargs تمام آرگومان‌های کلیدواژه‌ای را در یک دیکشنری جمع‌آوری می‌کند.
برای توابعی که نمی‌دانید چه کلیدهایی دریافت خواهند کرد، بسیار مفید است.
"""

# More examples with **kwargs (مثال‌های بیشتر با **kwargs)
def print_kwargs(**kwargs):
    """Prints all keyword arguments.
    (چاپ تمام آرگومان‌های کلیدواژه‌ای)"""
    print("Number of keyword arguments:", len(kwargs))
    # خروجی: Number of keyword arguments: X (ترجمه: تعداد آرگومان‌های کلیدواژه‌ای)
    for key, value in kwargs.items():
        print(f"{key}: {value}")  # خروجی: key: value (ترجمه: کلید: مقدار)

print_kwargs(name='Ali', age=30, city='Tehran')
# خروجی:
# Number of keyword arguments: 3
# name: Ali
# age: 30
# city: Tehran
# (ترجمه: مثال‌های بیشتر با **kwargs)

# Using **kwargs with conditional logic (استفاده از **kwargs با منطق شرطی)
def user_preferences(**kwargs):
    """Displays user preferences based on keyword arguments.
    (نمایش ترجیحات کاربر بر اساس آرگومان‌های کلیدواژه‌ای)"""
    if 'color' in kwargs:
        print(f"Favorite color: {kwargs['color']}")
        # خروجی: Favorite color: X (ترجمه: رنگ مورد علاقه: X)
    if 'food' in kwargs:
        print(f"Favorite food: {kwargs['food']}")
        # خروجی: Favorite food: X (ترجمه: غذای مورد علاقه: X)
    if not kwargs:
        print("No preferences specified")
        # خروجی: No preferences specified (ترجمه: ترجیحی مشخص نشده است)

user_preferences(color='blue', food='pizza')
# خروجی:
# Favorite color: blue
# Favorite food: pizza
# (ترجمه: ترجیحات کاربر)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
می‌توانید *args و **kwargs را در
 یک تابع همراه با هم استفاده کنید، اما *args باید قبل از **kwargs قرار گیرد.
"""
# Function combining *args and **kwargs (تابع ترکیبی *args و **kwargs)
def myfunc(*args, **kwargs):
    """Demonstrates combined use of positional and keyword arguments.
    (نشان می‌دهد که چگونه از آرگومان‌های موقعیتی و کلیدواژه‌ای استفاده شود)"""
    if 'fruit' in kwargs and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        # خروجی: I like X and Y and my favorite fruit is Z (ترجمه: من X و Y را دوست دارم و میوه مورد علاقه من Z است)
        print(f"May I have some {kwargs['juice']} juice?")
        # خروجی: May I have some X juice? (ترجمه: می‌توانم کمی آبمیوه X داشته باشم؟)
    else:
        print("Missing required keyword arguments")
        # خروجی: Missing required keyword arguments (ترجمه: آرگومان‌های کلیدواژه‌ای مورد نیاز وجود ندارند)

myfunc('eggs', 'spam', fruit='cherries', juice='orange')
# خروجی:
# I like eggs and spam and my favorite fruit is cherries
# May I have some orange juice?
# (ترجمه: مثال ترکیب *args و **kwargs)

# Correct order of arguments (ترتیب صحیح آرگومان‌ها)
def example_func(a, b, *args, c=10, **kwargs):
    """Demonstrates correct order of different argument types.
    (نشان می‌دهد که چگونه از انواع مختلف آرگومان‌ها استفاده شود)"""
    print("Positional arguments (a, b):", a, b)
    # خروجی: Positional arguments (a, b): X Y (ترجمه: آرگومان‌های موقعیتی)
    print("Additional positional arguments (*args):", args)
    # خروجی: Additional positional arguments (*args): (X, Y, ...) (ترجمه: آرگومان‌های موقعیتی اضافی)
    print("Keyword argument (c):", c)
    # خروجی: Keyword argument (c): X (ترجمه: آرگومان کلیدواژه‌ای)
    print("Additional keyword arguments (**kwargs):", kwargs)
    # خروجی: Additional keyword arguments (**kwargs): {...} (ترجمه: آرگومان‌های کلیدواژه‌ای اضافی)

example_func(1, 2, 3, 4, c=20, name='Ali', age=30)
# خروجی:
# Positional arguments (a, b): 1 2
# Additional positional arguments (*args): (3, 4)
# Keyword argument (c): 20
# Additional keyword arguments (**kwargs): {'name': 'Ali', 'age': 30}
# (ترجمه: ترتیب صحیح آرگومان‌ها)

# Incorrect order raises SyntaxError (ترتیب اشتباه باعث خطای سینتکسی می‌شود)
def incorrect_order_example(*args, a, b):
    """This will raise a SyntaxError because positional arguments
    cannot follow *args.
    (این باعث خطای سینتکسی می‌شود چون آرگومان‌های موقعیتی نمی‌توانند بعد از *args بیایند)"""
    pass

try:
    # This would cause a syntax error if uncommented
    # incorrect_order_example(1, 2, 3, a=4, b=5)
    print("Note: The incorrect order example is commented out to prevent syntax error")
    # خروجی: Note: The incorrect order example is commented out to prevent syntax error (ترجمه: نکته: مثال ترتیب اشتباه برای جلوگیری از خطای سینتکسی کامنت شده است)
except SyntaxError as e:
    print("Syntax error:", str(e))

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
نام‌های دلخواه برای *args و **kwargs
"""
# Using different names for *args and **kwargs (استفاده از نام‌های متفاوت برای *args و **kwargs)
def flexible_func(*positionals, **keywords):
    """Demonstrates that any names can be used for *args and **kwargs.
    (نشان می‌دهد که می‌توان از هر نامی برای *args و **kwargs استفاده کرد)"""
    print("Positional arguments:", positionals)
    # خروجی: Positional arguments: (X, Y, ...) (ترجمه: آرگومان‌های موقعیتی)
    print("Keyword arguments:", keywords)
    # خروجی: Keyword arguments: {...} (ترجمه: آرگومان‌های کلیدواژه‌ای)

flexible_func(1, 2, 3, name='Ali', city='Tehran')
# خروجی:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Ali', 'city': 'Tehran'}
# (ترجمه: نام‌های دلخواه برای *args و **kwargs)

# Rules for parameter order (قوانین ترتیب پارامترها)
def parameter_order_example(a, b, *args, c=10, d=20, **kwargs):
    """Demonstrates the correct order of different parameter types:
    1. Positional parameters (a, b)
    2. *args
    3. Keyword-only parameters with defaults (c, d)
    4. **kwargs
    (نشان می‌دهد که چگونه از انواع مختلف پارامترها استفاده شود:
    1. پارامترهای موقعیتی (a, b)
    2. *args
    3. پارامترهای کلیدواژه‌ای با مقادیر پیش‌فرض (c, d)
    4. **kwargs)"""
    print("a, b:", a, b)  # خروجی: a, b: X Y (ترجمه: a, b)
    print("*args:", args)  # خروجی: *args: (X, Y, ...) (ترجمه: *args)
    print("c, d:", c, d)  # خروجی: c, d: X Y (ترجمه: c, d)
    print("**kwargs:", kwargs)  # خروجی: **kwargs: {...} (ترجمه: **kwargs)

parameter_order_example(1, 2, 3, 4, c=30, name='Ali', age=30)
# خروجی:
# a, b: 1 2
# *args: (3, 4)
# c, d: 30 20
# **kwargs: {'name': 'Ali', 'age': 30}
# (ترجمه: قوانین ترتیب پارامترها)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
# Practical example: A decorator-like function (مثال عملی: تابعی شبیه دکوراتور)
def log_function_call(func):
    """A decorator that logs function calls.
    (یک دکوراتور که فراخوانی توابع را ثبت می‌کند)"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        # خروجی: Calling X with args: Y, kwargs: Z (ترجمه: فراخوانی X با args: Y, kwargs: Z)
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        # خروجی: X returned: Y (ترجمه: X بازگرداند: Y)
        return result
    return wrapper

# Apply the "decorator" (اعمال "دکوراتور")
@log_function_call
def add(a, b):
    """Adds two numbers.
    (جمع دو عدد)"""
    return a + b

@log_function_call
def greet(name, greeting="Hello"):
    """Greets a person with a customizable greeting.
    (سلام کردن با شخص با سلام قابل تنظیم)"""
    return f"{greeting}, {name}!"

# Test the decorated functions (آزمایش توابع دکوره شده)
add(5, 7)
# خروجی:
# Calling add with args: (5, 7), kwargs: {}
# add returned: 12
# (ترجمه: آزمایش توابع دکوره شده)

greet("Ali", greeting="Hi")
# خروجی:
# Calling greet with args: ('Ali',), kwargs: {'greeting': 'Hi'}
# greet returned: Hi, Ali!
# (ترجمه: آزمایش توابع دکوره شده)

"""
 نکته کلیدی:

*args و **kwargs انعطاف‌پذیری برای کار با تعداد دلخواهی از آرگومان‌ها فراهم می‌کنند.
*args آرگومان‌های موقعیتی را به صورت یک تاپل جمع‌آوری می‌کند.
**kwargs آرگومان‌های کلیدواژه‌ای را به صورت یک دیکشنری جمع‌آوری می‌کند.
در ترکیب آن‌ها، *args باید قبل از **kwargs قرار گیرد.
نام‌های args و kwargs قراردادی هستند و می‌توانید از هر نام دیگری استفاده کنید (البته با پیشوندهای * و **).
این ابزارها برای توابع عمومی، دکوراتورها و توابعی که نمی‌دانید چه آرگومان‌هایی دریافت خواهند کرد، بسیار مفید هستند.
"""
