# warehouse

## 创建model.py
你是一个精通数据库设计的设计人员，下面的表结构来管理一个仓库，里面的产品、进货、销售和配货的相关信息。
如果有不合理的地方青直接修改，帮我用python使用peewee库建立sqlite3数据库，如果英文有错误请帮我修改，写上注释，并且给每个表添加测试数据：

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