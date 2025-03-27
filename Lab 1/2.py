def vigenere_cipher(text, key, mode):
    """Шифрує або розшифровує текст методом Віженера."""
    result = []
    key = key.upper()
    key_len = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_len]) - ord('A')
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            if mode == 'encrypt':
                shifted_char = chr((ord(char) - start + shift) % 26 + start)
            elif mode == 'decrypt':
                shifted_char = chr((ord(char) - start - shift) % 26 + start)
            else:
                raise ValueError("Неправильний режим: повинен бути 'encrypt' або 'decrypt'")

            result.append(shifted_char)
            key_index += 1
        else:
            result.append(char)

    return "".join(result)

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
            key = input("Введіть ключ: ")
            encrypted_text = vigenere_cipher(text, key, 'encrypt')
            print("Зашифрований текст:", encrypted_text)
        elif choice == '2':
            text = input("Введіть текст для розшифрування: ")
            key = input("Введіть ключ: ")
            decrypted_text = vigenere_cipher(text, key, 'decrypt')
            print("Розшифрований текст:", decrypted_text)
        elif choice == '3':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()