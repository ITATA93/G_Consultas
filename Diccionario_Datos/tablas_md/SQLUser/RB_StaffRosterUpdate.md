# SQLUser.RB_StaffRosterUpdate

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| UPD_ParRef | bigint | PK |  | NO | RB_StaffRoster Parent Reference |
| UPD_Childsub | double |  |  | NO | Childsub |
| UPD_Date | date |  |  | SI | Date |
| UPD_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| UPD_Month | double |  |  | SI | Month |
| UPD_RowId | varchar |  |  | NO | - |
| UPD_Time | time |  |  | SI | Time |
| UPD_User_DR | bigint |  | FK | SI | Des Ref SSUser |
| UPD_Year | double |  |  | SI | Year |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*