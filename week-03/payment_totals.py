#!/usr/bin/env python3
"""
অ্যাসাইনমেন্ট ৫ — শুরু করার ফাইল

ভয় পাবেন না। এই ফাইলটা এখনই চলে — চালিয়ে দেখুন:

    python3 module-03/assignments/class-05-starter.py

শূন্য দেখাবে। আপনার কাজ ওই শূন্যগুলোকে আসল সংখ্যায় বদলানো।

তিনটা লেভেল আছে। লেভেল ১ সবার জন্য। ওটুকু হলেই জমা দিতে পারবেন।
পারলে ২, তারপর ৩।
"""

import os
import my_tools

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE_DIR, "data", "raw_sales.txt")


def main():
    PATH = os.path.join("data", "raw_sales.txt")

    with open(PATH, encoding="utf-8") as fh:
        lines = fh.read().strip().split("\n")

    # ============================================================
    #  লেভেল ১ — শুধু bkash
    #  লক্ষ্য:  bkash  3টা  ৳2484.00
    # ============================================================

    bkash_total = 0.0
    bkash_count = 0
    nagad_total = 0.0
    nagad_count = 0
    card_total = 0.0
    card_count = 0
    rocket_total = 0.0
    rocket_count = 0
    cod_total = 0.0
    cod_count = 0

    for raw in lines:
        parts = raw.split(";")
        amount = float(parts[5].strip().replace("৳", "").replace(",", ""))
        payment = parts[6].strip().lower()
        status = parts[7].strip().lower()

        # TODO ১: বাতিল অর্ডার বাদ দিন
        if status == "cancelled":
            # print(f"বাতিল অর্ডার বাদ দিলাম: {raw}")
            continue

        # TODO ২: payment অনুযায়ী যোগ করুন
        if payment == "bkash":
            bkash_total = bkash_total + amount
            bkash_count = bkash_count + 1
        elif payment == "nagad":
            nagad_total = nagad_total + amount
            nagad_count = nagad_count + 1
        elif payment == "card":
            card_total = card_total + amount
            card_count = card_count + 1
        elif payment == "rocket":
            rocket_total = rocket_total + amount
            rocket_count = rocket_count + 1
        elif payment == "cash on delivery":
            cod_total = cod_total + amount
            cod_count = cod_count + 1

   
    print("লেভেল ১")
    print(f"bkash  {bkash_count}টা  ৳{bkash_total:.2f}")
    print(f"nagad  {nagad_count}টা  ৳{nagad_total:.2f}")
    print(f"card   {card_count}টা  ৳{card_total:.2f}")
    print(f"rocket {rocket_count}টা  ৳{rocket_total:.2f}")
    print(f"cash on delivery {cod_count}টা  ৳{cod_total:.2f}")

    print("সব মিলিয়ে ৳{:.2f}".format(bkash_total + nagad_total + card_total + rocket_total + cod_total))

    print("লেভেল 2 & 3")
    print("sales_tools — পরীক্ষা")
    print(my_tools.clean_id("  ord100045 "))
    print(my_tools.clean_name("  RAHIM  uddin "))
    print(my_tools.clean_name("mim   begum"))
    print(my_tools.clean_amount(" ৳ 1,240.50 "))
    print(my_tools.taka(1240.5))
    print(my_tools.is_cancelled(" CANCELLED "))



if __name__ == "__main__":
    main()
