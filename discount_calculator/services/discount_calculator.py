from discount_calculator.database import UserDB, ProductDB


from datetime import date


class DiscountCalculator:
    def __init__(self, db):
        self.user_db = UserDB(db)
        self.product_db = ProductDB(db)

    def calculate_discount(self, product_id, user_id):
        user = self.user_db.get_user_data(user_id)
        product = self.product_db.get_product_data(product_id)
        if not user and not product:
            raise Exception()

        if self.today_is_black_friday:
            return product['price_in_cents'] * 0.1
        
        if self.is_user_birthday(user['date_of_birth']):
            return product['price_in_cents'] * 0.05

        return 0

    @property
    def today_is_black_friday(self):
        today = date.today()
        black_friday_date = date(today.year, 11, 25)

        return today == black_friday_date

    def is_user_birthday(self, user_birthday):
        today = date.today()

        return today == user_birthday
