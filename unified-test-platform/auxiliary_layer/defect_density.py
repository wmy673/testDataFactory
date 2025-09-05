def calculate_defect_density(defect_count: int, code_size: int) -> float:
    """
    计算缺陷密度（Defect Density）。
    缺陷密度 = 缺陷数量 / 代码规模（通常以千行代码KLOC为单位）

    :param defect_count: 缺陷数量
    :param code_size: 代码规模（以行数为单位）
    :return: 缺陷密度（每千行代码的缺陷数）
    """
    if code_size <= 0:
        raise ValueError("代码规模必须大于0")
    kloc = code_size / 1000  # 转换为千行代码
    return defect_count / kloc

# 示例用法
if __name__ == "__main__":
    defects = 10
    lines_of_code = 5000
    density = calculate_defect_density(defects, lines_of_code)
    print(f"缺陷密度为: {density:.2f} 个缺陷/KLOC")
