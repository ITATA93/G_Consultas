# lab.CT_DepartmentPatientEntry

**Schema:** lab
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDPE_ParRef | varchar | PK |  | NO | CT_Department Parent Reference |
| CTDPE_Description | varchar |  |  | SI | Description |
| CTDPE_Field | varchar |  |  | SI | Field |
| CTDPE_Length | varchar |  |  | SI | Length |
| CTDPE_MenuPosition | varchar |  |  | SI | Menu Position |
| CTDPE_Module | varchar |  |  | NO | Module |
| CTDPE_Position | varchar |  |  | SI | Position |
| CTDPE_RowID | varchar |  |  | NO | - |
| CTDPE_Sequence | double |  |  | NO | Sequence |
| CTDPE_TabName | varchar |  |  | SI | Tab Name |
| CTDPE_Type | varchar |  |  | SI | Type |
| CTDPE_WindowFormula | varchar |  |  | SI | Window Formula |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*