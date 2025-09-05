import os
from typing import BinaryIO

def save_upload_file(upload_file: BinaryIO, save_path: str, chunk_size: int = 8192) -> None:
    """
    保存上传的文件到指定路径，支持分块写入以适应大文件。

    :param upload_file: 上传文件的二进制流（如 request.files['file'].stream）
    :param save_path: 保存文件的完整路径
    :param chunk_size: 每次写入的字节数，默认 8192
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as f:
        while True:
            chunk = upload_file.read(chunk_size)
            if not chunk:
                break
            f.write(chunk)

def allowed_file(filename: str, allowed_extensions: set) -> bool:
    """
    判断文件扩展名是否允许上传。

    :param filename: 文件名
    :param allowed_extensions: 允许的扩展名集合（如 {'jpg', 'png', 'txt'}）
    :return: 是否允许
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# 示例用法
if __name__ == "__main__":
    # 假设有一个二进制文件流 upload_file
    class DummyFile:
        def __init__(self, content):
            self._content = content
            self._offset = 0
        def read(self, size=-1):
            if self._offset >= len(self._content):
                return b''
            if size == -1:
                size = len(self._content) - self._offset
            chunk = self._content[self._offset:self._offset+size]
            self._offset += size
            return chunk

    dummy = DummyFile(b"hello world")
    save_upload_file(dummy, "uploads/test.txt")
    print("文件是否允许上传:", allowed_file("test.txt", {"txt", "md"}))
