# SQLUser.RB_ApptCP

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CP_ParRef | varchar | PK |  | NO | RB_Appointment Parent Reference |
| CP_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| CP_Childsub | double |  |  | NO | Childsub |
| CP_DateComp | date |  |  | SI | Date Computed |
| CP_RowId | varchar |  |  | NO | - |
| CP_SeenBy | varchar |  |  | SI | Seen by |
| CP_Specialty_DR | bigint |  | FK | SI | Des Ref CTLoc |
| CP_TeamLeader | varchar |  |  | SI | TeamLeader |
| CP_TimeComp | time |  |  | SI | Time Computed |
| CP_TimeFrom | time |  |  | SI | TimeFrom |
| CP_TimeTo | time |  |  | SI | TimeTo |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*