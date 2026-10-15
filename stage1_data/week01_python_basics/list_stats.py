# list_stats.py —— 给一个数字列表，输出最大值、最小值、平均值、中位数
# 不使用 numpy，只用 Python 内置函数。
# 使用示例：
#   python list_stats.py

def mean(nums):
    """平均值"""
    return sum(nums) / len(nums)


def median(nums):
    """中位数：先排序，奇数个取中间，偶数个取中间两个的平均。"""
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:          # 奇数个
        return sorted_nums[mid]
    else:                   # 偶数个
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2


def main():
    nums = [5, 3, 8, 1, 9, 2, 7, 4]  # 测试用的数字列表（可随意换）
    print(f"数字列表: {nums}")
    print(f"最大值:   {max(nums)}")
    print(f"最小值:   {min(nums)}")
    print(f"平均值:   {mean(nums):.2f}")
    print(f"中位数:   {median(nums)}")


if __name__ == "__main__":
    main()
