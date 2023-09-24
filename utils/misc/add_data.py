
import psycopg2
from data import config

categories = [
    {
        "name": "🧾 Menyu" 
    },
    {
        "name": "🥂 Ichimliklar"
    },
    {
        "name": "Biz Xaqimizda"
    },
    {
        "name": "🌭 Hod-Dog",
        "parent_id": 1
    },
    {
        "name": "🌯 Lavash",
        "parent_id": 1
    },
    {
        "name": "🍔 Cheese Burger",
        "parent_id": 1
    },
    {
        "name": "🍔 GamBurger",
        "parent_id": 1
    },
    {
        "name": "Coca-Cola",
        "parent_id": 2 
    },
    {
        "name": "Fanta",
        "parent_id": 2 
    },
    {
        "name": "Sprite ",
        "parent_id": 2 
    }
]

def add_category(name, parent_id=None):
    try:
        connection = psycopg2.connect(user=config.DB_USER,
                                    password=config.DB_PASS,
                                    host=config.DB_HOST,
                                    port="5432",
                                    database=config.DB_NAME)
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO Categories (name, parent_id) VALUES (%s,%s )"""
        record_to_insert = (name, parent_id)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully Categories table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def add_category_to_db():
    for category in categories:
        add_category(name=category.get("name"), parent_id=category.get("parent_id"))

products = [
    {
        "name": "🌭 Канадский хот-дог",
        "description": "Приготовлено в Botir Hod-Dog",
        "image_url": "https://www.gorodtaraz.kz/upload/000/u1/35/74/kanadskii-hot-dog-photo-normal.jpg",
        "price":"15000" ,
        "category_id": 4
    },
    {
        "name": "🌭 Двойной хот-дог",
        "description": "Приготовлено в Botir Hod-Dog",
        "image_url": "https://www.gorodtaraz.kz/upload/000/u1/01/15/dvoinoi-hot-dog-photo-normal.jpg",
        "price":"20000",
        "category_id": 4 
    },
    {
        "name": "🌯 Лаваша с курицей",
        "description": "Ингредиенты\n\nлаваш 2 шт. или один большой;\nзелень петрушки и укропа 30 г;\nперец черный;\nсоль;\nлук репчатый 1 шт.;",
        "image_url": "https://testosam.ru/wp-content/uploads/2016/07/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-%E2%84%96-1-2.jpg",
        "price":"28000",
        "category_id": 5 
    },
    {
        "name": "🌯 Классический Lavash",
        "description": "Классический Lavash",
        "image_url": "https://yukber.uz/image/cache/catalog/kavash-700x700.jpg",
        "price":"25000",
        "category_id": 5 
    },
    {
        "name": "🍔 Cheese Burger",
        "description": "Burger King",
        "image_url": "https://www.kitchensanctuary.com/wp-content/uploads/2021/05/Double-Cheeseburger-square-FS-42-500x500.jpg",
        "price":"30000",
        "category_id": 6 
    },
    {
        "name": "🍔 GamBurger",
        "description": "Очень вкусный",
        "image_url": "https://burgerkings.ru/image/cache/catalog/photo/395727876-gamburger-parmedgano-600x600.jpg",
        "price":"32000",
        "category_id": 7
    },
    {
        "name": "Coca-Cola 1.5L",
        "description": "1.5L",
        "image_url": "https://web.lebazar.uz/resources/product/2023/4/18/medium_1684384950877101020102-00173.png",
        "price":"13000",
        "category_id": 8
    },
    {
        "name": "Coca-Cola 1L",
        "description": "1L",
        "image_url": "https://api.lochin.uz/media/file/image/2021-03/f97bbe8d-63bb-4bab-99af-97c4a99c7be3.jpg.500x500_q85_crop-scale.jpg",
        "price":"10000",
        "category_id": 8
    },
    {
        "name": "Coca-Cola 0.5L",
        "description": "0.5L",
        "image_url": "https://ru.coca-cola.uz/content/dam/one/uz/ru/product-images/coca-cola-classic.jpg",
        "price":"8000",
        "category_id": 8
    },
    {
        "name": "Fanta 1.5L",
        "description": "1.5L",
        "image_url": "https://web.lebazar.uz/resources/product/2023/4/18/medium_1684384664245101020102-00003.png",
        "price":"13000",
        "category_id": 9
    },
    {
        "name": "Fanta 1L",
        "description": "1L",
        "image_url": "https://images.uzum.uz/ce8a878v1htd23airm6g/original.jpg",
        "price":"10000",
        "category_id": 9
    },
    {
        "name": "Coca-Cola 0.5L",
        "description": "0.5L",
        "image_url": "https://arbuz.kz/image/s3/arbuz-kz-products/48707-fanta_0_5_l.jpg?w=1100&h=1100&_c=1695032890",
        "price":"8000",
        "category_id": 9
    },
    {
        "name": "Sprite 1.5L",
        "description": "1.5L",
        "image_url": "https://sushimito.ru/d/sprayt.jpg",
        "price":"13000",
        "category_id": 10
    },
    {
        "name": "Sprite 1L",
        "description": "1L",
        "image_url": "https://sushimito.ru/d/sprayt.jpg",
        "price":"10000",
        "category_id": 10
    },
    {
        "name": "Sprite 0.5L",
        "description": "0.5L",
        "image_url": "https://cdn.ynamdar.com/ynamdar/images/product/org_CCL301900_1.jpg?version=1300",
        "price":"8000",
        "category_id": 10
    },
]


def add_product(name, description, image_url, price, category_id):
    try:
        connection = psycopg2.connect(user=config.DB_USER,
                                    password=config.DB_PASS,
                                    host=config.DB_HOST,
                                    port="5432",
                                    database=config.DB_NAME)
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO Products (name, description, image_url, price, category_id) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (name, description, image_url, price, category_id)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully Products table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record Products table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def add_products_to_db():
    for product in products:
        add_product(name=product.get("name"), description=product.get("description"), image_url=product.get("image_url"), price=product.get("price"), category_id=product.get("category_id"))