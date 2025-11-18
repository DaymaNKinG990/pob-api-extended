# BuildModifier ↔ Serializer Integration Test Cases

## Module: tests/integrations/test_build_modifier_serializer_integration.py

### Overview
Интеграционные тест-кейсы для проверки взаимодействия между BuildModifier и сериализаторами (BuildXMLSerializer, ImportCodeGenerator).

---

## Test Case: TC-INT-MODIFIER-SERIALIZER-001
**Title:** Modify build then serialize to XML

**Category:** Positive

**Integration:** BuildModifier ↔ BuildXMLSerializer

**Description:** Проверка модификации build и сериализации в XML

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать test_item (Ring с модификаторами)
2. Добавить item через build._modifier.equip_item()
3. Сериализовать в XML через build.to_xml()
4. Парсить XML и проверить наличие Items элемента

**Expected Result:**
- xml is not None
- len(xml) > 0
- items_elem is not None (в XML есть Items элемент)

---

## Test Case: TC-INT-MODIFIER-SERIALIZER-002
**Title:** Modify build then generate import code

**Category:** Positive

**Integration:** BuildModifier ↔ ImportCodeGenerator

**Description:** Проверка модификации build и генерации import code

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать test_item (Belt с модификаторами)
2. Добавить item через build._modifier.equip_item()
3. Сгенерировать import code через ImportCodeGenerator.generate_from_api(build)

**Expected Result:**
- import_code is not None
- len(import_code) > 0

---

## Test Case: TC-INT-MODIFIER-SERIALIZER-003
**Title:** Multiple modifications then serialize

**Category:** Positive

**Integration:** BuildModifier ↔ BuildXMLSerializer ↔ ImportCodeGenerator

**Description:** Проверка множественных модификаций и сериализации

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать 3 items (Ring1, Ring2, Amulet)
2. Добавить все items через build._modifier.equip_item() в соответствующие слоты
3. Сериализовать в XML
4. Сгенерировать import code

**Expected Result:**
- xml is not None
- import_code is not None

---

## Test Case: TC-INT-MODIFIER-SERIALIZER-004
**Title:** Add skill then serialize

**Category:** Positive

**Integration:** BuildModifier ↔ BuildXMLSerializer

**Description:** Проверка добавления skill и сериализации

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать test_gem (Arc, level 20, quality 20)
2. Добавить skill через build._modifier.add_skill()
3. Сериализовать в XML
4. Парсить XML и проверить наличие Skills элемента

**Expected Result:**
- xml is not None
- skills_elem is not None (в XML есть Skills элемент)

---

## Test Case: TC-INT-MODIFIER-SERIALIZER-005
**Title:** Factory creates builder

**Category:** Positive

**Integration:** BuildFactory ↔ BuildBuilder ↔ PathOfBuildingAPI

**Description:** Проверка работы BuildFactory с BuildBuilder

**Preconditions:**
- Нет

**Test Steps:**
1. Создать BuildFactory
2. Создать build через create_build() builder
3. Установить class и level через builder
4. Получить API instance через builder.build()
5. Сериализовать в XML и создать новый build через factory.from_xml_bytes()

**Expected Result:**
- xml is not None

---

## Test Case: TC-INT-MODIFIER-SERIALIZER-006
**Title:** Factory and builder round trip

**Category:** Positive

**Integration:** BuildFactory ↔ BuildBuilder ↔ PathOfBuildingAPI

**Description:** Проверка round-trip: Factory → Builder → Factory

**Preconditions:**
- Нет

**Test Steps:**
1. Создать build с builder (Ranger, level 85)
2. Сериализовать в XML
3. Создать новый build из XML через factory.from_xml_bytes()
4. Сравнить class_name и level

**Expected Result:**
- build1.class_name == build2.class_name
- build1.level == build2.level

---
