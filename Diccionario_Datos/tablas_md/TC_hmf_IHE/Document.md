# TC_hmf_IHE.Document

**Schema:** TC_hmf_IHE
**Columnas:** 42
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| IHEDOC_Desc | varchar |  |  | SI | Description |
| IHEDOC_DocType_DR | bigint |  | FK | SI | des ref to PAC_DocumentType |
| IHEDOC_HSAuthor | varchar |  |  | SI | - |
| IHEDOC_HSAvailabilityStatus | varchar |  |  | SI | - |
| IHEDOC_HSClassCode | varchar |  |  | SI | - |
| IHEDOC_HSComments | varchar |  |  | SI | - |
| IHEDOC_HSConfidentialityCode | varchar |  |  | SI | - |
| IHEDOC_HSDateCreated | date |  |  | SI | Date Created |
| IHEDOC_HSDocumentSlots | varchar |  |  | SI | - |
| IHEDOC_HSEntryUUID | varchar |  |  | SI | - |
| IHEDOC_HSFormatCode | varchar |  |  | SI | - |
| IHEDOC_HSFormatScheme | varchar |  |  | SI | - |
| IHEDOC_HSHealthcareFacilityTypeCode | varchar |  |  | SI | - |
| IHEDOC_HSHomeCommunityId | varchar |  |  | SI | - |
| IHEDOC_HSLanguageCode | varchar |  |  | SI | - |
| IHEDOC_HSLegalAuthenticator | varchar |  |  | SI | - |
| IHEDOC_HSLogicalUUID | varchar |  |  | SI | - |
| IHEDOC_HSMimeType | varchar |  |  | SI | - |
| IHEDOC_HSObjectType | varchar |  |  | SI | - |
| IHEDOC_HSPatientId | varchar |  |  | SI | - |
| IHEDOC_HSPatientIdSource | varchar |  |  | SI | - |
| IHEDOC_HSPracticeSettingCode | varchar |  |  | SI | - |
| IHEDOC_HSRepositoryUniqueId | varchar |  |  | SI | - |
| IHEDOC_HSSourcePatientId | varchar |  |  | SI | - |
| IHEDOC_HSTimeCreated | time |  |  | SI | Time Created |
| IHEDOC_HSTitle | varchar |  |  | SI | - |
| IHEDOC_HSTypeCode | varchar |  |  | SI | - |
| IHEDOC_HSTypeDesc | varchar |  |  | SI | - |
| IHEDOC_HSTypeScheme | varchar |  |  | SI | - |
| IHEDOC_HSURI | varchar |  |  | SI | - |
| IHEDOC_HSUniqueId | varchar |  |  | SI | - |
| IHEDOC_HSUserCreated | varchar |  |  | SI | UpdateUser  |
| IHEDOC_HSVersion | varchar |  |  | SI | - |
| IHEDOC_Inactive | varchar |  |  | SI | Inactive |
| IHEDOC_PAAdm_DR | bigint |  | FK | SI | Des Ref Episode |
| IHEDOC_PAPerson_DR | bigint |  | FK | SI | Des Ref Patient |
| IHEDOC_UpdateDate | date |  |  | SI | UpdateDate |
| IHEDOC_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| IHEDOC_UpdateTime | time |  |  | SI | UpdateTime |
| IHEDOC_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| IHEDOC_websysDocument_DR | bigint |  | FK | SI | websysDocument |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*