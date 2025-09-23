"""
تاپل‌ها (Tuples) در پایتون ساختارهای داده‌ای هستند که بسیار شبیه به لیست‌ها عمل می‌کنند،
 اما تفاوت اصلی آن‌ها این است که تاپل‌ها تغییرناپذیر (Immutable) هستند، یعنی پس از ایجاد، نمی‌توان محتوای آن‌ها را تغییر داد.
 این ویژگی باعث می‌شود تاپل‌ها برای ذخیره داده‌هایی که نباید تغییر کنند (مانند روزهای هفته یا تاریخ‌های ثابت در تقویم) مناسب باشند.
"""
# Create a simple tuple (ایجاد یک تاپل ساده)
t = (1, 2, 3)
print("Simple tuple:", t)  # خروجی: Simple tuple: (1, 2, 3) (ترجمه: تاپل ساده)

# Tuple with mixed data types (تاپل با انواع داده‌های مختلف)
mixed_tuple = ('one', 2, 3.14, True)
print("Mixed data types tuple:", mixed_tuple)
# خروجی: Mixed data types tuple: ('one', 2, 3.14, True) (ترجمه: تاپل با انواع داده‌های مختلف)

# Empty tuple (تاپل خالی)
empty_tuple = ()
print("Empty tuple:", empty_tuple)  # خروجی: Empty tuple: () (ترجمه: تاپل خالی)

# Single element tuple (تاپل با یک عنصر - توجه به ویرگول)
single_element_tuple = (42,)
print("Single element tuple:", single_element_tuple)
# خروجی: Single element tuple: (42,) (ترجمه: تاپل با یک عنصر - توجه به ویرگول)

"""
برای ایجاد تاپل با یک عنصر، حتماً از ویرگول بعد از عنصر استفاده کنید،
 در غیر این صورت پایتون آن را به عنوان پرانتز معمولی تفسیر می‌کند.
تاپل‌ها با استفاده از پرانتز () و ویرگول برای جدا کردن عناصر ایجاد می‌شوند.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
روش‌های مختلفی برای ساخت تاپل‌ها وجود دارد
"""
# Create tuple using parentheses (ساخت تاپل با استفاده از پرانتز)
t1 = (1, 2, 3)
print("Tuple with parentheses:", t1)  # خروجی: Tuple with parentheses: (1, 2, 3) (ترجمه: تاپل با پرانتز)

# Create tuple without parentheses (ساخت تاپل بدون پرانتز - روش مجاز)
t2 = 1, 2, 3
print("Tuple without parentheses:", t2)  # خروجی: Tuple without parentheses: (1, 2, 3) (ترجمه: تاپل بدون پرانتز)

# Create tuple from list (ساخت تاپل از لیست)
list_to_tuple = tuple([4, 5, 6])
print("Tuple from list:", list_to_tuple)  # خروجی: Tuple from list: (4, 5, 6) (ترجمه: تاپل از لیست)

# Check length of tuple (بررسی طول تاپل)
print("Length of tuple:", len(t1))  # خروجی: Length of tuple: 3 (ترجمه: طول تاپل)

# Indexing in tuple (ایندکس‌گیری در تاپل)
print("First element of tuple:", t1[0])  # خروجی: First element of tuple: 1 (ترجمه: اولین عنصر تاپل)

# Slicing in tuple (برش در تاپل)
print("Last two elements:", t1[1:])  # خروجی: Last two elements: (2, 3) (ترجمه: دو عنصر آخر)
print("Reverse tuple:", t1[::-1])    # خروجی: Reverse tuple: (3, 2, 1) (ترجمه: معکوس کردن تاپل)

"""
ایندکس‌گیری و برش در تاپل‌ها دقیقاً مانند لیست‌ها کار می‌کند.
تاپل‌ها می‌توانند انواع مختلفی از داده‌ها را در خود نگه دارند (اعداد، رشته‌ها، مقادیر بولی و ...).
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
تاپل‌ها متدهای کمتری نسبت به لیست‌ها دارند، اما چند متد پرکاربرد دارند
"""
# Create a sample tuple (ایجاد یک تاپل نمونه)
t = ('one', 2, 'one', 'two', 'three')

# index() method: Find position of first occurrence (متد index(): یافتن موقعیت اولین تکرار)
print("Index of 'one':", t.index('one'))  # خروجی: Index of 'one': 0 (ترجمه: ایندکس 'one')

# count() method: Count occurrences of a value (متد count(): شمارش تکرار یک مقدار)
print("Count of 'one':", t.count('one'))  # خروجی: Count of 'one': 2 (ترجمه: تعداد تکرار 'one')

# Attempting to use unsupported method (تلاش برای استفاده از متد پشتیبانی نشده)
try:
    t.append('four')  # تاپل‌ها متد append ندارند
except AttributeError as e:
    print("Error when trying to append:", str(e))
    # خروجی: Error when trying to append: 'tuple' object has no attribute 'append' (ترجمه: خطا هنگام استفاده از append)

"""
index(value): ایندکس اولین تکرار مقدار مشخص شده را برمی‌گرداند. اگر مقدار پیدا نشود، خطا می‌دهد.
count(value): تعداد تکرار مقدار مشخص شده را برمی‌گرداند.
تاپل‌ها هیچ متد تغییردهنده‌ای (مانند append(), pop(), insert()) ندارند، چون تغییرناپذیر هستند.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
عدم تغییرپذیری (Immutability)
ویژگی اصلی تاپل‌ها تغییرناپذیری است. پس از ایجاد یک تاپل، نمی‌توان محتوای آن را تغییر داد:
"""
# Create a tuple (ایجاد یک تاپل)
t = ('one', 2, 3)

# Attempt to change an element (تلاش برای تغییر یک عنصر)
try:
    t[0] = 'change'
except TypeError as e:
    print("Error when trying to change element:", str(e))
    # خروجی: Error when trying to change element: 'tuple' object does not support item assignment (ترجمه: خطا هنگام تغییر عنصر)

# Attempt to append to tuple (تلاش برای افزودن به تاپل)
try:
    t.append('nope')
except AttributeError as e:
    print("Error when trying to append:", str(e))
    # خروجی: Error when trying to append: 'tuple' object has no attribute 'append' (ترجمه: خطا هنگام افزودن به تاپل)

# Attempt to delete element (تلاش برای حذف عنصر)
try:
    del t[0]
except TypeError as e:
    print("Error when trying to delete element:", str(e))
    # خروجی: Error when trying to delete element: 'tuple' object doesn't support item deletion (ترجمه: خطا هنگام حذف عنصر)

"""
چرا تغییرناپذیری مهم است؟
سلامت داده‌ها: اطمینان حاصل می‌کنید که داده‌ها در طول اجرای برنامه تغییر نمی‌کنند.
کارایی بیشتر: تاپل‌ها از نظر حافظه بهینه‌تر از لیست‌ها هستند.
قابلیت استفاده به عنوان کلید در دیکشنری: فقط اشیاء تغییرناپذیر می‌توانند کلید دیکشنری باشند.
"""

# Tuples can be dictionary keys (تاپل‌ها می‌توانند کلید دیکشنری باشند)
coordinates = {(0, 0): "Origin", (1, 2): "Point A", (3, 4): "Point B"}
print("Dictionary with tuple keys:", coordinates)
# خروجی: Dictionary with tuple keys: {(0, 0): 'Origin', (1, 2): 'Point A', (3, 4): 'Point B'} (ترجمه: دیکشنری با کلیدهای تاپل)

# Lists cannot be dictionary keys (لیست‌ها نمی‌توانند کلید دیکشنری باشند)
try:
    invalid_dict = {[0, 0]: "Error"}
except TypeError as e:
    print("Error with list as key:", str(e))
    # خروجی: Error with list as key: unhashable type: 'list' (ترجمه: خطا با لیست به عنوان کلید)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
زمان استفاده از تاپل‌ها (When to Use Tuples)
با وجود اینکه تاپل‌ها متدهای کمتری نسبت به لیست‌ها دارند، در موارد خاصی بسیار مفید هستند
"""

"""
داده‌های ثابت
وقتی می‌خواهید اطمینان حاصل کنید که داده‌ها تغییر نمی‌کنند
"""
# Days of the week (روزهای هفته - داده‌های ثابت)
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print("Days of week:", DAYS_OF_WEEK)
# خروجی: Days of week: ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') (ترجمه: روزهای هفته)

"""
بازگرداندن چند مقدار از تابع
تاپل‌ها به راحتی می‌توانند چند مقدار را به عنوان خروجی تابع برگردانند
"""
# Function returning multiple values (تابعی که چند مقدار برمی‌گرداند)
def get_min_max(numbers):
    return min(numbers), max(numbers)  # بازگرداندن یک تاپل

numbers = [1, 2, 3, 4, 5]
min_val, max_val = get_min_max(numbers)
print("Min value:", min_val)  # خروجی: Min value: 1 (ترجمه: مقدار مینیمم)
print("Max value:", max_val)  # خروجی: Max value: 5 (ترجمه: مقدار ماکسیمم)

"""
عملکرد بهتر در زمان اجرا
تاپل‌ها از نظر حافظه بهینه‌تر از لیست‌ها هستند
"""
import sys

# Compare memory usage (مقایسه مصرف حافظه)
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)

print("List memory size:", sys.getsizeof(list_example))
# خروجی: List memory size: 120 (ترجمه: حجم حافظه لیست)
print("Tuple memory size:", sys.getsizeof(tuple_example))
# خروجی: Tuple memory size: 80 (ترجمه: حجم حافظه تاپل)

"""
کلیدهای دیکشنری
همانطور که قبلاً دیدیم، تاپل‌ها می‌توانند کلید دیکشنری باشند
"""
# Using tuple as dictionary key (استفاده از تاپل به عنوان کلید دیکشنری)
location_data = {
    ('Tehran', 'Iran'): 15000000,
    ('New York', 'USA'): 8500000,
    ('Tokyo', 'Japan'): 14000000
}

print("Population of Tehran:", location_data[('Tehran', 'Iran')])
# خروجی: Population of Tehran: 15000000 (ترجمه: جمعیت تهران)

"""
نکته کلیدی:

از تاپل‌ها برای داده‌های ثابت و غیر قابل تغییر استفاده کنید.
تاپل‌ها عملکرد بهتری از نظر حافظه نسبت به لیست‌ها دارند.
تاپل‌ها می‌توانند به عنوان کلید در دیکشنری استفاده شوند.
برای توابعی که نیاز به بازگرداندن چند مقدار دارند، تاپل‌ها انتخاب خوبی هستند.
"""
