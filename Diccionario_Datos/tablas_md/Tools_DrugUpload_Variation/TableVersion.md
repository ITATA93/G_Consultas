# Tools_DrugUpload_Variation.TableVersion

**Schema:** Tools_DrugUpload_Variation
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| SchemaDateFrom | date |  |  | SI | Date From |
| SchemaDateTo | date |  |  | SI | Date To |
| SchemaVersion | integer |  |  | NO | SchemaVersion (per specification this can be posit... |
| TableName | varchar |  |  | NO | Property that declares which Download this Table v... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*