import xml.etree.ElementTree as ET

def export_to_xml(encrypted_users):
    root = ET.Element("users")
    for user, password in encrypted_users.items():
        user_element = ET.SubElement(root, "user")
        username_element = ET.SubElement(user_element, "username")
        username_element.text = user
        password_element = ET.SubElement(user_element, "password")
        password_element.text = password
    tree = ET.ElementTree(root)
    tree.write("encrypted_users.xml")

def menu():
    users = {}
    key = 5  # Clave de encriptación
    while True:
        print("""
        1. Crear usuario
        2. Encriptar usuarios
        3. Desencriptar usuarios
        4. Exportar usuarios encriptados a XML
        5. Salir
        """)
        option = input("Elige una opción: ")
        if option == '1':
            username = input("Ingresa el nombre del usuario: ")
            password = input("Ingresa la contraseña del usuario: ")
            user = create_user(username, password)
            users.update(user)
        elif option == '2':
            encrypted_users = encrypt_data(users, key)
            print("Usuarios encriptados:", encrypted_users)
        elif option == '3':
            decrypted_users = decrypt_data(encrypted_users, key)
            print("Usuarios desencriptados:", decrypted_users)
        elif option == '4':
            export_to_xml(encrypted_users)
            print("Usuarios encriptados exportados a XML.")
        elif option == '5':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

menu()