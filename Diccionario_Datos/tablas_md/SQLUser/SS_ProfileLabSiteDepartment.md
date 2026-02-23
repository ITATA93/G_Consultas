# SQLUser.SS_ProfileLabSiteDepartment

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSPLSD_ParRef | bigint | PK |  | NO | Parent table |
| SSPLSD_AllowAccessConfidentialEpisode | varchar |  |  | SI | Can see Confidential Episodes |
| SSPLSD_AllowAccessConfidentialResult | varchar |  |  | SI | Can see Confidential Results |
| SSPLSD_AllowAccessConfidentialTestSet | varchar |  |  | SI | Can see Confidential Test Sets |
| SSPLSD_AllowAccessStaffNote | varchar |  |  | SI | Can Access Staff Notes |
| SSPLSD_AllowEditEpisode | varchar |  |  | SI | Allow to Edit Episode |
| SSPLSD_AllowEditTestSet | varchar |  |  | SI | Allow to Edit Test Set |
| SSPLSD_AllowEnquireNonFinalResult | varchar |  |  | SI | Enquire on non-final results  |
| SSPLSD_AllowUpdateStaffNote | varchar |  |  | SI | Can Update Staff Notes  |
| SSPLSD_AllowViewEpisode | varchar |  |  | SI | Allow to View Episode |
| SSPLSD_AllowViewNonFinalTransferred | varchar |  |  | SI | Allow to View Non-Final Transferred Test Sets / Re... |
| SSPLSD_AllowViewTestItemHistory | varchar |  |  | SI | Allow to View Cumulative Results and Test Item His... |
| SSPLSD_AllowViewTestSet | varchar |  |  | SI | Allow to View Test Set |
| SSPLSD_AllowViewTransferred | varchar |  |  | SI | Allow to View Transferred Test Sets / Results / Pr... |
| SSPLSD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSPLSD_DateFrom | date |  |  | SI | Date From |
| SSPLSD_DateTo | date |  |  | SI | Date To |
| SSPLSD_LabDepartment_DR | bigint |  | FK | SI | Lab Department  |
| SSPLSD_LabSite_DR | bigint |  | FK | SI | LabSite |
| SSPLSD_RowID | varchar |  |  | NO | - |
| SSPLSD_Sequence | numeric |  |  | SI | Priority  Sequence |
| SSPLSD_SubjectType_DR | bigint |  | FK | SI | Lab Subject Type |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*