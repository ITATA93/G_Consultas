# lab.CF_LabtrakGenEntry

**Schema:** lab
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFLGE_ParRef | bigint | PK |  | NO | CF_LabTrak Parent Reference |
| CFLGE_Description | varchar |  |  | SI | Description |
| CFLGE_Field | varchar |  |  | SI | Field |
| CFLGE_Length | varchar |  |  | SI | Length |
| CFLGE_MenuPosition | varchar |  |  | SI | Menu Position |
| CFLGE_Module | varchar |  |  | NO | Module |
| CFLGE_Position | varchar |  |  | SI | Position |
| CFLGE_RowID | varchar |  |  | NO | - |
| CFLGE_Sequence | double |  |  | NO | Sequence |
| CFLGE_TabName | varchar |  |  | SI | Tab Name |
| CFLGE_Type | varchar |  |  | SI | Type |
| CFLGE_WindowFormula | varchar |  |  | SI | Window Formula |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*