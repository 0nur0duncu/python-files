# Python Walrus Operatörü (`:=`)

Walrus operatörü, Python 3.8 ile tanıtılan ve değişken atamasını bir ifadede gerçekleştirmenizi sağlayan bir operatördür. Bu, kodunuzu daha kompakt ve okunabilir hale getirebilir.

## Sürüm Kontrolü

İlk olarak, Python sürümünüzün 3.8 veya üstü olduğundan emin olun:

```sh
python --version
```

## Kullanım Örnekleri

### While Döngüsü

Walrus operatörü, bir döngünün koşulunda atama yapmak için kullanılabilir:

```python
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers) and (n := numbers[i]) < 6:
    print(n)
    i += 1
```

### If İfadesi

Bir if ifadesinde atama yaparak kodu daha temiz hale getirebilirsiniz:

```python
if (value := input("Enter a number: ")).isnumeric():
    num = int(value)
    print(f"You entered the number: {num}")
```

### Liste Anlamı

Walrus operatörü, liste anlamında daha verimli kod yazmanızı sağlar:

```python
values = [1, 2, 3, 4, 5, 6]
filtered_values = [doubled for value in values if (doubled := value * 2) > 5]
print(filtered_values)  # Output: [6, 8, 10, 12]
```

## Python'u Güncelleme

Python sürümünüz 3.8 veya daha yüksek değilse, en son sürümü [python.org](https://www.python.org/downloads) adresinden indirerek güncelleyebilirsiniz.
