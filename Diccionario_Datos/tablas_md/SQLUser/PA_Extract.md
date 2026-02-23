# SQLUser.PA_Extract

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXTR_RowId | bigint | PK |  | NO | - |
| EXTR_BatchNumber | varchar |  |  | SI | BatchNumber |
| EXTR_ESISDateFrom | date |  |  | SI | ESISDateFrom |
| EXTR_ESISDateRun | date |  |  | SI | ESIS DateRun |
| EXTR_ESISDateTo | date |  |  | SI | ESISDateTo |
| EXTR_ESISInternalNumber | varchar |  |  | SI | ESIS Internal Number |
| EXTR_ESISLastMMYY | varchar |  |  | SI | ESIS Lastextract MMYY |
| EXTR_ESISTimeRun | time |  |  | SI | ESIS Time Run |
| EXTR_ExtractType_DR | bigint |  | FK | SI | Des Ref PACExtractType |
| EXTR_FileName | varchar |  |  | SI | FileName |
| EXTR_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| EXTR_PRS2LastBatchClosingDat | date |  |  | SI | PRS2 Last Batch Closing Date |
| EXTR_PRS2LastBatchStartDate | date |  |  | SI | PRS2 Last Batch StartDate |
| EXTR_RollBackDate | date |  |  | SI | RollBackDate |
| EXTR_RollBackTime | time |  |  | SI | RollBackTime |
| EXTR_RollBackUser_DR | bigint |  | FK | SI | Des Ref RollBackUser |
| EXTR_SignifFacility_DR | bigint |  | FK | SI | Des Ref SignifFacility |
| Q185Q1 | - |  |  | SI | Tratamiento |
| Q185Q2 | - |  |  | SI | Fecha de Inicio |
| Q185Q3 | - |  |  | SI | Fecha de Termino |
| Q185Q4 | - |  |  | SI | Esquema / Tipo / Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*