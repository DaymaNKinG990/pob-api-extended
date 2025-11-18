# Full Workflow Integration Test Cases

## Module: tests/integrations/test_integration.py::TestFullWorkflow

### Overview
Интеграционные тест-кейсы для проверки полных рабочих процессов (end-to-end scenarios) от валидации до создания build.

---

## Test Case: TC-INT-WORKFLOW-001
**Title:** Complete workflow: validate → parse → build

**Category:** Positive

**Integration:** InputValidator ↔ XMLValidator ↔ DefaultBuildParser ↔ StatsBuilder ↔ ConfigBuilder ↔ ItemSetBuilder

**Description:** Проверка полного рабочего процесса: валидация → парсинг → построение всех компонентов

**Preconditions:**
- Есть валидный XML (sample_xml fixture)

**Test Steps:**
1. Закодировать sample_xml в bytes
2. Валидировать XML bytes через InputValidator.validate_xml_bytes()
3. Парсить XML в root элемент
4. Валидировать структуру через XMLValidator.validate_build_structure()
5. Создать DefaultBuildParser
6. Парсить build info, skills, items, trees через парсер
7. Построить stats, config, item sets через билдеры
8. Проверить все компоненты

**Expected Result:**
- build_info["class_name"] == "Scion"
- len(skills) == 1
- len(items) == 1
- len(trees) == 1
- stats.life == 163.0
- config.enemy_level == 84
- len(item_sets) == 1

---

## Test Case: TC-INT-WORKFLOW-002
**Title:** Factory workflow

**Category:** Positive

**Integration:** BuildFactory ↔ PathOfBuildingAPI

**Description:** Проверка полного рабочего процесса через фабрику

**Preconditions:**
- Есть валидный XML (sample_xml fixture)

**Test Steps:**
1. Закодировать sample_xml в bytes
2. Создать BuildFactory
3. Создать build через factory.from_xml_bytes()

**Expected Result:**
- build.class_name == "Scion"
- build.ascendancy_name == "Ascendant"
- build.level == 1
- build.bandit == "Alira"
- build.stats.life == 163.0
- build.config.enemy_level == 84
- len(build.skill_groups) == 1
- len(build.items) == 1
- len(build.trees) == 1

---
