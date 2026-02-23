# SQLUser.RB_StaffRosterEntry

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ENT_ParRef | bigint | PK |  | NO | RB_StaffRoster Parent Reference |
| ENT_CareProvider_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| ENT_Childsub | double |  |  | NO | Childsub |
| ENT_Date | date |  |  | SI | Date |
| ENT_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| ENT_RowId | varchar |  |  | NO | - |
| ENT_Schedule_DR | varchar |  | FK | SI | Des Ref RBResEffDateSession |
| ENT_ShiftLoad | double |  |  | SI | ShiftLoad |
| ENT_ShiftLoadDirty | varchar |  |  | SI | ShiftLoadDirty |
| ENT_Shift_DR | bigint |  | FK | SI | Des Ref CTShift |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*