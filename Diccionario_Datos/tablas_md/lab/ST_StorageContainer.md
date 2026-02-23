# lab.ST_StorageContainer

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Stock**. Control de existencias.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STC_RowID | varchar | PK |  | NO | - |
| STC_Container_DR | varchar |  | FK | NO | Container DR |
| STC_DateEnd | date |  |  | SI | Date End |
| STC_DateStart | date |  |  | SI | Date Start |
| STC_ExtendedDate | date |  |  | SI | Extended Date |
| STC_NumberOfSpecimens | double |  |  | SI | Number Of Specimens |
| STC_Specimen_DR | varchar |  | FK | SI | Specimen DR |
| STC_StoragePlace_DR | varchar |  | FK | SI | Storage Place DR |
| STC_WorkSheet_DR | varchar |  | FK | SI | Worksheet DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*