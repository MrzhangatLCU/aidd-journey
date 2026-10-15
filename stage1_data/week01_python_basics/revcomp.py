# revcomp.py —— 输出一段 DNA 序列的反向互补序列
# 规则：
#   互补: A<->T, G<->C
#   反向互补: 先反向，再逐个取互补（或先互补再反向，结果相同）
# 过关测试: "ATGC" -> "GCAT"
# 使用示例：
#   python revcomp.py

# 互补配对表
COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}


def reverse_complement(seq):
    """返回 DNA 序列的反向互补序列。"""
    seq = seq.upper()
    # 用列表推导式：取每个碱基的互补，再反转顺序
    return "".join(COMPLEMENT[base] for base in reversed(seq))


def main():
    seq = "ATGC"  # 测试序列，对应过关标准 "GCAT"
    result = reverse_complement(seq)
    print(f"原序列:       {seq}")
    print(f"反向互补序列: {result}")
    # 自检：结果应等于 GCAT
    assert result == "GCAT", "反向互补结果不正确！"


if __name__ == "__main__":
    main()
