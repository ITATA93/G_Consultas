# SQLUser.RB_ResEffDateSessOTSpec

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OTSPEC_ParRef | varchar | PK |  | NO | RB_ResEffDateSession Parent Reference |
| OTSPEC_AddedDate | date |  |  | SI | Added Date |
| OTSPEC_AddedTime | time |  |  | SI | Added Time |
| OTSPEC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLoc |
| OTSPEC_Childsub | double |  |  | NO | Childsub |
| OTSPEC_DateFrom | date |  |  | SI | Date From |
| OTSPEC_DateTo | date |  |  | SI | Date To |
| OTSPEC_LastUpdateDate | date |  |  | SI | Last Update Date |
| OTSPEC_LastUpdateTime | time |  |  | SI | Last Update Time |
| OTSPEC_LastUpdateUser_DR | bigint |  | FK | SI | Last Update User |
| OTSPEC_Main | varchar |  |  | SI | Main/Preferable |
| OTSPEC_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*