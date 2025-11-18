# Factory Integration Test Cases

## Module: tests/integrations/test_integration.py::TestFactoryIntegration

### Overview
Интеграционные тест-кейсы для проверки взаимодействия BuildFactory с другими компонентами (DefaultBuildParser, PathOfBuildingAPI).

---

## Test Case: TC-INT-FACTORY-001
**Title:** Factory with custom parser

**Category:** Positive

**Integration:** BuildFactory ↔ DefaultBuildParser

**Description:** Проверка использования фабрики с кастомным парсером

**Preconditions:**
- Есть валидный XML (sample_xml fixture)

**Test Steps:**
1. Закодировать sample_xml в bytes
2. Создать DefaultBuildParser
3. Создать BuildFactory с кастомным парсером
4. Создать build через factory.from_xml_bytes()

**Expected Result:**
- build.class_name == "Scion"
- build._parser is parser (тот же парсер, что был передан)

---

## Test Case: TC-INT-FACTORY-002
**Title:** Factory creates valid build

**Category:** Positive

**Integration:** BuildFactory ↔ PathOfBuildingAPI

**Description:** Проверка создания валидного build через фабрику

**Preconditions:**
- Есть валидный XML (sample_xml fixture)

**Test Steps:**
1. Закодировать sample_xml в bytes
2. Создать BuildFactory
3. Создать build через factory.from_xml_bytes()

**Expected Result:**
- build.class_name == "Scion"
- build.level == 1
- build.stats.life == 163.0
- build.config.enemy_level == 84
- len(build.skill_groups) == 1
- len(build.items) == 1

---
