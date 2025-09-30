"""
برنامه‌نویسی شیء‌گرا (OOP) یکی از موانع اصلی برای مبتدیان هنگام یادگیری پایتون است. این روش برنامه‌نویسی به ما امکان می‌دهد تا کدهای ساختارمند و قابل استفاده مجدد ایجاد کنیم.

چرا OOP مهم است؟
به ما امکان می‌دهد اشیاء دنیای واقعی را در کد شبیه‌سازی کنیم.
کدها را سازمان‌یافته‌تر و خواناتر می‌کند.
از تکرار کد جلوگیری می‌کند و امکان استفاده مجدد از کد را فراهم می‌کند.
"""
# Example of built-in object (مثال از شیء داخلی)
lst = [1, 2, 3]
print("Type of list:", type(lst))  # خروجی: Type of list: <class 'list'> (ترجمه: نوع لیست)
print("Count method result:", lst.count(2))  # خروجی: Count method result: 1 (ترجمه: نتیجه متد count)
"""
نکته کلیدی:
در پایتون، همه چیز یک شیء است. این بدان معناست که هر چیزی که در پایتون استفاده می‌کنید 
(اعداد، رشته‌ها، لیست‌ها و غیره) یک شیء از یک کلاس خاص هستند.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
در پایتون، هر چیزی که استفاده می‌کنید یک شیء است. می‌توانید با تابع type() نوع هر شیء را بررسی کنید.
"""
# Checking types of different objects (بررسی انواع اشیاء مختلف)
print("Type of integer:", type(1))  # خروجی: Type of integer: <class 'int'> (ترجمه: نوع عدد صحیح)
print("Type of list:", type([]))  # خروجی: Type of list: <class 'list'> (ترجمه: نوع لیست)
print("Type of tuple:", type(()))  # خروجی: Type of tuple: <class 'tuple'> (ترجمه: نوع تاپل)
print("Type of dictionary:", type({}))  # خروجی: Type of dictionary: <class 'dict'> (ترجمه: نوع دیکشنری)

"""
چگونه اشیاء خود را بسازیم؟
برای ساخت اشیاء سفارشی، از کلیدواژه class استفاده می‌کنیم. کلاس یک چکیده‌نگار (Blueprint) است 
که تعریف می‌کند که یک شیء در آینده چه ویژگی‌ها و رفتارهایی خواهد داشت.
"""
# Creating a simple class (ایجاد یک کلاس ساده)
class Sample:
    """A simple class definition (تعریف یک کلاس ساده)"""
    pass  # Placeholder for future code (جای‌گیرنده برای کد آینده)

# Creating an instance of the class (ایجاد یک نمونه از کلاس)
x = Sample()

# Checking the type of the instance (بررسی نوع نمونه)
print("Type of x:", type(x))  # خروجی: Type of x: <class '__main__.Sample'> (ترجمه: نوع x)

"""
نکات مهم:
به طور قرارداد، نام کلاس‌ها با حرف بزرگ شروع می‌شوند.
x اکنون ارجاع به یک نمونه جدید از کلاس Sample است.
فرآیند ایجاد یک شیء از یک کلاس را نمونه‌سازی (Instantiation) می‌نامند.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
کلاس‌ها می‌توانند شامل ویژگی‌ها (Attributes) و متدها (Methods) باشند. ویژگی‌ها مشخصه‌های یک شیء هستند، 
در حالی که متدها عملیاتی هستند که می‌توان با شیء انجام داد.
"""
# Basic attribute syntax (ساختار پایه ویژگی‌ها)
# self.attribute = something (self.attribute = چیزی)

# Class definition with attributes (تعریف کلاس با ویژگی‌ها)
class Dog:
    """A Dog class with breed attribute (کلاس سگ با ویژگی نژاد)"""
    def __init__(self, breed):
        """Initialize the breed attribute (راه‌اندازی اولیه ویژگی نژاد)"""
        self.breed = breed

# Creating instances of Dog class (ایجاد نمونه‌هایی از کلاس سگ)
sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')

# Accessing attributes (دسترسی به ویژگی‌ها)
print("Sam's breed:", sam.breed)  # خروجی: Sam's breed: Lab (ترجمه: نژاد سام)
print("Frank's breed:", frank.breed)  # خروجی: Frank's breed: Huskie (ترجمه: نژاد فرانک)

"""
نکات مهم درباره ویژگی‌ها:
متد خاص __init__() به طور خودکار پس از ایجاد شیء فراخوانی می‌شود.
self به نمونه فعلی کلاس ارجاع می‌دهد و به طور قراردادی نام‌گذاری شده است.
ویژگی‌ها را بدون پرانتز فراخوانی می‌کنیم چون تابع نیستند.
"""

"""
ویژگی‌های سطح کلاس برای همه نمونه‌های کلاس یکسان هستند.
"""


# Class with class object attribute (کلاس با ویژگی سطح کلاس)
class Dog :
	"""A Dog class with class object attribute (کلاس سگ با ویژگی سطح کلاس)"""
	# Class Object Attribute (ویژگی سطح کلاس)
	species = 'mammal'

	def __init__ ( self , breed , name ) :
		"""Initialize instance attributes (راه‌اندازی اولیه ویژگی‌های نمونه)"""
		self.breed = breed
		self.name = name


# Creating an instance (ایجاد یک نمونه)
sam = Dog ( 'Lab' , 'Sam' )

# Accessing instance and class attributes (دسترسی به ویژگی‌های نمونه و کلاس)
print ( "Sam's name:" , sam.name )  # خروجی: Sam's name: Sam (ترجمه: نام سام)
print ( "Sam's species:" , sam.species )  # خروجی: Sam's species: mammal (ترجمه: گونه سام)

"""
نکات مهم درباره ویژگی‌های سطح کلاس:
ویژگی‌های سطح کلاس خارج از هر متد در کلاس تعریف می‌شوند.
به طور قرارداد، آن‌ها را قبل از __init__ قرار می‌دهیم.
برای همه نمونه‌های کلاس یکسان هستند.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
متدها توابعی هستند که در بدنه یک کلاس تعریف می‌شوند.
 آن‌ها برای انجام عملیات با ویژگی‌های اشیاء ما استفاده می‌شوند.
"""
# Circle class with methods (کلاس دایره با متدها)
class Circle:
    """A Circle class with radius and methods (کلاس دایره با شعاع و متدها)"""
    # Class Object Attribute (ویژگی سطح کلاس)
    pi = 3.14

    def __init__(self, radius=1):
        """Initialize with radius (راه‌اندازی با شعاع)"""
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def setRadius(self, new_radius):
        """Set a new radius (تعیین شعاع جدید)"""
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    def getCircumference(self):
        """Calculate circumference (محاسبه محیط)"""
        return self.radius * self.pi * 2

# Creating an instance (ایجاد یک نمونه)
c = Circle()

# Using methods and accessing attributes (استفاده از متدها و دسترسی به ویژگی‌ها)
print('Initial radius:', c.radius)  # خروجی: Initial radius: 1 (ترجمه: شعاع اولیه)
print('Initial area:', c.area)  # خروجی: Initial area: 3.14 (ترجمه: مساحت اولیه)
print('Initial circumference:', c.getCircumference())  # خروجی: Initial circumference: 6.28 (ترجمه: محیط اولیه)

# Changing radius and seeing effects (تغییر شعاع و مشاهده اثرات)
c.setRadius(2)
print('\nAfter setRadius(2):')
print('New radius:', c.radius)  # خروجی: New radius: 2 (ترجمه: شعاع جدید)
print('New area:', c.area)  # خروجی: New area: 12.56 (ترجمه: مساحت جدید)
print('New circumference:', c.getCircumference())  # خروجی: New circumference: 12.56 (ترجمه: محیط جدید)

"""
نکات مهم درباره متدها:
متدها از self برای دسترسی به ویژگی‌های نمونه استفاده می‌کنند.
در متد __init__ برای دسترسی به ویژگی سطح کلاس باید از نام کلاس استفاده کنیم (مثل Circle.pi).
در سایر متدها می‌توانیم از self.pi یا Circle.pi استفاده کنیم.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
وراثت راهی برای ایجاد کلاس‌های جدید با استفاده از کلاس‌هایی است که قبلاً تعریف شده‌اند.
 کلاس‌های جدید ایجاد شده را کلاس‌های مشتق‌شده (Derived Classes) می‌نامند
 و کلاس‌هایی که از آن‌ها مشتق می‌شوند را کلاس‌های پایه (Base Classes) می‌نامند.
"""
# Base class (کلاس پایه)
class Animal:
    """Base Animal class (کلاس پایه حیوان)"""
    def __init__(self):
        print("Animal created")  # خروجی: Animal created (ترجمه: حیوان ایجاد شد)

    def whoAmI(self):
        """Identify as Animal (شناسایی به عنوان حیوان)"""
        print("Animal")

    def eat(self):
        """Animal eating behavior (رفتار خوردن حیوان)"""
        print("Eating")

# Derived class (کلاس مشتق‌شده)
class Dog(Animal):
    """Dog class derived from Animal (کلاس سگ مشتق‌شده از حیوان)"""
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")  # خروجی: Dog created (ترجمه: سگ ایجاد شد)

    def whoAmI(self):
        """Override parent method (بازتعریف متد والد)"""
        print("Dog")

    def bark(self):
        """Dog-specific method (متد خاص سگ)"""
        print("Woof!")

# Creating an instance of Dog (ایجاد یک نمونه از سگ)
d = Dog()

# Using methods from base and derived classes (استفاده از متدها از کلاس پایه و مشتق‌شده)
print("\nCalling methods:")
d.whoAmI()  # خروجی: Dog (ترجمه: سگ)
d.eat()  # خروجی: Eating (ترجمه: در حال خوردن)
d.bark()  # خروجی: Woof! (ترجمه: ووف!)

"""
مزایای وراثت:
استفاده مجدد از کد: کلاس مشتق‌شده از ویژگی‌ها و متدهای کلاس پایه استفاده می‌کند.
کاهش پیچیدگی: کد تمیزتر و سازمان‌یافته‌تری ایجاد می‌شود.
توسعه رفتار: کلاس مشتق‌شده می‌تواند رفتار کلاس پایه را تغییر دهد یا گسترش دهد.
انواع رفتار در وراثت:
وراثت رفتار: کلاس مشتق‌شده از رفتار کلاس پایه استفاده می‌کند (مثل متد eat()).
بازتعریف رفتار: کلاس مشتق‌شده رفتار کلاس پایه را تغییر می‌دهد (مثل متد whoAmI()).
توسعه رفتار: کلاس مشتق‌شده رفتار جدیدی اضافه می‌کند (مثل متد bark()).
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
در پایتون، چندشکلی به این معناست که کلاس‌های مختلف می‌توانند از نام متد یکسان استفاده کنند و
 این متدها می‌توانند از همان مکان فراخوانی شوند، حتی اگر اشیاء متفاوتی به آن‌ها ارسال شود.
"""
# Polymorphism example with Dog and Cat (مثال چندشکلی با سگ و گربه)
class Dog:
    """Dog class with speak method (کلاس سگ با متد speak)"""
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Dog-specific speak method (متد speak خاص سگ)"""
        return self.name + ' says Woof!'

class Cat:
    """Cat class with speak method (کلاس گربه با متد speak)"""
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Cat-specific speak method (متد speak خاص گربه)"""
        return self.name + ' says Meow!'

# Creating instances (ایجاد نمونه‌ها)
niko = Dog('Niko')
felix = Cat('Felix')

# Calling same method on different objects (فراخوانی متد یکسان روی اشیاء مختلف)
print(niko.speak())  # خروجی: Niko says Woof! (ترجمه: نیکو ووف می‌گوید!)
print(felix.speak())  # خروجی: Felix says Meow! (ترجمه: فلیکس میاؤ می‌گوید!)

"""
روش‌های نمایش چندشکلی:
1. با استفاده از حلقه for
2. با استفاده از توابع
کلاس‌های انتزاعی (Abstract Classes)
یک روش رایج‌تر برای نمایش چندشکلی، استفاده از کلاس‌های انتزاعی و وراثت است.
 کلاس انتزاعی کلاسی است که هرگز انتظار نمی‌رود نمونه‌سازی شود.
"""
# Polymorphism with for loop (چندشکلی با حلقه for)
for pet in [niko, felix]:
    print(pet.speak())
# خروجی:
# Niko says Woof!
# Felix says Meow!
# (ترجمه: چندشکلی با حلقه for)
#----------------------------------------------
# Polymorphism with functions (چندشکلی با توابع)
def pet_speak(pet):
    """Function that works with any pet object (تابعی که با هر شیء حیوان خانگی کار می‌کند)"""
    print(pet.speak())

pet_speak(niko)  # خروجی: Niko says Woof! (ترجمه: نیکو ووف می‌گوید!)
pet_speak(felix)  # خروجی: Felix says Meow! (ترجمه: فلیکس میاؤ می‌گوید!)
#----------------------------------------------
# Abstract class example (مثال کلاس انتزاعی)
class Animal:
    """Abstract Animal class (کلاس انتزاعی حیوان)"""
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Abstract method (متد انتزاعی)"""
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    """Dog implementation of Animal (پیاده‌سازی سگ از حیوان)"""
    def speak(self):
        return self.name + ' says Woof!'

class Cat(Animal):
    """Cat implementation of Animal (پیاده‌سازی گربه از حیوان)"""
    def speak(self):
        return self.name + ' says Meow!'

# Creating instances (ایجاد نمونه‌ها)
fido = Dog('Fido')
isis = Cat('Isis')

# Using polymorphism (استفاده از چندشکلی)
print(fido.speak())  # خروجی: Fido says Woof! (ترجمه: فیدو ووف می‌گوید!)
print(isis.speak())  # خروجی: Isis says Meow! (ترجمه: ایسیس میاؤ می‌گوید!)

"""
مثال‌های واقعی چندشکلی:
باز کردن فایل‌های مختلف - ابزارهای مختلف برای نمایش فایل‌های Word، pdf و Excel مورد نیاز است.
جمع اشیاء مختلف - عملگر + برای انجام محاسبات ریاضی و الحاق رشته‌ها استفاده می‌شود.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
کلاس‌ها در پایتون می‌توانند متدهای ویژه را با نام‌های خاص پیاده‌سازی کنند. این متدها در واقع
 به طور مستقیم فراخوانی نمی‌شوند، بلکه توسط سینتکس خاص زبان پایتون فراخوانی می‌شوند.
"""
# Book class with special methods (کلاس کتاب با متدهای ویژه)
class Book:
    """Book class with special methods (کلاس کتاب با متدهای ویژه)"""
    def __init__(self, title, author, pages):
        """Constructor method (متد سازنده)"""
        print("A book is created")  # خروجی: A book is created (ترجمه: یک کتاب ایجاد شد)
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """String representation (نمایش رشته‌ای)"""
        return "Title: %s, author: %s, pages: %s" % (self.title, self.author, self.pages)

    def __len__(self):
        """Length representation (نمایش طول)"""
        return self.pages

    def __del__(self):
        """Destructor method (متد تخریب‌کننده)"""
        print("A book is destroyed")  # خروجی: A book is destroyed (ترجمه: یک کتاب تخریب شد)

# Creating an instance (ایجاد یک نمونه)
book = Book("Python Rocks!", "Jose Portilla", 159)

# Using special methods (استفاده از متدهای ویژه)
print("\nSpecial Methods:")
print("String representation:", book)  # خروجی: String representation: Title: Python Rocks!, author: Jose Portilla, pages: 159 (ترجمه: نمایش رشته‌ای)
print("Length of book:", len(book))  # خروجی: Length of book: 159 (ترجمه: طول کتاب)

# Deleting the object (حذف شیء)
del book

"""
متدهای ویژه رایج:
__init__() - متد سازنده که هنگام ایجاد شیء فراخوانی می‌شود.
__str__() - برای نمایش رشته‌ای شیء هنگام استفاده از print().
__len__() - برای تعیین طول شیء هنگام استفاده از len().
__del__() - متد تخریب‌کننده که هنگام حذف شیء فراخوانی می‌شود.

نکات مهم درباره متدهای ویژه:
این متدها با استفاده از زیرخط (underscore) تعریف می‌شوند.
آن‌ها به ما امکان می‌دهند تا از توابع خاص پایتون روی اشیاء ساخته شده از کلاس خودمان استفاده کنیم.
هر متد ویژه برای یک عملکرد خاص در پایتون طراحی شده است.
"""


"""
نکته کلیدی:

در پایتون، همه چیز یک شیء است.
کلاس‌ها چکیده‌نگار (Blueprint) برای ایجاد اشیاء هستند.
ویژگی‌ها مشخصه‌های شیء و متدها عملیات قابل انجام روی شیء هستند.
وراثت امکان استفاده مجدد از کد و توسعه رفتار را فراهم می‌کند.
چندشکلی به اشیاء مختلف اجازه می‌دهد از روش‌های یکسانی استفاده کنند.
متدهای ویژه امکان تعامل با سینتکس پایتون را فراهم می‌کنند.
"""