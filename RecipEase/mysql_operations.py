from RecipEase import recipe_db

cur = recipe_db.cursor()
# recipe_db.commit()

def insert(username,email,password,pic_filename):
# writes user data into users table
    try:
        insert_command = "INSERT INTO users (Username, Email, Password, Pic_filename) VALUES (%s,%s,AES_ENCRYPT(%s,'PaSswOrD'),%s);"
        cur.execute(insert_command,(username,email,password,pic_filename))
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        recipe_db.rollback()
    finally:
        recipe_db.commit()

def read(user_id):
# retrieves user data from users table
    try:
        read_command = f"SELECT Username, Email, AES_DECRYPT(Password,'PaSswOrD'), Pic_filename FROM users WHERE ID = {user_id};"
        cur.execute(read_command)
        record = cur.fetchone()
        print(f"Username = {record[0]}")
        print(f"Email = {record[1]}")
        print(f"Password = {record[2]}")
        print(f"Pic_filename = {record[3]}")
        print("")
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        recipe_db.rollback()
    finally:
        recipe_db.commit()

# users = [
#             ('efrohi', 'ef@ro.hi', 'p4ss'),
#             ('hillash', 'hil@la.sh', 'p0ss')
#         ]
