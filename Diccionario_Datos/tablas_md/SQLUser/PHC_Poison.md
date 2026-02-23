# SQLUser.PHC_Poison

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCPO_RowId | bigint | PK |  | NO | - |
| PHCPO_Approval | varchar |  |  | SI | Approval Details Required Flag |
| PHCPO_Code | varchar |  |  | NO | Drug Poison Code |
| PHCPO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCPO_CreatedDate | date |  |  | SI | Created Date |
| PHCPO_CreatedTime | time |  |  | SI | Created Time |
| PHCPO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCPO_Desc | varchar |  |  | NO | Description |
| PHCPO_MHRpt | varchar |  |  | NO | Report for Ministry of Health Flag |
| PHCPO_OTCFlag | varchar |  |  | NO | Allow purchase through OTC |
| PHCPO_Owner | varchar |  |  | SI | Owner |
| PHCPO_SaleRpt | varchar |  |  | NO | Daily Sale Record Flag |
| PHCPO_UpdatedDate | date |  |  | SI | Updated Date |
| PHCPO_UpdatedTime | time |  |  | SI | Updated Time |
| PHCPO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*