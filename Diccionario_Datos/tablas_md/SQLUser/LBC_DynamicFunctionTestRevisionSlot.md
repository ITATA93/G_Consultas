# SQLUser.LBC_DynamicFunctionTestRevisionSlot

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCDFTRS_ParRef | bigint | PK |  | NO | Parent table |
| ChildQ09DR | - |  |  | SI | Child Reference: Persons permitted to visit patien... |
| LBCDFTRS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCDFTRS_RowID | varchar |  |  | NO | - |
| LBCDFTRS_Sequence | double |  |  | SI | Slot sequence number within the dynamic function t... |
| LBCDFTRS_TestItems | varchar |  |  | SI | Test items associated with this slot
List of poss... |
| LBCDFTRS_TestSets | varchar |  |  | SI | Test sets associated with this slot
List of possi... |
| LBCDFTRS_TimeOffset | integer |  |  | SI | Slot offset time 
for this slot from start/openin... |
| LBCDFTRS_TimeWindow | integer |  |  | SI | Slot time window
for this slot. Tolerance interva... |
| LBCDFTRS_UseTIRanges | varchar |  |  | SI | Use Test Item Ranges for this slot |
| Q10Q1 | - |  |  | SI | Name |
| Q10Q2 | - |  |  | SI | Relationship |
| Q10Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*