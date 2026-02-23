# SQLUser.LBC_StorageGroup

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSG_RowID | bigint | PK |  | NO | - |
| ChildQ08DR | - |  |  | SI | Child Reference: Control Horario de Contención Fis... |
| LBCSG_Code | varchar |  |  | NO | Code |
| LBCSG_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCSG_CreatedDate | date |  |  | SI | Created Date |
| LBCSG_CreatedTime | time |  |  | SI | Created Time |
| LBCSG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCSG_DateTo | date |  |  | SI | Last day the record is active |
| LBCSG_Desc | varchar |  |  | NO | Description |
| LBCSG_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCSG_Owner | varchar |  |  | SI | Owner |
| LBCSG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q14Q1 | - |  |  | SI | Fármaco |
| Q14Q2 | - |  |  | SI | Dosis |
| Q14Q3 | - |  |  | SI | Vía |
| Q14Q4 | - |  |  | SI | Hora |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*