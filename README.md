# warehouse

## 创建model.py
你是一个精通数据库设计的设计人员，下面的表结构来管理一个仓库，里面的产品、进货、销售和配货的相关信息。
如果有不合理的地方请直接修改，帮我用python使用peewee库建立sqlite3数据库，如果英文有错误请帮我修改，写上注释，并且给每个表添加测试数据：

表：仓库（Warehouse）
仓库ID（Warehouse ID）：主键，唯一标识仓库
仓库名称（Warehouse Name）：仓库的名称
仓库地址（Warehouse Address）：仓库的地址
仓库登录密码（Warehouse Login Address）：仓库的登录密码
管理员名称（Admin Name）：管理员的名称

表：产品（Product）
产品ID（Product ID）：主键，唯一标识产品
产品名称（Product Name）：产品的名称
产品型号（Product Model）：产品的型号

表：进货（Purchase）
进货ID（Purchase ID）：主键，唯一标识进货记录
进货日期（Purchase Date）：进货的日期
货车支付的运费（Shipping Cost）：卡车支付的运费
货车的车牌号（Shipping Car No）：卡车的车牌号

表：进货详情（Purchase Details）
进货详情ID（Purchase Details ID）：主键，唯一标识进货详情记录
进货ID（Purchase ID）：外键，关联到进货表中的进货ID
产品ID（Product ID）：外键，关联到产品表中的产品ID
进货数量（Purchase Quantity）：进货的产品数量

表：销售单位（Sales Unit）
销售单位ID（Sales Unit ID）：主键，唯一标识销售单位
销售单位名称（Sales Unit Name）：销售单位的名称
地点（Location）：销售单位的地址
电话（Phone）：销售单位的电话

表：配货（Allocation）
配货ID（Allocation ID）：主键，唯一标识配货记录
销售单位ID（Sales Unit ID）：外键，关联到销售单位表中的销售单位ID
发货日期（Shipment Date）：发货的日期
运输地点（Delivery Location）：需要运输到的地点

表：配货详情（Allocation Details）
配货详情ID（Allocation Details ID）：主键，唯一标识配货详情记录
配货ID（Allocation ID）：外键，关联到配货表中的配货ID
产品ID（Product ID）：外键，关联到产品表中的产品ID
出货价格（Selling Price）：该产品的出货价格
配货数量（Allocation Quantity）：配货的产品数量



## 根据上面的数据，帮我查询产品A剩余的库存


## 对接到fastapi

下面使用python的pewee库编写的数据库代码，帮我对接到fastapi的不同接口上
```python
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

```