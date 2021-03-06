import pdb
from models.reciept import Reciept


from models.product import Product
import repositories.products_repository as products_repository


from models.staff import Staff
import repositories.staff_repository as staff_repository


from models.manufacturer import Manufacturer
import repositories.manufacturers_repository as manufacturers_repository

from models.reciept import Reciept
import repositories.reciept_repository as reciept_repository


manufacturer_1 = Manufacturer("Brakes", "0789563742")
manufacturers_repository.save(manufacturer_1)
manufacturer_2 = Manufacturer("Mitchell & Mitchell", "0472736466")
manufacturers_repository.save(manufacturer_2)
manufacturer_3 = Manufacturer("Organic Matter", "0378934625")
manufacturers_repository.save(manufacturer_3)
manufacturer_4 = Manufacturer("Chip 'n Dale", "07382036256")
manufacturers_repository.save(manufacturer_4)

staff_1 = Staff("Gregory Miles", 5)
staff_repository.save(staff_1)
staff_2 = Staff("Jess Lee", 3)
staff_repository.save(staff_2)
staff_3 = Staff("Tony Hawk", 12)
staff_repository.save(staff_3)

product_1 = Product("Cappuccino", "Medium", 100, 0.5, 2.5, manufacturer_3)
products_repository.save(product_1)
product_2 = Product("Latte", "Medium", 100, 0.6, 2.75, manufacturer_3)
products_repository.save(product_2)
product_3 = Product("Hot Dog", "American Special", 5, 3, 5.50, manufacturer_4)
products_repository.save(product_3)
product_4 = Product("Herbal Tea", "Health 100", 50, 0.1, 1.00, manufacturer_2)
products_repository.save(product_4)
product_5 = Product("Specialty Glasswear", "Home Made", 0, 10, 20, manufacturer_1)
products_repository.save(product_5)

reciept_1 = Reciept(product_1, staff_2, "03:04:05", 6)
reciept_repository.save(reciept_1)
reciept_2 = Reciept(product_2, staff_3, "12:45:03", 2)
reciept_repository.save(reciept_2)
reciept_3 = Reciept(product_3, staff_1, "13:45:24", 1)
reciept_repository.save(reciept_3)
reciept_4 = Reciept(product_4, staff_1, "13:46:34", 9)
reciept_repository.save(reciept_4)
reciept_5 = Reciept(product_5, staff_3, "14:00:03", 6)
reciept_repository.save(reciept_5)
reciept_6 = Reciept(product_3, staff_1, "16:23:54", 2)
reciept_repository.save(reciept_6)
reciept_7 = Reciept(product_3, staff_2, "11:23:54", 6)
reciept_repository.save(reciept_7)
reciept_8 = Reciept(product_1, staff_3, "11:33:26", 5)
reciept_repository.save(reciept_8)
reciept_9 = Reciept(product_1, staff_3, "10:53:01", 5)
reciept_repository.save(reciept_9)
reciept_10 = Reciept(product_2, staff_1, "16:03:02", 5)
reciept_repository.save(reciept_10)
reciept_11 = Reciept(product_4, staff_1, "11:23:24", 10)
reciept_repository.save(reciept_11)
reciept_12 = Reciept(product_3, staff_1, "12:14:54", 5)
reciept_repository.save(reciept_12)
reciept_13 = Reciept(product_3, staff_2, "13:23:10", 6)
reciept_repository.save(reciept_13)
reciept_14 = Reciept(product_5, staff_2, "14:45:21", 1)
reciept_repository.save(reciept_14)
reciept_15 = Reciept(product_2, staff_3, "15:24:32", 2)
reciept_repository.save(reciept_15)
reciept_16 = Reciept(product_1, staff_1, "16:23:43", 3)
reciept_repository.save(reciept_16)

# product_1_update = Product("Edward", "Heaps of Ed", 30, 40, 500, manufacturer_2)
# products_repository.update(product_1_update)


pdb.set_trace()

