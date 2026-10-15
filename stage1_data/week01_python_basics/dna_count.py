# dna_count.py —— 统计一段 DNA 字符串中 A/T/G/C 各出现多少次及百分比
# 使用示例：
#   python dna_count.py

def count_dna(seq):
    """统计 DNA 字符串中 A/T/G/C 的数量，返回字典。"""
    counts = {"A": 0, "T": 0, "G": 0, "C": 0}
    for base in seq.upper():
        if base in counts:
            counts[base] += 1
    return counts


def main():
    seq = "ATGCGTACGATC"  # 测试用的 DNA 序列（你自己可以换成任意一段）
    counts = count_dna(seq)
    total = len(seq)

    print(f"DNA 序列: {seq}")
    print(f"总长度: {total} bp")
    print("碱基统计:")
    for base in "ATGC":
        num = counts[base]
        pct = num / total * 100
        print(f"  {base}: {num} 次, 占 {pct:.2f}%")


if __name__ == "__main__":
    main()
