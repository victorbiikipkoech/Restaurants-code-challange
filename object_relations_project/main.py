from customer import Customer
from restaurant import Restaurant
from review import Review

# instances to test code
customer1 = Customer("victor", "kipkoech")
restaurant1 = Restaurant("westlands")
review1 = Review(customer1, restaurant1, 4)

# Associate the review with the restaurant
restaurant1.reviews.append(review1)

# Example
print(customer1.full_name())
print(Restaurant.all())
print(Review.all())
print(restaurant1.customers())
