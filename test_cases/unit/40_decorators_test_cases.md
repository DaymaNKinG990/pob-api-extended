# Decorators Unit Test Cases

## Module: pobapi.decorators

### Overview
Юнит-тест-кейсы для модуля decorators, который содержит декораторы `memoized_property` и `listify`.

---

## Test Case: TC-DECORATORS-001
**Title:** memoized_property() first access

**Category:** Positive

**Description:** Проверка мемоизации свойства при первом доступе

**Preconditions:**
- Класс с методом, декорированным @memoized_property

**Test Steps:**
1. Создать класс с @memoized_property методом
2. Первый раз обратиться к свойству
3. Проверить, что метод вызван
4. Проверить, что результат сохранен в атрибуте

**Expected Result:**
- Метод вызван один раз
- Результат сохранен в `_{method_name}` атрибуте
- Свойство возвращает результат

---

## Test Case: TC-DECORATORS-002
**Title:** memoized_property() second access

**Category:** Positive

**Description:** Проверка мемоизации свойства при повторном доступе

**Preconditions:**
- Класс с @memoized_property методом
- Первый доступ уже выполнен

**Test Steps:**
1. Создать класс с @memoized_property методом
2. Первый раз обратиться к свойству
3. Второй раз обратиться к свойству
4. Проверить, что метод вызван только один раз

**Expected Result:**
- Метод вызван только при первом доступе
- При втором доступе используется кэшированное значение
- Результат одинаковый

---

## Test Case: TC-DECORATORS-003
**Title:** memoized_property() attribute name

**Category:** Positive

**Description:** Проверка правильности имени атрибута для мемоизации

**Preconditions:**
- Нет

**Test Steps:**
1. Создать класс с @memoized_property методом с именем `test_prop`
2. Обратиться к свойству
3. Проверить наличие атрибута `_test_prop`

**Expected Result:**
- Атрибут `_test_prop` создан
- Имя атрибута соответствует `_{method_name}`

---

## Test Case: TC-DECORATORS-004
**Title:** memoized_property() different instances

**Category:** Positive

**Description:** Проверка, что мемоизация работает независимо для разных экземпляров

**Preconditions:**
- Нет

**Test Steps:**
1. Создать два экземпляра класса с @memoized_property
2. Обратиться к свойству в обоих экземплярах
3. Проверить, что каждый экземпляр имеет свой кэш

**Expected Result:**
- Каждый экземпляр имеет свой кэш
- Мемоизация работает независимо
- Результаты корректны

---

## Test Case: TC-DECORATORS-005
**Title:** listify() generator to list conversion

**Category:** Positive

**Description:** Проверка преобразования генератора в список

**Preconditions:**
- Функция-генератор создана

**Test Steps:**
1. Создать функцию-генератор
2. Применить @listify декоратор
3. Вызвать функцию
4. Проверить результат

**Expected Result:**
- Результат является list
- Все элементы генератора присутствуют
- Порядок элементов сохранен

---

## Test Case: TC-DECORATORS-006
**Title:** listify() empty generator

**Category:** Edge Case

**Description:** Проверка преобразования пустого генератора

**Preconditions:**
- Нет

**Test Steps:**
1. Создать функцию-генератор, возвращающую пустую последовательность
2. Применить @listify декоратор
3. Вызвать функцию
4. Проверить результат

**Expected Result:**
- Результат является пустым list
- result == []

---

## Test Case: TC-DECORATORS-007
**Title:** listify() preserves arguments

**Category:** Positive

**Description:** Проверка, что декоратор сохраняет аргументы функции

**Preconditions:**
- Нет

**Test Steps:**
1. Создать функцию-генератор с параметрами
2. Применить @listify декоратор
3. Вызвать функцию с различными аргументами
4. Проверить результаты

**Expected Result:**
- Аргументы переданы корректно
- Результаты соответствуют аргументам
- Декоратор не изменяет сигнатуру функции

---

## Test Case: TC-DECORATORS-008
**Title:** listify() wraps function metadata

**Category:** Positive

**Description:** Проверка, что декоратор сохраняет метаданные функции (@wraps)

**Preconditions:**
- Нет

**Test Steps:**
1. Создать функцию-генератор с docstring и именем
2. Применить @listify декоратор
3. Проверить __name__ и __doc__ декорированной функции

**Expected Result:**
- __name__ сохранен
- __doc__ сохранен
- Метаданные функции не потеряны

---

## Test Case: TC-DECORATORS-009
**Title:** memoized_property() with different return types

**Category:** Positive

**Description:** Проверка мемоизации свойства с различными типами возвращаемых значений

**Preconditions:**
- Нет

**Test Steps:**
1. Создать класс с @memoized_property методами, возвращающими разные типы
2. Обратиться к каждому свойству
3. Проверить результаты

**Expected Result:**
- Все типы данных мемоизируются корректно
- Результаты корректны
- Типы сохранены

---

## Test Case: TC-DECORATORS-010
**Title:** listify() with kwargs

**Category:** Positive

**Description:** Проверка преобразования генератора с kwargs

**Preconditions:**
- Нет

**Test Steps:**
1. Создать функцию-генератор с kwargs
2. Применить @listify декоратор
3. Вызвать функцию с kwargs
4. Проверить результат

**Expected Result:**
- kwargs переданы корректно
- Результат является list
- Результат корректен
