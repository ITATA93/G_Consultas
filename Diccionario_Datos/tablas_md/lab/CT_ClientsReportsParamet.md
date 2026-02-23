# lab.CT_ClientsReportsParamet

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCLD_ParRef | varchar | PK |  | NO | CT_ClientsReports Parent Reference |
| CTCLD_Childsub | double |  |  | NO | Childsub |
| CTCLD_Destination_DR | varchar |  | FK | SI | Des Ref to Destination |
| CTCLD_NumberOfCopies | double |  |  | SI | Number Of Copies |
| CTCLD_Parameter | varchar |  |  | SI | Parameter |
| CTCLD_RowId | varchar |  |  | NO | - |
| CTCLD_Site_DR | varchar |  | FK | SI | Site |
| CTCLD_Suspend | varchar |  |  | SI | Suspend |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*