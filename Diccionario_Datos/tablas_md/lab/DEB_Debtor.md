# lab.DEB_Debtor

**Schema:** lab
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEB_RowId | varchar | PK |  | NO | - |
| DEB_Alias | varchar |  |  | SI | Alias |
| DEB_BloodGroupEntered_DR | varchar |  | FK | SI | Blood Group Entered DR |
| DEB_BloodGroupOriginal_DR | varchar |  | FK | SI | Blood Group Original DR |
| DEB_BloodGroup_DR | varchar |  | FK | SI | Blood Group DR |
| DEB_DebtorCode | varchar |  |  | NO | Debtor Code |
| DEB_DonorTestsFailed | varchar |  |  | SI | Donor Tests Failed |
| DEB_EXM_Stop | varchar |  |  | SI | EXM Stop |
| DEB_EXM_SuspensionEnd | date |  |  | SI | EXM Suspension End Date |
| DEB_EXM_SuspensionStart | date |  |  | SI | EXM Suspension Start Date |
| DEB_EXM_User_DR | varchar |  | FK | SI | EXM User DR |
| DEB_FamilyDoctor_DR | varchar |  | FK | SI | Family Doctor DR |
| DEB_FatherMRN_DR | varchar |  | FK | SI | Father MRN DR |
| DEB_Genotype_DR | varchar |  | FK | SI | Genotype DR |
| DEB_HistoryAccounts | varchar |  |  | SI | Accounts History |
| DEB_HistoryClinical | varchar |  |  | SI | Clinical History |
| DEB_HistoryEXM | varchar |  |  | SI | EXM History |
| DEB_LegacyMigrationCompleted1 | varchar |  |  | SI | Legacy Migration Completed 1 |
| DEB_LegacyMigrationCompleted2 | varchar |  |  | SI | Legacy Migration Completed 2 |
| DEB_LegacyRecordStatus | varchar |  |  | SI | Legacy Record Status |
| DEB_MotherMRN_DR | varchar |  | FK | SI | Mother MRN DR |
| DEB_OutstandingBalance | double |  |  | SI | Outstanding Balance |
| DEB_PatientWarning_DR | varchar |  | FK | SI | Patient Warning DR |
| DEB_RecentVisit_DR | varchar |  | FK | SI | Des Ref Recent Visit |
| DEB_xxx | varchar |  |  | SI | Partner MRN DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*