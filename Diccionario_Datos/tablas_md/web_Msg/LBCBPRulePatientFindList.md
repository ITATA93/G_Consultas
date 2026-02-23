# web_Msg.LBCBPRulePatientFindList

**Schema:** web_Msg
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| Active | varchar |  |  | SI | Active  |
| AdvancedSearchOpen | varchar |  |  | SI | Open the Advanced Accordion if used in a search |
| AntigenDR | bigint |  | FK | SI | Antigen |
| BloodGroupStatus | varchar |  |  | SI | Blood Group Status |
| BloodProductDR | bigint |  | FK | SI | Blood Product |
| CMVStatus | varchar |  |  | SI | CMV Status |
| ClinicalConditionDR | bigint |  | FK | SI | Clinical Condition |
| Description | varchar |  |  | SI | Description |
| EpisodeAge | varchar |  |  | SI | Episode Age |
| EpisodeAgeFloatGet | double |  |  | SI | Return a floating point representation of the age |
| HbSStatus | varchar |  |  | SI | HbS Status |
| HighTitreHaemolysinsStatus | varchar |  |  | SI | High Titre Haemolysins Status |
| ID | varchar |  |  | NO | - |
| IrradiatedStatus | varchar |  |  | SI | Irradiated Status |
| PatientBloodGroupDR | bigint |  | FK | SI | Patient Blood Group |
| PatientFlagDR | bigint |  | FK | SI | Patient Flag |
| Pregnant | varchar |  |  | SI | Pregnant |
| ReadOnly | bit |  |  | SI | - |
| RuleAction | varchar |  |  | SI | Rule Action |
| SessionId | varchar |  |  | SI | - |
| SexDR | bigint |  | FK | SI | Sex |
| StandardSearchOpen | varchar |  |  | SI | Open the Standard Accordion if used in a search |
| UnitAge | double |  |  | SI | Age of Unit |
| UnitBloodGroupDR | bigint |  | FK | SI | Unit Blood Group |
| childsub | bigint |  |  | NO | - |
| hiddenAntibodyList | varchar |  |  | SI | Antibodies // HTMLTextBox ? |
| hiddenBloodProductGroupList | varchar |  |  | SI | Blood Product Groups |
| hiddenEntryModesList | varchar |  |  | SI | Entry Modes |
| hiddenPatientAdditionalBloodGroupList | varchar |  |  | SI | Patient Additional Blood Groups |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*