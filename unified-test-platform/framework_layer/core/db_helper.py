import sqlite3
from typing import Any, List, Tuple, Dict, Optional

class DBHelper:
    """
    数据库辅助工具类，支持基本的增删改查操作（以 SQLite 为例）。
    """

    def __init__(self, db_path: str):
        """
        初始化数据库连接。

        :param db_path: 数据库文件路径
        """
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row  # 查询结果可通过字段名访问

    def execute(self, sql: str, params: Tuple = ()) -> None:
        """
        执行单条 SQL 语句（如插入、更新、删除）。

        :param sql: SQL 语句
        :param params: 参数元组
        """
        with self.conn:
            self.conn.execute(sql, params)

    def query(self, sql: str, params: Tuple = ()) -> List[Dict[str, Any]]:
        """
        执行查询语句，返回结果列表。

        :param sql: 查询 SQL
        :param params: 参数元组
        :return: 查询结果列表，每行为字典
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    def query_one(self, sql: str, params: Tuple = ()) -> Optional[Dict[str, Any]]:
        """
        执行查询语句，返回单条结果。

        :param sql: 查询 SQL
        :param params: 参数元组
        :return: 单条结果字典或 None
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, params)
        row = cursor.fetchone()
        return dict(row) if row else None

    def close(self):
        """
        关闭数据库连接。
        """
        self.conn.close()

# 示例用法
if __name__ == "__main__":
    db = DBHelper("example.db")
    db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    db.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    users = db.query("SELECT * FROM users")
    print("用户列表:", users)
    db.close() 
