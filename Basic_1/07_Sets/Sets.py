"""
مجموعه‌ها (Sets) در پایتون، مجموعه‌ای نامرتب از عناصر یونیک (منحصر به فرد) هستند.
 این بدان معناست که هر عنصر فقط یک بار در مجموعه ظاهر می‌شود و ترتیب عناصر مهم نیست.
"""

"""
مجموعه‌ها را می‌توان با استفاده از تابع set() ایجاد کرد
"""
# Create an empty set (ایجاد یک مجموعه خالی)
x = set()
print("Empty set:", x)  # خروجی: Empty set: set() (ترجمه: مجموعه خالی)

# Add elements to set with add() method (افزودن عناصر به مجموعه با متد add())
x.add(1)
print("Set after adding 1:", x)  # خروجی: Set after adding 1: {1} (ترجمه: مجموعه پس از افزودن 1)

x.add(2)
print("Set after adding 2:", x)  # خروجی: Set after adding 2: {1, 2} (ترجمه: مجموعه پس از افزودن 2)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
ویژگی منحصر به فرد: عناصر تکراری مجاز نیستند
اگر سعی کنید عنصری را که قبلاً در مجموعه وجود دارد، دوباره اضافه کنید، هیچ تغییری ایجاد نمی‌شود
"""

# Try to add duplicate element (تلاش برای افزودن عنصر تکراری)
x.add(1)
print("Set after trying to add duplicate 1:", x)
# خروجی: Set after trying to add duplicate 1: {1, 2} (ترجمه: مجموعه پس از تلاش برای افزودن 1 تکراری)

"""
تبدیل لیست به مجموعه
یکی از کاربردهای مفید مجموعه‌ها، حذف عناصر تکراری از لیست‌ها است
"""

# Create a list with duplicate elements (ایجاد لیست با عناصر تکراری)
list1 = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]
print("Original list with duplicates:", list1)
# خروجی: Original list with duplicates: [1, 1, 2, 2, 3, 4, 5, 6, 1, 1] (ترجمه: لیست اصلی با عناصر تکراری)

# Convert list to set to get unique elements (تبدیل لیست به مجموعه برای گرفتن عناصر یونیک)
unique_set = set(list1)
print("Set with unique elements:", unique_set)
# خروجی: Set with unique elements: {1, 2, 3, 4, 5, 6} (ترجمه: مجموعه با عناصر یونیک)

"""
نکات مهم درباره مجموعه‌ها
مجموعه‌ها از آکولاد {} برای نمایش استفاده می‌کنند، اما این به معنای دیکشنری نیست (دیکشنری‌ها کلید-مقدار دارند، مجموعه‌ها فقط عناصر یونیک).
مجموعه‌ها غیر قابل ایندکس‌گیری هستند (چون نامرتب هستند).
مجموعه‌ها قابل تغییر (Mutable) هستند و می‌توانید عناصر را به آن‌ها اضافه یا حذف کنید.
"""

# Set operations examples (مثال‌های عملیات روی مجموعه‌ها)
my_set = {1, 2, 3}

# Add element (افزودن عنصر)
my_set.add(4)
print("After add(4):", my_set)  # خروجی: After add(4): {1, 2, 3, 4} (ترجمه: پس از add(4))

# Remove element (حذف عنصر)
my_set.remove(2)
print("After remove(2):", my_set)  # خروجی: After remove(2): {1, 3, 4} (ترجمه: پس از remove(2))

# Discard element (حذف عنصر بدون خطا در صورت عدم وجود)
my_set.discard(5)  # خطا نمی‌دهد چون 5 وجود ندارد
print("After discard(5):", my_set)  # خروجی: After discard(5): {1, 3, 4} (ترجمه: پس از discard(5))
