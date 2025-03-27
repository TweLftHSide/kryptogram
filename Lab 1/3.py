def permutation_cipher(text, key, mode):
    """Шифрує або розшифровує текст методом перестановочного шифру."""
    key_len = len(key)
    result = []

    if mode == 'encrypt':
        for i in range(0, len(text), key_len):
            block = text[i:i + key_len]
            for j in key:
                if j - 1 < len(block):
                    result.append(block[j - 1])
    elif mode == 'decrypt':
        block_len = (len(text) + key_len - 1) // key_len
        blocks = [''] * key_len
        for i, char in enumerate(text):
            blocks[i % key_len] += char

        for i in range(block_len):
            for j in range(key_len):
                if i < len(blocks[key.index(j + 1)]):
                    result.append(blocks[key.index(j + 1)][i])
    else:
        raise ValueError("Неправильний режим: повинен бути 'encrypt' або 'decrypt'")

    return "".join(result)

def main():
    """Головна функція програми."""
    while True:
        print("\nОберіть дію:")
        print("1. Шифрування")
        print("2. Розшифрування")
        print("3. Вихід")

        choice = input("Введіть ваш вибір (1/2/3): ")

        if choice == '1':
            text = input("Введіть текст для шифрування: ")
            key = list(map(int, input("Введіть ключ (наприклад, 3 1 2): ").split()))
            encrypted_text = permutation_cipher(text, key, 'encrypt')
            print("Зашифрований текст:", encrypted_text)
        elif choice == '2':
            text = input("Введіть текст для розшифрування: ")
            key = list(map(int, input("Введіть ключ (наприклад, 3 1 2): ").split()))
            decrypted_text = permutation_cipher(text, key, 'decrypt')
            print("Розшифрований текст:", decrypted_text)
        elif choice == '3':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()