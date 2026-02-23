# web_Msg.LB_BloodProductSuitabilityResult

**Schema:** web_Msg
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBBPSR_ABORhException_DR | varchar |  | FK | SI | ABO / Rh Exception record <br /> |
| LBBPSR_Acknowledged | varchar |  |  | SI | A flag to indicate that the user has acknowledged ... |
| LBBPSR_Action | varchar |  |  | NO | Action |
| LBBPSR_AntibodyIncompatibleAntigen_DR | varchar |  | FK | SI | Antibody Incompatible Antigen |
| LBBPSR_BloodProductSuitabilityRule_DR | varchar |  | FK | SI | Blood Product Suitability Rule |
| LBBPSR_BloodProduct_DR | bigint |  | FK | SI | The context Blood Produce. Used to index the rules... |
| LBBPSR_MaternalResult | varchar |  |  | SI | A flag to indicate that the result was based on te... |
| LBBPSR_Message | varchar |  |  | NO | Message |
| LBBPSR_PatientRule_DR | bigint |  | FK | SI | Blood Product Suitability Patient-level Rule
Used... |
| LBBPSR_Source | varchar |  |  | NO | Source
See BPRuleSourceVALUELIST |
| LBBPSR_TestSet_DR | bigint |  | FK | SI | The context Test Set. Used to index the rules to t... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*