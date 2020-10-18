class ProductDB:
    def __init__(self, db_client):
        self.products_collection = db_client['products']

    def get_product_data(self, product_id):
        return self.products_collection.find_one({'id': product_id})
