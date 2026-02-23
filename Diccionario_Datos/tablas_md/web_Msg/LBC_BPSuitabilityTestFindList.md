# web_Msg.LBC_BPSuitabilityTestFindList

**Schema:** web_Msg
**Columnas:** 42
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| BloodGroupStatus | varchar |  |  | SI | Blood Group Status |
| BloodProductDR | bigint |  | FK | SI | Blood Product |
| BloodProductGroupDR | bigint |  | FK | SI | Blood Product Group |
| CMVStatus | varchar |  |  | SI | CMV Status |
| ClinicalConditionDR | bigint |  | FK | SI | Clinical Condition |
| ClinicalConditions | varchar |  |  | SI | Calculated Clinical Condition |
| DOB | date |  |  | SI | Date of Birth |
| DonationDate | date |  |  | SI | Donation Date
Used to calculate the unit age |
| DonationTime | time |  |  | SI | Donation Time
Used to calculate the unit age |
| EntryModeDR | bigint |  | FK | SI | Mode of Entry |
| EpisodeAge | varchar |  |  | SI | Episode Age |
| EpisodeAgeFloat | varchar |  |  | SI | Episode Age Float. The floating point representati... |
| EpisodeAgeFloatGet | varchar |  |  | SI | Return a floating point representation of the age.... |
| EthnicityDR | bigint |  | FK | SI | Ethnicity |
| HbSStatus | varchar |  |  | SI | HbS Status |
| HepatitisE | varchar |  |  | SI | Hepatitis E |
| HighTitreHaemolysinsStatus | varchar |  |  | SI | High Titre Haemolysins Status |
| ID | varchar |  |  | NO | - |
| IncludeMiscRuleTesting | bit |  |  | SI | A toggle to include/exclude the miscellaneous rule... |
| IrradiatedStatus | varchar |  |  | SI | Irradiated Status |
| LBBloodProductDR | bigint |  | FK | SI | The context Blood Produce. Used to index the rules... |
| LBTestSetDR | bigint |  | FK | SI | The context Test Set. Used to index the rules to t... |
| NeonatalMode | varchar |  |  | SI | Flag to indicate that this configuration applies o... |
| PatientBloodGroupDR | bigint |  | FK | SI | Patient Blood Group |
| PatientFlagDR | bigint |  | FK | SI | Patient Flag |
| Pregnant | varchar |  |  | SI | Pregnant |
| ReadOnly | bit |  |  | SI | - |
| RequiredByDate | date |  |  | SI | Required by date. Used to test age suitability of ... |
| RequiredByTime | time |  |  | SI | Required by time Used to test age suitability of a... |
| SessionId | varchar |  |  | SI | - |
| SexDR | bigint |  | FK | SI | Sex |
| SpeciesDR | bigint |  | FK | SI | Species
Select the species type. The lookup refer... |
| UnitBloodGroupDR | bigint |  | FK | SI | Unit Blood Group |
| WeeksPregnant | double |  |  | SI | Number Of Weeks Pregnant |
| childsub | bigint |  |  | NO | - |
| hiddenAntibodyList | varchar |  |  | SI | Antibodies // HTMLTextBox ? |
| hiddenAntigenList | varchar |  |  | SI | Antigen |
| hiddenClinicalConditionsList | varchar |  |  | SI | Clinical Condition List (^ delimited) |
| hiddenPatientAdditionalBloodGroupList | varchar |  |  | SI | Patient Additional Blood Groups |
| hiddenPatientFlagList | varchar |  |  | SI | Patient Flag List |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*