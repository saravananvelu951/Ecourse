from django import template

register = template.Library()

@register.filter(name="incart")
def incart(course,cart):
    keys = cart.keys()
    #print(keys)
    for key in keys:
        if int(key) ==course.id:
            return True
    return False

@register.filter(name="cart_quantity")
def cart_quantity(course,cart):
    keys = cart.keys()
    #print(keys)
    for key in keys:
        if int(key) ==course.id:
            return cart.get(key)
    return False

@register.filter(name="total_price")
def total_price(course,cart):
    return course.course_price * cart_quantity(course,cart)

@register.filter(name="payable_amount")
def payable_amount(course,cart):
    total = 0
    for i in course: 
        total = total + total_price(i,cart)
    return total

@register.filter(name="order_total_price")
def order_total_price(price,quantity):
    
    return price * quantity  
