# SQLUser.RTC_DefCodingMRMove

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DCMM_RowId | bigint | PK |  | NO | - |
| DCMM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DCMM_Comments | varchar |  |  | SI | Comments |
| DCMM_ContactPerson | varchar |  |  | SI | Contact Person |
| DCMM_CreatedDate | date |  |  | SI | Created Date |
| DCMM_CreatedTime | time |  |  | SI | Created Time |
| DCMM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DCMM_DateFrom | date |  |  | SI | Date From |
| DCMM_DateTo | date |  |  | SI | Date To |
| DCMM_DestinationLoc_DR | bigint |  | FK | SI | Des Ref DestinationLoc |
| DCMM_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| DCMM_MRType_DR | bigint |  | FK | SI | Des Ref MRType |
| DCMM_Owner | varchar |  |  | SI | Owner |
| DCMM_Pager | varchar |  |  | SI | Pager |
| DCMM_ReqReason_DR | bigint |  | FK | SI | Des Ref ReqReason |
| DCMM_Telephone | varchar |  |  | SI | Telephone |
| DCMM_UpdatedDate | date |  |  | SI | Updated Date |
| DCMM_UpdatedTime | time |  |  | SI | Updated Time |
| DCMM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DCMM_Volume | varchar |  |  | SI | Volume |
| DCMM_VolumesToMove | varchar |  |  | SI | Volumes To Move |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*