import sys
import pandas as pd

def adjust_theta0(learning_rate, errors):
	error_sum = sum(errors)
	return learning_rate * (1 / len(errors)) * error_sum

def adjust_theta1(learning_rate, errors, data):
	weighted_error_sum = 0
	for index, error in enumerate(errors):
		weighted_error_sum += error * data[index]
	return learning_rate * (1 / len(errors)) * weighted_error_sum

def get_errors(data, theta0, theta1):
	errors = []
	for _, row in data.iterrows():
		price_estimation = estimate_price(row['km'], theta0, theta1)
		errors.append(price_estimation - row['price'])
	return errors

def estimate_price(mileage, theta0, theta1):
	estimate_price = theta0 + theta1 * mileage
	return estimate_price

def get_data():
	try:
		df = pd.read_csv(sys.argv[1])
		return df

	except FileNotFoundError as err:
		print(f"{err}.\nUsage: train_model [data_csv_path]")
		exit()
	except pd.errors.EmptyDataError as err:
		print(f"{err}.\nUsage: train_model [data_csv_path]")
		exit()
	except pd.errors.ParserError as err:
		print(f"{err}.\nUsage: train_model [data_csv_path]")
		exit()
	except UnicodeDecodeError as err:
		print(f"{err}.\nUsage: train_model [data_csv_path]")
		exit()

def main():
	df = get_data()
	df.reset_index(drop=True)

	X = df['km'].values.astype(float)
	Y = df['price'].values.astype(float)

	theta0 = 0
	theta1 = 0
	learning_rate_theta1 = 0.00000000001
	learning_rate_theta0 = 0.01

	for step in range(5000):
		errors = get_errors(df, theta0, theta1)
		theta0 -= adjust_theta0(learning_rate_theta0, errors)
		theta1 -= adjust_theta1(learning_rate_theta1, errors, X)

	print(f"theta0: {theta0}, theta1: {theta1}")

if __name__ == '__main__':
	main()