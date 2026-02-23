# lab.CF_LabtrakGenEntryLayouts

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFLGL_ParRef | bigint | PK |  | NO | CF_LabtrakGenEntry Parent Reference |
| CFLGL_Description | varchar |  |  | SI | Description |
| CFLGL_Field | varchar |  |  | NO | Field |
| CFLGL_Name | varchar |  |  | NO | Layouts Name |
| CFLGL_Position | varchar |  |  | SI | Position |
| CFLGL_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*