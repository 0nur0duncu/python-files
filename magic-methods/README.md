# Python Magic Methods

Python'da magic (özel) metodlar sınıfların davranışlarını özelleştirmek için kullanılır. İşte önemli magic metodlar ve özetleri:

## Yapıcılar ve Temsilciler

- `__init__(self, ...)`: Nesne oluşturulduğunda çağrılır.
- `__repr__(self)`: Nesnenin resmi (developers) temsilini döner.
- `__str__(self)`: Nesnenin string (users) temsilini döner.

## Koleksiyon ve İndeksleme

- `__len__(self)`: Nesnenin uzunluğunu döner.
- `__getitem__(self, key)`: İndeksleme ile elemanlara erişimi sağlar.
- `__setitem__(self, key, value)`: İndeksleme ile elemanları ayarlar.
- `__delitem__(self, key)`: İndeksleme ile elemanları siler.

## İterasyon

- `__iter__(self)`: Nesnenin iteratörünü döner.
- `__next__(self)`: Bir sonraki elemanı döner.

## Fonksiyonellik

- `__call__(self, *args, **kwargs)`: Nesnenin fonksiyon gibi çağrılmasını sağlar.

## Context Manager

- `__enter__(self)`: Context'e girildiğinde çağrılır.
- `__exit__(self, exc_type, exc_value, traceback)`: Context'ten çıkıldığında çağrılır.

## Attribute Erişimi

- `__getattr__(self, name)`: Öznitelik bulunamadığında çağrılır.
- `__setattr__(self, name, value)`: Öznitelik ayarlandığında çağrılır.
- `__delattr__(self, name)`: Öznitelik silindiğinde çağrılır.

## Descriptor Protokolü

- `__get__(self, instance, owner)`: Descriptor'a erişildiğinde çağrılır.
- `__set__(self, instance, value)`: Descriptor'a değer atandığında çağrılır.
- `__delete__(self, instance)`: Descriptor'dan değer silindiğinde çağrılır.

## Yeni ve Yok Edici

- `__new__(cls, ...)`: Yeni bir nesne örneği oluşturulduğunda çağrılır.
- `__del__(self)`: Nesne yok edilmeden önce çağrılır.

## Operatör Aşırı Yükleme

- `__add__(self, other)`: `+` operatörü için toplama işlemi.
- `__eq__(self, other)`: Eşitlik karşılaştırması.
- `__lt__(self, other)`: Küçüktür karşılaştırması.

Bu metodlar, Python'da sınıflarınızın daha esnek ve güçlü olmasını sağlar.
