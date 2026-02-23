# SQLUser.RB_ApptScheduleSpec

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPEC_ParRef | varchar | PK |  | NO | RB_ApptSchedule Parent Reference |
| SPEC_AddedDate | date |  |  | SI | Added Date |
| SPEC_AddedTime | time |  |  | SI | Added Time |
| SPEC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLoc |
| SPEC_ChildSub | double |  |  | NO | Child sub |
| SPEC_LastUpdateDate | date |  |  | SI | Last Update Date |
| SPEC_LastUpdateTime | time |  |  | SI | Last Update Time |
| SPEC_LastUpdateUser | bigint |  |  | SI | Last Update User Des Ref |
| SPEC_Main | varchar |  |  | SI | Main/Preferable |
| SPEC_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*