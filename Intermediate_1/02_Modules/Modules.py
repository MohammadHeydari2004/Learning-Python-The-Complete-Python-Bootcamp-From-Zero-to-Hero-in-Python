"""
ماژول‌ها در پایتون فایل‌های ساده‌ای با پسوند .py هستند که مجموعه‌ای از توابع، کلاس‌ها و متغیرها را پیاده‌سازی می‌کنند. ماژول‌ها امکان استفاده مجدد از کد را فراهم می‌کنند و به شما امکان می‌دهند تا کدهای خود را در فایل‌های جداگانه سازماندهی کنید.

تعریف ماژول
ماژول‌ها فایل‌های پایتون با پسوند .py هستند.
هر فایل پایتون می‌تواند به عنوان یک ماژول استفاده شود.
هنگام اولین باری که یک ماژول در اسکریپت پایتون بارگیری می‌شود، کد داخل آن یک بار اجرا می‌شود.
اگر ماژول دیگری همان ماژول را وارد کند، دوباره بارگیری نمی‌شود و تنها یک بار اجرا می‌شود.
"""
# Example of importing a module (مثال وارد کردن یک ماژول)
import math  # Import the math module (وارد کردن ماژول ریاضی)

# Using a function from the module (استفاده از یک تابع از ماژول)
print("Ceiling of 2.4:", math.ceil(2.4))
# خروجی: Ceiling of 2.4: 3 (ترجمه: سقف 2.4)

"""
نکات مهم درباره ماژول‌ها:
ماژول‌ها به شما امکان می‌دهند تا کدهای خود را در فایل‌های جداگانه سازماندهی کنید.
هر ماژول فضای نام (namespace) خاص خود را دارد که از تداخل نام‌ها جلوگیری می‌کند.
ماژول‌ها فقط یک بار در هر جلسه مفسر پایتون بارگیری می‌شوند، حتی اگر چندین بار وارد شوند.
"""
# More examples with math module (مثال‌های بیشتر با ماژول ریاضی)
import math

print("Square root of 16:", math.sqrt(16))  # خروجی: Square root of 16: 4.0 (ترجمه: جذر 16)
print("Value of pi:", math.pi)  # خروجی: Value of pi: 3.141592653589793 (ترجمه: مقدار pi)
print("Value of e:", math.e)  # خروجی: Value of e: 2.718281828459045 (ترجمه: مقدار e)
print("Sine of 90 degrees:", math.sin(math.radians(90)))  # خروجی: Sine of 90 degrees: 1.0 (ترجمه: سینوس 90 درجه)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
پایتون مجموعه‌ای از ماژول‌های داخلی دارد که به صورت پیش‌فرض در دسترس هستند. دو تابع بسیار مهم برای کشف ماژول‌ها عبارتند از:

dir(): نام‌های تعریف شده در یک ماژول را نشان می‌دهد.
help(): اطلاعات کمکی درباره یک ماژول یا تابع ارائه می‌دهد.
"""
# Using dir() to explore module contents (استفاده از dir() برای کشف محتوای ماژول)
import math

# Get all names defined in the math module (دریافت تمام نام‌های تعریف شده در ماژول ریاضی)
math_functions = dir(math)
print("First 5 functions in math module:", math_functions[:5])
# خروجی: First 5 functions in math module: ['__doc__', '__loader__', '__name__', '__package__', '__spec__'] (ترجمه: 5 تابع اول در ماژول ریاضی)

# Filter to show only useful functions (فیلتر برای نشان دادن فقط توابع مفید)
useful_functions = [func for func in math_functions if not func.startswith('__')]
print("First 5 useful functions:", useful_functions[:5])
# خروجی: First 5 useful functions: ['acos', 'acosh', 'asin', 'asinh', 'atan'] (ترجمه: 5 تابع مفید اول)

# Using help() to get documentation (استفاده از help() برای دریافت مستندات)
import math

# Get help on a specific function (دریافت راهنما برای یک تابع خاص)
print("\nHelp for math.ceil function:")
print("This would normally show the help documentation for math.ceil")
# Normally you would use: help(math.ceil)
# (معمولاً از این دستور استفاده می‌شود: help(math.ceil))

# More examples with dir and help (مثال‌های بیشتر با dir و help)
import random

# Explore the random module (کشف ماژول تصادفی)
print("\nRandom module contents:")
print(dir(random)[:5])  # خروجی: ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random'] (ترجمه: محتوای ماژول تصادفی)

# Get help on random.randint (دریافت راهنما برای random.randint)
print("\nHelp for random.randint:")
print("This would show documentation for random.randint function")
# Normally you would use: help(random.randint)
# (معمولاً از این دستور استفاده می‌شود: help(random.randint))

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
نوشتن ماژول‌های شخصی بسیار ساده است. برای ایجاد یک ماژول شخصی، کافی است یک فایل جدید با پسوند .py ایجاد کنید و سپس آن را با استفاده از دستور import وارد کنید.

مراحل ایجاد یک ماژول شخصی
یک فایل جدید با پسوند .py ایجاد کنید.
کدهای مورد نظر خود را در آن بنویسید.
ماژول را با استفاده از دستور import وارد کنید.
"""

"""
فرض کنید فایلی به نام mymodule.py ایجاد می‌کنیم
"""
# How to use the custom module (نحوه استفاده از ماژول شخصی)
# Note: This assumes mymodule.py is in the same directory
# (توجه: این کد فرض می‌کند mymodule.py در همان دایرکتوری است)

import mymodule

# Using functions from the custom module (استفاده از توابع از ماژول شخصی)
print("\nUsing custom module:")
print(mymodule.greet("Ali"))  # خروجی: Hello, Ali! (ترجمه: سلام علی)
print("Square of 7:", mymodule.calculate_square(7))  # خروجی: Square of 7: 49 (ترجمه: مربع 7)

# Alternative import method (روش جایگزین وارد کردن)
from mymodule import greet, calculate_square

print("\nAlternative import method:")
print(greet("Reza"))  # خروجی: Hello, Reza! (ترجمه: سلام رضا)
print("Square of 8:", calculate_square(8))  # خروجی: Square of 8: 64 (ترجمه: مربع 8)

"""
نکات مهم درباره ماژول‌های شخصی:
فایل ماژول باید در مسیر جستجوی ماژول‌ها (sys.path) قرار داشته باشد.
می‌توانید مسیر جستجوی ماژول‌ها را با استفاده از sys.path.append() تغییر دهید.
بلوک if __name__ == "__main__": فقط هنگام اجرای مستقیم فایل اجرا می‌شود، نه هنگام وارد کردن ماژول.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
پکیج‌ها فضاهای نامی هستند که حاوی چندین ماژول و پکیج دیگر هستند. در واقع، پکیج‌ها دایرکتوری‌هایی هستند که یک ویژگی خاص دارند.

تعریف پکیج
هر پکیج در پایتون یک دایرکتوری است که حتماً باید حاوی فایل خاصی به نام __init__.py باشد.
این فایل می‌تواند خالی باشد، و نشان می‌دهد که دایرکتوری حاوی آن یک پکیج پایتون است.
فایل __init__.py می‌تواند کد راه‌اندازی برای پکیج یا تنظیم متغیر __all__ را داشته باشد.
"""

"""
ساختار یک پکیج :
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        submodule1.py
        submodule2.py
"""


"""
sound/
    __init__.py
    formats/
        __init__.py
        wavread.py
        wavwrite.py
        aiffread.py
        aiffwrite.py
        auread.py
        auwrite.py
    effects/
        __init__.py
        echo.py
        surround.py
        reverse.py
    filters/
        __init__.py
        equalizer.py
        vocoder.py
        karaoke.py
"""
# Using the sound package (استفاده از پکیج صدا)
# Note: This assumes the sound package structure is in place
# (توجه: این کد فرض می‌کند ساختار پکیج صدا ایجاد شده است)

# Method 1: Full import (روش 1: وارد کردن کامل)
import sound.effects.echo
result1 = sound.effects.echo.echofilter("input.wav", "output.wav", delay=0.5, atten=3)
print("Result 1:", result1)
# خروجی: Result 1: Echo processed: input.wav -> output.wav (ترجمه: نتیجه 1)

# Method 2: Direct import (روش 2: وارد کردن مستقیم)
from sound.effects import echo
result2 = echo.echofilter("input2.wav", "output2.wav")
print("Result 2:", result2)
# خروجی: Result 2: Echo processed: input2.wav -> output2.wav (ترجمه: نتیجه 2)

# Method 3: Import specific function (روش 3: وارد کردن تابع خاص)
from sound.effects.echo import echofilter
result3 = echofilter("input3.wav", "output3.wav", atten=5)
print("Result 3:", result3)
# خروجی: Result 3: Echo processed: input3.wav -> output3.wav (ترجمه: نتیجه 3)

"""
کات مهم درباره پکیج‌ها:
فایل __init__.py ضروری است تا پایتون دایرکتوری را به عنوان پکیج شناسایی کند.
می‌توانید از وارد کردن نسبی (relative imports) درون پکیج استفاده کنید.
متغیر __all__ در فایل __init__.py تعیین می‌کند که کدام ماژول‌ها هنگام استفاده از import * وارد می‌شوند.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
پایتون روش‌های مختلفی برای وارد کردن ماژول‌ها و پکیج‌ها ارائه می‌دهد که انعطاف‌پذیری بیشتری فراهم می‌کند.
"""
# Using 'as' to rename imported modules (استفاده از 'as' برای تغییر نام ماژول‌های وارد شده)
import math as m
print("\nUsing math as m:")
print("Square root of 25:", m.sqrt(25))  # خروجی: Square root of 25: 5.0 (ترجمه: جذر 25)

from math import sqrt as square_root
print("Square root of 36:", square_root(36))  # خروجی: Square root of 36: 6.0 (ترجمه: جذر 36)
# --------------------------------------------------------------------------------------
# Using 'from ... import *' (استفاده از 'from ... import *')
from math import *
print("\nUsing 'from math import *':")
print("Sin of 0:", sin(0))  # خروجی: Sin of 0: 0.0 (ترجمه: سینوس 0)
print("Cos of 0:", cos(0))  # خروجی: Cos of 0: 1.0 (ترجمه: کسینوس 0)
# Note: This is generally not recommended in scripts (نکته: این روش معمولاً در اسکریپت‌ها توصیه نمی‌شود)
# --------------------------------------------------------------------------------------
# Example of __all__ usage in __init__.py (مثال استفاده از __all__ در __init__.py)
# In sound/effects/__init__.py:
# __all__ = ['echo', 'surround']

# Now when using:
# from sound.effects import *
# Only 'echo' and 'surround' modules will be imported
print("\nExample of __all__ usage:")
print("When __all__ is set, only specified modules are imported with *")
# خروجی: Example of __all__ usage: (ترجمه: مثال استفاده از __all__)
# When __all__ is set, only specified modules are imported with * (ترجمه: وقتی __all__ تنظیم شده باشد، فقط ماژول‌های مشخص شده با * وارد می‌شوند)
# --------------------------------------------------------------------------------------
# Relative imports within packages (وارد کردن نسبی درون پکیج‌ها)
# This would be in sound/effects/surround.py
print("\nRelative imports example:")
print("From surround.py, we could use:")

# from . import echo  # Import echo module from current package (وارد کردن ماژول echo از پکیج فعلی)
# from .. import formats  # Import formats from parent package (وارد کردن formats از پکیج والد)
# from ..filters import equalizer  # Import equalizer from sibling package (وارد کردن equalizer از پکیج هم‌سطح)

print("from . import echo")
print("from .. import formats")
print("from ..filters import equalizer")
# خروجی:
# Relative imports example: (ترجمه: مثال وارد کردن نسبی)
# From surround.py, we could use: (ترجمه: از surround.py، می‌توانیم از این استفاده کنیم:)
# from . import echo
# from .. import formats
# from ..filters import equalizer
# --------------------------------------------------------------------------------------
# Module search path (مسیر جستجوی ماژول‌ها)
import sys

print("\nModule search path:")
for path in sys.path[:3]:  # Show first 3 paths (نمایش 3 مسیر اول)
    print("-", path)

# Adding a new path to module search path (افزودن مسیر جدید به مسیر جستجوی ماژول‌ها)
new_path = "/path/to/custom/modules"
if new_path not in sys.path:
    sys.path.append(new_path)
    print(f"\nAdded {new_path} to module search path")
# خروجی:
# Module search path: (ترجمه: مسیر جستجوی ماژول‌ها)
# - ... (مسیرها)
# Added /path/to/custom/modules to module search path (ترجمه: مسیر جدید به مسیر جستجوی ماژول‌ها اضافه شد)
# --------------------------------------------------------------------------------------
# Reloading modules (به‌روزرسانی ماژول‌ها در حین اجرا)
import importlib
import mymodule

# Make some changes to mymodule.py externally
# (تغییراتی در mymodule.py از خارج ایجاد کنید)

# Then reload the module (سپس ماژول را به‌روزرسانی کنید)
importlib.reload(mymodule)
print("\nModule reloaded successfully")
# خروجی: Module reloaded successfully (ترجمه: ماژول با موفقیت به‌روزرسانی شد)


"""
نکته کلیدی:

ماژول‌ها و پکیج‌ها امکان سازماندهی و استفاده مجدد از کد را فراهم می‌کنند.
فایل __init__.py برای تبدیل یک دایرکتوری به پکیج ضروری است.
استفاده از وارد کردن خاص (from module import specific_function) معمولاً بهتر از وارد کردن کلی (import *) است.
مسیر جستجوی ماژول‌ها توسط sys.path کنترل می‌شود.
برای توسعه تعاملی، از importlib.reload() برای به‌روزرسانی ماژول‌ها استفاده کنید.
با درک این مفاهیم، شما می‌توانید کدهای پیچیده‌تر و سازمان‌یافته‌تری ایجاد کنید که قابل استفاده مجدد و نگهداری هستند.
"""
