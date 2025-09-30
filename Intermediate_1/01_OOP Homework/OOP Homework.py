"""
در این تمرین، ما با استفاده از مفاهیم برنامه‌نویسی شیء‌گرا (OOP) دو کلاس ساده اما مفید را پیاده‌سازی خواهیم کرد.
 این تمرین به شما کمک می‌کند تا درک بهتری از نحوه تعریف کلاس‌ها، ویژگی‌ها و متدها در پایتون داشته باشید.

چرا این تمرین مهم است؟
به شما کمک می‌کند تا با ساختار کلاس‌ها آشنا شوید.
نحوه تعریف ویژگی‌ها و متدها را تمرین می‌کنید.
از مفاهیم ریاضی ساده برای درک بهتر OOP استفاده می‌کند.

نکته کلیدی:
در برنامه‌نویسی شیء‌گرا، کلاس‌ها چکیده‌نگار (Blueprint) برای ایجاد اشیاء هستند
و اشیاء دارای ویژگی‌ها (Attributes) و متدها (Methods) هستند.
"""

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
کلاس خط (Problem 1: Line Class)
در این مسئله، باید یک کلاس به نام Line ایجاد کنیم که مختصات دو نقطه را به عنوان ورودی دریافت کند و بتواند فاصله و شیب خط را محاسبه کند.
"""

# # Define the Line class (تعریف کلاس خط)
# class Line ( object ) :
# 	"""A class to represent a line between two points (کلاسی برای نمایش خط بین دو نقطه)"""
#
# 	def __init__ ( self , coor1 , coor2 ) :
# 		"""Initialize the line with two coordinates (راه‌اندازی خط با دو مختصات)"""
# 		self.coor1 = coor1  # First coordinate as tuple (مختصات اول به صورت تاپل)
# 		self.coor2 = coor2  # Second coordinate as tuple (مختصات دوم به صورت تاپل)
# """
# متد __init__ سازنده کلاس است و هنگام ایجاد یک شیء جدید فراخوانی می‌شود.
# این متد دو مختصات را به عنوان ورودی دریافت کرده و آن‌ها را به عنوان ویژگی‌های شیء ذخیره می‌کند.
# """
# # Example of creating a Line object (مثال ایجاد یک شیء خط)
# coordinate1 = (3, 2)  # First point (x=3, y=2) (نقطه اول)
# coordinate2 = (8, 10)  # Second point (x=8, y=10) (نقطه دوم)
# li = Line(coordinate1, coordinate2)  # Create a Line object (ایجاد یک شیء خط)
#
# print("First coordinate:", li.coor1)  # خروجی: First coordinate: (3, 2) (ترجمه: مختصات اول)
# print("Second coordinate:", li.coor2)  # خروجی: Second coordinate: (8, 10) (ترجمه: مختصات دوم)


"""
این متد فاصله بین دو نقطه را با استفاده از فرمول فاصله اقلیدسی محاسبه می‌کند:
distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
"""
# # Add distance method to Line class (افزودن متد distance به کلاس خط)
# class Line ( object ) :
# 	def __init__ ( self , coor1 , coor2 ) :
# 		self.coor1 = coor1
# 		self.coor2 = coor2
#
# 	def distance ( self ) :
# 		"""Calculate the Euclidean distance between two points (محاسبه فاصله اقلیدسی بین دو نقطه)"""
# 		x1 , y1 = self.coor1  # Unpack first coordinate (بسته‌گشایی مختصات اول)
# 		x2 , y2 = self.coor2  # Unpack second coordinate (بسته‌گشایی مختصات دوم)
# 		return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Square root (جذر)
#
#
# # Create line and calculate distance (ایجاد خط و محاسبه فاصله)
# li = Line ( (3 , 2) , (8 , 10) )
# print ( "Distance between points:" , li.distance ( ) )
# # خروجی: Distance between points: 9.433981132056603 (ترجمه: فاصله بین نقاط)


"""
این متد شیب خط را با استفاده از فرمول شیب محاسبه می‌کند:
slope = (y2 - y1) / (x2 - x1)
"""
# # Add slope method to Line class (افزودن متد slope به کلاس خط)
# class Line ( object ) :
# 	def __init__ ( self , coor1 , coor2 ) :
# 		self.coor1 = coor1
# 		self.coor2 = coor2
#
# 	def distance ( self ) :
# 		x1 , y1 = self.coor1
# 		x2 , y2 = self.coor2
# 		return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
# 	def slope ( self ) :
# 		"""Calculate the slope of the line (محاسبه شیب خط)"""
# 		x1 , y1 = self.coor1  # Unpack coordinates (بسته‌گشایی مختصات)
# 		x2 , y2 = self.coor2
# 		return (y2 - y1) / (x2 - x1)  # Slope formula (فرمول شیب)
#
#
# # Create line and calculate slope (ایجاد خط و محاسبه شیب)
# li = Line ( (3 , 2) , (8 , 10) )
# print ( "Slope of the line:" , li.slope ( ) )
# # خروجی: Slope of the line: 1.6 (ترجمه: شیب خط)

"""
نکات مهم درباره کلاس خط:
ما از self برای دسترسی به ویژگی‌های نمونه استفاده می‌کنیم.
با استفاده از بسته‌گشایی تاپل (x1, y1 = self.coor1)، مختصات را به راحتی استخراج می‌کنیم.
این کلاس نمونه‌ای ساده از استفاده از OOP برای حل مسائل ریاضی است.
"""

# Complete Line class (کلاس کامل خط)
class Line ( object ) :
	"""Complete Line class with distance and slope methods (کلاس کامل خط با متدهای فاصله و شیب)"""

	def __init__ ( self , coor1 , coor2 ) :
		"""Initialize with two coordinates (راه‌اندازی با دو مختصات)"""
		self.coor1 = coor1
		self.coor2 = coor2

	def distance ( self ) :
		"""Calculate Euclidean distance (محاسبه فاصله اقلیدسی)"""
		x1 , y1 = self.coor1
		x2 , y2 = self.coor2
		return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

	def slope ( self ) :
		"""Calculate slope of the line (محاسبه شیب خط)"""
		x1 , y1 = self.coor1
		x2 , y2 = self.coor2
		return (y2 - y1) / (x2 - x1)


# Test the Line class (تست کلاس خط)
coordinate1 = (3 , 2)
coordinate2 = (8 , 10)
li = Line ( coordinate1 , coordinate2 )

print ( "Testing Line class:" )
print ( "Distance:" , li.distance ( ) )  # خروجی: Distance: 9.433981132056603 (ترجمه: فاصله)
print ( "Slope:" , li.slope ( ) )  # خروجی: Slope: 1.6 (ترجمه: شیب)

# -----------------------------------------------------------------------------------------------------
print("-" * 80)
"""
در این مسئله، باید یک کلاس به
 نام Cylinder ایجاد کنیم که ارتفاع و شعاع استوانه را به عنوان ورودی دریافت کند
 و بتواند حجم و مساحت سطح استوانه را محاسبه کند.
"""
# # Define the Cylinder class (تعریف کلاس استوانه)
# class Cylinder :
# 	"""A class to represent a cylinder (کلاسی برای نمایش استوانه)"""
#
# 	def __init__ ( self , height = 1 , radius = 1 ) :
# 		"""Initialize the cylinder with height and radius (راه‌اندازی استوانه با ارتفاع و شعاع)"""
# 		self.height = height  # Height of cylinder (ارتفاع استوانه)
# 		self.radius = radius  # Radius of cylinder (شعاع استوانه)


"""
متد init
متد __init__ سازنده کلاس استوانه است و
 دو پارامتر اختیاری height و radius را دریافت می‌کند که مقادیر پیش‌فرض 1 دارند.
"""
# # Example of creating Cylinder objects (مثال ایجاد اشیاء استوانه)
# c1 = Cylinder()  # Default values (مقادیر پیش‌فرض)
# c2 = Cylinder(2, 3)  # Custom values (مقادیر سفارشی)
#
# print("Default height:", c1.height)  # خروجی: Default height: 1 (ترجمه: ارتفاع پیش‌فرض)
# print("Default radius:", c1.radius)  # خروجی: Default radius: 1 (ترجمه: شعاع پیش‌فرض)
# print("Custom height:", c2.height)  # خروجی: Custom height: 2 (ترجمه: ارتفاع سفارشی)
# print("Custom radius:", c2.radius)  # خروجی: Custom radius: 3 (ترجمه: شعاع سفارشی)


"""
متد volume
این متد حجم استوانه را با استفاده از فرمول زیر محاسبه می‌کند:
volume = π * radius^2 * height
"""
# # Add volume method to Cylinder class (افزودن متد volume به کلاس استوانه)
# class Cylinder :
# 	def __init__ ( self , height = 1 , radius = 1 ) :
# 		self.height = height
# 		self.radius = radius
#
# 	def volume ( self ) :
# 		"""Calculate the volume of the cylinder (محاسبه حجم استوانه)"""
# 		return self.height * 3.14 * (self.radius) ** 2  # π * r^2 * h
#
#
# # Create cylinder and calculate volume (ایجاد استوانه و محاسبه حجم)
# c = Cylinder ( 2 , 3 )
# print ( "Volume of cylinder:" , c.volume ( ) )
#
#
# # خروجی: Volume of cylinder: 56.52 (ترجمه: حجم استوانه)


"""
متد surface_area
این متد مساحت سطح استوانه را با استفاده از فرمول زیر محاسبه می‌کند:
surface_area = 2 * π * radius^2 + 2 * π * radius * height
که شامل مساحت دو دایره (بالا و پایین) و مساحت جانبی است.
"""
# # Add surface_area method to Cylinder class (افزودن متد surface_area به کلاس استوانه)
# class Cylinder :
# 	def __init__ ( self , height = 1 , radius = 1 ) :
# 		self.height = height
# 		self.radius = radius
#
# 	def volume ( self ) :
# 		return self.height * 3.14 * (self.radius) ** 2
#
# 	def surface_area ( self ) :
# 		"""Calculate the surface area of the cylinder (محاسبه مساحت سطح استوانه)"""
# 		top = 3.14 * (self.radius) ** 2  # Area of top circle (مساحت دایره بالایی)
# 		return (2 * top) + (2 * 3.14 * self.radius * self.height)  # Total surface area (مساحت کل)
#
#
# # Create cylinder and calculate surface area (ایجاد استوانه و محاسبه مساحت سطح)
# c = Cylinder ( 2 , 3 )
# print ( "Surface area of cylinder:" , c.surface_area ( ) )
# # خروجی: Surface area of cylinder: 94.2 (ترجمه: مساحت سطح استوانه)


"""
نکات مهم درباره کلاس استوانه:
ما از مقدار تقریبی π = 3.14 استفاده کردیم (در عمل می‌توان از math.pi استفاده کرد).
متد surface_area به طور هوشمندانه از مساحت دایره بالایی برای محاسبه مساحت کل استفاده می‌کند.
این کلاس نمونه‌ای از استفاده از OOP برای مدل‌سازی اشیاء سه‌بعدی است.
"""

# Complete Cylinder class (کلاس کامل استوانه)
class Cylinder :
	"""Complete Cylinder class with volume and surface area methods (کلاس کامل استوانه با متدهای حجم و مساحت سطح)"""

	def __init__ ( self , height = 1 , radius = 1 ) :
		"""Initialize with height and radius (راه‌اندازی با ارتفاع و شعاع)"""
		self.height = height
		self.radius = radius

	def volume ( self ) :
		"""Calculate volume (محاسبه حجم)"""
		return self.height * 3.14 * (self.radius) ** 2

	def surface_area ( self ) :
		"""Calculate surface area (محاسبه مساحت سطح)"""
		top = 3.14 * (self.radius) ** 2
		return (2 * top) + (2 * 3.14 * self.radius * self.height)


# Test the Cylinder class (تست کلاس استوانه)
c = Cylinder ( 2 , 3 )

print ( "\nTesting Cylinder class:" )
print ( "Volume:" , c.volume ( ) )  # خروجی: Volume: 56.52 (ترجمه: حجم)
print ( "Surface Area:" , c.surface_area ( ) )  # خروجی: Surface Area: 94.2 (ترجمه: مساحت سطح)


"""
نکات کلیدی برای تمرین‌های OOP:
همیشه با تعریف واضح کلاس شروع کنید.
متد __init__ برای راه‌اندازی اولیه ویژگی‌ها استفاده می‌شود.
متدها باید منطقی و مرتبط با کلاس باشند.
برای محاسبات پیچیده‌تر، از کتابخانه‌های استاندارد پایتون (مثل math) استفاده کنید.
تست کردن کلاس‌ها با مقادیر مختلف بسیار مهم است.
"""

"""
درک کامل از برنامه‌نویسی شیء‌گرا به شما کمک می‌کند
 تا کدهای ساختارمندتر، خواناتر و قابل استفاده مجدد ایجاد کنید.
 با تمرین بیشتر، شما می‌توانید کلاس‌های پیچیده‌تری برای مدل‌سازی اشیاء واقعی ایجاد کنید.
"""
