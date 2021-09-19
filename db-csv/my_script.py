import csv
import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn


def create_category(conn, cotegories):
    sql = 'INSERT INTO core_categories(name) VALUES(?)'
    cur = conn.cursor()
    cur.execute(sql, cotegories)
    return cur.lastrowid


def create_country(conn, country):
    sql = ' INSERT INTO core_country(name) VALUES(?) '
    cur = conn.cursor()
    cur.execute(sql, country)
    return cur.lastrowid


def create_province(conn, province, country):
    cur = conn.cursor()

    cur.execute("SELECT id FROM core_country WHERE name=?", (country,))
    country_id = cur.fetchall()[0][0]

    sql = 'INSERT INTO core_province(name, country_id) VALUES(?, ?)'

    cur.execute(sql, (province, country_id))
    return cur.lastrowid


def create_city(conn, city, province):
    cur = conn.cursor()
    cur.execute("SELECT id FROM core_province WHERE name=?", (province,))
    province_id = cur.fetchall()[0][0]

    sql = 'INSERT INTO core_city(name, province_id) VALUES(?, ?)'
    cur.execute(sql, (city, province_id))
    return cur.lastrowid


def create_address(conn, address, city):
    cur = conn.cursor()
    cur.execute("SELECT id FROM core_city WHERE name=?", (city,))
    city_id = cur.fetchall()[0][0]

    sql = 'INSERT INTO core_address(street, city_id, latitude, longitude, postalCode) VALUES(?, ?, ?, ?, ?)'
    cur.execute(sql, (address, city_id, latitude, longitude, postalCode))
    return cur.lastrowid


def create_store(conn, store_name, website, street, category_name):
    cur = conn.cursor()
    cur.execute("SELECT id FROM core_address WHERE street=?", (street,))
    address_id = cur.fetchall()[0][0]

    cur.execute("SELECT id FROM core_categories WHERE name=?", (category_name,))
    category_id = cur.fetchall()[0][0]

    sql = 'INSERT INTO core_store(name, address_id, categories_id, websites) VALUES(?, ?, ?, ?)'
    cur.execute(sql, (store_name, address_id, category_id, website))
    return cur.lastrowid


conn = create_connection('C:\\Users\\Paulo\\Documents\\meus projetos e cursos\\DjangoRestApi\\api-loja\\db.sqlite3')

category_list = []
country_list = []
province_list = []
city_list = []
address_list = []
store_list = []


with open("datasets/Fast_Food_Restaurants_US.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        address = row[1]
        categories = row[2]
        city = row[3]
        country = row[4]
        latitude = row[5]
        longitude = row[6]
        name = row[7]
        postalCode = row[8]
        province = row[9]
        websites = row[10]

        if categories not in category_list:
            create_category(conn, (categories,))
            category_list.append(categories)

        if country not in country_list:
            create_country(conn, (country,))
            country_list.append(country)

        if province not in province_list:
            create_province(conn, province, country)
            province_list.append(province)

        if city not in city_list:
            create_city(conn, city, province)
            city_list.append(city)

        if address not in address_list:
            create_address(conn, address, city)
            address_list.append(address)

        if name not in store_list:
            create_store(conn, name, websites, address, categories)
            store_list.append(name)

    conn.commit()
