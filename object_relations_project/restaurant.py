class Restaurant:
    restaurants = ["westlands"]

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.restaurants.append(self)

    def get_name(self):
        return self.name

    def get_reviews(self):
        return self.reviews

    def customers(self):
        return list(set([review.customer for review in self.reviews]))

    @classmethod
    def all(cls):
        return cls.restaurants

