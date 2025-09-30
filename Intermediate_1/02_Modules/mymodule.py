# Contents of mymodule.py (محتوای mymodule.py)
"""
This is a custom module for demonstration purposes.
(این یک ماژول سفارشی برای اهداف نمایشی است)
"""

def greet(name):
    """Returns a greeting message.
    (بازگرداندن پیام سلام)"""
    return f"Hello, {name}!"

def calculate_square(num):
    """Calculates the square of a number.
    (محاسبه مربع یک عدد)"""
    return num * num

# This code runs only when the module is executed directly
# (این کد فقط هنگامی اجرا می‌شود که ماژول به صورت مستقیم اجرا شود)
if __name__ == "__main__":
    print("This module is being run directly")
    print(greet("User"))
    print("Square of 5:", calculate_square(5))