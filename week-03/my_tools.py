def clean_id(text):
    """ঘরের আগে-পরের ফাঁকা জায়গা মুছে, সব বড় হাতের করে ফেরত দেয়।

    "  ord100045 "  →  "ORD100045"
    """
    return text.strip().upper()


def clean_name(text):
    """নামের বাড়তি স্পেস সরিয়ে, প্রতি শব্দের প্রথম অক্ষর বড় করে দেয়।

    "  RAHIM  uddin "  →  "Rahim Uddin"
    "mim   begum"      →  "Mim Begum"
    """
    return " ".join(text.strip().title().split())


def clean_amount(text):
    """৳ আর কমা সরিয়ে টাকার অঙ্কটা সংখ্যায় ফেরত দেয়।

    " ৳ 1,240.50 "  →  1240.5
    """
    text = text.replace("৳", "").replace(",", "").strip()
    return float(text)


def taka(value):
    """সংখ্যাটাকে টাকার চেহারায় সাজিয়ে দেয়।

    1240.5  →  "৳1240.50"
    """
    return f"৳{value:.2f}"


def is_cancelled(status):
    """অর্ডারটা বাতিল কি না — True বা False ফেরত দেয়।"""
    return status.strip().lower() == "cancelled"

if __name__ == "__main__":
    print("sales_tools — পরীক্ষা")
    print(clean_id("  ord100045 "))
    print(clean_name("  RAHIM  uddin "))
    print(clean_name("mim   begum"))
    print(clean_amount(" ৳ 1,240.50 "))
    print(taka(1240.5))
    print(is_cancelled(" CANCELLED "))