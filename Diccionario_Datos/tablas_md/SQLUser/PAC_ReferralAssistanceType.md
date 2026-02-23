# SQLUser.PAC_ReferralAssistanceType

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFASTP_RowId | bigint | PK |  | NO | - |
| ChildQ29DR | - |  |  | SI | Child Reference: Mobility |
| Q23Q1 | - |  |  | SI | Nails / Hands assessment for |
| Q23Q2 | - |  |  | SI | Clean |
| Q23Q3 | - |  |  | SI | Infections |
| Q23Q4 | - |  |  | SI | Fungal |
| Q23Q5 | - |  |  | SI | Trimming needed |
| Q23Q6 | - |  |  | SI | Current lesions, carbuncles and/or cysts |
| Q23Q7 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFASTP_Code | varchar |  |  | NO | Code |
| REFASTP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFASTP_CreatedDate | date |  |  | SI | Created Date |
| REFASTP_CreatedTime | time |  |  | SI | Created Time |
| REFASTP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFASTP_DateFrom | date |  |  | SI | Date From |
| REFASTP_DateTo | date |  |  | SI | Date To |
| REFASTP_Desc | varchar |  |  | NO | Description |
| REFASTP_NationalCode | varchar |  |  | SI | National Code |
| REFASTP_Owner | varchar |  |  | SI | Owner |
| REFASTP_Subregion_DR | bigint |  | FK | SI | Subregion |
| REFASTP_UpdatedDate | date |  |  | SI | Updated Date |
| REFASTP_UpdatedTime | time |  |  | SI | Updated Time |
| REFASTP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*