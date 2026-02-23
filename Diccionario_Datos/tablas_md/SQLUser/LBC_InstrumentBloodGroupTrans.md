# SQLUser.LBC_InstrumentBloodGroupTrans

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINBGT_ParRef | bigint | PK |  | NO | Parent instrument DR |
| LBCINBGT_BloodGroup_DR | bigint |  | FK | SI | Internal Blood Group |
| LBCINBGT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINBGT_DateFrom | date |  |  | SI | Date From |
| LBCINBGT_DateTo | date |  |  | SI | Date To |
| LBCINBGT_InstrumentBloodGroup | varchar |  |  | SI | Instrument Blood Group |
| LBCINBGT_RowID | varchar |  |  | NO | - |
| Q24Q1 | - |  |  | SI | Baby Number |
| Q24Q2 | - |  |  | SI | Fetal heart baseline |
| Q24Q3 | - |  |  | SI | 3 Accelerations |
| Q24Q4 | - |  |  | SI | Unreactive |
| Q24Q5 | - |  |  | SI | Variability |
| Q24Q6 | - |  |  | SI | Decelerations |
| Q24Q7 | - |  |  | SI | Difficult to interpret |
| Q24Q8 | - |  |  | SI | Acceptable |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*