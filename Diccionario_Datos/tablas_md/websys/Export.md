# websys.Export

> Data Export Framer

**Schema:** websys
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Data Export Framer

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Code | varchar |  |  | NO | - |
| CrossCheckCode | varchar |  |  | SI | cache call to return string containing value of cr... |
| DateFrom | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| ExclusionCode | varchar |  |  | SI | cache call to decide if this RowID is to be includ... |
| ExtractStatus | varchar |  |  | SI | - |
| GenerateDate | date |  |  | SI | - |
| GenerateStatus | varchar |  |  | SI | - |
| GenerateTime | time |  |  | SI | - |
| IsParent | varchar |  |  | NO | - |
| KillOnExtract | bit |  |  | SI | - |
| MasterClass | varchar |  |  | NO | - |
| OnlyRunOnTheFly | bit |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| ReportType | bigint |  |  | SI | - |
| UpdateDate | date |  |  | SI | - |
| UpdateTime | time |  |  | SI | - |
| UseWindowsEOL | bit |  |  | SI | Indicates if EOL is UNIX type (Line Feed 0x10), ot... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*