# SQLUser.PHC_PBSSeverity

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSSEV_RowId | bigint | PK |  | NO | - |
| PBSSEV_Code | varchar |  |  | NO | Code |
| PBSSEV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSSEV_CreatedDate | date |  |  | SI | Created Date |
| PBSSEV_CreatedTime | time |  |  | SI | Created Time |
| PBSSEV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSSEV_DateFrom | date |  |  | SI | Date From |
| PBSSEV_DateTo | date |  |  | SI | Date To |
| PBSSEV_Desc | varchar |  |  | NO | Description |
| PBSSEV_Owner | varchar |  |  | SI | Owner |
| PBSSEV_UpdatedDate | date |  |  | SI | Updated Date |
| PBSSEV_UpdatedTime | time |  |  | SI | Updated Time |
| PBSSEV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*