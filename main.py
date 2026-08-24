print("welcome to the Interavtive Personal Data Collector")

name = input("Enter Your Name :-")
age = int(input("Enter Your Age:-"))
height = float(input("Enter Your Height In Meters :-"))
fav =int(input("Enter Favourtive Number:-"))


print("Thank You! Here is The information we collected :")

print(f"(Name{name}(Type:{type(name)}),menory address {id(name)}")
print(f"(Age{age}(Type:{type(age)}),menory address {id(age)}")
print(f"(Height{height}(Type:{type(height)}),menory address {id(height)}")
print(f"(Favourite{fav}(Type:{type(fav)}),menory address {id(fav)}")


current_year = 2026
birth_year = current_year - age 

print(f" Your biirth Year Is Approximately {birth_year} (Based on your age OF {age})")
print("Thank you, for using personal data collector.")
