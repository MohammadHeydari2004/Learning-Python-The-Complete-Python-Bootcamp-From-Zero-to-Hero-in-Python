"""
وقتی در پایتون یک متغیر ایجاد می‌کنید، نام آن در یک فضای نام (Namespace) ذخیره می‌شود.
 متغیرها همچنین یک حوزه (Scope) دارند که تعیین می‌کند دیگر بخش‌های کد شما به آن متغیر دسترسی دارند یا خیر.
"""
# Example of variable scope confusion (مثال ابهام در حوزه متغیر)
x = 25  # Global variable (متغیر سراسری)

def printer():
    x = 50  # Local variable (متغیر محلی)
    return x

print("Global x value:", x)        # خروجی: Global x value: 25 (ترجمه: مقدار x سراسری)
print("printer() return value:", printer())  # خروجی: printer() return value: 50 (ترجمه: مقدار بازگشتی printer())

"""
چرا خروجی‌ها متفاوت هستند؟
پایتون برای تشخیص اینکه کدام x را در کد خود ارجاع می‌دهید، از قوانین خاصی پیروی می‌کند. این جایی است که مفهوم حوزه (Scope) اهمیت پیدا می‌کند.

سه قانون کلی حوزه متغیرها:
تخصیص نام‌ها به طور پیش‌فرض متغیرهای محلی را ایجاد یا تغییر می‌دهد.
ارجاع به نام‌ها حداکثر در چهار حوزه جستجو می‌کند:
محلی (Local)
توابع دربرگیرنده (Enclosing functions)
سراسری (Global)
داخلی (Built-in)
نام‌های اعلام شده در دستورات global و nonlocal، نام‌های تخصیص داده شده را به حوزه‌های ماژول و تابع دربرگیرنده نگاشت می‌دهند.
نکته کلیدی:
درک مفهوم حوزه در کد شما برای تخصیص و فراخوانی صحیح نام متغیرها بسیار مهم است.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
قانون LEGB (LEGB Rule)
پایتون از قانون LEGB برای تعیین حوزه متغیرها استفاده می‌کند:

L: محلی (Local) —
 نام‌های تخصیص داده شده به هر نحو درون یک تابع (با def یا lambda) و در آن تابع به صورت global اعلام نشده‌اند.
 
E: محلی توابع دربرگیرنده (Enclosing function locals) —
 نام‌ها در حوزه محلی هر تابع دربرگیرنده (با def یا lambda)، از داخلی‌ترین به خارجی‌ترین.
 
G: سراسری (Global) — 
نام‌های تخصیص داده شده در سطح بالای یک فایل ماژول، یا درون یک تابع با global اعلام شده‌اند.

B: داخلی (Built-in) — 
نام‌های از پیش تخصیص داده شده در ماژول نام‌های داخلی: open, range, SyntaxError و غیره.
"""
# x is local in this lambda function (x در این تابع لامبدا محلی است)
f = lambda x: x ** 2
result = f(5)
print("Result of lambda function:", result)  # خروجی: Result of lambda function: 25 (ترجمه: نتیجه تابع لامبدا)

# Example of enclosing function scope (مثال حوزه توابع دربرگیرنده)
name = 'This is a global name'  # Global variable (متغیر سراسری)


def greet ( ) :
    # Enclosing function scope (حوزه تابع دربرگیرنده)
    name = 'Sammy'  # This shadows the global name (این نام جهانی را سایه می‌زند)

    def hello ( ) :
        # Uses name from the enclosing function (از نام تابع دربرگیرنده استفاده می‌کند)
        print ( 'Hello ' + name )

    hello ( )


greet ( )  # خروجی: Hello Sammy (ترجمه: سلام Sammy)

# Accessing global variable (دسترسی به متغیر سراسری)
print("Global name value:", name)  # خروجی: Global name value: This is a global name (ترجمه: مقدار نام سراسری)

# Built-in functions are always available (توابع داخلی همیشه در دسترس هستند)
print("Built-in len function:", len)  # خروجی: Built-in len function: <built-in function len> (ترجمه: تابع len داخلی)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
متغیرهای محلی (Local Variables)
وقتی در تعریف یک تابع، متغیرهایی را اعلان می‌کنید،
 این متغیرها به هیچ وجه با متغیرهای دیگری که نام مشابهی دارند و خارج از تابع استفاده شده‌اند،
 مرتبط نیستند. یعنی نام متغیرها نسبت به تابع محلی هستند. 
این مفهوم را حوزه متغیر می‌نامند.
"""
# Example of local variables (مثال متغیرهای محلی)
x = 50  # Global variable (متغیر سراسری)

def func(x):
    # x here is a local variable (x در اینجا یک متغیر محلی است)
    print('x is', x)  # خروجی: x is 50 (ترجمه: x برابر است با)
    x = 2
    print('Changed local x to', x)  # خروجی: Changed local x to 2 (ترجمه: x محلی به 2 تغییر کرد)

func(x)
print('x is still', x)  # خروجی: x is still 50 (ترجمه: x همچنان برابر است با)
"""
تحلیل مثال:
در اولین باری که مقدار x را در بدنه تابع چاپ می‌کنیم، پایتون از مقدار پارامتر ارسالی استفاده می‌کند.
سپس مقدار x را برابر با 2 قرار می‌دهیم. نام x محلی برای تابع ما است.
بنابراین، وقتی مقدار x را در تابع تغییر می‌دهیم، x تعریف شده در بلوک اصلی بدون تغییر می‌ماند.
در آخرین دستور چاپ، مقدار x را همان‌طور که در بلوک اصلی تعریف شده است، نمایش می‌دهیم و این تأیید می‌کند که توسط تخصیص محلی در تابع فراخوانی شده قبلی تحت تأثیر قرار نگرفته است.

نکته مهم:
متغیرهای تعریف شده درون تابع، فقط در آن تابع قابل دسترسی هستند.
تغییرات اعمال شده به متغیرهای محلی، روی متغیرهای سراسری با همان نام تأثیری ندارد.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
اگر بخواهید مقداری را به نامی تخصیص دهید که در سطح بالای برنامه تعریف شده است
 (یعنی نه درون هیچ حوزه‌ای مثل توابع یا کلاس‌ها)،
 باید به پایتون بگویید که این نام محلی نیست، بلکه سراسری است.
 برای این کار از دستور global استفاده می‌کنیم.
"""
# Example of global statement (مثال دستور global)
x = 50  # Global variable (متغیر سراسری)

def func():
    global x  # Declare x as global (اعلام x به عنوان سراسری)
    print('This function is now using the global x!')  # خروجی: This function is now using the global x! (ترجمه: این تابع اکنون از x سراسری استفاده می‌کند!)
    print('Because of global x is:', x)  # خروجی: Because of global x is: 50 (ترجمه: به دلیل global x برابر است با)
    x = 2
    print('Ran func(), changed global x to', x)  # خروجی: Ran func(), changed global x to 2 (ترجمه: func() اجرا شد، x سراسری به 2 تغییر کرد)

print('Before calling func(), x is:', x)  # خروجی: Before calling func(), x is: 50 (ترجمه: قبل از فراخوانی func()، x برابر است با)
func()
print('Value of x (outside of func()) is:', x)  # خروجی: Value of x (outside of func()) is: 2 (ترجمه: مقدار x (خارج از func()) برابر است با)
"""
تحلیل مثال:
با استفاده از دستور global x، اعلام می‌کنیم که x یک متغیر سراسری است.
بنابراین، وقتی مقدار x را درون تابع تغییر می‌دهیم، این تغییر در بلوک اصلی نیز منعکس می‌شود.
نکات مهم درباره دستور global:
می‌توانید چندین متغیر سراسری را با یک دستور global مشخص کنید، مثلاً: global x, y, z.
استفاده از global معمولاً توصیه نمی‌شود چون خوانایی کد را کاهش می‌دهد و به راحتی نمی‌توان فهمید که این متغیر از کجا تعریف شده است.
از global فقط زمانی استفاده کنید که واقعاً نیاز به تغییر یک متغیر سراسری درون تابع دارید.
"""

# Multiple global variables (چندین متغیر سراسری)
a = 10
b = 20

def modify_globals():
    global a, b  # Declare multiple globals (اعلام چندین متغیر سراسری)
    a = 100
    b = 200

print("Before modification - a:", a, "b:", b)  # خروجی: Before modification - a: 10 b: 20 (ترجمه: قبل از تغییر - a و b)
modify_globals()
print("After modification - a:", a, "b:", b)  # خروجی: After modification - a: 100 b: 200 (ترجمه: بعد از تغییر - a و b)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
وقتی یک تابع درون یک تابع دیگر تعریف می‌شود (توابع تو در تو)، حوزه‌های مختلفی ایجاد می‌شوند
 که پایتون بر اساس قانون LEGB از آن‌ها استفاده می‌کند.
"""
# Example of nested scopes (مثال حوزه‌های تو در تو)
x = 'global x'


def outer ( ) :
    x = 'outer x'

    def inner ( ) :
        x = 'inner x'
        print ( 'inner x:' , x )  # خروجی: inner x: inner x (ترجمه: x داخلی)

    inner ( )
    print ( 'outer x:' , x )  # خروجی: outer x: outer x (ترجمه: x خارجی)


outer ( )
print ( 'global x:' , x )  # خروجی: global x: global x (ترجمه: x سراسری)


# Using nonlocal to access enclosing scope (استفاده از nonlocal برای دسترسی به حوزه دربرگیرنده)
def outer ( ) :
    x = 'outer x'

    def inner ( ) :
        nonlocal x  # Access variable from enclosing scope (دسترسی به متغیر از حوزه دربرگیرنده)
        x = 'modified outer x'
        print ( 'inner modified x:' , x )  # خروجی: inner modified x: modified outer x (ترجمه: x داخلی تغییر یافته)

    inner ( )
    print ( 'outer x after inner:' , x )  # خروجی: outer x after inner: modified outer x (ترجمه: x خارجی بعد از داخلی)


outer ( )

"""
نکات مهم درباره حوزه‌های تو در تو:
دستور nonlocal به شما امکان می‌دهد به متغیرهایی در حوزه توابع دربرگیرنده دسترسی پیدا کنید.
nonlocal فقط برای حوزه‌های دربرگیرنده کار می‌کند، نه برای حوزه سراسری (global).
اگر متغیری با استفاده از nonlocal اعلام شود، نمی‌تواند در حوزه سراسری تعریف شده باشد.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
شما می‌توانید از توابع globals() و locals() برای بررسی متغیرهای فعلی محلی و سراسری استفاده کنید.
"""
# Example of globals() and locals() (مثال globals() و locals())
x = 10
y = 20


def test_scope ( ) :
    a = 30
    b = 40

    print ( "Local variables:" , locals ( ) )  # خروجی: Local variables: {'a': 30, 'b': 40, ...} (ترجمه: متغیرهای محلی)
    print (
        "Global variables:" , globals ( )
        )  # خروجی: Global variables: {..., 'x': 10, 'y': 20, ...} (ترجمه: متغیرهای سراسری)


test_scope ( )

"""
نکات مهم درباره globals() و locals():
locals() دیکشنری‌ای از تمام متغیرهای محلی در حوزه فعلی را برمی‌گرداند.
globals() دیکشنری‌ای از تمام متغیرهای سراسری در ماژول فعلی را برمی‌گرداند.
این توابع برای دیباگ کردن و بررسی حوزه‌ها بسیار مفید هستند.
"""

# Advanced example of scope checking (مثال پیشرفته‌تر بررسی حوزه)
x = 'global'


def outer ( ) :
    x = 'outer'

    def inner ( ) :
        x = 'inner'
        print (
            "Inner locals:" , list ( locals ( ).keys ( ) )
            )  # خروجی: Inner locals: ['x'] (ترجمه: کلیدهای محلی داخلی)
        print ( "Inner x:" , x )  # خروجی: Inner x: inner (ترجمه: x داخلی)

    inner ( )
    print (
        "Outer locals:" , list ( locals ( ).keys ( ) )
        )  # خروجی: Outer locals: ['x', 'inner'] (ترجمه: کلیدهای محلی خارجی)
    print ( "Outer x:" , x )  # خروجی: Outer x: outer (ترجمه: x خارجی)


outer ( )
print (
    "Global keys:" , list ( globals ( ).keys ( ) ) [ -5 : ]
    )  # خروجی: Global keys: [..., 'x', 'outer', ...] (ترجمه: کلیدهای سراسری)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
نکته آخر این است که همه چیز در پایتون یک شیء است! می‌توانید متغیرها را به توابع اختصاص دهید، دقیقاً مانند اعداد!
"""
# Functions are objects too (توابع هم شیء هستند)
def greet():
    return "Hello!"

# Assign function to a variable (اختصاص تابع به یک متغیر)
my_greeting = greet

# Call the function through the variable (فراخوانی تابع از طریق متغیر)
print("Function call via variable:", my_greeting())  # خروجی: Function call via variable: Hello! (ترجمه: فراخوانی تابع از طریق متغیر)

# Check if they are the same object (بررسی اینکه آیا آن‌ها یک شیء هستند)
print("Are greet and my_greeting the same?", greet is my_greeting)  # خروجی: Are greet and my_greeting the same? True (ترجمه: آیا greet و my_greeting یکی هستند؟)


# More complex example with nested functions (مثال پیچیده‌تر با توابع تو در تو)
def create_multiplier(factor):
    """Returns a function that multiplies by the given factor.
    (بازگرداندن تابعی که در عامل داده شده ضرب می‌کند)"""
    def multiplier(x):
        return x * factor
    return multiplier

# Create specific multiplier functions (ایجاد توابع ضرب‌کننده خاص)
double = create_multiplier(2)
triple = create_multiplier(3)

print("Double of 5:", double(5))  # خروجی: Double of 5: 10 (ترجمه: دوبرابر 5)
print("Triple of 5:", triple(5))  # خروجی: Triple of 5: 15 (ترجمه: سه برابر 5)

"""
نکته مهم:
توابع در پایتون شیء هستند و می‌توانند به عنوان ورودی به توابع دیگر ارسال شوند یا توسط متغیرها ارجاع داده شوند.
این ویژگی اساس بسیاری از مفاهیم پیشرفته در پایتون مانند دکوراتورها (Decorators) است.
"""

"""
نکته کلیدی:

پایتون از قانون LEGB برای تعیین حوزه متغیرها استفاده می‌کند.
متغیرهای محلی فقط در تابع خودشان قابل دسترسی هستند.
برای دسترسی به متغیرهای سراسری درون تابع از دستور global استفاده کنید.
برای دسترسی به متغیرهای حوزه‌های دربرگیرنده از دستور nonlocal استفاده کنید.
از توابع globals() و locals() برای بررسی حوزه‌ها استفاده کنید.
همه چیز در پایتون یک شیء است، از جمله توابع!
"""
