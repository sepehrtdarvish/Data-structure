class DisjointSet:
    def __init__(self, size):
        # مقداردهی اولیه آرایه والد
        self.parent = [-1] * size

    def find(self, i):
        # تابع پیدا کردن ریشه مجموعه
        if self.parent[i] == -1:
            return i
        # بهینه‌سازی با فشرده‌سازی مسیر
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        # ترکیب دو مجموعه
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x


# بررسی وجود حلقه در گراف با استفاده از Union-Find
def contains_cycle(edges, num_nodes):
    ds = DisjointSet(num_nodes)

    for edge in edges:
        x, y = edge
        # اگر دو گره به یک مجموعه تعلق دارند، حلقه پیدا شده است
        if ds.find(x) == ds.find(y):
            return True
        ds.union(x, y)
    
    return False


# مثال استفاده
edges = [(0, 1), (1, 2), (0, 2)]  # لیست یال‌ها
num_nodes = 3  # تعداد رئوس گراف

if contains_cycle(edges, num_nodes):
    print("گراف شامل حلقه است.")
else:
    print("گراف شامل حلقه نیست.")
