def calculate_code_coverage(covered_lines: int, total_lines: int) -> float:
    """
    计算代码覆盖率（Code Coverage）。
    代码覆盖率 = 被覆盖的代码行数 / 代码总行数

    :param covered_lines: 被测试覆盖的代码行数
    :param total_lines: 代码总行数
    :return: 覆盖率（百分比，0~100）
    """
    if total_lines <= 0:
        raise ValueError("代码总行数必须大于0")
    coverage = (covered_lines / total_lines) * 100
    return coverage

# 示例用法
if __name__ == "__main__":
    covered = 450
    total = 500
    coverage = calculate_code_coverage(covered, total)
    print(f"代码覆盖率为: {coverage:.2f}%") 
