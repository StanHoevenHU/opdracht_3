import psycopg2

con = psycopg2.connect(
    host = 'localhost',       
    database = 'Relational for MongoDB',  
    user = 'postgres',        
    password = 'PGdatabase1!'
)

cur = con.cursor()

def based_on_bought_before(product_id, get_top, get_amount):

    list_to_return = list()

    cur.execute(f"""
        SELECT product_id
        FROM product
        WHERE product_id IN (
            SELECT product_id
            FROM session_product
            WHERE
                bought = true AND 
                product_id IN (
                    SELECT product_id
                    FROM product
                    WHERE
                        sub_sub_category IN (
                            SELECT sub_sub_category
                            FROM product
                            WHERE product_id = '{product_id}'
                        )
                )
            GROUP BY PRODUCT_ID
            ORDER BY COUNT(product_id) DESC
            LIMIT {get_top}
        )
        ORDER BY selling_price
        LIMIT {get_amount}
    """
    )

    products_to_recommend = cur.fetchall()

    for each in products_to_recommend:
        list_to_return.append(each[0])
    
    return list_to_return

def based_on_similar_customer(profile_id):
    list_to_return = list()

    cur.execute(f"""
        SELECT product_id
        FROM profile_product
        WHERE 
            profile_id IN (
                SELECT profile_id
                FROM profile_product
                WHERE
                    product_id IN (
                        SELECT product_id
                        FROM profile_product
                        WHERE profile_id = '{profile_id}'
                    ) AND
                    viewed = 'true'
                GROUP BY profile_id
                ORDER BY COUNT(profile_id) DESC
                LIMIT 2
            ) AND
            NOT product_id IN (
                SELECT product_id
                FROM profile_product
                WHERE profile_id = '{profile_id}'
            )
        GROUP BY product_id
        ORDER BY COUNT(product_id) DESC
        LIMIT 4

    """

    )

    products_to_recommend = cur.fetchall()

    for each in products_to_recommend:
        list_to_return.append(each[0])
    
    return list_to_return

print(based_on_bought_before(44130, 10, 4))
print(based_on_similar_customer('5a393d68ed295900010384ca'))