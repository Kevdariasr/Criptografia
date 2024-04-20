def menu():
    print("1. Crear usuario")
    print("2. Encriptar usuarios")
    print("3. Desencriptar usuarios")
    print("4. Salir")
    return input("Elige una opción: ")

def create_user(users):
    username = input("Ingresa el nombre del usuario: ")
    password = input("Ingresa la contraseña del usuario: ")
    users[username] = password

def encrypt_data(data, key):
    encrypted_data = ""
    for char in data:
        encrypted_data += chr(ord(char) + key)
    return encrypted_data

def decrypt_data(data, key):
    decrypted_data = ""
    for char in data:
        decrypted_data += chr(ord(char) - key)
    return decrypted_data

def encrypt_users(users, key):
    return {encrypt_data(user, key): encrypt_data(password, key) for user, password in users.items()}

def decrypt_users(users, key):
    return {decrypt_data(user, key): decrypt_data(password, key) for user, password in users.items()}


def main():
    users = {}
    key = 5  # Clave de encriptación
    while True:
        option = menu()
        if option == '1':
            create_user(users)
        elif option == '2':
            encrypted_users = encrypt_users(users, key)
            print("Usuarios encriptados:", encrypted_users)
        elif option == '3':
            decrypted_users = decrypt_users(users, key)
            print("Usuarios desencriptados:", decrypted_users)
        elif option == '4':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()