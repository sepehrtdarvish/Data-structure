# جدول هش با زنجیره‌سازی
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # ایجاد لیست‌هایی برای زنجیره‌سازی

    # تابع هش با روش تقسیم
    def hash_function(self, key):
        return key % self.size

    # افزودن یک جفت کلید-مقدار به جدول
    def insert(self, key, value):
        index = self.hash_function(key)  # محاسبه اندیس
        for pair in self.table[index]:
            if pair[0] == key:  # اگر کلید قبلاً وجود داشت، مقدار را به‌روزرسانی کن
                pair[1] = value
                return
        self.table[index].append([key, value])  # اگر کلید جدید است، به لیست اضافه کن

    # جستجوی مقدار بر اساس کلید
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # مقدار مرتبط با کلید را برگردان
        return None  # اگر کلید پیدا نشد

    # حذف یک کلید-مقدار
    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)  # کلید-مقدار را حذف کن
                return True
        return False  # اگر کلید پیدا نشد

    # نمایش جدول هش
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# مثال: استفاده از جدول هش
hash_table = HashTable(size=7)  # جدول هش با 7 سطل

# درج داده‌ها
hash_table.insert(10, "Data A")
hash_table.insert(20, "Data B")
hash_table.insert(15, "Data C")
hash_table.insert(17, "Data D")  # برخورد به‌خاطر هش برابر با 3
hash_table.insert(3, "Data E")   # برخورد به‌خاطر هش برابر با 3

# نمایش جدول
print("Initial Hash Table:")
hash_table.display()

# جستجو در جدول
print("\nSearch for key 15:", hash_table.search(15))  # پیدا می‌شود
print("Search for key 99:", hash_table.search(99))  # پیدا نمی‌شود

# حذف یک کلید
hash_table.delete(17)
print("\nAfter deleting key 17:")
hash_table.display()
