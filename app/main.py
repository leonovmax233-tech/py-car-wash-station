class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings


    def calculate_washing_price(self, car):
        price = (car.comfort_class * (self.clean_power - car.clean_mark) *
                 self.average_rating / self.distance_from_city_center)
        if (self.clean_power - car.clean_mark) <= 0:
            return  0
        return round(price, 1)


    def serve_cars(self, cars_list):
        total_income = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                total_income += price
        return round(total_income, 1)


    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power


    def rate_service(self, new_rate):
        new_avg = (self.average_rating * self.count_of_ratings + new_rate) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(new_avg, 1)


# Створюємо об'єкти
bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')
ws = CarWashStation(6, 8, 3.9, 11)
# Перевіряємо початкові clean_mark
print('Before:', bmw.clean_mark, audi.clean_mark, mercedes.clean_mark)
# Викликаємо serve_cars і друкуємо дохід
income = ws.serve_cars([bmw, audi, mercedes])
print('Income:', income)
# Перевіряємо clean_mark після мийки
print('After:', bmw.clean_mark, audi.clean_mark, mercedes.clean_mark)
# Перевірка calculate_washing_price (не миє машину)
ford = Car(2, 1, 'Ford')
wash_cost = ws.calculate_washing_price(ford)
print('Wash cost for Ford (should not change Ford.clean_mark):', wash_cost, ford.clean_mark)
# Перевірка rate_service
print('Rating before:', ws.average_rating, ws.count_of_ratings)
ws.rate_service(5)
print('Rating after:', ws.average_rating, ws.count_of_ratings)
