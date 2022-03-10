class SaleRecord():
    
    region: str
    item_type: str
    units_sold: str
    unit_price: str
    unit_cost: str   

    def __init__(self, region,item_type,units_sold,unit_price,unit_cost) -> None:
        self.region = region,
        self.item_type = item_type,
        self.units_sold = units_sold,
        self.unit_price = unit_price,
        self.unit_cost = unit_cost,