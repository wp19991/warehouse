from fastapi import FastAPI

from model import Warehouse, db

app = FastAPI()


# 连接数据库
@app.on_event("startup")
def connect_db():
    db.connect()


# 断开数据库连接
@app.on_event("shutdown")
def disconnect_db():
    db.close()


# 获取所有仓库
@app.get("/warehouses")
async def get_warehouses():
    warehouses = Warehouse.select()
    return {"warehouses": [warehouse.warehouse_name for warehouse in warehouses]}


# 获取单个仓库
@app.get("/warehouses/{warehouse_id}")
async def get_warehouse(warehouse_id: int):
    warehouse = Warehouse.get_or_none(warehouse_id=warehouse_id)
    if warehouse:
        return warehouse
    return {"error": "Warehouse not found"}


# 更新仓库
@app.put("/warehouses")
async def update_warehouse(warehouse_id: int, updated_warehouse_name: str):
    warehouse = Warehouse.get_or_none(warehouse_id=warehouse_id)
    if warehouse:
        warehouse.warehouse_name = updated_warehouse_name
        # 更新其他属性
        warehouse.save()
        return {"message": "Warehouse updated successfully"}
    return {"error": "Warehouse not found"}


# 删除仓库
@app.delete("/warehouses")
async def delete_warehouse(warehouse_id: int):
    warehouse = Warehouse.get_or_none(warehouse_id=warehouse_id)
    if warehouse:
        warehouse.delete_instance()
        return {"message": "Warehouse deleted successfully"}
    return {"error": "Warehouse not found"}
