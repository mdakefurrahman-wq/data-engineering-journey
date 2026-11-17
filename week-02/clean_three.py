raw_a = "  ord100047 ;2026-10-08;  Tanvir Hossain  ; Dim 12pc ;3; ৳ 441.75 ; Cash on Delivery ;DELIVERED"
raw_b = "ORD100048 ; 2026-10-08 ; SUMAIYA  KHAN ; Ilish 1kg ;1;৳ 1,520.00; bkash ; cancelled"
raw_c = "ord100049;2026-10-09; rakib  mia ;Broiler Murgi 1kg; 4 ;৳ 812.00;Card;delivered" 


"""
TODO 

ধাপ	কী	কীভাবে
১	আটটা টুকরোয় ভাগ	.split(";")
২	ফাঁকা জায়গা মুছুন	প্রতিটায় .strip()
৩	হাতের অক্ষর	id .upper(), নাম .title(), payment আর status .lower()
৪	সংখ্যায় বদলান	quantity → int, amount → ৳ আর কমা সরিয়ে float
৫	হিসাব	প্রতি ইউনিটের দাম = মোট ÷ পরিমাণ
৬	ছাপান	চার লাইনের f-string
"""


def clean_order(raw):
    """Clean one semicolon-delimited raw order string."""
    order_id, date, customer_name, item, quantity, amount, payment, status = (
        part.strip() for part in raw.split(";")
    )

    order_id = order_id.upper()
    customer_name = customer_name.title()
    payment = payment.lower()
    status = status.lower()
    quantity = int(quantity)
    amount = float(amount.replace("৳", "").replace(",", "").strip())

    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")

    unit_price = amount / quantity
    return {
        "order_id": order_id,
        "date": date,
        "customer_name": customer_name,
        "item": item,
        "quantity": quantity,
        "amount": amount,
        "unit_price": unit_price,
        "payment": payment,
        "status": status,
    }


for index, raw in enumerate((raw_a, raw_b, raw_c)):
    order = clean_order(raw)
    print(
        f"{order['order_id']}  ·  {order['date']}\n"
        f"{order['customer_name']} কিনেছেন {order['item']} — {order['quantity']}টা\n"
        f"মোট ৳{order['amount']:,.2f}  (প্রতিটা ৳{order['unit_price']:,.2f})\n"
        f"পেমেন্ট: {order['payment']}  ·  অবস্থা: {order['status']}"
    )
    if index < 2:
        print()


