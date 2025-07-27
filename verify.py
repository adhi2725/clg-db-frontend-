# import mysql.connector
# import bcrypt

# def verify_staff_login(staff_id: int, input_password: str) -> bool:
#     mydb = mysql.connector.connect(
#         host="cnlbvh.h.filess.io",
#         user="clgfees_towertrace",
#         password="4227ca4efc7d0fa1193fef328a8792f427b6774e",
#         database="clgfees_towertrace",
#         port=3307
#     )
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT password FROM staff WHERE staff_id = %s", (staff_id,))
#     result = mycursor.fetchone()

#     mycursor.close()
#     mydb.close()

#     if result and bcrypt.checkpw(input_password.encode(), result[0].encode()):
#         return True
#     return False
# staff_id = int(input("Enter Staff ID: "))
# password = input("Enter Password: ")

# if verify_staff_login(staff_id, password):
#     print("✅ Login successful!")
# else:
#     print("❌ Invalid staff ID or password.")

import mysql.connector
import bcrypt

def verify_staff_login(staff_id: int, password: str) -> bool:
    try:
        mydb = mysql.connector.connect(
            host="cnlbvh.h.filess.io",
            user="clgfees_towertrace",
            password="4227ca4efc7d0fa1193fef328a8792f427b6774e",
            database="clgfees_towertrace",
            port=3307
        )

        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT password FROM staff WHERE staff_id = %s", (staff_id,))
        result = mycursor.fetchone()

        mycursor.close()
        mydb.close()

        if result:
            stored_hashed_pw = result["password"].encode('utf-8')  # DB value
            return bcrypt.checkpw(password.encode('utf-8'), stored_hashed_pw)

        return False

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return False
