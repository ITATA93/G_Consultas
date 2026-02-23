# lab.CT_BillLocationPatholog

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBLP_ParRef | varchar | PK |  | NO | CT_BillLocation Parent Reference |
| CTBLP_Date | date |  |  | NO | Date |
| CTBLP_Pathologist_DR | varchar |  | FK | SI | Pathologist_DR |
| CTBLP_ProviderNumber | varchar |  |  | SI | Provider Number |
| CTBLP_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*