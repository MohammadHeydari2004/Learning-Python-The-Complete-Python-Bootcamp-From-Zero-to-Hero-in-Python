"""
لیست‌ها در پایتون نسخه‌ی عمومی‌تر از مفهوم دنباله (Sequence) هستند.
 برخلاف رشته‌ها، لیست‌ها قابل تغییر (Mutable) هستند، یعنی می‌توانید عناصر داخل لیست را تغییر دهید.
لیست‌ها با استفاده از باقلاوه ([]) و کاما برای جدا کردن عناصر ساخته می‌شوند
"""
# Create a list of integers (ایجاد لیست اعداد صحیح)
my_list = [1, 2, 3]
print("Integer list:", my_list)  # خروجی: Integer list: [1, 2, 3] (ترجمه: لیست اعداد صحیح)

# List with mixed data types (لیست با انواع داده‌های مختلف)
mixed_list = ['A string', 23, 100.232, 'o']
print("Mixed data types list:", mixed_list)  # خروجی: Mixed data types list: ['A string', 23, 100.232, 'o'] (ترجمه: لیست با انواع داده‌های مختلف)

# Get list length with len() (محاسبه طول لیست با len())
print("Length of mixed list:", len(mixed_list))  # خروجی: Length of mixed list: 4 (ترجمه: طول لیست مخلوط)

# لیست‌ها می‌توانند انواع مختلفی از اشیاء را در خود نگه دارند (اعداد صحیح، اعشاری، رشته‌ها و حتی سایر لیست‌ها).

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
ایندکس‌گیری و برش لیست‌ها (Indexing and Slicing Lists)
لیست‌ها از همان سیستم ایندکس‌گیری و برش رشته‌ها پیروی می‌کنند. ایندکس‌ها از صفر شروع می‌شوند
"""
# Create a sample list (ایجاد یک لیست نمونه)
my_list = ['one', 'two', 'three', 4, 5]

# Access element at index 0 (دسترسی به عنصر ایندکس 0)
print("Element at index 0:", my_list[0])  # خروجی: Element at index 0: one (ترجمه: عنصر ایندکس 0)

# Slice from index 1 to the end (برش از ایندکس 1 تا انتها)
print("Slice from index 1 to end:", my_list[1:])  # خروجی: Slice from index 1 to end: ['two', 'three', 4, 5] (ترجمه: برش از ایندکس 1 تا انتها)

# Slice up to index 3 (برش تا ایندکس 3)
print("Slice up to index 3:", my_list[:3])  # خروجی: Slice up to index 3: ['one', 'two', 'three'] (ترجمه: برش تا ایندکس 3)

# Concatenate lists with + (الحاق لیست‌ها با +)
print("Concatenated list:", my_list + ['new item'])  # خروجی: Concatenated list: ['one', 'two', 'three', 4, 5, 'new item'] (ترجمه: لیست الحاق شده)

# Note: Concatenation is not permanent unless reassigned (نکته: الحاق موقت است مگر اینکه مقداردهی مجدد شود)
print("Original list after concatenation:", my_list)  # خروجی: Original list after concatenation: ['one', 'two', 'three', 4, 5] (ترجمه: لیست اصلی پس از الحاق)

# Duplicate list with * (تکرار لیست با *)
print("Doubled list:", my_list * 2)
# خروجی: Doubled list: ['one', 'two', 'three', 4, 5, 'one', 'two', 'three', 4, 5] (ترجمه: لیست دوبرابر شده)

"""
الحاق لیست‌ها با + یا تکرار با * موقت است و برای دائمی کردن تغییرات باید لیست را مقداردهی مجدد کنید.
اگر از ایندکس خارج از محدوده استفاده کنید، خطای IndexError رخ می‌دهد.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
متدهای پایه لیست‌ها (Basic List Methods)
لیست‌ها انعطاف‌پذیری بیشتری نسبت به آرایه‌ها در سایر زبان‌های برنامه‌نویسی دارند، چون:

اندازه‌ی ثابتی ندارند
محدودیت نوع داده‌ای ندارند
"""

"""
متد append()
برای اضافه کردن دائمی یک عنصر به انتهای لیست:
"""
# Create a new list (ایجاد یک لیست جدید)
list1 = [1, 2, 3]

# Append an item permanently (افزودن مداوم یک عنصر)
list1.append('append me!')
print("List after append:", list1)  # خروجی: List after append: [1, 2, 3, 'append me!'] (ترجمه: لیست پس از append)

"""
متد pop()
برای حذف و بازگرداندن یک عنصر از لیست
"""
# Pop the item at index 0 (حذف عنصر ایندکس 0)
popped_item = list1.pop(0)
print("Popped item:", popped_item)  # خروجی: Popped item: 1 (ترجمه: عنصر حذف شده)
print("List after popping index 0:", list1)  # خروجی: List after popping index 0: [2, 3, 'append me!'] (ترجمه: لیست پس از حذف ایندکس 0)

# Pop the last item (default) (حذف آخرین عنصر به صورت پیش‌فرض)
last_item = list1.pop()
print("Last popped item:", last_item)  # خروجی: Last popped item: append me! (ترجمه: آخرین عنصر حذف شده)
print("List after popping last item:", list1)  # خروجی: List after popping last item: [2, 3] (ترجمه: لیست پس از حذف آخرین عنصر)

"""
متدهای sort() و reverse()
برای مرتب‌سازی و معکوس کردن لیست
"""
# Create a new list for sorting (ایجاد لیست جدید برای مرتب‌سازی)
new_list = ['a', 'e', 'x', 'b', 'c']

# Reverse the list (معکوس کردن لیست)
new_list.reverse()
print("List after reverse:", new_list)  # خروجی: List after reverse: ['c', 'b', 'x', 'e', 'a'] (ترجمه: لیست پس از معکوس کردن)

# Sort the list (مرتب‌سازی لیست)
new_list.sort()
print("List after sort:", new_list)  # خروجی: List after sort: ['a', 'b', 'c', 'e', 'x'] (ترجمه: لیست پس از مرتب‌سازی)

"""
نکات مهم:
sort() لیست را به ترتیب صعودی مرتب می‌کند (برای اعداد) یا به ترتیب الفبایی (برای رشته‌ها).
هر دو متد sort() و reverse() تغییرات را به صورت مستقیم روی لیست اصلی اعمال می‌کنند و نیازی به مقداردهی مجدد نیست.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
لیست‌های تودرتو (Nesting Lists)
یکی از ویژگی‌های قدرتمند پایتون امکان تودرتو بودن ساختارهای داده‌ای است، یعنی می‌توانید لیست‌ها را درون لیست‌های دیگر قرار دهید
"""
# Create three separate lists (ایجاد سه لیست جداگانه)
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

# Create a matrix (list of lists) (ایجاد یک ماتریس (لیست لیست‌ها))
matrix = [lst_1, lst_2, lst_3]
print("Matrix:", matrix)  # خروجی: Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] (ترجمه: ماتریس)

# Access first item in matrix (دسترسی به اولین آیتم در ماتریس)
print("First row of matrix:", matrix[0])  # خروجی: First row of matrix: [1, 2, 3] (ترجمه: اولین سطر ماتریس)

# Access first item of the first row (دسترسی به اولین آیتم از اولین سطر)
print("First element of first row:", matrix[0][0])  # خروجی: First element of first row: 1 (ترجمه: اولین عنصر از اولین سطر)

"""
کاربرد عملی:
این ساختار برای نمایش داده‌های ساختار یافته مانند ماتریس‌ها در ریاضیات بسیار مفید است.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
فهم لیست‌ها (List Comprehensions)
فهم لیست‌ها (List Comprehensions) یک ویژگی پیشرفته در پایتون است که امکان ساخت سریع لیست‌ها را فراهم می‌کند.
 این ویژگی نیاز به درک حلقه‌های for دارد که بعداً توضیح داده خواهد شد.
"""
# Create a matrix (ایجاد یک ماتریس)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# List comprehension to get first column (فهم لیست برای گرفتن اولین ستون)
first_col = [row[0] for row in matrix]
print("First column of matrix:", first_col)  # خروجی: First column of matrix: [1, 4, 7] (ترجمه: اولین ستون ماتریس)

# Another example: squares of numbers (مثال دیگر: مربع اعداد)
squares = [x**2 for x in range(1, 6)]
print("Squares of numbers 1-5:", squares)  # خروجی: Squares of numbers 1-5: [1, 4, 9, 16, 25] (ترجمه: مربع اعداد 1 تا 5)
