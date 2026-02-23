# Tools_Upload_OrderSet.XMLFiles

**Schema:** Tools_Upload_OrderSet
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CreatedDate | date |  |  | SI | Date this record was created |
| CreatedTime | time |  |  | SI | Time this record was created |
| HideDate | timestamp |  |  | SI | Hide without process |
| PathName | varchar |  |  | SI | Path Source name of xml file |
| ProcessedDate | timestamp |  |  | SI | Hide because processed |
| SourceFileName | varchar |  |  | SI | Source file name of xml file |
| VendorName | varchar |  |  | SI | Vendor name of xml file |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*