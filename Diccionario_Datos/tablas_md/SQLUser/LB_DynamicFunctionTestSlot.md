# SQLUser.LB_DynamicFunctionTestSlot

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDFTS_ParRef | bigint | PK |  | NO | Parent table |
| LBDFTS_Closed | varchar |  |  | SI | Flag to indicate that this slot has been closed an... |
| LBDFTS_CollectionDate | date |  |  | SI | Collection Date |
| LBDFTS_CollectionTime | time |  |  | SI | Collection Time |
| LBDFTS_DynamicFunctionTestRevisionSlot_DR | varchar |  | FK | SI | Link to the code table definition of this DFT slot |
| LBDFTS_RowID | varchar |  |  | NO | - |
| LBDFTS_Sequence | double |  |  | SI | Sequence number of this slot |
| LBDFTS_SpecimenContainers | varchar |  |  | SI | Specimen containers associated with this slot |
| LBDFTS_TestSets | varchar |  |  | SI | Lab test sets present in this slot |
| Q64Q1 | - |  |  | SI | Edad aproximada (años) |
| Q64Q2 | - |  |  | SI | Tipo de resultado |
| Q64Q3 | - |  |  | SI | Duración aproximada (semanas) |
| Q64Q4 | - |  |  | SI | Resultado Perinatal |
| Q64Q5 | - |  |  | SI | Descripción |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*