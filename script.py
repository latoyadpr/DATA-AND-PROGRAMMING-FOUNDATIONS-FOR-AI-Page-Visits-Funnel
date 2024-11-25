import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])

              
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(checkout.head())
print(purchase.head())

visits_cart = visits.merge(cart, how='left', on='user_id')

length_of_visits_cart = len(visits_cart)
print(length_of_visits_cart)

null_cart_time_count = visits_cart['cart_time'].isnull().sum()
print(null_cart_time_count)

total_visitors = len(visits_cart)
no_cart_users = visits_cart['cart_time'].isnull().sum()

percentage_no_cart = (float(no_cart_users) / total_visitors) * 100
print(percentage_no_cart)


cart_checkout = cart.merge(checkout, how='left', on='user_id')

null_checkout_time_count = cart_checkout['checkout_time'].isnull().sum()

total_cart_users = len(cart_checkout)
percentage_no_checkout = (float(null_checkout_time_count) / total_cart_users) * 100

print(percentage_no_checkout)


all_data = visits.merge(cart, how='left', on='user_id')\
                 .merge(checkout, how='left', on='user_id')\
                 .merge(purchase, how='left', on='user_id')

print(all_data.head())


total_checkout_users = all_data['checkout_time'].notnull().sum()
no_purchase_users = all_data['purchase_time'].isnull().sum()

percentage_no_purchase = (float(no_purchase_users) / total_checkout_users) * 100
print(percentage_no_purchase)


all_data['time_to_purchase'] = all_data['purchase_time'] - all_data['visit_time']


print(all_data['time_to_purchase'])

average_time_to_purchase = all_data['time_to_purchase'].mean()
print(average_time_to_purchase)
