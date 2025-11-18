# Calculator Minion Unit Test Cases

## Module: pobapi.calculator.minion

### Overview
Unit test cases for the calculator.minion module, which handles minion statistics calculations.

---

## Test Case: TC-CALC-MINION-001
**Title:** MinionStats.__init__() with defaults

**Category:** Positive

**Description:** Verify initialization of MinionStats with default values

**Preconditions:**
- None

**Test Steps:**
1. Call `MinionStats()`
2. Verify attribute values

**Input:**
- No parameters (default initialization)

**Expected Result:**
- stats.damage_physical == 0.0
- stats.damage_fire == 0.0
- stats.damage_cold == 0.0
- stats.damage_lightning == 0.0
- stats.damage_chaos == 0.0
- stats.life == 0.0
- stats.energy_shield == 0.0
- stats.armour == 0.0
- stats.evasion == 0.0
- stats.attack_speed == 1.0
- stats.cast_speed == 1.0
- stats.movement_speed == 1.0
- stats.crit_chance == 5.0
- stats.crit_multiplier == 150.0
- stats.accuracy == 0.0
- stats.fire_resistance == 0.0
- stats.cold_resistance == 0.0
- stats.lightning_resistance == 0.0
- stats.chaos_resistance == 0.0
- stats.dps == 0.0

---

## Test Case: TC-CALC-MINION-002
**Title:** MinionStats.total_damage property

**Category:** Positive

**Description:** Verify the total_damage property for calculating total damage

**Preconditions:**
- MinionStats created with various damage types

**Test Steps:**
1. Create MinionStats with various damage types
2. Call `stats.total_damage`
3. Verify the result

**Input:**
- stats = MinionStats(
    damage_physical=100.0,
    damage_fire=50.0,
    damage_cold=25.0,
    damage_lightning=10.0,
    damage_chaos=5.0
  )

**Expected Result:**
- stats.total_damage == 190.0
- Type: float

---

## Test Case: TC-CALC-MINION-003
**Title:** MinionCalculator.__init__() initialization

**Category:** Positive

**Description:** Verify MinionCalculator initialization

**Preconditions:**
- None

**Test Steps:**
1. Create MinionCalculator
2. Verify initialization

**Input:**
- modifier_system = ModifierSystem() (initialized modifier system)

**Expected Result:**
- minion_calculator.modifiers is not None
- isinstance(minion_calculator.modifiers, ModifierSystem) == True

---

## Test Case: TC-CALC-MINION-004
**Title:** MinionCalculator.calculate_minion_damage() with no modifiers

**Category:** Positive

**Description:** Verify the calculate_minion_damage() method without modifiers

**Preconditions:**
- MinionCalculator is initialized

**Test Steps:**
1. Call `minion_calculator.calculate_minion_damage()`
2. Verify the result

**Input:**
- base_damage = None (or empty dict {})
- context = None (or empty dict {})

**Expected Result:**
- isinstance(result, dict) == True
- result.get("Physical", 0.0) == 0.0
- result.get("Fire", 0.0) == 0.0
- result.get("Cold", 0.0) == 0.0
- result.get("Lightning", 0.0) == 0.0
- result.get("Chaos", 0.0) == 0.0
- All values are float type

---

## Test Case: TC-CALC-MINION-005
**Title:** MinionCalculator.calculate_minion_damage() with base damage

**Category:** Positive

**Description:** Verify the calculate_minion_damage() method with base damage

**Preconditions:**
- None

**Test Steps:**
1. Create base_damage dict with specific values
2. Call `calculate_minion_damage(base_damage)`
3. Verify the result

**Input:**
- base_damage = {"Physical": 100.0, "Fire": 50.0}
- context = None (or empty dict {})
- No modifiers added to modifier system

**Expected Result:**
- isinstance(result, dict) == True
- "Physical" in result == True
- "Fire" in result == True
- "Cold" in result == True
- "Lightning" in result == True
- "Chaos" in result == True
- result["Physical"] >= 0.0
- result["Fire"] >= 0.0
- result["Cold"] == 0.0
- result["Lightning"] == 0.0
- result["Chaos"] == 0.0
- All values are float type

---

## Test Case: TC-CALC-MINION-006
**Title:** MinionCalculator.calculate_minion_damage() with modifiers

**Category:** Positive

**Description:** Verify the calculate_minion_damage() method with modifiers

**Preconditions:**
- MinionDamage modifiers are added

**Test Steps:**
1. Add MinionDamage modifiers
2. Call calculate_minion_damage()
3. Verify the result

**Input:**
- base_damage = {"Physical": 100.0}
- context = None (or empty dict {})
- Modifier added: MinionDamage, value=50.0, type=INCREASED

**Expected Result:**
- isinstance(result, dict) == True
- result["Physical"] >= 0.0
- result["Fire"] == 0.0
- result["Cold"] == 0.0
- result["Lightning"] == 0.0
- result["Chaos"] == 0.0
- All values are float type

---

## Test Case: TC-CALC-MINION-007
**Title:** MinionCalculator.calculate_minion_life() with no modifiers

**Category:** Positive

**Description:** Verify the calculate_minion_life() method without modifiers

**Preconditions:**
- MinionCalculator is initialized

**Test Steps:**
1. Call `minion_calculator.calculate_minion_life()`
2. Verify the result

**Input:**
- base_life = 0.0 (default)
- context = None (or empty dict {})
- No modifiers added to modifier system

**Expected Result:**
- result == 0.0
- Type: float

---

## Test Case: TC-CALC-MINION-008
**Title:** MinionCalculator.calculate_minion_life() with modifiers

**Category:** Positive

**Description:** Verify the calculate_minion_life() method with modifiers

**Preconditions:**
- MinionLife modifiers are added

**Test Steps:**
1. Add MinionLife modifiers
2. Call calculate_minion_life()
3. Verify the result

**Input:**
- base_life = 0.0 (default)
- context = None (or empty dict {})
- Modifier added: MinionLife, value=100.0, type=FLAT
- Modifier added: MinionLife, value=50.0, type=INCREASED

**Expected Result:**
- result >= 100.0
- Type: float

---

## Test Case: TC-CALC-MINION-009
**Title:** MinionCalculator.calculate_all_minion_stats() empty

**Category:** Edge Case

**Description:** Verify the calculate_all_minion_stats() method without modifiers

**Preconditions:**
- None

**Test Steps:**
1. Call `calculate_all_minion_stats()`
2. Verify the result

**Input:**
- base_damage = None (or empty dict {})
- base_life = 0.0 (default)
- base_es = 0.0 (default)
- base_attack_speed = 1.0 (default)
- base_cast_speed = 1.0 (default)
- context = None (or empty dict {})
- No modifiers added to modifier system

**Expected Result:**
- isinstance(result, MinionStats) == True
- result.damage_physical == 0.0
- result.damage_fire == 0.0
- result.damage_cold == 0.0
- result.damage_lightning == 0.0
- result.damage_chaos == 0.0
- result.life == 0.0
- result.energy_shield == 0.0
- result.attack_speed == 1.0
- result.cast_speed == 1.0
- result.movement_speed == 1.0
- result.crit_chance == 5.0
- result.crit_multiplier == 150.0
- result.dps == 0.0

---

## Test Case: TC-CALC-MINION-010
**Title:** MinionCalculator.calculate_all_minion_stats() with modifiers

**Category:** Positive

**Description:** Verify the calculate_all_minion_stats() method with modifiers

**Preconditions:**
- Minion modifiers are added

**Test Steps:**
1. Add minion modifiers
2. Call calculate_all_minion_stats()
3. Verify the result

**Input:**
- base_damage = None (or empty dict {})
- base_life = 0.0 (default)
- base_es = 0.0 (default)
- base_attack_speed = 1.0 (default)
- base_cast_speed = 1.0 (default)
- context = None (or empty dict {})
- Modifier added: MinionDamage, value=50.0, type=INCREASED
- Modifier added: MinionLife, value=100.0, type=FLAT

**Expected Result:**
- isinstance(result, MinionStats) == True
- result.life > 0.0
- All statistics calculated with modifiers applied
- All values are float type

---

## Test Case: TC-CALC-MINION-011
**Title:** MinionCalculator.calculate_minion_resistances()

**Category:** Positive

**Description:** Verify the calculate_minion_resistances() method for calculating minion resistances

**Preconditions:**
- MinionResistances modifiers are added

**Test Steps:**
1. Add modifiers for minion resistances
2. Call calculate_minion_resistances()
3. Verify the result

**Input:**
- context = None (or empty dict {})
- Modifier added: MinionFireResistance, value=75.0, type=FLAT

**Expected Result:**
- isinstance(result, dict) == True
- result["fire"] == 75.0
- result["cold"] == 0.0
- result["lightning"] == 0.0
- result["chaos"] == 0.0
- All values are float type

---

## Test Case: TC-CALC-MINION-012
**Title:** MinionCalculator.calculate_minion_attack_speed()

**Category:** Positive

**Description:** Verify the calculate_minion_attack_speed() method for calculating minion attack speed

**Preconditions:**
- MinionAttackSpeed modifiers are added

**Test Steps:**
1. Add modifiers for minion attack speed
2. Call calculate_minion_attack_speed()
3. Verify the result

**Input:**
- base_speed = 1.0 (default)
- context = None (or empty dict {})
- Modifier added: MinionAttackSpeed, value=20.0, type=INCREASED

**Expected Result:**
- result >= 1.0
- result > 0.0
- Type: float

---

## Test Case: TC-CALC-MINION-013
**Title:** MinionCalculator.calculate_minion_limit()

**Category:** Positive

**Description:** Verify the calculate_minion_limit() method for calculating minion limit

**Preconditions:**
- MinionLimit modifiers are added

**Test Steps:**
1. Add MinionLimit modifiers
2. Call calculate_minion_limit() via modifier_system.calculate_stat("MinionLimit", base_value)
3. Verify the result

**Input:**
- base_value = 0.0
- Modifier added: MinionLimit, value=5.0, type=FLAT

**Expected Result:**
- result == 5.0
- Type: float

**Alternative Input (with increased modifier):**
- base_value = 10.0
- Modifier added: MinionLimit, value=50.0, type=INCREASED

**Expected Result:**
- result == 15.0 (10.0 * 1.5)
- Type: float

---

## Test Case: TC-CALC-MINION-014
**Title:** MinionCalculator.calculate_minion_life() with more/less modifiers

**Category:** Positive

**Description:** Verify the calculate_minion_life() method with more/less modifiers

**Preconditions:**
- More/less modifiers are added

**Test Steps:**
1. Add more/less modifiers for MinionLife
2. Call calculate_minion_life()
3. Verify the result

**Input:**
- base_life = 0.0 (default)
- context = None (or empty dict {})
- Modifier added: MinionLife, value=100.0, type=FLAT
- Modifier added: MinionLifeMore, value=20.0, type=MORE
- Modifier added: MinionLifeLess, value=10.0, type=LESS

**Expected Result:**
- result > 0.0
- result >= 100.0
- Type: float

---

## Test Case: TC-CALC-MINION-015
**Title:** MinionCalculator.calculate_minion_damage() with more/less modifiers

**Category:** Positive

**Description:** Verify the calculate_minion_damage() method with more/less modifiers

**Preconditions:**
- More/less modifiers are added

**Test Steps:**
1. Add more/less modifiers for MinionDamage
2. Call calculate_minion_damage()
3. Verify the result

**Input:**
- base_damage = None (or empty dict {})
- context = None (or empty dict {})
- Modifier added: MinionPhysicalDamage, value=100.0, type=FLAT
- Modifier added: MinionDamageMore, value=30.0, type=MORE
- Modifier added: MinionDamageLess, value=10.0, type=LESS

**Expected Result:**
- isinstance(result, dict) == True
- "Physical" in result == True
- result["Physical"] > 0.0
- Type: float

---

## Test Case: TC-CALC-MINION-016
**Title:** MinionCalculator.calculate_minion_energy_shield()

**Category:** Positive

**Description:** Verify the calculate_minion_energy_shield() method for calculating minion energy shield

**Preconditions:**
- MinionEnergyShield modifiers are added

**Test Steps:**
1. Add modifiers for minion energy shield
2. Call calculate_minion_energy_shield()
3. Verify the result

**Input:**
- base_es = 0.0 (default)
- context = None (or empty dict {})
- Modifier added: MinionEnergyShield, value=100.0, type=FLAT
- Modifier added: MinionEnergyShieldMore, value=20.0, type=MORE
- Modifier added: MinionEnergyShieldLess, value=10.0, type=LESS

**Expected Result:**
- result > 0.0
- Type: float

---

## Test Case: TC-CALC-MINION-017
**Title:** MinionCalculator.calculate_minion_attack_speed() with increased

**Category:** Positive

**Description:** Verify the calculate_minion_attack_speed() method with increased modifiers

**Preconditions:**
- Increased modifiers are added

**Test Steps:**
1. Add increased modifiers for MinionAttackSpeed
2. Call calculate_minion_attack_speed()
3. Verify the result

**Input:**
- base_speed = 1.0 (default)
- context = None (or empty dict {})
- Modifier added: MinionAttackSpeed, value=10.0, type=FLAT
- Modifier added: MinionAttackSpeed, value=30.0, type=INCREASED

**Expected Result:**
- result > 1.0
- Type: float

---

## Test Case: TC-CALC-MINION-018
**Title:** MinionCalculator.calculate_minion_attack_speed() with more/less

**Category:** Positive

**Description:** Verify the calculate_minion_attack_speed() method with more/less modifiers

**Preconditions:**
- More/less modifiers are added

**Test Steps:**
1. Add more/less modifiers for MinionAttackSpeed
2. Call calculate_minion_attack_speed()
3. Verify the result

**Input:**
- base_speed = 1.0 (default)
- context = None (or empty dict {})
- Modifier added: MinionAttackSpeedMore, value=25.0, type=MORE
- Modifier added: MinionAttackSpeedLess, value=5.0, type=LESS

**Expected Result:**
- result > 0.0
- Type: float

---

## Test Case: TC-CALC-MINION-019
**Title:** MinionCalculator.calculate_minion_cast_speed()

**Category:** Positive

**Description:** Verify the calculate_minion_cast_speed() method for calculating minion cast speed

**Preconditions:**
- MinionCastSpeed modifiers are added

**Test Steps:**
1. Add modifiers for minion cast speed
2. Call calculate_minion_cast_speed()
3. Verify the result

**Input:**
- base_speed = 1.0 (default)
- context = None (or empty dict {})
- Modifier added: MinionCastSpeed, value=10.0, type=FLAT
- Modifier added: MinionCastSpeed, value=40.0, type=INCREASED

**Expected Result:**
- result > 1.0
- Type: float

**Alternative Input (with more/less modifiers):**
- base_speed = 1.0 (default)
- context = None (or empty dict {})
- Modifier added: MinionCastSpeedMore, value=15.0, type=MORE
- Modifier added: MinionCastSpeedLess, value=5.0, type=LESS

**Expected Result:**
- result > 0.0
- Type: float
