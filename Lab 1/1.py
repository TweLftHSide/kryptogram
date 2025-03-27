def encrypt_caesar(text, shift):
    """Шифрує текст методом Цезаря."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt_caesar(text, shift):
    """Розшифровує текст, зашифрований методом Цезаря."""
    return encrypt_caesar(text, -shift)

def main():
    """Головна функція програми."""
    while True:
        print("\n Оберіть дію:")
        print("1. Шифрування")
        print("2. Розшифрування")
        print("3. Вихід")

        choice = input("Введіть ваш вибір (1/2/3): ")

        if choice == '1':
            text = input("Введіть текст для шифрування: ")
            shift = int(input("Введіть зсув: "))
            encrypted_text = encrypt_caesar(text, shift)
            print("Зашифрований текст:", encrypted_text)
        elif choice == '2':
            text = input("Введіть текст для розшифрування: ")
            shift = int(input("Введіть зсув: "))
            decrypted_text = decrypt_caesar(text, shift)
            print("Розшифрований текст:", decrypted_text)
        elif choice == '3':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()