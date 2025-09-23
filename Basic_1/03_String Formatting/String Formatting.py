"""
قالب‌بندی رشته‌ها به شما امکان می‌دهد اشیاء را مستقیماً در رشته قرار دهید، بدون نیاز به الحاق (چسباندن) دستی آن‌ها با استفاده از علامت +
"""
player = 'Thomas'
points = 33

# روش الحاق (بدون قالب‌بندی)
print("Old way: 'Last night, " + player + ' scored ' + str(points) + ' points."')
# خروجی: Old way: 'Last night, Thomas scored 33 points.' (ترجمه: روش قدیمی)

# روش قالب‌بندی (خواناتر و تمیزتر)
print(f"New way: f'Last night, {player} scored {points} points.'")
# خروجی: New way: f'Last night, Thomas scored 33 points.' (ترجمه: روش جدید)

"""
در پایتون سه روش اصلی برای قالب‌بندی رشته‌ها وجود دارد:

پلاسمهولدرهای قدیمی با علامت % (روش قدیمی)
متد .format() (روش میانه)
f-strings (روش جدید در پایتون 3.6+)
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)

"""
قالب‌بندی با پلاسمهولدرها (Formatting with %)
در این روش از علامت % به عنوان عملگر قالب‌بندی رشته استفاده می‌شود
"""
# استفاده از %s برای جایگزینی رشته
print("I'm going to inject %s here." % 'something')
# خروجی: I'm going to inject something here. (ترجمه: متن جایگزین شد)

# چندین مقدار با استفاده از تاپل
print("I'm going to inject %s text here, and %s text here." % ('some', 'more'))
# خروجی: I'm going to inject some text here, and more text here. (ترجمه: دو مقدار جایگزین شد)

# استفاده از متغیرها
x, y = 'some', 'more'
print("Values from variables: %s and %s" % (x, y))
# خروجی: Values from variables: some and more (ترجمه: مقادیر از متغیرها)

"""
تفاوت %s و %r
%s: از تابع str() برای تبدیل استفاده می‌کند (فقط متن)
%r: از تابع repr() برای تبدیل استفاده می‌کند (شامل گیومه و کاراکترهای خاص)
"""
print('He said his name was %s.' % 'Fred')  # خروجی: He said his name was Fred. (ترجمه: بدون گیومه)
print('He said his name was %r.' % 'Fred')  # خروجی: He said his name was 'Fred'. (ترجمه: با گیومه)

print('I caught a fish: %s' % 'this \tbig')  # خروجی: I caught a fish: this 	big. (ترجمه: تب اجرا شد)
print('I caught a fish: %r' % 'this \tbig')  # خروجی: I caught a fish: 'this \tbig'. (ترجمه: تب به صورت متنی)

"""
قالب‌بندی اعداد اعشاری
فرمت %5.2f به این معنی است:

5: حداقل تعداد کاراکترها (با فاصله پر می‌شود)
.2f: دو رقم اعشار نمایش داده شود
"""
print('Number: %5.2f' % 13.144)  # خروجی: Number: 13.14 (ترجمه: دو رقم اعشار)
print('Number: %10.1f' % 13.144) # خروجی: Number:       13.1 (ترجمه: 10 کاراکتر با یک رقم اعشار)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
قالب‌بندی با متد .format()
روش بهتری برای قالب‌بندی رشته‌ها که خواناتر و انعطاف‌پذیرتر است
"""
# ساختار کلی
print('String here {} then also {}'.format('something1', 'something2'))
# خروجی: String here something1 then also something2 (ترجمه: ساختار پایه)

# مثال کاربردی
print('This is a string with an {}'.format('insert'))
# خروجی: This is a string with an insert (ترجمه: متن با درج)

"""
مزایای .format() نسبت به %
دسترسی با ایندکس
استفاده از کلیدواژه‌ها
استفاده مجدد از متغیرها
تنظیم تراز و دقت
"""
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
# خروجی: The quick brown fox (ترجمه: دسترسی با ایندکس)

print('First: {a}, Second: {b}, Third: {c}'.format(a=1, b='Two', c=12.3))
# خروجی: First: 1, Second: Two, Third: 12.3 (ترجمه: استفاده از کلیدواژه)

print('A {p} saved is a {p} earned.'.format(p='penny'))
# خروجی: A penny saved is a penny earned. (ترجمه: استفاده مجدد از متغیر)

# تراز‌دهی و عرض فیلد
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))  # خروجی: Fruit    | Quantity (ترجمه: تراز‌دهی)
print('{0:8} | {1:9}'.format('Apples', 3.0))       # خروجی: Apples   |       3.0 (ترجمه: تراز‌دهی عدد)

# تراز چپ، وسط و راست
print('{0:<8} | {1:^8} | {2:>8}'.format('Left', 'Center', 'Right'))
# خروجی: Left     |  Center  |    Right (ترجمه: تراز‌دهی‌های مختلف)

# پر کردن با کاراکتر خاص
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left', 'Center', 'Right'))
# خروجی: Left==== | -Center- | ...Right (ترجمه: پرکردن با کاراکتر خاص)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
f-strings (Formatted String Literals)
مخصوص پایتون 3.6+ - روش جدید و بهینه‌تر برای قالب‌بندی رشته‌ها:

مزایا نسبت به روش‌های قبلی
متغیرهای خارجی را مستقیماً در رشته فراخوانی می‌کند
نیازی به استفاده از .format() نیست
خوانایی بالاتری دارد
"""
name = 'Fred'

# استفاده مستقیم از متغیر
print(f"He said his name is {name}.")
# خروجی: He said his name is Fred. (ترجمه: استفاده مستقیم از متغیر)

# استفاده از !r برای نمایش گیومه
print(f"He said his name is {name!r}")
# خروجی: He said his name is 'Fred' (ترجمه: نمایش با گیومه)

"""
قالب‌بندی اعداد اعشاری در f-strings
"""
num = 23.45678

# روش معمولی
print("Standard: {0:10.4f}".format(num))  # خروجی: Standard:   23.4568 (ترجمه: روش استاندارد)

# روش f-string
print(f"f-string: {num:{10}.{6}}")         # خروجی: f-string:   23.4568 (ترجمه: روش f-string)

# استفاده از سینتکس .format درون f-string
print(f"Combined: {num:10.4f}")           # خروجی: Combined:   23.4568 (ترجمه: ترکیب روش‌ها)

"""
نکته مهم در f-strings
در f-strings، دقت (precision) به کل تعداد ارقام اشاره می‌کند، نه فقط ارقام بعد از اعشار
"""
num = 23.45
print(f"Note: {num:{10}.{6}}")  # خروجی: Note:     23.45 (ترجمه: دقت کلی ارقام)

"""
روش	مثال                        	       استفاده‌های رایج
% Operator	            print("Name: %s, Age: %d" % ("Ali", 25))        	 کدهای قدیمی پایتون
.format() Method     	print("Name: {}, Age: {}".format("Ali", 25))        	کدهای میانه و پایتون 2.x
f-strings       	    print(f"Name: {name}, Age: {age}")          	  کدهای جدید (پایتون 3.6+)
"""
