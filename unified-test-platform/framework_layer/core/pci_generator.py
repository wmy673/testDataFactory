import random
import string

def generate_pci(length: int = 16, prefix: str = "") -> str:
    """
    生成指定长度的伪 PCI（主键/唯一标识符），可选前缀。

    :param length: PCI 总长度（包含前缀），默认16
    :param prefix: 可选前缀字符串
    :return: 生成的 PCI 字符串
    """
    if length <= len(prefix):
        raise ValueError("PCI 长度必须大于前缀长度")
    # 只包含大写字母和数字
    chars = string.ascii_uppercase + string.digits
    body_len = length - len(prefix)
    body = ''.join(random.choices(chars, k=body_len))
    return prefix + body

# 示例用法
if __name__ == "__main__":
    pci = generate_pci()
    print("生成的PCI:", pci)
    pci2 = generate_pci(length=20, prefix="UTP-")
    print("带前缀的PCI:", pci2)
