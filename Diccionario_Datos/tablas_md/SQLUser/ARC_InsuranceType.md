# SQLUser.ARC_InsuranceType

**Schema:** SQLUser
**Columnas:** 45
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INST_RowId | bigint | PK |  | NO | - |
| ChildQ82DR | - |  |  | SI | Child Reference: Sexualidad |
| INST_AccommodationType | varchar |  |  | SI | Accommodation Type |
| INST_AccountClass | bigint |  |  | SI | Account Class |
| INST_BillingLogic | varchar |  |  | SI | BillingLogic |
| INST_CareType | varchar |  |  | SI | Care Type |
| INST_Category | varchar |  |  | SI | Category |
| INST_Code | varchar |  |  | NO | Code |
| INST_Code1 | varchar |  |  | SI | Code1 |
| INST_Code2 | varchar |  |  | SI | Code2 |
| INST_Code3 | varchar |  |  | SI | Code3 |
| INST_Code4 | varchar |  |  | SI | Code4 |
| INST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INST_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| INST_CompanyAddress | varchar |  |  | SI | Company Address |
| INST_CreatedDate | date |  |  | SI | Created Date |
| INST_CreatedTime | time |  |  | SI | Created Time |
| INST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INST_DRGGrouperVersion_DR | bigint |  | FK | SI | Des Ref DRGGrouperVersion |
| INST_DateFrom | date |  |  | SI | Date From |
| INST_DateTo | date |  |  | SI | Date To |
| INST_DefaultAuxInsType_DR | bigint |  | FK | SI | Des Ref Default AuxInsType |
| INST_Desc | varchar |  |  | NO | Description |
| INST_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| INST_DoNotDefaultCopy | varchar |  |  | SI | DoNot Default/Copy |
| INST_InsBatchOnly | varchar |  |  | SI | Ins. Batch Only |
| INST_LinkInsType_DR | bigint |  | FK | SI | Des Ref InsType |
| INST_MultiPart | varchar |  |  | SI | MultiPart |
| INST_Owner | varchar |  |  | SI | Owner |
| INST_PayMode_DR | bigint |  | FK | SI | Des Ref PayMode |
| INST_PayorApprovalICDDiag_DR | bigint |  | FK | SI | Des Ref ARCPayorApprovalDiag |
| INST_PayorGroup_DR | bigint |  | FK | SI | Des Ref PayorGroup |
| INST_Priority_DR | bigint |  | FK | SI | Des Ref Priority |
| INST_ProgramFundingSource | varchar |  |  | SI | Program Funding Source |
| INST_ReportOnsetCode | varchar |  |  | SI | Report Onset Code |
| INST_ReportPrivateRoomAddOn | varchar |  |  | SI | Report Private Room AddOn Separately |
| INST_SplitBillsByLoc | varchar |  |  | SI | Split Bills By Location |
| INST_UnqualifiedAdm | varchar |  |  | SI | Unqualified Admission |
| INST_UpdatedDate | date |  |  | SI | Updated Date |
| INST_UpdatedTime | time |  |  | SI | Updated Time |
| INST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q81Q1 | - |  |  | SI | Área |
| Q81Q2 | - |  |  | SI | Evaluación |
| Q81Q3 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*