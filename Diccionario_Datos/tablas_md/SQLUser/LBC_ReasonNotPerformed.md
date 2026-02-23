# SQLUser.LBC_ReasonNotPerformed

**Schema:** SQLUser
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRNP_RowID | bigint | PK |  | NO | - |
| LBCRNP_AssignToWorksheet | varchar |  |  | SI | Flag to indicate if test set is still to be assign... |
| LBCRNP_Billable | varchar |  |  | SI | Flag to indicate if the test set is still to be in... |
| LBCRNP_Code | varchar |  |  | SI | Code |
| LBCRNP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCRNP_CodeTranslated | varchar |  |  | SI | - |
| LBCRNP_CreatedDate | date |  |  | SI | Created Date |
| LBCRNP_CreatedTime | time |  |  | SI | Created Time |
| LBCRNP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCRNP_DateFrom | date |  |  | NO | Effective date for the record |
| LBCRNP_DateTo | date |  |  | SI | Last day the record is active  |
| LBCRNP_Desc | varchar |  |  | SI | Description |
| LBCRNP_DescTranslated | varchar |  |  | SI | - |
| LBCRNP_OrderStatus_DR | bigint |  | FK | SI | Order Item Status |
| LBCRNP_Owner | varchar |  |  | SI | Owner |
| LBCRNP_PhoneQueue_DR | bigint |  | FK | SI | Put On Phone Queue |
| LBCRNP_RemoveTSComments | varchar |  |  | SI | Remove Test Set Comments |
| LBCRNP_RemoveTSIComments | varchar |  |  | SI | Remove Test Set Item Comments |
| LBCRNP_Reportable | varchar |  |  | SI | Flag to indicate if test set is still reportable |
| LBCRNP_ReportableMessage | varchar |  |  | SI | Report message |
| LBCRNP_SpecialInterestQueue_DR | bigint |  | FK | SI | Put On Special Interest Queue |
| LBCRNP_SuppressDoctorReport | varchar |  |  | SI | Suppress Test Set reporting in Doctor Reports |
| LBCRNP_UpdatedDate | date |  |  | SI | Updated Date |
| LBCRNP_UpdatedTime | time |  |  | SI | Updated Time |
| LBCRNP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q16Q1 | - |  |  | SI | Área de Preparación de la Piel |
| Q16Q2 | - |  |  | SI | Lateralidad |
| Q16Q3 | - |  |  | SI | Plano |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*