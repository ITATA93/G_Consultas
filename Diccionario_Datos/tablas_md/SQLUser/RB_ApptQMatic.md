# SQLUser.RB_ApptQMatic

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QM_ParRef | varchar | PK |  | NO | RB_Appointment Parent Reference |
| QM_Childsub | double |  |  | NO | Childsub |
| QM_CreateDate | date |  |  | SI | CreateDate |
| QM_CreateTime | time |  |  | SI | CreateTime |
| QM_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| QM_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| QM_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| QM_Number | varchar |  |  | SI | Number |
| QM_RowId | varchar |  |  | NO | - |
| QM_Status | varchar |  |  | SI | Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*