# websys.CTEntryMap

> "Reference Map

**Schema:** websys
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Reference Map

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ClassName | varchar |  |  | NO | - |
| DataSourceDR | bigint |  | FK | NO | - |
| DateFrom | date |  |  | NO | Date From |
| DateTo | date |  |  | SI | Date To |
| MAP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MAP_Owner | varchar |  |  | SI | Owner |
| VendorProduct | varchar |  |  | SI | can be used to name the Product additionally to CT... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*