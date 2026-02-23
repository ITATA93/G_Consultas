# lab.CF_CustomParameter

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFPARAM_ParRef | bigint | PK |  | NO | - |
| CFPARAM_Name | varchar |  |  | NO | Name of this parameter (unique) |
| CFPARAM_RowID | varchar |  |  | NO | - |
| CFPARAM_Value | varchar |  |  | SI | Value of this parameter |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*