# SQLUser.RB_ResEffDateSessionCP

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CP_ParRef | varchar | PK |  | NO | RB_ResEffDateSession Parent Reference |
| CP_AddedDate | date |  |  | SI | Added Date |
| CP_AddedTime | time |  |  | SI | Added Time |
| CP_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| CP_CareProviderType | varchar |  |  | SI | CareProviderType |
| CP_Childsub | double |  |  | NO | Childsub |
| CP_DateFrom | date |  |  | SI | Date From |
| CP_DateTo | date |  |  | SI | Date To |
| CP_LastUpdateDate | date |  |  | SI | Last Update Date |
| CP_LastUpdateTime | time |  |  | SI | Last Update Time |
| CP_LastUpdateUser_DR | bigint |  | FK | SI | Last Update User |
| CP_MultiDispTeam | varchar |  |  | SI | MultiDispTeam |
| CP_MultiDispTeam_DR | bigint |  | FK | SI | Des Ref MultiDispTeam |
| CP_RowId | varchar |  |  | NO | - |
| CP_SecondSurg | varchar |  |  | SI | Second Surgeon |
| CP_SessionDate | date |  |  | SI | SessionDate |
| CP_Specialty_DR | bigint |  | FK | SI | Des Ref CTLoc |
| CP_TeamLeader | varchar |  |  | SI | TeamLeader |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*