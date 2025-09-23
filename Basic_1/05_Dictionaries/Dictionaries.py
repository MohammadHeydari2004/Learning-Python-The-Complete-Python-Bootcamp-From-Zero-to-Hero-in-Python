"""
دیکشنری‌ها (Dictionaries) نوعی از ساختارهای داده‌ای تطبیقی (Mappings) در پایتون هستند که برخلاف دنباله‌ها (Sequences) مانند لیست‌ها،
 عناصر را بر اساس کلید (Key) ذخیره می‌کنند،
 نه بر اساس موقعیت نسبی. این تفاوت اساسی بسیار مهم است،
 چون دیکشنری‌ها ترتیب عناصر را حفظ نمی‌کنند و دسترسی به عناصر از طریق کلیدهای منحصر به فرد انجام می‌شود.
یک دیکشنری پایتون از کلید و مقدار مرتبط با آن تشکیل شده است.
 این مقدار می‌تواند تقریباً هر شیء پایتونی باشد (اعداد، رشته‌ها، لیست‌ها و حتی دیکشنری‌های دیگر).
"""
# Create a simple dictionary (ایجاد یک دیکشنری ساده)
my_dict = {'name': 'Ali', 'age': 30}
print("Simple dictionary:", my_dict)
# خروجی: Simple dictionary: {'name': 'Ali', 'age': 30} (ترجمه: دیکشنری ساده)

# Dictionary with different data types (دیکشنری با انواع داده‌های مختلف)
complex_dict = {
    'name': 'Ali',
    'age': 30,
    'scores': [85, 90, 95],
    'address': {'city': 'Tehran', 'zip': '12345'}
}
print("Complex dictionary:", complex_dict)
# خروجی: Complex dictionary: {'name': 'Ali', 'age': 30, 'scores': [85, 90, 95], 'address': {'city': 'Tehran', 'zip': '12345'}} (ترجمه: دیکشنری پیچیده)

"""
دیکشنری‌ها از کلیدهای منحصر به فرد استفاده می‌کنند.
ترتیب عناصر در دیکشنری‌های پایتون 3.7+ بر اساس ترتیب افزودن حفظ می‌شود (در نسخه‌های قبلی این ترتیب تضمین نمی‌شد).
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
دیکشنری‌ها با استفاده از آکولاد ({}) و دو نقطه (:) برای نشان دادن کلید و مقدار ساخته می‌شوند
"""
# Create dictionary with {} (ساخت دیکشنری با آکولاد)
my_dict = {'key1': 'value1', 'key2': 'value2'}
print("Dictionary with string values:", my_dict)
# خروجی: Dictionary with string values: {'key1': 'value1', 'key2': 'value2'} (ترجمه: دیکشنری با مقادیر رشته‌ای)

# Dictionary with mixed data types (دیکشنری با انواع داده‌های مختلف)
mixed_dict = {
    'key1': 123,
    'key2': [12, 23, 33],
    'key3': ['item0', 'item1', 'item2']
}
print("Dictionary with mixed data types:", mixed_dict)
# خروجی: Dictionary with mixed data types: {'key1': 123, 'key2': [12, 23, 33], 'key3': ['item0', 'item1', 'item2']} (ترجمه: دیکشنری با انواع داده‌های مختلف)

# Create empty dictionary (ساخت دیکشنری خالی)
empty_dict = {}
print("Empty dictionary:", empty_dict)  # خروجی: Empty dictionary: {} (ترجمه: دیکشنری خالی)

# Add keys through assignment (افزودن کلیدها از طریق مقداردهی)
empty_dict['animal'] = 'Dog'
empty_dict['answer'] = 42
print("Dictionary after adding keys:", empty_dict)
# خروجی: Dictionary after adding keys: {'animal': 'Dog', 'answer': 42} (ترجمه: دیکشنری پس از افزودن کلیدها)

# دیکشنری‌ها بسیار انعطاف‌پذیر هستند و می‌توانند انواع مختلفی از داده‌ها را به عنوان مقدار نگه دارند (اعداد، لیست‌ها، دیکشنری‌های دیگر و ...).

# -----------------------------------------------------------------------------------------------------
print("-" * 80)

# برای دسترسی به مقادیر دیکشنری از کلیدها استفاده می‌شود

# Create a sample dictionary (ایجاد یک دیکشنری نمونه)
my_dict = {'key1': 123, 'key2': [12, 23, 33], 'key3': ['item0', 'item1', 'item2']}

# Access value by key (دسترسی به مقدار با کلید)
print("Value of key3:", my_dict['key3'])
# خروجی: Value of key3: ['item0', 'item1', 'item2'] (ترجمه: مقدار کلید key3)

# Access element inside a list value (دسترسی به عنصر داخل یک مقدار لیستی)
print("First item of key3:", my_dict['key3'][0])
# خروجی: First item of key3: item0 (ترجمه: اولین آیتم کلید key3)

# Apply methods on values (اعمال متدها بر روی مقادیر)
print("Uppercase of first item:", my_dict['key3'][0].upper())
# خروجی: Uppercase of first item: ITEM0 (ترجمه: حروف بزرگ اولین آیتم)

# Modify dictionary values (تغییر مقادیر دیکشنری)
print("Original value of key1:", my_dict['key1'])  # خروجی: Original value of key1: 123 (ترجمه: مقدار اصلی کلید key1)
my_dict['key1'] = my_dict['key1'] - 123
print("Modified value of key1:", my_dict['key1'])  # خروجی: Modified value of key1: 0 (ترجمه: مقدار تغییر یافته کلید key1)

# Using += for self subtraction (استفاده از += برای کاهش خودکار)
my_dict['key1'] -= 123
print("Value after -= operation:", my_dict['key1'])  # خروجی: Value after -= operation: -123 (ترجمه: مقدار پس از عملیات -=)

"""
اگر سعی کنید به کلیدی دسترسی پیدا کنید که وجود ندارد، خطای KeyError رخ می‌دهد.
برای جلوگیری از این خطا می‌توانید از متد get() استفاده کنید که در بخش متدهای پایه توضیح داده خواهد شد.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
یکی از ویژگی‌های قدرتمند پایتون امکان تودرتو بودن ساختارهای داده‌ای است، یعنی می‌توانید دیکشنری‌ها را درون دیکشنری‌های دیگر قرار دهید
"""
# Create a nested dictionary (ایجاد یک دیکشنری تودرتو)
nested_dict = {
    'key1': {
        'nestkey': {
            'subnestkey': 'value'
        }
    }
}
print("Nested dictionary:", nested_dict)
# خروجی: Nested dictionary: {'key1': {'nestkey': {'subnestkey': 'value'}}} (ترجمه: دیکشنری تودرتو)

# Access deeply nested values (دسترسی به مقادیر عمیقاً تودرتو)
print("Value of subnestkey:", nested_dict['key1']['nestkey']['subnestkey'])
# خروجی: Value of subnestkey: value (ترجمه: مقدار subnestkey)

# More practical nested example (مثال عملی‌تر از دیکشنری تودرتو)
user_info = {
    'name': 'Ali',
    'age': 30,
    'contact': {
        'email': 'ali@example.com',
        'phone': '123-456-7890'
    },
    'education': {
        'degree': 'Bachelor',
        'university': 'Tehran University',
        'graduation_year': 2015
    }
}

# Access nested information (دسترسی به اطلاعات تودرتو)
print("User email:", user_info['contact']['email'])
# خروجی: User email: ali@example.com (ترجمه: ایمیل کاربر)
print("University:", user_info['education']['university'])
# خروجی: University: Tehran University (ترجمه: دانشگاه)

"""
این ساختار برای نمایش داده‌های ساختار یافته مانند اطلاعات کاربر،
 داده‌های API و پیکربندی‌های پیچیده بسیار مفید است
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
دیکشنری‌ها چندین متد مفید برای دستکاری و بازیابی اطلاعات دارند:
"""
# Create a sample dictionary (ایجاد یک دیکشنری نمونه)
d = {'key1': 1, 'key2': 2, 'key3': 3}

# Get all keys (دریافت تمام کلیدها)
print("All keys:", d.keys())
# خروجی: All keys: dict_keys(['key1', 'key2', 'key3']) (ترجمه: تمام کلیدها)

# Get all values (دریافت تمام مقادیر)
print("All values:", d.values())
# خروجی: All values: dict_values([1, 2, 3]) (ترجمه: تمام مقادیر)

# Get all key-value pairs as tuples (دریافت تمام جفت‌های کلید-مقدار به صورت تاپل)
print("All items:", d.items())
# خروجی: All items: dict_items([('key1', 1), ('key2', 2), ('key3', 3)]) (ترجمه: تمام آیتم‌ها)

# Check if a key exists (بررسی وجود یک کلید)
print("Is 'key1' in dictionary?", 'key1' in d)  # خروجی: Is 'key1' in dictionary? True (ترجمه: آیا کلید key1 در دیکشنری وجود دارد؟)
print("Is 'key4' in dictionary?", 'key4' in d)  # خروجی: Is 'key4' in dictionary? False (ترجمه: آیا کلید key4 در دیکشنری وجود دارد؟)

# Get value with get() method (دریافت مقدار با متد get())
print("Value of key2:", d.get('key2'))  # خروجی: Value of key2: 2 (ترجمه: مقدار کلید key2)
print("Value of key4 (default):", d.get('key4', 'Not found'))  # خروجی: Value of key4 (default): Not found (ترجمه: مقدار کلید key4 با مقدار پیش‌فرض)

"""
keys(): یک view object برمی‌گرداند که لیستی از تمام کلیدهای دیکشنری است.
values(): یک view object برمی‌گرداند که لیستی از تمام مقادیر دیکشنری است.
items(): یک view object برمی‌گرداند که لیستی از تاپل‌های (کلید, مقدار) است.
get(key, default=None): مانند d[key] عمل می‌کند اما اگر کلید وجود نداشته باشد، به جای خطا مقدار پیش‌فرض را برمی‌گرداند.
"""

"""
 نکته کلیدی:

دیکشنری‌ها برای ذخیره داده‌های کلید-مقدار ایده‌آل هستند.
برای دسترسی به مقادیر از کلیدها استفاده کنید، نه از موقعیت عددی.
از متدهای keys(), values(), و items() برای بازیابی اطلاعات دیکشنری استفاده کنید.
دیکشنری‌های تودرتو امکان نمایش ساختارهای داده‌ای پیچیده را فراهم می‌کنند.
"""
