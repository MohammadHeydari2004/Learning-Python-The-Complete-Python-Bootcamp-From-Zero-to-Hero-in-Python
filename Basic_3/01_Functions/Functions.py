"""
توابع در پایتون یکی از اصلی‌ترین بلوک‌های سازنده برنامه‌های بزرگ‌تر هستند که به ما امکان می‌دهند کد را برای حل مسائل مختلف سازماندهی کنیم.

تعریف رسمی تابع
به طور رسمی، تابع دستگاهی مفید است که مجموعه‌ای از دستورات را گروه‌بندی می‌کند تا بتوان آن‌ها را بیش از یک بار اجرا کرد.
توابع همچنین به ما امکان می‌دهند پارامترهایی را مشخص کنیم که می‌توانند به عنوان ورودی به تابع ارسال شوند.
"""
# Example of built-in function (مثال تابع داخلی)
print("Length of 'hello':", len('hello'))
# خروجی: Length of 'hello': 5 (ترجمه: طول رشته 'hello')

"""
چرا از توابع استفاده کنیم؟
از نوشتن مجدد کد یکسان جلوگیری می‌کنند.
امکان استفاده مجدد از کد را فراهم می‌کنند.
به سازماندهی و طراحی بهتر برنامه کمک می‌کنند.
برای کارهای تکراری بسیار مفید هستند (مثل محاسبه طول یک رشته با len()).
نکته کلیدی:
توابع یکی از پایه‌ای‌ترین روش‌ها برای
 استفاده مجدد از کد در پایتون هستند و به ما امکان می‌دهند به سمت طراحی برنامه فکر کنیم.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
برای تعریف یک تابع در پایتون از کلیدواژه def استفاده می‌کنیم. ساختار کلی آن به این صورت است
"""
# General function syntax (ساختار کلی تابع)
def name_of_function(arg1, arg2):
    """
    This is the docstring - a description of what the function does.
    این بخش توضیحات تابع است - توضیحی درباره اینکه تابع چه کاری انجام می‌دهد.
    """
    # Code to execute (کدی که اجرا می‌شود)
    # Return statement if needed (دستور بازگشت در صورت نیاز)

# Define a simple function (تعریف یک تابع ساده)
def say_hello ( ) :
    """Prints 'hello' to the console.
    (چاپ 'hello' در کنسول)"""
    print ( 'hello' )

# Call the function (فراخوانی تابع)
say_hello ( )  # خروجی: hello (ترجمه: سلام)

"""
نکات مهم در تعریف توابع:
نام تابع باید معنادار باشد (مثل len برای تابع طول).
نام تابع نباید با نام توابع داخلی پایتون یکسان باشد.
پس از نام تابع حتماً از پرانتز () استفاده کنید.
بدنه تابع باید تورفتگی (Indentation) داشته باشد.
می‌توانید از docstring (رشته توضیحات) برای توضیح کار تابع استفاده کنید.
"""
# Function with docstring (تابع با docstring)
def greeting ( name ) :
    """Greets the person with the given name.
    (سلام کردن با شخص با نام داده شده)"""
    print ( f'Hello {name}' )

# View docstring with help() (مشاهده docstring با help())
# help(greeting)  # This would show the docstring in console (این دستور در کنسول docstring را نشان می‌دهد)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
برای اجرای یک تابع تعریف شده، باید آن را فراخوانی (Call) کنید. این کار با نوشتن نام تابع و پرانتز انجام می‌شود.
"""
# Define a function (تعریف تابع)
def say_hello():
    print('hello')

# Call the function correctly (فراخوانی صحیح تابع)
say_hello()  # خروجی: hello (ترجمه: سلام)

# Incorrect call (فراخوانی اشتباه)
print("Function without parentheses:", say_hello)
# خروجی: Function without parentheses: <function say_hello at 0x...> (ترجمه: تابع بدون پرانتز)

"""
نکته مهم:
اگر پرانتز () را فراموش کنید، پایتون تابع را اجرا نمی‌کند و فقط به شما نشان می‌دهد که یک تابع است.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
پارامترها ورودی‌هایی هستند که به تابع ارسال می‌شوند و تابع می‌تواند از آن‌ها در محاسبات خود استفاده کند.
"""
# Function with parameter (تابع با پارامتر)
def greeting(name):
    """Greets the person with the given name.
    (سلام کردن با شخص با نام داده شده)"""
    print(f'Hello {name}')

# Call with argument (فراخوانی با آرگومان)
greeting('Jose')  # خروجی: Hello Jose (ترجمه: سلام جوزه)
greeting('Ali')   # خروجی: Hello Ali (ترجمه: سلام علی)

# Function with multiple parameters (تابع با چندین پارامتر)
def add_greeting(first_name, last_name):
    """Greets a person with first and last name.
    (سلام کردن با نام و نام خانوادگی)"""
    print(f'Hello {first_name} {last_name}')

add_greeting('Ali', 'Rezaei')  # خروجی: Hello Ali Rezaei (ترجمه: سلام علی رضایی)


"""
نکات مهم درباره پارامترها:
تعداد آرگومان‌ها هنگام فراخوانی باید با تعداد پارامترها مطابقت داشته باشد.
ترتیب آرگومان‌ها مهم است مگر اینکه از نام پارامترها استفاده کنید
"""
# Using keyword arguments (استفاده از آرگومان‌های کلیدواژه‌ای)
def describe_pet(animal_type, pet_name):
    """Displays information about a pet.
    (نمایش اطلاعات درباره حیوان خانگی)"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet(pet_name='Willie', animal_type='dog')
# خروجی:
# I have a dog.
# My dog's name is Willie.
# (ترجمه: من یک سگ دارم. نام سگ من ویلی است.)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
تفاوت اصلی بین return و print این است که return نتیجه
 را برای استفاده بعدی ذخیره می‌کند، در حالی که print فقط نتیجه را نمایش می‌دهد.
"""
# Function with return (تابع با return)
def add_num(num1, num2):
    """Adds two numbers and returns the result.
    (جمع دو عدد و بازگرداندن نتیجه)"""
    return num1 + num2

# Using the returned value (استفاده از مقدار بازگشتی)
result = add_num(4, 5)
print("Result of addition:", result)  # خروجی: Result of addition: 9 (ترجمه: نتیجه جمع)
print("Double the result:", result * 2)  # خروجی: Double the result: 18 (ترجمه: دو برابر نتیجه)

# Function with print (تابع با print)
def print_result(a, b):
    """Adds two numbers and prints the result.
    (جمع دو عدد و چاپ نتیجه)"""
    print(a + b)

# Calling the function (فراخوانی تابع)
print("Calling print_result(10, 5):")
print_result(10, 5)  # خروجی: 15 (ترجمه: نتیجه چاپ می‌شود)

# Trying to save the result (تلاش برای ذخیره نتیجه)
my_result = print_result(20, 20)
print("Type of my_result:", type(my_result))
# خروجی: Type of my_result: <class 'NoneType'> (ترجمه: نوع my_result)

"""
تحلیل تفاوت‌ها:
توابع با return می‌توانند نتیجه را برای استفاده بعدی ذخیره کنند.
توابع با print فقط نتیجه را نمایش می‌دهند و None برمی‌گردانند.
اگر بخواهید نتیجه را در متغیری ذخیره کنید، حتماً باید از return استفاده کنید.
"""
# Comparing both approaches (مقایسه هر دو روش)
def return_result(a, b):
    return a + b

def print_result(a, b):
    print(a + b)

# Using return (استفاده از return)
result1 = return_result(10, 5)
print("Using return - result1:", result1)  # خروجی: Using return - result1: 15 (ترجمه: استفاده از return)

# Using print (استفاده از print)
result2 = print_result(10, 5)
print("Using print - result2:", result2)  # خروجی: Using print - result2: None (ترجمه: استفاده از print)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
توابع می‌توانند شامل ساختارهای شرطی و حلقه‌ها باشند تا عملکرد پیچیده‌تری داشته باشند.
"""
# Check if a number is even (بررسی اینکه آیا یک عدد زوج است)
def even_check(number):
    """Checks if a number is even.
    (بررسی اینکه آیا یک عدد زوج است)"""
    return number % 2 == 0

print("Is 20 even?", even_check(20))  # خروجی: Is 20 even? True (ترجمه: آیا 20 زوج است؟)
print("Is 21 even?", even_check(21))  # خروجی: Is 21 even? False (ترجمه: آیا 21 زوج است؟)

# Check if any number in a list is even (بررسی اینکه آیا هر عددی در لیست زوج است)
def check_even_list(num_list):
    """Checks if any number in the list is even.
    (بررسی اینکه آیا هر عددی در لیست زوج است)"""
    for number in num_list:
        if number % 2 == 0:
            return True
    return False

print("Any even in [1,2,3]?", check_even_list([1, 2, 3]))  # خروجی: Any even in [1,2,3]? True (ترجمه: آیا هر زوجی در لیست وجود دارد؟)
print("Any even in [1,3,5]?", check_even_list([1, 3, 5]))  # خروجی: Any even in [1,3,5]? False (ترجمه: آیا هر زوجی در لیست وجود دارد؟)

# Return all even numbers in a list (بازگرداندن تمام اعداد زوج در لیست)
def get_even_numbers(num_list):
    """Returns a list of all even numbers in the input list.
    (بازگرداندن لیستی از تمام اعداد زوج در لیست ورودی)"""
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

print("Even numbers in [1,2,3,4,5,6]:", get_even_numbers([1, 2, 3, 4, 5, 6]))
# خروجی: Even numbers in [1,2,3,4,5,6]: [2, 4, 6] (ترجمه: اعداد زوج در لیست)
print("Even numbers in [1,3,5]:", get_even_numbers([1, 3, 5]))
# خروجی: Even numbers in [1,3,5]: [] (ترجمه: اعداد زوج در لیست)

"""
نکته مهم:
دستور return اجرای تابع را متوقف می‌کند و نتیجه را برمی‌گرداند.
برای بررسی کامل لیست‌ها، باید return را در جای مناسب قرار دهید.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
توابع در پایتون می‌توانند چندین مقدار را به
 صورت تاپل بازگردانند که این امکان را فراهم می‌کند تا چندین نتیجه را دریافت کنید.
"""


# Return a tuple (بازگرداندن یک تاپل)
def employee_check ( work_hours ) :
	"""Finds the employee with the most hours worked.
	(یافتن کارمندی که بیشترین ساعت کار کرده است)"""
	current_max = 0
	employee_of_month = ''

	for employee , hours in work_hours :
		if hours > current_max :
			current_max = hours
			employee_of_month = employee

	return (employee_of_month , current_max)


# List of employees and their hours (لیست کارمندان و ساعت‌های کاری آن‌ها)
work_hours = [ ('Abby' , 100) , ('Billy' , 400) , ('Cassie' , 800) ]

# Get the result (دریافت نتیجه)
result = employee_check ( work_hours )
print ( "Employee of the month:" , result )  # خروجی: Employee of the month: ('Cassie', 800) (ترجمه: کارمند ماه)

# Tuple unpacking (بسته‌گشایی تاپل)
name , hours = employee_check ( work_hours )
print ( f"{name} worked {hours} hours" )  # خروجی: Cassie worked 800 hours (ترجمه: کسی 800 ساعت کار کرده است)

"""
نکات مهم درباره برگرداندن چندین مقدار:
پایتون به طور خودکار چندین مقدار را به صورت تاپل برمی‌گرداند.
می‌توانید از بسته‌گشایی تاپل (Tuple Unpacking) برای اختصاص هر مقدار به یک متغیر استفاده کنید.
این روش برای بازگرداندن چندین نتیجه از یک تابع بسیار مفید است.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
توابع اغلب از نتایج توابع دیگر استفاده می‌کنند. این تعامل بین توابع امکان ساخت برنامه‌های پیچیده‌تر را فراهم می‌کند.
"""
# Import shuffle function (وارد کردن تابع shuffle)
from random import shuffle


# Function to shuffle a list (تابع برای شافل کردن لیست)
def shuffle_list ( mylist ) :
	"""Shuffles the list in-place and returns it.
	(شافل کردن لیست در جا و بازگرداندن آن)"""
	shuffle ( mylist )
	return mylist


# Function to get player's guess (تابع برای دریافت حدس بازیکن)
def player_guess ( ) :
	"""Asks the player to guess a position (0, 1, or 2).
	(درخواست از بازیکن برای حدس زدن موقعیت (0، 1 یا 2))"""
	guess = ''
	while guess not in [ '0' , '1' , '2' ] :
		guess = input ( "Pick a number: 0, 1, or 2: " )
	return int ( guess )


# Function to check the guess (تابع برای بررسی حدس)
def check_guess ( mylist , guess ) :
	"""Checks if the guess is correct.
	(بررسی اینکه آیا حدس درست است)"""
	if mylist [ guess ] == 'O' :
		print ( 'Correct Guess!' )
	else :
		print ( 'Wrong! Better luck next time' )
		print ( mylist )


# Main game logic (منطق اصلی بازی)
def play_game ( ) :
	"""Plays the guessing game.
	(اجرای بازی حدس زدن)"""
	# Initial list with 'O' in the middle (لیست اولیه با 'O' در وسط)
	mylist = [ ' ' , 'O' , ' ' ]

	# Shuffle the list (شافل کردن لیست)
	mixedup_list = shuffle_list ( mylist )

	# Get player's guess (دریافت حدس بازیکن)
	guess = player_guess ( )

	# Check the guess (بررسی حدس)
	check_guess ( mixedup_list , guess )


# Start the game (شروع بازی)
print ( "Let's play a guessing game!" )
play_game ( )

"""
نکات مهم درباره تعامل توابع:
توابع می‌توانند نتایج یکدیگر را به عنوان ورودی دریافت کنند.
این تعامل امکان ساخت سیستم‌های پیچیده‌تر را فراهم می‌کند.
هر تابع باید یک وظیفه خاص را انجام دهد (اصل SRP - Single Responsibility Principle).
"""


"""
 نکته کلیدی:

توابع از اصلی‌ترین ابزارهای پایتون برای استفاده مجدد از کد هستند.
هر تابع باید یک وظیفه مشخص را انجام دهد.
از return برای بازگرداندن نتیجه‌ای استفاده کنید که می‌خواهید بعداً از آن استفاده کنید.
از docstring برای توضیح کار تابع استفاده کنید تا کد شما خواناتر شود.
توابع می‌توانند با یکدیگر تعامل داشته باشند و سیستم‌های پیچیده‌تر بسازند.
"""
