# Calculator Party Unit Test Cases

## Module: pobapi.calculator.party

### Overview
Юнит-тест-кейсы для модуля calculator.party, который отвечает за расчет партийных бонусов.

---

## Test Case: TC-CALC-PARTY-001
**Title:** PartyMember.__init__() with defaults

**Category:** Positive

**Description:** Проверка инициализации PartyMember с дефолтными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PartyMember()`
2. Проверить значения атрибутов

**Expected Result:**
- member.name == "Party Member"
- member.aura_effectiveness == 100.0
- member.auras == []
- member.buffs == []
- member.support_gems == []

---

## Test Case: TC-CALC-PARTY-002
**Title:** PartyMember.__init__() with custom values

**Category:** Positive

**Description:** Проверка инициализации PartyMember с кастомными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PartyMember(name="Support Build", auras=["Hatred", "Anger"], aura_effectiveness=50.0)`
2. Проверить значения атрибутов

**Expected Result:**
- member.name == "Support Build"
- len(member.auras) == 2
- member.aura_effectiveness == 50.0

---

## Test Case: TC-CALC-PARTY-003
**Title:** PartyCalculator.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации PartyCalculator

**Preconditions:**
- Нет

**Test Steps:**
1. Создать PartyCalculator
2. Проверить инициализацию

**Expected Result:**
- party_calculator.modifiers is not None

---

## Test Case: TC-CALC-PARTY-004
**Title:** PartyCalculator.add_party_member_auras() empty auras

**Category:** Edge Case

**Description:** Проверка метода add_party_member_auras() для члена партии без аур

**Preconditions:**
- PartyMember с пустым списком auras

**Test Steps:**
1. Создать PartyMember(auras=[])
2. Вызвать `party_calculator.add_party_member_auras(member)`
3. Проверить результат

**Expected Result:**
- modifiers == []
- Пустой список аур обработан корректно

---

## Test Case: TC-CALC-PARTY-005
**Title:** PartyCalculator.add_party_member_auras() Hatred aura

**Category:** Positive

**Description:** Проверка метода add_party_member_auras() для Hatred ауры

**Preconditions:**
- PartyMember с Hatred аурой

**Test Steps:**
1. Создать PartyMember(auras=["Hatred"])
2. Вызвать `party_calculator.add_party_member_auras(member)`
3. Проверить результат

**Expected Result:**
- len(modifiers) >= 1
- ColdDamage модификатор присутствует
- mod.mod_type == ModifierType.MORE

---

## Test Case: TC-CALC-PARTY-006
**Title:** PartyCalculator.add_party_member_auras() common auras

**Category:** Positive

**Description:** Проверка метода add_party_member_auras() для распространенных аур

**Preconditions:**
- PartyMember с различными аурами

**Test Steps:**
1. Создать PartyMember(name="Support", auras=["Anger", "Purity of Fire", "Grace", "Haste"])
2. Вызвать `party_calculator.add_party_member_auras(member, aura_effectiveness=100.0)`
3. Проверить результаты

**Expected Result:**
- **Anger aura:**
  - assert len([m for m in modifiers if "anger" in m.source.lower()]) == 2
  - assert any(m.stat == "FireDamage" and m.value == 36.0 and m.mod_type == ModifierType.MORE for m in modifiers)
  - assert any(m.stat == "PhysicalAsExtraFire" and m.value == 15.0 and m.mod_type == ModifierType.FLAT for m in modifiers)
- **Purity of Fire aura:**
  - assert len([m for m in modifiers if "purity_of_fire" in m.source.lower() or "purity of fire" in m.source.lower()]) == 1
  - assert any(m.stat == "FireResistance" and m.value == 22.0 and m.mod_type == ModifierType.FLAT for m in modifiers)
- **Grace aura:**
  - assert len([m for m in modifiers if "grace" in m.source.lower()]) == 1
  - assert any(m.stat == "Evasion" and m.value == 3000.0 and m.mod_type == ModifierType.FLAT for m in modifiers)
- **Haste aura:**
  - assert len([m for m in modifiers if "haste" in m.source.lower()]) == 3
  - assert any(m.stat == "AttackSpeed" and m.value == 21.0 and m.mod_type == ModifierType.INCREASED for m in modifiers)
  - assert any(m.stat == "CastSpeed" and m.value == 21.0 and m.mod_type == ModifierType.INCREASED for m in modifiers)
  - assert any(m.stat == "MovementSpeed" and m.value == 21.0 and m.mod_type == ModifierType.INCREASED for m in modifiers)
- **Total modifiers count:**
  - assert len(modifiers) == 7  # 2 from Anger + 1 from Purity of Fire + 1 from Grace + 3 from Haste
- **Source validation:**
  - assert all(m.source.startswith("party:") for m in modifiers)
  - assert all(member.name.lower() in m.source.lower() for m in modifiers)

---

## Test Case: TC-CALC-PARTY-007
**Title:** PartyCalculator.add_party_member_auras() with effectiveness

**Category:** Positive

**Description:** Проверка метода add_party_member_auras() с учетом effectiveness

**Preconditions:**
- PartyMember с aura_effectiveness < 100.0

**Test Steps:**
1. Создать PartyMember с aura_effectiveness=50.0
2. Вызвать add_party_member_auras()
3. Проверить результат

**Expected Result:**
- Модификаторы применены с учетом effectiveness
- Значения скорректированы
- Результат корректен

---

## Test Case: TC-CALC-PARTY-008
**Title:** PartyCalculator.add_party_member_buffs() empty buffs

**Category:** Edge Case

**Description:** Проверка метода add_party_member_buffs() для члена партии без баффов

**Preconditions:**
- PartyMember с пустым списком buffs

**Test Steps:**
1. Создать PartyMember(buffs=[])
2. Вызвать `party_calculator.add_party_member_buffs(member)`
3. Проверить результат

**Expected Result:**
- modifiers == []
- Пустой список баффов обработан корректно

---

## Test Case: TC-CALC-PARTY-009
**Title:** PartyCalculator.add_party_member_buffs() onslaught buff

**Category:** Positive

**Description:** Проверка метода add_party_member_buffs() для onslaught баффа

**Preconditions:**
- PartyMember с onslaught buff

**Test Steps:**
1. Создать PartyMember(buffs=["Onslaught"])
2. Вызвать `party_calculator.add_party_member_buffs(member)`
3. Проверить результат

**Expected Result:**
- Модификаторы для Onslaught присутствуют
- Результат корректен

---

## Test Case: TC-CALC-PARTY-010
**Title:** PartyCalculator.add_party_member_support_effects() empty

**Category:** Edge Case

**Description:** Проверка метода add_party_member_support_effects() для члена партии без support effects

**Preconditions:**
- PartyMember с пустым списком support_gems

**Test Steps:**
1. Создать PartyMember(support_gems=[])
2. Вызвать `party_calculator.add_party_member_support_effects(member)`
3. Проверить результат

**Expected Result:**
- modifiers == []
- Пустой список обработан корректно

---

## Test Case: TC-CALC-PARTY-011
**Title:** PartyCalculator.add_party_member_support_effects() with support gems

**Category:** Positive

**Description:** Проверка метода add_party_member_support_effects() с support gems

**Preconditions:**
- PartyMember с support_gems

**Test Steps:**
1. Создать PartyMember с support_gems=["Added Fire Damage Support", "Increased Area of Effect Support"]
2. Вызвать add_party_member_support_effects()
3. Проверить результат

**Expected Result:**
- support_gem_alpha: "Added Fire Damage Support" (level 20) produces:
  - stat="moreFireDamage", value=67.5, mod_type=ModifierType.MORE (percentage-based multiplier)
  - stat="physicalToFire", value=50.0, mod_type=ModifierType.FLAT (flat conversion percentage)
  - source="party:{member.name}:support:added fire damage support"
- support_gem_beta: "Increased Area of Effect Support" (level 20) produces:
  - stat="moreAreaOfEffect", value=77.5, mod_type=ModifierType.MORE (percentage-based multiplier)
  - source="party:{member.name}:support:increased area of effect support"
- Total modifiers count: 3 (2 from support_gem_alpha, 1 from support_gem_beta)
- All modifiers are properly marked with party source prefix
- MORE modifiers stack multiplicatively with other MORE modifiers
- FLAT modifier (physicalToFire) provides flat conversion value
- Final combined effect: both support gems contribute their modifiers independently

---

## Test Case: TC-CALC-PARTY-012
**Title:** PartyCalculator.calculate_party_aura_effectiveness() base

**Category:** Positive

**Description:** Проверка метода calculate_party_aura_effectiveness() с базовым значением

**Preconditions:**
- Нет модификаторов PartyAuraEffectiveness
- context пустой или None
- Модификаторы не применяются к базовому значению

**Test Steps:**
1. Вызвать `calculate_party_aura_effectiveness(context)` с пустым context или None
2. Проверить, что результат равен базовому значению

**Expected Result:**
- Базовое значение возвращено — 50.0
- Результат равен 50.0 (базовая эффективность аур от членов партии составляет 50%)
- Результат корректен и может быть использован для автоматизированной проверки равенства

---

## Test Case: TC-CALC-PARTY-013
**Title:** PartyCalculator.calculate_party_aura_effectiveness() with modifiers

**Category:** Positive

**Description:** Проверка метода calculate_party_aura_effectiveness() с модификаторами

**Preconditions:**
- Модификаторы PartyAuraEffectiveness добавлены

**Test Steps:**
1. Добавить модификаторы PartyAuraEffectiveness
2. Вызвать calculate_party_aura_effectiveness()
3. Проверить результат

**Expected Result:**
- Effectiveness рассчитан с учетом модификаторов
- Результат корректен

---

## Test Case: TC-CALC-PARTY-014
**Title:** PartyCalculator.process_party() empty party

**Category:** Edge Case

**Description:** Проверка метода process_party() для пустой партии

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `party_calculator.process_party([])`
2. Проверить результат

**Expected Result:**
- modifiers == []
- Пустая партия обработана корректно

---

## Test Case: TC-CALC-PARTY-015
**Title:** PartyCalculator.process_party() multiple members

**Category:** Positive

**Description:** Проверка метода process_party() для нескольких членов партии

**Preconditions:**
- Несколько PartyMember созданы

**Test Steps:**
1. Создать список PartyMember
2. Вызвать `party_calculator.process_party(members)`
3. Проверить результат

**Expected Result:**
- Модификаторы от всех членов применены
- Результат корректен

---

## Test Case: TC-CALC-PARTY-016
**Title:** PartyCalculator.add_party_member_auras() None auras

**Category:** Edge Case

**Description:** Проверка метода add_party_member_auras() для None auras

**Preconditions:**
- PartyMember с auras=None

**Test Steps:**
1. Создать PartyMember с auras=None
2. Вызвать add_party_member_auras()
3. Проверить результат

**Expected Result:**
- modifiers == []
- None обработан корректно

---

## Test Case: TC-CALC-PARTY-017
**Title:** PartyCalculator.add_party_member_buffs() None buffs

**Category:** Edge Case

**Description:** Проверка метода add_party_member_buffs() для None buffs

**Preconditions:**
- PartyMember с buffs=None

**Test Steps:**
1. Создать PartyMember с buffs=None
2. Вызвать add_party_member_buffs()
3. Проверить результат

**Expected Result:**
- modifiers == []
- None обработан корректно

---

## Test Case: TC-CALC-PARTY-018
**Title:** PartyCalculator.add_party_member_support_effects() None support_gems

**Category:** Edge Case

**Description:** Проверка метода add_party_member_support_effects() для None support_gems

**Preconditions:**
- PartyMember с support_gems=None

**Test Steps:**
1. Создать PartyMember с support_gems=None
2. Вызвать add_party_member_support_effects()
3. Проверить результат

**Expected Result:**
- modifiers == []
- None обработан корректно

---

## Test Case: TC-CALC-PARTY-019
**Title:** PartyCalculator.calculate_party_aura_effectiveness() None context

**Category:** Edge Case

**Description:** Проверка метода calculate_party_aura_effectiveness() с None контекстом

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать calculate_party_aura_effectiveness() с None контекстом
2. Проверить обработку

**Expected Result:**
- None контекст обработан корректно
- Результат корректен или выбрасывается исключение


- None контекст заменяется на пустой словарь {} внутри функции
- Исключения не выбрасываются
