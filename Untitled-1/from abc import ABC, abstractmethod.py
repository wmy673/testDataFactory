from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import random
import string
from typing import Dict, List, Type, Union

# 基础数据模型
class TestData(ABC):
    """测试数据基类"""
    @abstractmethod
    def to_dict(self) -> Dict:
        """将数据转换为字典格式"""
        pass

class UserData(TestData):
    """用户测试数据模型"""
    def __init__(self, user_id: int, username: str, email: str, is_active: bool, created_at: datetime):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.is_active = is_active
        self.created_at = created_at
    
    def to_dict(self) -> Dict:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat()
        }

class ProductData(TestData):
    """产品测试数据模型"""
    def __init__(self, product_id: int, name: str, price: float, category: str, in_stock: bool):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
    
    def to_dict(self) -> Dict:
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "in_stock": self.in_stock
        }

class OrderData(TestData):
    """订单测试数据模型"""
    def __init__(self, order_id: int, user_id: int, products: List[int], total: float, status: str):
        self.order_id = order_id
        self.user_id = user_id
        self.products = products
        self.total = total
        self.status = status
    
    def to_dict(self) -> Dict:
        return {
            "order_id": self.order_id,
            "user_id": self.user_id,
            "products": self.products,
            "total": self.total,
            "status": self.status
        }

# 工厂接口
class TestDataFactory(ABC):
    """测试数据工厂接口"""
    @abstractmethod
    def create(self, **kwargs) -> TestData:
        """创建测试数据实例"""
        pass
    
    @abstractmethod
    def create_batch(self, count: int, **kwargs) -> List[TestData]:
        """批量创建测试数据"""
        pass

# 具体工厂实现
class UserDataFactory(TestDataFactory):
    """用户测试数据工厂"""
    def create(self, **kwargs) -> UserData:
        # 提供默认值或使用传入的参数
        user_id = kwargs.get('user_id', random.randint(1000, 9999))
        username = kwargs.get('username', self._generate_username())
        email = kwargs.get('email', f"{username}@example.com")
        is_active = kwargs.get('is_active', random.choice([True, False]))
        created_at = kwargs.get('created_at', datetime.now() - timedelta(days=random.randint(0, 365)))
        
        return UserData(user_id, username, email, is_active, created_at)
    
    def create_batch(self, count: int, **kwargs) -> List[UserData]:
        return [self.create(**kwargs) for _ in range(count)]
    
    def _generate_username(self) -> str:
        """生成随机用户名"""
        prefix = random.choice(["user", "client", "customer", "member"])
        suffix = ''.join(random.choices(string.digits, k=4))
        return f"{prefix}_{suffix}"

class ProductDataFactory(TestDataFactory):
    """产品测试数据工厂"""
    def create(self, **kwargs) -> ProductData:
        product_id = kwargs.get('product_id', random.randint(10000, 99999))
        name = kwargs.get('name', self._generate_product_name())
        price = kwargs.get('price', round(random.uniform(5.0, 500.0), 2))
        category = kwargs.get('category', random.choice(["Electronics", "Clothing", "Books", "Home"]))
        in_stock = kwargs.get('in_stock', random.choice([True, False]))
        
        return ProductData(product_id, name, price, category, in_stock)
    
    def create_batch(self, count: int, **kwargs) -> List[ProductData]:
        return [self.create(**kwargs) for _ in range(count)]
    
    def _generate_product_name(self) -> str:
        """生成随机产品名"""
        adjectives = ["Premium", "Smart", "Eco", "Luxury", "Wireless", "Portable"]
        nouns = ["Phone", "Laptop", "Watch", "Headphones", "Charger", "Speaker"]
        return f"{random.choice(adjectives)} {random.choice(nouns)}"

class OrderDataFactory(TestDataFactory):
    """订单测试数据工厂"""
    def __init__(self, user_factory: UserDataFactory, product_factory: ProductDataFactory):
        self.user_factory = user_factory
        self.product_factory = product_factory
    
    def create(self, **kwargs) -> OrderData:
        order_id = kwargs.get('order_id', random.randint(100000, 999999))
        
        # 创建关联数据
        user = kwargs.get('user', self.user_factory.create())
        products = kwargs.get('products', [self.product_factory.create() for _ in range(random.randint(1, 5))])
        
        # 计算订单总额
        total = sum(p.price for p in products)
        
        status = kwargs.get('status', random.choice(["Pending", "Shipped", "Delivered", "Cancelled"]))
        
        return OrderData(
            order_id=order_id,
            user_id=user.user_id,
            products=[p.product_id for p in products],
            total=total,
            status=status
        )
    
    def create_batch(self, count: int, **kwargs) -> List[OrderData]:
        return [self.create(**kwargs) for _ in range(count)]

# 工厂选择器
class TestDataFactorySelector:
    """根据类型选择对应的工厂"""
    def __init__(self):
        self.factories = {
            "user": UserDataFactory(),
            "product": ProductDataFactory(),
            "order": None  # 需要特殊处理
        }
        
        # 初始化订单工厂需要依赖其他工厂
        self.factories["order"] = OrderDataFactory(
            self.factories["user"],
            self.factories["product"]
        )
    
    def get_factory(self, data_type: str) -> TestDataFactory:
        """获取指定类型的工厂"""
        factory = self.factories.get(data_type.lower())
        if not factory:
            raise ValueError(f"Unsupported data type: {data_type}")
        return factory

# 使用示例
if __name__ == "__main__":
    factory_selector = TestDataFactorySelector()
    
    # 创建单个用户
    user_factory = factory_selector.get_factory("user")
    user = user_factory.create()
    print("单个用户数据:", user.to_dict())
    
    # 创建批量产品
    product_factory = factory_selector.get_factory("product")
    products = product_factory.create_batch(3)
    print("\n批量产品数据:")
    for p in products:
        print(p.to_dict())
    
    # 创建订单（包含关联的用户和产品）
    order_factory = factory_selector.get_factory("order")
    order = order_factory.create()
    print("\n订单数据:", order.to_dict())
    
    # 创建带特定参数的测试数据
    specific_user = user_factory.create(
        username="test_user",
        email="test@example.com",
        is_active=True
    )
    print("\n特定用户数据:", specific_user.to_dict())