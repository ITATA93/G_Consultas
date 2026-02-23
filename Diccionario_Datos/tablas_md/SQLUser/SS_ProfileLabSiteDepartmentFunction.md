# SQLUser.SS_ProfileLabSiteDepartmentFunction

**Schema:** SQLUser
**Columnas:** 39
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSPLBSD_ParRef | bigint | PK |  | NO | Parent table |
| SSPLBSD_AllowAdditionalBloodGroupOverride | varchar |  |  | SI | Allow to Override Additional Blood Group / Antibod... |
| SSPLBSD_AllowAuthoriseTestSetWorkGroups | varchar |  |  | SI | Allow to authorise test set in workgroups |
| SSPLBSD_AllowBPEntryAtUnitAlloc | varchar |  |  | SI | Allow book in of blood product stock at stock allo... |
| SSPLBSD_AllowChangeBilling | varchar |  |  | SI | Allow to Change Billing Flag |
| SSPLBSD_AllowCrossmatchOnProvGrp | varchar |  |  | SI | Allow authorisation of crossmatch on provisional g... |
| SSPLBSD_AllowEditBloodProductDetails | varchar |  |  | SI | Allow Edit of Blood Product Details |
| SSPLBSD_AllowEmergencyIssue | varchar |  |  | SI | Allow Emergency Issue of Blood  |
| SSPLBSD_AllowInstantReprint | varchar |  |  | SI | Allow Instant Reprint  |
| SSPLBSD_AllowIssueExpiringBP | varchar |  |  | SI | Allow Issue Expiring Blood Products |
| SSPLBSD_AllowIssueOnPosABScreen | varchar |  |  | SI | Allow issue on positive antibody screen  |
| SSPLBSD_AllowManualBloodGroupEntry | varchar |  |  | SI | Allow Manual Blood Group Entry |
| SSPLBSD_AllowMarkNotPerformed | varchar |  |  | SI | Allow Mark Test Set or Test Item as Not Performed ... |
| SSPLBSD_AllowModifySpecimenSuitabilityPeriod | varchar |  |  | SI | Allow Modify Specimen Suitability Period |
| SSPLBSD_AllowPatientBloodGroupOverride | varchar |  |  | SI | Allow to Override Patient Blood Group |
| SSPLBSD_AllowPrintNonAuthorisedLabels | varchar |  |  | SI | Allow Print of Non-Authorised Product Labels |
| SSPLBSD_AllowQCPromoteEvalToCurrent | varchar |  |  | SI | Allowed to promote Evaluation QC to Current |
| SSPLBSD_AllowQCUpdateBatchCloseDate | varchar |  |  | SI | Allowed to update QC Batch Close Date |
| SSPLBSD_AllowQCValuesOverride | varchar |  |  | SI | Allowed to Override QC Values |
| SSPLBSD_AllowRemoveFromExternalInterfaceQueue | varchar |  |  | SI | Allow to Remove from On External Interface Queues  |
| SSPLBSD_AllowRemoveFromHoldQueue | varchar |  |  | SI | Allow to Remove from On Hold Queues  |
| SSPLBSD_AllowRemoveFromOutbreakQueue | varchar |  |  | SI | Allow to Remove from Outbreak Queues  |
| SSPLBSD_AllowRemoveFromSpecialInterestQueue | varchar |  |  | SI | Allow to remove from Special Interest Queues  |
| SSPLBSD_AllowReportPreview | varchar |  |  | SI | Allow to preview report |
| SSPLBSD_AllowTestSetAuthorise | varchar |  |  | SI | Allow to authorise test sets |
| SSPLBSD_AllowTestSetAuthoriseExpiredValidity | varchar |  |  | SI | Allow to authorise test sets with expired validity |
| SSPLBSD_AllowTestSetDeAuthorise | varchar |  |  | SI | Allow to de-authorise test sets |
| SSPLBSD_AllowTestSetValidate | varchar |  |  | SI | Allow to validate test sets |
| SSPLBSD_AllowTestSetValidateExpiredValidity | varchar |  |  | SI | Allow to validate test sets with expired validity |
| SSPLBSD_AllowValidateTestSetWorkGroups | varchar |  |  | SI | Allow to validate test set in workgroups |
| SSPLBSD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSPLBSD_DateFrom | date |  |  | SI | Date From |
| SSPLBSD_DateTo | date |  |  | SI | Date To |
| SSPLBSD_ForceBGVerification | varchar |  |  | SI | Force Blood-Group Interpretation Verification |
| SSPLBSD_LabDepartment_DR | bigint |  | FK | SI | Lab Department |
| SSPLBSD_LabSite_DR | bigint |  | FK | SI | Lab Site |
| SSPLBSD_RowID | varchar |  |  | NO | - |
| SSPLBSD_Sequence | numeric |  |  | SI | Priority  Sequence |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*