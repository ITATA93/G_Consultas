# web_Msg.LBC_TestSetRevisionTurnaroundTime

**Schema:** web_Msg
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTSRTT_AlertTurnaroundTime | integer |  |  | SI | Alert Turnaround Time (minutes)  |
| LBCTSRTT_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCTSRTT_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTSRTT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRTT_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRTT_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRTT_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCTSRTT_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTSRTT_MaxOutlierTime | integer |  |  | SI | Max Outlier Time  (minutes) |
| LBCTSRTT_ParRef | bigint |  |  | SI | Parent Reference LBCTestSetRevisionDR |
| LBCTSRTT_Priority_DR | bigint |  | FK | SI | Priority |
| LBCTSRTT_RowID | varchar |  |  | SI | - |
| LBCTSRTT_Sequence | double |  |  | SI | Rule Sequence |
| LBCTSRTT_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBCTSRTT_Species_DR | bigint |  | FK | SI | Species |
| LBCTSRTT_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTSRTT_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTSRTT_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCTSRTT_TargetTurnaroundTime | integer |  |  | SI | Target Turnaround Time (minutes) |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*