# epr.CTDischargeSummaryType

**Schema:** epr
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DSTAbnormalResults | varchar |  |  | SI | AbnormalResults |
| DSTAlerts | varchar |  |  | SI | Alerts |
| DSTAllResults | varchar |  |  | SI | AllResults |
| DSTAllergies | varchar |  |  | SI | Allergies |
| DSTCode | varchar |  |  | NO | Code |
| DSTCodeTableTags | varchar |  |  | SI | - |
| DSTCounterTypeDR | bigint |  | FK | SI | DAH - 67960 - User Defined Counter |
| DSTDateFrom | date |  |  | SI | Date From |
| DSTDateTo | date |  |  | SI | Date To |
| DSTDesc | varchar |  |  | SI | Description |
| DSTDiagnosis | varchar |  |  | SI | Diagnosis |
| DSTDischargeMedicationOrders | varchar |  |  | SI | DischargeMedicationOrders |
| DSTDocumentType | varchar |  |  | SI | Document Type |
| DSTEPRChartBookDR | bigint |  | FK | SI | Chart book to use for this Discharge Summary Type |
| DSTEmailBody | varchar |  |  | SI | Email Body value |
| DSTEmailBodyExpression | varchar |  |  | SI | DAH - 69651 - Email Body Expression |
| DSTEmailSubjectHeading | varchar |  |  | SI | Email Subject Heading |
| DSTEpisodeType | varchar |  |  | SI | EpisodeType |
| DSTEpissubtypeDR | bigint |  | FK | SI | - |
| DSTExcludeDoctor | varchar |  |  | SI | Doctors To Exclude |
| DSTIHEDocTypeDR | bigint |  | FK | SI | - |
| DSTMultipleVersions | varchar |  |  | SI | Multiple Versions |
| DSTOperation | varchar |  |  | SI | Operation |
| DSTProcedure | varchar |  |  | SI | Procedure |
| DSTReferralDischargeSummary | varchar |  |  | SI | Referral Discharge Summary |
| DSTReportDR | bigint |  | FK | NO | websys.Report DR |
| DSTSignificantOrders | varchar |  |  | SI | SignificantOrders |
| DSTSignificantResults | varchar |  |  | SI | SignificantResults |
| DST_Owner | varchar |  |  | SI | - |
| NotUsedDSTDocumentName | varchar |  |  | SI | Document Name |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*