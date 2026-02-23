# web_Msg.LB_DynamicFunctionTestSlot

**Schema:** web_Msg
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| CollectionDate | date |  |  | SI | Collection Date |
| CollectionTime | time |  |  | SI | Collection Time |
| ID | varchar |  |  | NO | - |
| LBDFTS_Closed | varchar |  |  | SI | Flag to indicate that this slot has been closed an... |
| LBDFTS_CollectionDate | date |  |  | SI | Collection Date |
| LBDFTS_CollectionTime | time |  |  | SI | Collection Time |
| LBDFTS_DynamicFunctionTestRevisionSlot_DR | varchar |  | FK | SI | Link to the code table definition of this DFT slot |
| LBDFTS_ParRef | bigint |  |  | SI | Parent table
Required by User.LBDynamicFunctionTe... |
| LBDFTS_RowID | varchar |  |  | SI | - |
| LBDFTS_Sequence | double |  |  | SI | Sequence number of this slot |
| LBDFTS_SpecimenContainers | varchar |  |  | SI | Specimen containers associated with this slot |
| LBDFTS_TestSets | varchar |  |  | SI | Lab test sets present in this slot |
| ParRef_DR | varchar |  | FK | SI | Parent message object associated with this slot |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SpecimenContainers | varchar |  |  | SI | Specimen container message object associated with ... |
| TestSetMsgs | varchar |  |  | SI | Test set message object associated with this slot |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*