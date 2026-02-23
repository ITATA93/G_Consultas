# SQLUser.LBC_InstrumentSensitivityTrans

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINST_ParRef | bigint | PK |  | NO | Parent instrument DR |
| LBCINST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINST_DateFrom | date |  |  | SI | Date From |
| LBCINST_DateTo | date |  |  | SI | Date To |
| LBCINST_InstrumentSensitivity | varchar |  |  | SI | Instrument sensitivity |
| LBCINST_RowID | varchar |  |  | NO | - |
| LBCINST_Sensitivity_DR | bigint |  | FK | SI | Internal sensitivity |
| Q26Q1 | - |  |  | SI | Dosis |
| Q26Q2 | - |  |  | SI | Fecha Prevista |
| Q26Q3 | - |  |  | SI | Fecha Efectiva |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*