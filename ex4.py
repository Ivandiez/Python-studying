# make variables and assign values to those variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
# a variable cars_not_driven that value is the cars, those stay in place
cars_not_driven = cars - drivers
cars_driven = drivers
# a variable carpool_capacity that says about how many peoples we can take in a cars
carpool_capacity = cars_driven * space_in_a_car
# this variable says about the average of person, who can seat in a car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
