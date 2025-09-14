"""
ایجاد و بررسی تاپل‌ها (Constructing Tuples)
تاپل‌ها با استفاده از پرانتز () و جدا کردن عناصر با کاما ایجاد می‌شوند.
"""
print("--- ایجاد تاپل‌ها ---")

# ایجاد یک تاپل از اعداد
my_tuple_numbers = (1, 2, 3)
print("تاپل اعداد: ", my_tuple_numbers)  # خروجی: (1, 2, 3)

# بررسی طول تاپل — مشابه لیست‌ها
print("طول تاپل اعداد: ", len(my_tuple_numbers))  # خروجی: 3

# تاپل با انواع مختلف داده
my_mixed_tuple = ('one', 2, True, 3.14)
print("تاپل با انواع مختلف داده: ", my_mixed_tuple)  # خروجی: ('one', 2, True, 3.14)

# تاپل تک عضوی — توجه به کاما ضروری است!
single_element_tuple = (42,)  # تاپل تک عضوی
not_a_tuple = (42)       # این یک عدد است، نه تاپل
print("تاپل تک عضوی: ", single_element_tuple)  # خروجی: (42,)
print("نوع متغیر not_a_tuple (عدد است، نه تاپل): ", type(not_a_tuple))  # خروجی: <class 'int'>

# ایجاد تاپل بدون پرانتز — با استفاده از کاما
my_tuple_no_parentheses = 'a', 'b', 'c'
print("تاپل بدون پرانتز: ", my_tuple_no_parentheses)  # خروجی: ('a', 'b', 'c')
print("نوع متغیر: ", type(my_tuple_no_parentheses))  # خروجی: <class 'tuple'>

# ***********************************************************************************************
"""
اندیس‌گذاری و برش در تاپل‌ها (Indexing & Slicing)
تاپل‌ها، دنباله‌ای (sequence) از عناصر هستند، بنابراین می‌توان از اندیس‌گذاری و برش در آن‌ها استفاده کرد.
"""
print("\n--- اندیس‌گذاری و برش در تاپل‌ها ---")

my_indexing_tuple = ('zero', 'one', 'two', 'three', 'four')

# اندیس‌گذاری — شروع از صفر
print("عنصر اول (اندیس 0): ", my_indexing_tuple[0])     # خروجی: zero
print("عنصر دوم (اندیس 1): ", my_indexing_tuple[1])     # خروجی: one
print("عنصر آخر (اندیس -1): ", my_indexing_tuple[-1])   # خروجی: four (آخرین عنصر)

# برش تاپل — مشابه لیست‌ها
print("برش از اندیس 1 تا انتها: ", my_indexing_tuple[1:])     # خروجی: ('one', 'two', 'three', 'four')
print("برش از ابتدا تا اندیس 3 (غیر از 3): ", my_indexing_tuple[:3])     # خروجی: ('zero', 'one', 'two')
print("برش از اندیس 1 تا 4 (غیر از 4): ", my_indexing_tuple[1:4])   # خروجی: ('one', 'two', 'three')
print("برش معکوس (وارونه): ", my_indexing_tuple[::-1]) # خروجی: ('four', 'three', 'two', 'one', 'zero')

# ***************************************************************************************
"""
متدهای مهم تاپل‌ها (Basic Tuple Methods)
تاپل‌ها متدهای کمتری نسبت به لیست‌ها دارند، اما چند متد پرکاربرد مهم دارند:
.index(value) - اندیس اولین رخداد مقدار مشخص را برمی‌گرداند
.count(value) - تعداد تکرار مقدار مشخص را برمی‌گرداند
"""
print("\n--- متدهای مهم تاپل‌ها ---")

my_fruit_tuple = ('apple', 'banana', 'apple', 'cherry', 'apple')

# .index() — پیدا کردن اندیس اولین رخداد
print("اندیس اولین 'apple': ", my_fruit_tuple.index('apple'))  # خروجی: 0
print("اندیس 'cherry': ", my_fruit_tuple.index('cherry'))  # خروجی: 3

# .count() — شمارش تعداد تکرار یک مقدار
print("تعداد 'apple': ", my_fruit_tuple.count('apple'))  # خروجی: 3
print("تعداد 'banana': ", my_fruit_tuple.count('banana'))  # خروجی: 1

# *****************************************************************************************************
"""
تغییرناپذیری (Immutability) و اهمیت آن
🔹 چرا تغییرناپذیری مهم است؟
تغییرناپذیری یعنی پس از ایجاد یک تاپل، نمی‌توانید محتوای آن را تغییر دهید. این ویژگی مزایای مهمی دارد:
سلامت داده‌ها (Data Integrity): اطمینان از اینکه داده‌ها در طول اجرای برنامه تغییر نمی‌کنند.
کارایی بهتر: تاپل‌ها معمولاً از لیست‌ها سریع‌تر هستند و حافظه کمتری مصرف می‌کنند.
قابلیت استفاده به عنوان کلید در دیکشنری: فقط اشیاء تغییرناپذیر می‌توانند کلید دیکشنری باشند.
"""
print("\n--- تغییرناپذیری ---")

immutable_tuple = ('one', 2, 3.14)

# تلاش برای تغییر یک عنصر — باعث خطا می‌شود
try:
    immutable_tuple[0] = 'change'
except TypeError as e:
    print("خطا در تغییر عنصر: ", e)  # خروجی: 'tuple' object does not support item assignment

# تلاش برای افزودن عنصر — باعث خطا می‌شود
try:
    immutable_tuple.append('nope')
except AttributeError as e:
    print("خطا در افزودن عنصر: ", e)  # خروجی: 'tuple' object has no attribute 'append'

# تلاش برای حذف عنصر — باعث خطا می‌شود
try:
    del immutable_tuple[0]
except TypeError as e:
    print("خطا در حذف عنصر: ", e)  # خروجی: 'tuple' object doesn't support item deletion

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
 راه‌حل برای "تغییر" تاپل
اگر واقعاً نیاز به تغییر تاپل دارید، باید یک تاپل جدید ایجاد کنید
"""
print("\n--- راه‌حل برای 'تغییر' تاپل ---")

original_tuple = (1, 2, 3)
# تبدیل تاپل به لیست، تغییر، و بازگشت به تاپل
temp_list = list(original_tuple)
temp_list[0] = 'changed'
new_tuple = tuple(temp_list)
print("تاپل اصلی: ", original_tuple)  # خروجی: (1, 2, 3)
print("تاپل جدید (پس از تغییر): ", new_tuple)  # خروجی: ('changed', 2, 3)

# ********************************************************************************
"""
مقایسه لیست و تاپل
"""
print("\n--- مقایسه لیست و تاپل ---")

import sys
import timeit

# مقایسه مصرف حافظه
list_example = [1, 2, 3, 'a', 'b', 'c']
tuple_example = (1, 2, 3, 'a', 'b', 'c')
print("مصرف حافظه لیست (بایت): ", sys.getsizeof(list_example))
print("مصرف حافظه تاپل (بایت): ", sys.getsizeof(tuple_example))

# مقایسه سرعت
list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print(f"زمان ساخت لیست (ثانیه): {list_time:.6f}")
print(f"زمان ساخت تاپل (ثانیه): {tuple_time:.6f}")

# ********************************************************************************
"""
 زمان‌های مناسب استفاده از تاپل‌ها :
"""
print("\n--- زمان‌های مناسب استفاده از تاپل‌ها ---")

# داده‌های ثابت و غیرقابل تغییر
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print("روزهای هفته (تاپل ثابت): ", DAYS_OF_WEEK)

# کلیدهای دیکشنری
location = {(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"}
print("دیکشنری با کلیدهای تاپل: ", location)

# بازگشت چند مقدار از توابع
def get_user_info():
    return "Ali", 25, "Tehran"

name, age, city = get_user_info()
print(f"اطلاعات کاربر از تابع: نام: {name}, سن: {age}, شهر: {city}")

# حفاظت از داده‌ها در طول اجرای برنامه
CONFIG = ('production', 'https://api.example.com', 8080)
print("پیکربندی (تاپل ثابت): ", CONFIG)

# داده‌هایی که نباید تغییر کنند
RGB_COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}
print("رنگ‌های RGB (مقادیر تاپل): ", RGB_COLORS)

# ********************************************************************************
"""
کاربردهای عملی و پیشرفته تاپل‌ها
"""
print("\n--- کاربردهای عملی و پیشرفته تاپل‌ها ---")

# بسته‌بندی و باز کردن تاپل‌ها (Tuple Packing & Unpacking)
# بسته‌بندی — ایجاد تاپل بدون پرانتز
packed_tuple = 1, 2, 3
print("تاپل بسته‌بندی شده: ", packed_tuple)  # خروجی: (1, 2, 3)

# باز کردن — تخصیص به متغیرها
a, b, c = packed_tuple
print(f"متغیرهای باز شده: a = {a}, b = {b}, c = {c}")  # خروجی: a = 1 b = 2 c = 3

# باز کردن جزئی با استفاده از *
first, *rest = (1, 2, 3, 4, 5)
print(f"متغیر اول: {first}")  # خروجی: 1
print(f"بقیه عناصر: {rest}")    # خروجی: [2, 3, 4, 5]

# باز کردن برای تبادل مقادیر — بدون نیاز به متغیر موقت
x = 10
y = 20
x, y = y, x
print(f"مقادیر بعد از جابجایی: x = {x}, y = {y}")  # خروجی: x = 20 y = 10

# استفاده در حلقه‌ها
# استفاده در حلقه‌های for
coordinates = [(1, 2), (3, 4), (5, 6)]
print("استفاده از تاپل در حلقه for:")
for x, y in coordinates:
    print(f"  نقطه: ({x}, {y})")

# استفاده با enumerate
names = ['Ali', 'Reza', 'Sara']
print("استفاده از enumerate:")
for i, name in enumerate(names):
    print(f"  {i+1}. {name}")

# تبدیل بین لیست و تاپل
# تبدیل لیست به تاپل
my_list_to_convert = [1, 2, 3]
converted_tuple = tuple(my_list_to_convert)
print("لیست به تاپل تبدیل شد: ", converted_tuple)  # خروجی: (1, 2, 3)

# تبدیل تاپل به لیست
my_tuple_to_convert = ('a', 'b', 'c')
converted_list = list(my_tuple_to_convert)
print("تاپل به لیست تبدیل شد: ", converted_list)  # خروجی: ['a', 'b', 'c']

# تاپل‌های تو در تو
# ایجاد تاپل‌های تو در تو
nested_tuple = (1, (2, 3), (4, (5, 6)))
print("تاپل تو در تو: ", nested_tuple)
print("عنصر nested[1]: ", nested_tuple[1])        # خروجی: (2, 3)
print("عنصر nested[1][0]: ", nested_tuple[1][0])  # خروجی: 2
print("عنصر nested[2][1][0]: ", nested_tuple[2][1][0])  # خروجی: 5

# استفاده در توابع
# تابعی که چند مقدار برمی‌گرداند
def min_max(numbers):
    return min(numbers), max(numbers)

data = [3, 1, 4, 1, 5, 9, 2, 6]
min_val, max_val = min_max(data)
print(f"حداقل و حداکثر از تابع: Min: {min_val}, Max: {max_val}")  # خروجی: Min: 1, Max: 9

# ********************************************************************************
"""
مجموعه‌ها (Sets)
🔹 تعریف و ویژگی‌های اصلی
مجموعه‌ها (Sets) یک ساختار داده غیرترتیبی و بدون عناصر تکراری هستند.
 این ویژگی‌ها آن‌ها را برای موارد خاصی بسیار مناسب می‌کند.
ویژگی‌های کلیدی:
عدم ترتیب: عناصر در مجموعه‌ها ترتیب خاصی ندارند
عدم تکرار: هر عنصر فقط یک بار در مجموعه وجود دارد
عناصر قابل هش: عناصر مجموعه‌ها باید غیرقابل تغییر (immutable) باشند (مثل int, str, tuple)
سرعت بالا: عملیات عضویت (in) در مجموعه‌ها بسیار سریع‌تر از لیست‌ها است
"""
print("\n--- مجموعه‌ها (Sets) ---")

# روش‌های ایجاد مجموعه:
# روش 1: استفاده از تابع set()
my_set = set()
print("مجموعه خالی (با set()): ", my_set)  # خروجی: set()

# افزودن عناصر با متد add()
my_set.add(1)
my_set.add(2)
print("مجموعه بعد از افزودن عناصر: ", my_set)  # خروجی: {1, 2}

# روش 2: استفاده از آکولاد {}
my_set2 = {1, 2, 3}
print("مجموعه با {}: ", my_set2)  # خروجی: {1, 2, 3}

# روش 3: تبدیل لیست به مجموعه (برای حذف عناصر تکراری)
list_with_duplicates = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]
unique_set_from_list = set(list_with_duplicates)
print("مجموعه از لیست (حذف تکراری‌ها): ", unique_set_from_list)  # خروجی: {1, 2, 3, 4, 5, 6}

# روش 4: تبدیل رشته به مجموعه
char_set_from_string = set("hello")
print("مجموعه از کاراکترهای رشته: ", char_set_from_string)  # خروجی: {'l', 'o', 'e', 'h'} (ترتیب تضمین نشده)

# ********************************************************************************
"""
متدهای مهم مجموعه‌ها
"""
print("\n--- متدهای مهم مجموعه‌ها ---")

# ایجاد مجموعه‌ها
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# اجتماع (union)
print("اجتماع set1 و set2 (union): ", set1.union(set2))  # خروجی: {1, 2, 3, 4, 5}
print("اجتماع set1 و set2 (|): ", set1 | set2)  # همان اجتماع با عملگر |

# اشتراک (intersection)
print("اشتراک set1 و set2 (intersection): ", set1.intersection(set2))  # خروجی: {3}
print("اشتراک set1 و set2 (&): ", set1 & set2)  # همان اشتراک با عملگر &

# تفاضل (difference)
print("تفاضل set1 - set2 (difference): ", set1.difference(set2))  # خروجی: {1, 2}
print("تفاضل set1 - set2 (-): ", set1 - set2)  # همان تفاضل با عملگر -

# تفاضل متقارن (symmetric difference)
print("تفاضل متقارن set1 و set2 (symmetric_difference): ", set1.symmetric_difference(set2))  # خروجی: {1, 2, 4, 5}
print("تفاضل متقارن set1 و set2 (^): ", set1 ^ set2)  # همان تفاضل متقارن با عملگر ^

# زیرمجموعه و ابرمجموعه
set3 = {1, 2}
print("آیا set3 زیرمجموعه set1 است؟ (issubset): ", set3.issubset(set1))  # خروجی: True
print("آیا set1 ابرمجموعه set3 است؟ (issuperset): ", set1.issuperset(set3))  # خروجی: True

# ********************************************************************************
"""
مجموعه‌های غیرقابل تغییر (frozenset)
frozenset نوعی از مجموعه است که غیرقابل تغییر (immutable) است.
"""
print("\n--- مجموعه‌های غیرقابل تغییر (frozenset) ---")

my_frozen_set = frozenset([1, 2, 3, 2]) # تکراری حذف می‌شود
print("frozenset: ", my_frozen_set) # خروجی: frozenset({1, 2, 3})

# ********************************************************************************
"""
کاربردهای عملی مجموعه‌ها
"""
print("\n--- کاربردهای عملی مجموعه‌ها ---")

# حذف عناصر تکراری از لیست:
unique_items_list = list(set([1, 2, 2, 3, 4, 4, 5]))
print("حذف تکراری‌ها از لیست: ", unique_items_list)  # خروجی: [1, 2, 3, 4, 5] (ترتیب ممکن است متفاوت باشد)

# مقایسه لیست‌ها برای یافتن عناصر مشترک:
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
common_elements = set(list_a) & set(list_b)
print("عناصر مشترک دو لیست: ", common_elements)  # خروجی: {3, 4}

# یافتن عناصر منحصر به فرد در یک متن
text = "hello world hello python world"
unique_words_in_text = set(text.split())
print("کلمات منحصر به فرد در متن: ", unique_words_in_text)  # خروجی: {'hello', 'world', 'python'}

# بررسی عضویت سریع
# بررسی سریع عضویت در مجموعه در مقابل لیست
import timeit
# ایجاد لیست و مجموعه بزرگ
large_list = list(range(10000))
large_set = set(large_list)
# زمان بررسی عضویت در لیست
list_membership_time = timeit.timeit('9999 in large_list', globals=globals(), number=1000)
# زمان بررسی عضویت در مجموعه
set_membership_time = timeit.timeit('9999 in large_set', globals=globals(), number=1000)
print(f"زمان بررسی عضویت در لیست (ثانیه): {list_membership_time:.6f}")
print(f"زمان بررسی عضویت در مجموعه (ثانیه): {set_membership_time:.6f}")

# *******************************************************************************
"""
مقادیر بولین (Booleans) و None
🔹 تعریف و ویژگی‌های اصلی
مقادیر بولین تنها دو مقدار دارند: True و False.
این مقادیر برای ارزیابی شرایط و تصمیم‌گیری در برنامه‌ها استفاده می‌شوند.
"""
print("\n--- مقادیر بولین (Booleans) و None ---")

# ایجاد مقادیر بولین
# روش 1: استفاده مستقیم از True و False
a_bool = True
b_bool = False
print(f"مقادیر بولین: a = {a_bool}, b = {b_bool}")  # خروجی: a = True b = False

# روش 2: استفاده از عملگرهای مقایسه‌ای
x_val = 5
y_val = 10
print(f"{x_val} > {y_val} = {x_val > y_val}")  # خروجی: False
print(f"{x_val} < {y_val} = {x_val < y_val}")  # خروجی: True
print(f"{x_val} == {y_val} = {x_val == y_val}")  # خروجی: False
print(f"{x_val} != {y_val} = {x_val != y_val}")  # خروجی: True

# روش 3: استفاده از عملگرهای منطقی
print(f"True and False = {True and False}")  # خروجی: False
print(f"True or False = {True or False}")  # خروجی: True
print(f"not True = {not True}")  # خروجی: False

# ********************************************************************************
"""
مقادیر پیش‌فرض بولین برای انواع داده
"""
print("\n--- مقادیر پیش‌فرض بولین برای انواع داده ---")

# تست مقادیر بولین برای انواع داده
print(f"bool(0) = {bool(0)}")  # خروجی: False
print(f"bool(42) = {bool(42)}")  # خروجی: True
print(f"bool('') = {bool('')}")  # خروجی: False
print(f"bool('hello') = {bool('hello')}")  # خروجی: True
print(f"bool([]) = {bool([])}")  # خروجی: False
print(f"bool([1, 2, 3]) = {bool([1, 2, 3])}")  # خروجی: True
print(f"bool({{}}) = {bool({})}")  # خروجی: False
print(f"bool({{'a': 1}}) = {bool({'a': 1})}")  # خروجی: True
print(f"bool(set()) = {bool(set())}")  # خروجی: False
print(f"bool({{1, 2, 3}}) = {bool({1, 2, 3})}")  # خروجی: True

# ********************************************************************************
"""
عملگرهای منطقی (and, or, not) و Short-circuit evaluation
"""
print("\n--- عملگرهای منطقی و Short-circuit evaluation ---")

# Short-circuit evaluation
def check_value(x):
    print(f"در حال بررسی {x}")
    return x > 5

# در اینجا فقط check_value(10) اجرا می‌شود چون 10 > 5 است و or نیازی به بررسی بیشتر ندارد
print("نتیجه or (check_value(10) or check_value(3)): ")
result1 = check_value(10) or check_value(3)
print(f"Result 1 = {result1}")

# در اینجا فقط check_value(3) اجرا می‌شود چون 3 > 5 نیست و and نیازی به بررسی بیشتر ندارد
print("نتیجه and (check_value(3) and check_value(10)): ")
result2 = check_value(3) and check_value(10)
print(f"Result 2 = {result2}")

# ********************************************************************************
"""
None — نشان‌دهنده "هیچ چیز"
None یک شیء خاص در پایتون است که نشان‌دهنده وجود نداشتن مقدار یا هیچ چیز است.
"""
print("\n--- None ---")

# تعریف متغیر با مقدار None
b_none = None
print(f"متغیر b = {b_none}")  # خروجی: None
print(f"type(b) = {type(b_none)}")  # خروجی: <class 'NoneType'>
print(f"bool(None) = {bool(None)}")  # خروجی: False
print(f"None == False = {None == False}")  # خروجی: False

# استفاده در توابع
def find_item(items, target):
    for item in items:
        if item == target:
            return item
    return None  # نشان‌دهنده عدم یافتن مورد جستجو

result_find = find_item([1, 2, 3], 4)
if result_find is None:
    print("آیتم یافت نشد")
else:
    print("آیتم یافت شد:", result_find)

# برای بررسی None همیشه از is استفاده کنید، نه ==
x_none = None
if x_none is None:  # ✅ درست
    print("x is None (با is)")
if x_none == None:  # ❌ توصیه نمی‌شود
    print("x is None (با ==)")

# ********************************************************************************
"""
کاربردهای بولین و None در برنامه‌نویسی
"""
print("\n--- کاربردهای بولین و None در برنامه‌نویسی ---")

# شرط‌های if/else
age_user = 20
if age_user >= 18:
    print("شما بالغ هستید")
else:
    print("شما نوجوان هستید")

# حلقه‌های while:
print("حلقه while تا 5:")
count_loop = 0
while count_loop < 5:
    print(f"  شمارش: {count_loop}")
    count_loop += 1

# توابع بازگشتی بولین
def is_even(number):
    return number % 2 == 0

print(f"is_even(4) = {is_even(4)}")  # خروجی: True
print(f"is_even(5) = {is_even(5)}")  # خروجی: False

# بررسی وجود داده‌ها
users_dict = {"Ali": 25, "Sara": 30}
def user_exists(name):
    return name in users_dict

print(f"user_exists('Ali') = {user_exists('Ali')}")  # خروجی: True
print(f"user_exists('Reza') = {user_exists('Reza')}")  # خروجی: False

# پرچم‌های کنترلی
is_connected_flag = False

def connect():
    global is_connected_flag
    # کد اتصال به سرور
    is_connected_flag = True

def disconnect():
    global is_connected_flag
    # کد قطع اتصال
    is_connected_flag = False

connect()
print(f"وضعیت اتصال: is_connected = {is_connected_flag}")  # خروجی: True

# ********************************************************************************
"""
چرا کار با فایل‌ها مهم است؟
"""
print("\n--- کار با فایل‌ها ---")

# ********************************************************************************
"""
باز کردن فایل‌ها
 تابع open()
"""
print("\n--- باز کردن فایل‌ها ---")

# ********************************************************************************
"""
 خطاهای رایج در باز کردن فایل:
"""
print("\n--- خطاهای رایج در باز کردن فایل ---")

try:
    # تلاش برای باز کردن فایلی که وجود ندارد
    file_nonexistent = open('nonexistent.txt', 'r')
except FileNotFoundError as e:
    print(f"خطا: {e} - فایل مورد نظر یافت نشد")

try:
    # تلاش برای باز کردن فایل با مسیر اشتباه
    file_wrong_path = open('wrong/path/example.txt', 'r')
except FileNotFoundError as e:
    print(f"خطا: {e} - مسیر فایل اشتباه است")

# ********************************************************************************
"""
مدیریت مسیر فایل
"""
print("\n--- مدیریت مسیر فایل ---")

import os

# گرفتن مسیر فعلی
current_directory = os.getcwd()
print("مسیر فعلی:", current_directory)

# ایجاد مسیر کامل (این بخش نیاز به وجود پوشه 'data' دارد)
# file_path_full = os.path.join(current_directory, 'data', 'example.txt')
# print("مسیر کامل فایل:", file_path_full)

# بررسی وجود فایل (این بخش نیاز به وجود فایل 'test.txt' دارد)
# if os.path.exists(file_path_full):
#     file_to_check = open(file_path_full, 'r')
#     print("فایل وجود دارد و باز شد")
#     file_to_check.close()
# else:
#     print("فایل وجود ندارد")

# ********************************************************************************
"""
متدهای خواندن فایل
"""
print("\n--- متدهای خواندن فایل ---")

# ایجاد یک فایل متنی برای مثال
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('خط اول\n')
    f.write('خط دوم\n')
    f.write('خط سوم\n')

# باز کردن فایل برای خواندن
try:
    file_to_read = open('test.txt', 'r', encoding='utf-8')
    # خواندن تمام محتوای فایل
    content_full = file_to_read.read()
    print("محتوای کامل فایل:")
    print(content_full)
    # توجه: پس از خواندن، مکان‌نما در انتهای فایل قرار می‌گیرد
    # برای خواندن مجدد باید مکان‌نما را به ابتدا برگردانیم
    file_to_read.seek(0)

    # خواندن خط به خط
    line1_read = file_to_read.readline()
    print(f"خط اول: {line1_read.strip()}")  # استفاده از strip() برای حذف \n
    line2_read = file_to_read.readline()
    print(f"خط دوم: {line2_read.strip()}")

    # بازگرداندن مکان‌نما به ابتدا
    file_to_read.seek(0)
    # خواندن تمام خطوط به صورت لیست
    lines_list = file_to_read.readlines()
    print("همه خطوط به صورت لیست:")
    for i, line in enumerate(lines_list, 1):
        print(f"  خط {i}: {line.strip()}")

    # حتماً فایل را ببندید
    file_to_read.close()

except FileNotFoundError:
    print("فایل test.txt برای خواندن یافت نشد.")

# ********************************************************************************
"""
تکرار روی فایل بدون استفاده از readlines()
"""
print("\n--- تکرار روی فایل با حلقه for ---")

# روش بهینه‌تر برای خواندن فایل‌های بزرگ
try:
    with open('test.txt', 'r', encoding='utf-8') as file_for_loop:
        for line in file_for_loop:
            print(f"  خط: {line.strip()}")
except FileNotFoundError:
    print("فایل test.txt برای خواندن با حلقه یافت نشد.")

# ********************************************************************************
"""
 مثال‌های نوشتن در فایل
"""
print("\n--- مثال‌های نوشتن در فایل ---")

# نوشتن در فایل با حالت 'w' (اگر فایل وجود داشته باشد محتوای قبلی پاک می‌شود)
with open('write_example.txt', 'w', encoding='utf-8') as file_write:
    file_write.write('این خط اول است.\n')
    file_write.write('این خط دوم است.\n')
    print("محتوا به فایل نوشته شد")

# خواندن محتوای فایل برای بررسی
try:
    with open('write_example.txt', 'r', encoding='utf-8') as file_read_write:
        print("\nمحتوای فایل بعد از نوشتن:")
        print(file_read_write.read())
except FileNotFoundError:
    print("فایل write_example.txt برای خواندن یافت نشد.")

# استفاده از writelines() برای نوشتن لیستی از خطوط
lines_to_write = ['خط اول\n', 'خط دوم\n', 'خط سوم\n']
with open('writelines_example.txt', 'w', encoding='utf-8') as file_writelines:
    file_writelines.writelines(lines_to_write)
    print("لیست خطوط به فایل نوشته شد")

# خواندن محتوای فایل برای بررسی
try:
    with open('writelines_example.txt', 'r', encoding='utf-8') as file_read_writelines:
        print("\nمحتوای فایل با استفاده از writelines():")
        print(file_read_writelines.read())
except FileNotFoundError:
    print("فایل writelines_example.txt برای خواندن یافت نشد.")

# ********************************************************************************
"""
 نکات مهم درباره نوشتن در فایل
"""
print("\n--- نکات مهم درباره نوشتن در فایل ---")

# ایجاد یک فایل با محتوا
with open('temp.txt', 'w', encoding='utf-8') as f_temp:
    f_temp.write('محتوای اولیه')

# نوشتن مجدد با حالت 'w'
with open('temp.txt', 'w', encoding='utf-8') as f_temp_write:
    f_temp_write.write('محتوای جدید')

# خواندن - فقط محتوای جدید وجود دارد
try:
    with open('temp.txt', 'r', encoding='utf-8') as f_temp_read:
        print(f"محتوای فایل temp.txt: {f_temp_read.read()}")  # خروجی: محتوای جدید
except FileNotFoundError:
    print("فایل temp.txt یافت نشد.")

# ********************************************************************************
"""
 اضافه کردن به فایل‌ها
"""
print("\n--- اضافه کردن به فایل‌ها ---")

# ایجاد یک فایل اولیه
with open('append_example.txt', 'w', encoding='utf-8') as f_append:
    f_append.write('محتوای اولیه\n')

# اضافه کردن به فایل
with open('append_example.txt', 'a', encoding='utf-8') as file_append:
    file_append.write('این خط جدید اضافه شد.\n')
    file_append.write('این هم خط دیگری است.\n')
    print("خطوط جدید اضافه شدند")

# خواندن محتوای فایل برای بررسی
try:
    with open('append_example.txt', 'r', encoding='utf-8') as file_read_append:
        print("\nمحتوای فایل بعد از اضافه کردن:")
        print(file_read_append.read())
except FileNotFoundError:
    print("فایل append_example.txt برای خواندن یافت نشد.")

# ********************************************************************************
"""
مدیریت فایل‌ها با بلاک with
"""
print("\n--- مدیریت فایل‌ها با بلاک with ---")

# خواندن و پردازش فایل
# ایجاد فایل ورودی برای این مثال
with open('data.txt', 'w', encoding='utf-8') as f_data:
    f_data.write('داده 1\n')
    f_data.write('داده 2\n')
    f_data.write('داده 3\n')

try:
    with open('data.txt', 'r', encoding='utf-8') as file_process:
        lines_process = file_process.readlines()
        print("پردازش خطوط فایل data.txt:")
        for line in lines_process:
            processed_line = line.strip().upper()
            print(f"  پردازش شده: {processed_line}")
except FileNotFoundError:
    print("فایل data.txt برای پردازش یافت نشد.")

# نوشتن در فایل با پردازش داده‌ها
input_data_list = ['داده 1', 'داده 2', 'داده 3']
with open('processed_data.txt', 'w', encoding='utf-8') as file_write_processed:
    for item in input_data_list:
        file_write_processed.write(f"پردازش شده: {item}\n")
print("داده‌های پردازش شده به فایل processed_data.txt نوشته شد.")

# کپی کردن محتوای یک فایل به فایل دیگر
# ایجاد فایل منبع برای کپی
with open('source.txt', 'w', encoding='utf-8') as f_src:
    f_src.write('داده منبع خط 1\n')
    f_src.write('داده منبع خط 2\n')

try:
    with open('source.txt', 'r', encoding='utf-8') as src, open('destination.txt', 'w', encoding='utf-8') as dest:
        for line in src:
            dest.write(line.upper())
    print("فایل source.txt به destination.txt کپی و تبدیل به حروف بزرگ شد.")
except FileNotFoundError:
    print("فایل source.txt برای کپی یافت نشد.")

# ********************************************************************************
"""
 فایل‌های متنی (Text Files)
"""
print("\n--- فایل‌های متنی ---")

# خواندن فایل متنی
try:
    with open('text_file.txt', 'r', encoding='utf-8') as file_read_text:
        content_text = file_read_text.read()
        print("محتوای فایل متنی text_file.txt:", content_text)
except FileNotFoundError:
    print("فایل text_file.txt برای خواندن یافت نشد.")

# نوشتن در فایل متنی
with open('text_file.txt', 'w', encoding='utf-8') as file_write_text:
    file_write_text.write('سلام دنیا! این یک فایل فارسی است.')
print("محتوای فارسی به فایل text_file.txt نوشته شد.")

# ********************************************************************************
"""
فایل‌های باینری (Binary Files)
"""
print("\n--- فایل‌های باینری ---")

# کپی کردن یک فایل تصویری (این بخش نیاز به وجود فایل 'source.jpg' دارد)
# try:
#     with open('source.jpg', 'rb') as src_bin, open('destination.jpg', 'wb') as dest_bin:
#         # خواندن و نوشتن به بلوک‌های 4096 بایتی
#         chunk_size_bin = 4096
#         while True:
#             chunk = src_bin.read(chunk_size_bin)
#             if not chunk:
#                 break
#             dest_bin.write(chunk)
#     print("تصویر source.jpg به destination.jpg کپی شد")
# except FileNotFoundError:
#     print("فایل source.jpg برای کپی یافت نشد.")

# خواندن فایل صوتی (این بخش نیاز به وجود فایل 'audio.mp3' دارد)
# try:
#     with open('audio.mp3', 'rb') as file_audio:
#         header_audio = file_audio.read(10)  # خواندن 10 بایت اول
#         print("هدر فایل صوتی (در قالب هگزادسیمال):", header_audio.hex())
# except FileNotFoundError:
#     print("فایل audio.mp3 برای خواندن یافت نشد.")

# ********************************************************************************
"""
 نکات ایمنی و بهترین روش‌ها
"""
print("\n--- نکات ایمنی و بهترین روش‌ها ---")

# مدیریت خطاهای فایل
try:
    with open('critical_file.txt', 'r', encoding='utf-8') as file_critical:
        content_critical = file_critical.read()
except FileNotFoundError:
    print("فایل critical_file.txt پیدا نشد")
except PermissionError:
    print("دسترسی لازم برای خواندن critical_file.txt وجود ندارد")
except Exception as e:
    print(f"خطای ناشناخته در خواندن critical_file.txt: {e}")

# همیشه encoding را مشخص کنید، به خصوص برای فایل‌های غیر انگلیسی
try:
    with open('text_file.txt', 'r', encoding='utf-8') as file_encoding:
        content_encoding = file_encoding.read()
        print("محتوای فایل text_file.txt (با encoding مشخص):", content_encoding)
except FileNotFoundError:
    print("فایل text_file.txt برای خواندن با encoding یافت نشد.")

# برای فایل‌های بسیار بزرگ
# اینجا فقط یک مثال ساختگی است
# def process_line(line):
#     return line.upper()
# try:
#     with open('large_file.txt', 'r', encoding='utf-8') as file_large:
#         for line in file_large:
#             # پردازش هر خط به صورت جداگانه
#             processed_line_large = process_line(line)
#             print(processed_line_large.strip())
# except FileNotFoundError:
#     print("فایل large_file.txt برای پردازش خط به خط یافت نشد.")

# *******************************************************************************
"""
مقدمه‌ای بر عملگرهای مقایسه‌ای
"""
print("\n--- عملگرهای مقایسه‌ای ---")

# ********************************************************************************
"""
عملگرهای مقایسه‌ای
"""
print("\n--- مقایسه‌های ساده ---")

# اعداد
print(f"2 == 2: {2 == 2}")  # خروجی: True
print(f"1 == 0: {1 == 0}")  # خروجی: False

# رشته‌ها
print(f"'hello' == 'hello': {'hello' == 'hello'}")  # خروجی: True
print(f"'Hello' == 'hello': {'Hello' == 'hello'}")  # خروجی: False (حساس به بزرگی و کوچکی حروف)

# لیست‌ها
print(f"[1, 2] == [1, 2]: {[1, 2] == [1, 2]}")  # خروجی: True
print(f"[1, 2] == [2, 1]: {[1, 2] == [2, 1]}")  # خروجی: False (ترتیب مهم است)

# اعداد
print(f"2 != 1: {2 != 1}")  # خروجی: True
print(f"2 != 2: {2 != 2}")  # خروجی: False

# رشته‌ها
print(f"'python' != 'java': {'python' != 'java'}")  # خروجی: True
print(f"'text' != 'text': {'text' != 'text'}")  # خروجی: False

# مقادیر بولین
print(f"True != False: {True != False}")  # خروجی: True
print(f"False != False: {False != False}")  # خروجی: False

# اعداد
print(f"2 > 1: {2 > 1}")  # خروجی: True
print(f"2 > 4: {2 > 4}")  # خروجی: False
print(f"5.5 > 5: {5.5 > 5}")  # خروجی: True

# رشته‌ها (بر اساس ترتیب الفبایی)
print(f"'b' > 'a': {'b' > 'a'}")  # خروجی: True
print(f"'cat' > 'dog': {'cat' > 'dog'}")  # خروجی: False ('c' قبل از 'd' در الفبا می‌آید)

# اعداد
print(f"2 < 4: {2 < 4}")  # خروجی: True
print(f"2 < 1: {2 < 1}")  # خروجی: False

# رشته‌ها
print(f"'apple' < 'banana': {'apple' < 'banana'}")  # خروجی: True ('a' قبل از 'b')
print(f"'Z' < 'a': {'Z' < 'a'}")  # خروجی: True (کدهای ASCII 'Z'=90, 'a'=97)

# بزرگ‌تر یا مساوی
print(f"2 >= 2: {2 >= 2}")  # خروجی: True
print(f"2 >= 1: {2 >= 1}")  # خروجی: True
print(f"1 >= 2: {1 >= 2}")  # خروجی: False

# کوچک‌تر یا مساوی
print(f"2 <= 2: {2 <= 2}")  # خروجی: True
print(f"2 <= 4: {2 <= 4}")  # خروجی: True
print(f"4 <= 2: {4 <= 2}")  # خروجی: False

# ********************************************************************************
"""
تفاوت بین == و is
"""
print("\n--- تفاوت بین == و is ---")

# تفاوت بین == و is
a_list = [1, 2, 3]
b_list = [1, 2, 3]
c_list = a_list
print(f"a == b (مقادیر): {a_list == b_list}")  # خروجی: True (مقادیر برابر هستند)
print(f"a is b (هویت): {a_list is b_list}")  # خروجی: False (اشیاء متفاوتی هستند)
print(f"a is c (هویت): {a_list is c_list}")  # خروجی: True (به یک شیء اشاره می‌کنند)

# مثال با مقادیر ساده (این رفتار ممکن است بسته به پیاده‌سازی متفاوت باشد)
x_small = 256
y_small = 256
print(f"x is y (256 - بهینه‌سازی): {x_small is y_small}")  # خروجی: True (به دلیل بهینه‌سازی پایتون برای اعداد کوچک)

x_large = 257
y_large = 257
print(f"x is y (257 - ممکن است متفاوت باشد): {x_large is y_large}")  # خروجی: ممکن است True یا False باشد

# ********************************************************************************
"""
مقایسه‌های بین انواع مختلف
"""
print("\n--- مقایسه‌های بین انواع مختلف ---")

# پایتون به راحتی اعداد صحیح و اعشاری را با یکدیگر مقایسه می‌کند
print(f"3 == 3.0: {3 == 3.0}")  # خروجی: True
print(f"2.5 > 2: {2.5 > 2}")  # خروجی: True
print(f"10 < 10.1: {10 < 10.1}")  # خروجی: True

# رشته‌ها بر اساس کدهای ASCII/Unicode مقایسه می‌شوند
# حروف بزرگ قبل از حروف کوچک در کد ASCII می‌آیند
print(f"'A' < 'a': {'A' < 'a'}")  # خروجی: True (65 < 97)
print(f"'Z' < 'a': {'Z' < 'a'}")  # خروجی: True (90 < 97)

# مقایسه رشته‌های چندکاراکتری
print(f"'apple' < 'banana': {'apple' < 'banana'}")  # خروجی: True
print(f"'apple' < 'application': {'apple' < 'application'}")  # خروجی: True
print(f"'cat' > 'cap': {'cat' > 'cap'}")  # خروجی: True (مقایسه کاراکتر به کاراکتر)

# لیست‌ها و تاپل‌ها به صورت الفبایی و عنصر به عنصر مقایسه می‌شوند
print(f"[1, 2, 3] < [1, 2, 4]: {[1, 2, 3] < [1, 2, 4]}")  # خروجی: True
print(f"[1, 2, 3] < [1, 3, 2]: {[1, 2, 3] < [1, 3, 2]}")  # خروجی: True
print(f"[1, 2] < [1, 2, 3]: {[1, 2] < [1, 2, 3]}")  # خروجی: True
print(f"(1, 'a') < (1, 'b'): {(1, 'a') < (1, 'b')}")  # خروجی: True

# در پایتون 3.6+، دیکشنری‌ها می‌توانند با یکدیگر مقایسه شوند (فقط برابری)
print(f"{{'a': 1, 'b': 2}} == {{'b': 2, 'a': 1}}: { {'a': 1, 'b': 2} == {'b': 2, 'a': 1} }")  # خروجی: True

# ********************************************************************************
"""
مقایسه‌های غیرمجاز (این بخش خطا ایجاد می‌کند و کامنت شده است)
"""
print("\n--- مقایسه‌های غیرمجاز (خطاها) ---")

# مقایسه‌های غیرمجاز
# try:
#     print(f"5 < '5': {5 < '5'}")
# except TypeError as e:
#     print(f"خطا در مقایسه 5 < '5': {e}")  # خروجی: '>' not supported between instances of 'int' and 'str'

# try:
#     print(f"[1, 2] < {{'a': 1}}:")
#     result_invalid = [1, 2] < {'a': 1}
# except TypeError as e:
#     print(f"خطا در مقایسه [1, 2] < {{'a': 1}}: {e}")  # خروجی: '<' not supported between instances of 'list' and 'dict'

# ********************************************************************************
"""
مقایسه‌های زنجیره‌ای (Chained Comparisons)
"""
print("\n--- مقایسه‌های زنجیره‌ای ---")

# مثال ساده
x_chain = 5
print(f"1 < x < 10 (برای x={x_chain}): {1 < x_chain < 10}")  # خروجی: True
print(f"5 <= x < 10 (برای x={x_chain}): {5 <= x_chain < 10}")  # خروجی: True
print(f"x < 10 < x*10 < 100 (برای x={x_chain}): {x_chain < 10 < x_chain*10 < 100}")  # خروجی: True

# مثال پیچیده‌تر
age_person = 25
print(f"18 <= age <= 65 (برای سن {age_person}): {18 <= age_person <= 65}")  # خروجی: True (آیا سن بین 18 تا 65 است؟)

temperature_val = 22
print(f"20 <= temperature <= 25 (برای دمای {temperature_val}): {20 <= temperature_val <= 25}")  # خروجی: True

# مثال با عملگرهای مختلف
print(f"1 < 2 <= 2 < 3: {1 < 2 <= 2 < 3}")  # خروجی: True

# ********************************************************************************
"""
تفاوت == و is (تکرار برای تاکید)
"""
print("\n--- تفاوت == و is (تکرار) ---")

# همیشه از is برای مقایسه با None استفاده کنید
x_none_check = None
# روش صحیح
print(f"x is None: {x_none_check is None}")  # True
# روش توصیه نشده
print(f"x == None: {x_none_check == None}")  # کار می‌کند اما توصیه نمی‌شود

# به دلیل دقت محدود اعداد اعشاری، از == برای مقایسه دقیق اعداد اعشاری خودداری کنید:
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")  # False!

# روش صحیح برای مقایسه اعداد اعشاری
tolerance_compare = 1e-10
result_float_compare = abs((0.1 + 0.2) - 0.3) < tolerance_compare
print(f"abs((0.1 + 0.2) - 0.3) < tolerance (برای 0.1+0.2==0.3): {result_float_compare}")  # True

# ********************************************************************************
"""
عملگرهای منطقی (and, or, not)
"""
print("\n--- عملگرهای منطقی ---")

# عملگر and
print(f"1 < 2 and 2 < 3: {1 < 2 and 2 < 3}")  # خروجی: True
print(f"1 < 2 and 2 > 3: {1 < 2 and 2 > 3}")  # خروجی: False
# Short-circuit در and: اگر یکی از شرایط False باشد، ارزیابی متوقف می‌شود
# 2/0 ارزیابی نمی‌شود چون 1>2 False است
print(f"1 > 2 and 2/0 < 3 (Short-circuit): {1 > 2 and 2/0 < 3}")  # خروجی: False (خطا نمی‌دهد چون 2/0 ارزیابی نمی‌شود)

# عملگر or
print(f"1 == 2 or 2 < 3: {1 == 2 or 2 < 3}")  # خروجی: True
print(f"1 == 1 or 100 == 1: {1 == 1 or 100 == 1}")  # خروجی: True
# Short-circuit در or: اگر یکی از شرایط True باشد، ارزیابی متوقف می‌شود
# خطای تقسیم بر صفر رخ نمی‌دهد چون 1>2 False است و 2/0 ارزیابی می‌شود
# print(f"1 > 2 or 2/0 < 3: {1 > 2 or 2/0 < 3}")  # این خط خطا می‌دهد چون 2/0 ارزیابی می‌شود

# ********************************************************************************
"""
اولویت ارزیابی در عبارات ترکیبی
"""
print("\n--- اولویت ارزیابی ---")

a_priority = 5
b_priority = 10
# این عبارت معادل (a < b) and (b > 1) or (a == 5) است
print(f"a < b > 1 or a == 5 (برای a={a_priority}, b={b_priority}): {a_priority < b_priority > 1 or a_priority == 5}")  # خروجی: True

# and دارای اولویت بالاتری نسبت به or دارد
print(f"False or False and True: {False or False and True}")  # خروجی: False
print(f"(False or False) and True: {(False or False) and True}")  # خروجی: False
print(f"False or (False and True): {False or (False and True)}")  # خروجی: False

# مثال پیچیده‌تر
x_complex = 5
y_complex = 10
print(f"1 < x < 10 and (x == 5 or x > 7) (برای x={x_complex}): {1 < x_complex < 10 and (x_complex == 5 or x_complex > 7)}")  # خروجی: True

# استفاده از and
print(f"5 < x < 10 and y > 8 (برای x={x_complex}, y={y_complex}): {5 < x_complex < 10 and y_complex > 8}")  # خروجی: True

# استفاده از or
print(f"x < 3 or y > 15 (برای x={x_complex}, y={y_complex}): {x_complex < 3 or y_complex > 15}")  # خروجی: False

# استفاده از not
print(f"not (x > 10) (برای x={x_complex}): {not (x_complex > 10)}")  # خروجی: True

# ترکیب پیچیده
print(f"1 < x < 10 and (y > 15 or x + y > 12) (برای x={x_complex}, y={y_complex}): {1 < x_complex < 10 and (y_complex > 15 or x_complex + y_complex > 12)}")  # خروجی: True

