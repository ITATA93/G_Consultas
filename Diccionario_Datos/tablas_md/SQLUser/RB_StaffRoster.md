# SQLUser.RB_StaffRoster

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STAFFR_RowId | bigint | PK |  | NO | - |
| STAFFR_Code | varchar |  |  | SI | Code |
| STAFFR_DateFrom | date |  |  | SI | Date From |
| STAFFR_DateTo | date |  |  | SI | Date To |
| STAFFR_Desc | varchar |  |  | SI | Description |
| STAFFR_DisplayDate | date |  |  | SI | DisplayDate |
| STAFFR_DisplayLocations_DR | bigint |  | FK | SI | Des Ref CTLocationList |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*