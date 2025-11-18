# Parser ↔ Builder Integration Test Cases

## Module: tests/integrations/test_integration.py::TestParserBuilderIntegration

### Overview
Интеграционные тест-кейсы для проверки взаимодействия между парсерами (BuildInfoParser, SkillsParser, ItemsParser) и билдерами (StatsBuilder, ConfigBuilder, ItemSetBuilder).

---

## Test Case: TC-INT-PARSER-BUILDER-001
**Title:** Parser to builder flow

**Category:** Positive

**Integration:** BuildInfoParser ↔ SkillsParser ↔ ItemsParser ↔ StatsBuilder ↔ ConfigBuilder ↔ ItemSetBuilder

**Description:** Проверка полного потока: парсинг XML → использование данных в билдерах → проверка результатов

**Preconditions:**
- Есть валидный XML (sample_xml fixture)

**Test Steps:**
1. Парсить XML в root элемент
2. Парсить build info через BuildInfoParser.parse()
3. Парсить skill groups через SkillsParser.parse_skill_groups()
4. Парсить items через ItemsParser.parse_items()
5. Построить stats через StatsBuilder.build()
6. Извлечь level из build_info и построить config через ConfigBuilder.build()
7. Построить item sets через ItemSetBuilder.build_all()

**Expected Result:**
- stats.life == 163.0
- config.enemy_level == 84
- len(item_sets) == 1
- len(skills) == 1
- len(items) == 1

---
