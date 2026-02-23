# lab.CT_Specialty

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Catalogo de **Especialidades Medicas**.
Especialidades clinicas disponibles.
Usado en profesionales y servicios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSPL_RowId | varchar | PK |  | NO | - |
| CTSPL_Code | varchar |  |  | NO | Code |
| CTSPL_Desc | varchar |  |  | SI | Description |
| CTSPL_MedicareConing | varchar |  |  | SI | Medicare Coning |
| CTSPL_Type | varchar |  |  | SI | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*