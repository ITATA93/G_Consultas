# lab.CTBB_StockLevel

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBSL_RowID | varchar | PK |  | NO | - |
| BBSL_BBBloodGroup_DR | varchar |  | FK | SI | Blood Group DR |
| BBSL_BBLocation_DR | varchar |  | FK | SI | BB Location DR |
| BBSL_BBProductGroup_DR | varchar |  | FK | SI | BB Product Group DR |
| BBSL_BBProduct_DR | varchar |  | FK | SI | BB Product DR |
| BBSL_MaxValue | double |  |  | SI | Max Value |
| BBSL_MinValue | double |  |  | SI | Min Value |
| BBSL_Sequence | varchar |  |  | NO | Sequence |
| BBSL_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*