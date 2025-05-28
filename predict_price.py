def estimate_price(mileage, theta0, theta1):
	estimate_price = theta0 + theta1 * mileage
	return estimate_price

def get_mileage_from_user():
	raw = input("Mileage: ")

	max_mileage = 396320

	try:
		num = int(raw)
		if num < 0:
			raise ValueError("negative numbers are not allowed")
		if num > max_mileage:
			raise ValueError(f"mileage must be below {max_mileage}")
		return num

	except ValueError as err:
		print(f"{err}. Please input different mileage.")
		exit()

def main():
	mileage = get_mileage_from_user()

	estimate_price = 8499.114139501155 + -0.021445093505184455 * mileage
	print(f"Price prediction: {int(estimate_price)}")

if __name__ == '__main__':
	main()