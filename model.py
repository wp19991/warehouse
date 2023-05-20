from peewee import *

db = SqliteDatabase('warehouse.db')  # 创建一个名为"warehouse.db"的SQLite数据库


# 仓库（Warehouse）表
class Warehouse(Model):
    warehouse_id = AutoField(primary_key=True)  # 仓库ID，自增主键
    warehouse_name = CharField(unique=True)  # 仓库名称，唯一
    warehouse_address = CharField()  # 仓库地址
    warehouse_login_password = CharField()  # 仓库登录密码
    admin_name = CharField()  # 管理员名称

    class Meta:
        database = db


# 产品（Product）表
class Product(Model):
    product_id = AutoField(primary_key=True)  # 产品ID，自增主键
    product_name = CharField()  # 产品名称
    product_model = CharField()  # 产品型号

    class Meta:
        database = db


# 进货（Purchase）表
class Purchase(Model):
    purchase_id = AutoField(primary_key=True)  # 进货ID，自增主键
    purchase_date = DateField()  # 进货日期
    shipping_cost = DecimalField()  # 货车支付的运费
    shipping_car_no = CharField()  # 货车的车牌号

    class Meta:
        database = db


# 进货详情（Purchase Details）表
class PurchaseDetails(Model):
    purchase_details_id = AutoField(primary_key=True)  # 进货详情ID，自增主键
    purchase = ForeignKeyField(Purchase, backref='purchase_details')  # 外键，关联到进货表
    product = ForeignKeyField(Product, backref='purchase_details')  # 外键，关联到产品表
    purchase_quantity = IntegerField()  # 进货数量

    class Meta:
        database = db


# 销售单位（Sales Unit）表
class SalesUnit(Model):
    sales_unit_id = AutoField(primary_key=True)  # 销售单位ID，自增主键
    sales_unit_name = CharField(unique=True)  # 销售单位名称，唯一
    location = CharField()  # 地点
    phone = CharField()  # 电话

    class Meta:
        database = db


# 配货（Allocation）表
class Allocation(Model):
    allocation_id = AutoField(primary_key=True)  # 配货ID，自增主键
    sales_unit = ForeignKeyField(SalesUnit, backref='allocations')  # 外键，关联到销售单位表
    shipment_date = DateField()  # 发货日期
    delivery_location = CharField()  # 运输地点

    class Meta:
        database = db


# 配货详情（Allocation Details）表
class AllocationDetails(Model):
    allocation_details_id = AutoField(primary_key=True)  # 配货详情ID，自增主键
    allocation = ForeignKeyField(Allocation, backref='allocation_details')  # 外键，关联到配货表
    product = ForeignKeyField(Product, backref='allocation_details')  # 外键，关联到产品表
    selling_price = DecimalField()  # 出货价格
    allocation_quantity = IntegerField()  # 配货数量

    class Meta:
        database = db


if __name__ == '__main__':
    # 创建所有表
    db.create_tables([Warehouse, Product, Purchase, PurchaseDetails, SalesUnit, Allocation, AllocationDetails])

    # 添加测试数据
    # 仓库数据
    warehouse_data = [
        {'warehouse_name': '仓库A', 'warehouse_address': '地址A', 'warehouse_login_password': '密码A', 'admin_name': '管理员A'},
        {'warehouse_name': '仓库B', 'warehouse_address': '地址B', 'warehouse_login_password': '密码B', 'admin_name': '管理员B'}
    ]
    Warehouse.insert_many(warehouse_data).execute()

    # 产品数据
    product_data = [
        {'product_name': '产品A', 'product_model': '型号A'},
        {'product_name': '产品B', 'product_model': '型号B'}
    ]
    Product.insert_many(product_data).execute()

    # 进货数据
    purchase_data = [
        {'purchase_date': '2023-05-18', 'shipping_cost': 100.00, 'shipping_car_no': '车牌号A'},
        {'purchase_date': '2023-05-19', 'shipping_cost': 150.00, 'shipping_car_no': '车牌号B'}
    ]
    Purchase.insert_many(purchase_data).execute()

    # 进货详情数据
    purchase_details_data = [
        {'purchase': 1, 'product': 1, 'purchase_quantity': 10},
        {'purchase': 1, 'product': 2, 'purchase_quantity': 5},
        {'purchase': 2, 'product': 2, 'purchase_quantity': 8}
    ]
    PurchaseDetails.insert_many(purchase_details_data).execute()

    # 销售单位数据
    sales_unit_data = [
        {'sales_unit_name': '销售单位A', 'location': '地点A', 'phone': '电话A'},
        {'sales_unit_name': '销售单位B', 'location': '地点B', 'phone': '电话B'}
    ]
    SalesUnit.insert_many(sales_unit_data).execute()

    # 配货数据
    allocation_data = [
        {'sales_unit': 1, 'shipment_date': '2023-05-19', 'delivery_location': '运输地点A'},
        {'sales_unit': 2, 'shipment_date': '2023-05-20', 'delivery_location': '运输地点B'}
    ]
    Allocation.insert_many(allocation_data).execute()

    # 配货详情数据
    allocation_details_data = [
        {'allocation': 1, 'product': 1, 'selling_price': 200.00, 'allocation_quantity': 8},
        {'allocation': 1, 'product': 2, 'selling_price': 250.00, 'allocation_quantity': 5},
        {'allocation': 2, 'product': 2, 'selling_price': 300.00, 'allocation_quantity': 10}
    ]
    AllocationDetails.insert_many(allocation_details_data).execute()

    # 查询产品A的剩余库存
    product_a = Product.get(Product.product_name == '产品A')
    total_purchase_quantity = PurchaseDetails.select(fn.SUM(PurchaseDetails.purchase_quantity)).where(
        PurchaseDetails.product == product_a).scalar()
    total_allocation_quantity = AllocationDetails.select(fn.SUM(AllocationDetails.allocation_quantity)).where(
        AllocationDetails.product == product_a).scalar()

    remaining_stock = total_purchase_quantity - total_allocation_quantity

    print(f"产品A的剩余库存为: {remaining_stock}")

    # 数据库连接关闭
    db.close()
