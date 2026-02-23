# SQLUser.RBC_TransferApptReason

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APTRAN_RowId | bigint | PK |  | NO | - |
| APTRAN_Code | varchar |  |  | NO | Code |
| APTRAN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APTRAN_CreatedDate | date |  |  | SI | Created Date |
| APTRAN_CreatedTime | time |  |  | SI | Created Time |
| APTRAN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APTRAN_DateFrom | date |  |  | SI | Date From |
| APTRAN_DateTo | date |  |  | SI | Date To |
| APTRAN_Default | bit |  |  | SI | Default |
| APTRAN_Desc | varchar |  |  | NO | Description |
| APTRAN_Initiator | varchar |  |  | SI | Initiator |
| APTRAN_NationalCode | varchar |  |  | SI | National Code |
| APTRAN_Owner | varchar |  |  | SI | Owner |
| APTRAN_ResetTTGClock | varchar |  |  | SI | Reset TTG Clock |
| APTRAN_UpdatedDate | date |  |  | SI | Updated Date |
| APTRAN_UpdatedTime | time |  |  | SI | Updated Time |
| APTRAN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*