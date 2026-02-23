# TC_hmf_IHE.DocumentSummary

**Schema:** TC_hmf_IHE
**Columnas:** 40
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| IHEDOCSUM_Archived | bit |  |  | SI | - |
| IHEDOCSUM_Facility | varchar |  |  | SI | Des Ref UpdateHospital |
| IHEDOCSUM_HSAvailabilityStatus | varchar |  |  | SI | - |
| IHEDOCSUM_HSClassCode | varchar |  |  | SI | - |
| IHEDOCSUM_HSClassDesc | varchar |  |  | SI | - |
| IHEDOCSUM_HSClassScheme | varchar |  |  | SI | - |
| IHEDOCSUM_HSConfidentialityCode | varchar |  |  | SI | - |
| IHEDOCSUM_HSConfidentialityDesc | varchar |  |  | SI | - |
| IHEDOCSUM_HSConfidentialityScheme | varchar |  |  | SI | - |
| IHEDOCSUM_HSDateCreated | date |  |  | SI | Date Created |
| IHEDOCSUM_HSDocumentSlots | varchar |  |  | SI | - |
| IHEDOCSUM_HSEntryUUID | varchar |  |  | SI | - |
| IHEDOCSUM_HSFormatCode | varchar |  |  | SI | - |
| IHEDOCSUM_HSFormatDesc | varchar |  |  | SI | - |
| IHEDOCSUM_HSFormatScheme | varchar |  |  | SI | - |
| IHEDOCSUM_HSHealthcareFacilityTypeCode | varchar |  |  | SI | - |
| IHEDOCSUM_HSHealthcareFacilityTypeDesc | varchar |  |  | SI | - |
| IHEDOCSUM_HSHealthcareFacilityTypeScheme | varchar |  |  | SI | - |
| IHEDOCSUM_HSMimeType | varchar |  |  | SI | - |
| IHEDOCSUM_HSPatientId | varchar |  |  | SI | - |
| IHEDOCSUM_HSPatientIdSource | varchar |  |  | SI | - |
| IHEDOCSUM_HSPracticeSettingCode | varchar |  |  | SI | - |
| IHEDOCSUM_HSPracticeSettingDesc | varchar |  |  | SI | - |
| IHEDOCSUM_HSPracticeSettingScheme | varchar |  |  | SI | - |
| IHEDOCSUM_HSQueryDocNo | integer |  |  | SI | - |
| IHEDOCSUM_HSQueryResponse | bigint |  |  | SI | - |
| IHEDOCSUM_HSRepositoryUniqueId | varchar |  |  | SI | - |
| IHEDOCSUM_HSSourcePatientId | varchar |  |  | SI | - |
| IHEDOCSUM_HSTimeCreated | time |  |  | SI | Time Created |
| IHEDOCSUM_HSTitle | varchar |  |  | SI | - |
| IHEDOCSUM_HSTypeCode | varchar |  |  | SI | - |
| IHEDOCSUM_HSTypeDesc | varchar |  |  | SI | - |
| IHEDOCSUM_HSTypeScheme | varchar |  |  | SI | - |
| IHEDOCSUM_HSUniqueId | varchar |  |  | SI | - |
| IHEDOCSUM_HSUserCreated | varchar |  |  | SI | User Created |
| IHEDOCSUM_HSVersion | varchar |  |  | SI | - |
| IHEDOCSUM_PAAdm_DR | bigint |  | FK | SI | Des Ref Episode |
| IHEDOCSUM_PAPerson_DR | bigint |  | FK | SI | Des Ref Patient |
| IHEDOCSUM_Session | varchar |  |  | SI | Description |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*