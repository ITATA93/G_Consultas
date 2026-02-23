# SQLUser.SS_ProfileClinicalTimeLine

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSPCTL_ParRef | bigint | PK |  | NO | Parent table |
| SSPCTL_ClinicalTimeLine_DR | bigint |  | FK | SI | Clinical Timeline |
| SSPCTL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSPCTL_CreatedDate | date |  |  | SI | Created Date |
| SSPCTL_CreatedTime | time |  |  | SI | Created Time |
| SSPCTL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SSPCTL_DateFrom | date |  |  | SI | Date From |
| SSPCTL_DateTo | date |  |  | SI | Date To |
| SSPCTL_IsDefaultTimeline | bit |  |  | SI | Flag to indicate the default timeline of this acce... |
| SSPCTL_RowID | varchar |  |  | NO | - |
| SSPCTL_UpdatedDate | date |  |  | SI | Updated Date |
| SSPCTL_UpdatedTime | time |  |  | SI | Updated Time |
| SSPCTL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*