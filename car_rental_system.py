class Cars:
	def __init__ (self, name, contact, email, timespan, cartype):
		self.name = name
		self.contact = contact
		self.email = email
		self.time = timespan
		self.amount = 1
		self.type = cartype
		self.quantity = {"Mini": 5,
				"SUV": 4,
				"Prime": 8}
		self.inventory = show_inventory

        #def inventory(self):
               # if (self.inventory == 'Y'):
                 #       for i in self.quantity:
                     #           print(i, self.quantity[i])
                #else:
                    #    continue

	def cartype(self):
		
		if (self.time >= 12):
			if (self.type == "MINI"):
				self.amount = 5000*self.time
				if True: 
					self.quantity['Mini'] = self.quantity['Mini'] - 1
			elif (self.type == "SUV"):
				self.amount = 8000*self.time
				if True: 
					self.quantity['SUV'] = self.quantity['SUV'] - 1
			elif (self.type == "PRIME"):
				self.amount = 10000*self.time 		
				if True: 
					self.quantity['Prime'] = self.quantity['Prime'] - 1
		else:
			print("Sorry!! We dont rent cars below 12 hrs")	

	def bill(self):
		self.name = name
		self.contact = contact
		self.email = email
		print("        Welcome to Tapatap Cars")
		print("****************************************")
		print("Renters Name:" + self.name)	
		print("Renters Contact:" + self.contact)
		print("Renters Email ID:" + self.email)
		print("Renters timespan:" + str(self.time))
		print("Renters Cartype:" + self.type)
		print("Total Amount: {}".format(self.amount))


name = input("Enter your name: ")
contact = input("Enter your contact number: ")
email = input("Enter your Email ID: ")
timespan = int(input("Enter number of hours you want to rent the car: "))
cartype = input("Enter type of car you want to rent (MINI, SUV, Prime): ").upper()
show_inventory = input("Do you want to check the available cars and their quantity").upper()
c1 = Cars(name, contact, email, timespan, cartype)
c1.cartype()
c1.bill()
