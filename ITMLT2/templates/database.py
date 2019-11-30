import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

products_db = myclient["products"]

order_management_db = myclient["order_management"]


def get_product(code):
    products_coll = products_db["products"]

    product = products_coll.find_one({"code":code})

    return product

def get_products():
    product_list = []

    products_coll = products_db["products"]

    for p in products_coll.find({}):
        product_list.append(p)

    return product_list


    for i,v in products.items():
        product = v
        product.setdefault("code",i)
        product_list.append(product)
    return product_list


def get_user(username):
    customers_coll = order_management_db['customers']
    user=customers_coll.find_one({"username":username})
    return user


def get_branch(code):
    branches_coll = products_db["branches"]

    branch = branches_coll.find_one({"code":code})

    return branch

def get_branches():
    branch_list = []

    branches_coll = products_db["branches"]

    for p in branches_coll.find({}):
        branch_list.append(p)

    return branch_list

def create_order(order):
    orders_coll = order_management_db['orders']
    orders_coll.insert(order)
    
def get_orders(username):
    order_list = []
    orders_coll = order_management_db['orders']

    for o in orders_coll.find({"username":username}):
        order_list.append(o)
    return order_list

def count_orders(username):
    orders_coll = order_management_db["orders"]
    numberoforders = []
    numberoforders = orders_coll.count({"username":username})
    return numberoforders

def change_db(username, newpassword1):
    password_coll=order_management_db["customers"]
    customer=({"username":username})
    password = {"$set":{"password": newpassword1 }}
#    order_management.update_one (customer, password)
    password_coll.find_one_and_update(customer,password)
    return
    
def get_password(username):
    customer_coll = order_management_db['customers']
    user=customer_coll.find_one({"username":username})
    password=user['password']
    return password
    
    
