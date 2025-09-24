"""
مقادیر بولین (Booleans) نوعی از داده‌ها هستند که فقط دو مقدار ممکن دارند: True و False. این مقادیر برای ارزیابی شرط‌ها و منطق برنامه‌نویسی استفاده می‌شوند.
"""

"""
می‌توانید مستقیماً مقادیر بولین را ایجاد کنید
"""
# Create boolean variables (ایجاد متغیرهای بولین)
a = True
b = False
print("Boolean True:", a)  # خروجی: Boolean True: True (ترجمه: مقدار بولین True)
print("Boolean False:", b)  # خروجی: Boolean False: False (ترجمه: مقدار بولین False)

"""
استفاده از عملگرهای مقایسه‌ای
معمولاً مقادیر بولین از طریق عملگرهای مقایسه‌ای ایجاد می‌شوند
"""
# Comparison operators return booleans (عملگرهای مقایسه‌ای مقادیر بولین برمی‌گردانند)
print("1 > 2:", 1 > 2)  # خروجی: 1 > 2: False (ترجمه: 1 بزرگتر از 2)
print("5 < 10:", 5 < 10)  # خروجی: 5 < 10: True (ترجمه: 5 کوچکتر از 10)
print("3 == 3:", 3 == 3)  # خروجی: 3 == 3: True (ترجمه: 3 برابر با 3)
print("4 != 4:", 4 != 4)  # خروجی: 4 != 4: False (ترجمه: 4 نامساوی با 4)

"""
مقدار None
None یک جایگاه‌نگهدار (Placeholder) است که برای نشان دادن عدم وجود مقدار یا مقدار تعریف نشده استفاده می‌شود:
"""
# Using None as placeholder (استفاده از None به عنوان جایگاه‌نگهدار)
result = None
print("Initial result value:", result)  # خروجی: Initial result value: None (ترجمه: مقدار اولیه نتیجه)

# Later in code, assign actual value (بعداً در کد، مقدار واقعی را اختصاص دهید)
result = 42
print("After calculation, result:", result)  # خروجی: After calculation, result: 42 (ترجمه: پس از محاسبه، نتیجه)

"""
نکات مهم درباره مقادیر بولین
در پایتون، True معادل عدد صحیح 1 و False معادل عدد صحیح 0 است.
مقادیر بولین در عملیات‌های منطقی (and, or, not) استفاده می‌شوند.
None با هیچ مقدار دیگری برابر نیست (حتی با False یا 0).
"""
# Boolean logic examples (مثال‌های منطق بولین)
print("True and False:", True and False)  # خروجی: True and False: False (ترجمه: True و False)
print("True or False:", True or False)    # خروجی: True or False: True (ترجمه: True یا False)
print("not True:", not True)              # خروجی: not True: False (ترجمه: نه True)

# None comparison (مقایسه None)
print("None == None:", None == None)      # خروجی: None == None: True (ترجمه: None برابر با None)
print("None == False:", None == False)    # خروجی: None == False: False (ترجمه: None برابر با False)

"""
نکته کلیدی:

از مجموعه‌ها برای کار با داده‌های یونیک و انجام عملیات ریاضی مجموعه‌ها استفاده کنید.
مقادیر بولین اساس تصمیم‌گیری در برنامه‌ها را تشکیل می‌دهند.
از None برای نشان دادن وضعیت "مقدار تعریف نشده" یا "هنوز محاسبه نشده" استفاده کنید.
"""
