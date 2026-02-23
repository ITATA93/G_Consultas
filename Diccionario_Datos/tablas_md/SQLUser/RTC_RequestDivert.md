# SQLUser.RTC_RequestDivert

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REQDIV_RowId | bigint | PK |  | NO | - |
| REQDIV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REQDIV_CreatedDate | date |  |  | SI | Created Date |
| REQDIV_CreatedTime | time |  |  | SI | Created Time |
| REQDIV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REQDIV_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| REQDIV_MRLocation_DR | bigint |  | FK | SI | Des Ref CTLOC |
| REQDIV_Owner | varchar |  |  | SI | Owner |
| REQDIV_RecordType_DR | bigint |  | FK | SI | Des Ref RecordType |
| REQDIV_ReqReason_DR | bigint |  | FK | SI | Des Ref ReqReason |
| REQDIV_ShowHome | varchar |  |  | SI | Show Home |
| REQDIV_SignFacDR | bigint |  | FK | SI | CT Significant Facility DR |
| REQDIV_UpdatedDate | date |  |  | SI | Updated Date |
| REQDIV_UpdatedTime | time |  |  | SI | Updated Time |
| REQDIV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*