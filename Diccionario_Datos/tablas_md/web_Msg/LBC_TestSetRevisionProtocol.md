# web_Msg.LBC_TestSetRevisionProtocol

**Schema:** web_Msg
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTSRP_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTSRP_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| LBCTSRP_Container_DR | bigint |  | FK | SI | Container |
| LBCTSRP_DateFrom | date |  |  | SI | Date From
Effective date for the record
Required... |
| LBCTSRP_DateTo | date |  |  | SI | Date To
Last day the record is active
Optional. ... |
| LBCTSRP_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCTSRP_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTSRP_ParRef | bigint |  |  | SI | - |
| LBCTSRP_Priority_DR | bigint |  | FK | SI | Priority |
| LBCTSRP_Protocol_DR | bigint |  | FK | SI | Lab Protocol
Required by User.LBCTestSetRevisionP... |
| LBCTSRP_RowID | varchar |  |  | SI | - |
| LBCTSRP_Sequence | numeric |  |  | SI | Rule Sequence |
| LBCTSRP_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBCTSRP_Species_DR | bigint |  | FK | SI | Species |
| LBCTSRP_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTSRP_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTSRP_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*