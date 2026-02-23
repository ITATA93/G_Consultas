# Tools_DrugUpload.OrderAlerts

**Schema:** Tools_DrugUpload
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Alert | varchar |  |  | NO | Alert (Text) |
| Code | varchar |  |  | NO | Item Code reference |
| DateFrom | date |  |  | SI | as given  |
| DateTo | date |  |  | SI | as given  |
| Gender | varchar |  |  | SI | as given M,F,"" |
| ICD10 | varchar |  |  | SI | ICD10 reference (Code for "reading reference") |
| ICD9 | varchar |  |  | SI | ICD9 reference (Code for "reading reference") |
| ICDrow | varchar |  |  | NO | ICD Rowreference (Row for "generation reference") |
| LowerAge | double |  |  | SI | as given  |
| LowerAgePeriod | varchar |  |  | SI | as given W,M,Y |
| Period | varchar |  |  | SI | as given min,H,D,W,M,Y |
| ReasonRequired | varchar |  |  | SI | as given Y/N |
| Severity | varchar |  |  | SI | Severity (RowID) |
| TimeFrame | varchar |  |  | SI | as given  |
| UpperAge | double |  |  | SI | as given  |
| UpperAgePeriod | varchar |  |  | SI | as given W,M,Y |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*