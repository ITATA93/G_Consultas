# websys.DocumentSigning

> "Documents for Digital Certificate Signing Workbench

**Schema:** websys
**Columnas:** 39
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Documents for Digital Certificate Signing Workbench

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DDSBatchID | varchar |  |  | SI | - |
| DDSComments | varchar |  |  | SI | - |
| DDSConsentQuestionnaire | varchar |  |  | SI | Consent Questionnaire attached with the report |
| DDSCreateCPDR | varchar |  | FK | SI | - |
| DDSCreateDate | date |  |  | SI | - |
| DDSCreateTime | time |  |  | SI | - |
| DDSCreateUserDR | bigint |  | FK | SI | - |
| DDSDocPrintDesc | varchar |  |  | SI | - |
| DDSDocReportDR | bigint |  | FK | SI | Associated Report Definition |
| DDSDocReportUID | varchar |  |  | SI | Unique Identifier connected to the report DDSDocRe... |
| DDSDocStatus | varchar |  |  | SI | [U]nsigned - Document previewd by the user, yet to... |
| DDSDocumentStream | longvarbinary |  |  | SI | Compiled Report Document as a stream; |
| DDSEpisodeDR | bigint |  | FK | SI | - |
| DDSForSignByCP | varchar |  |  | SI | Care Providers Nominated to Sign the document |
| DDSFreeText1 | varchar |  |  | SI | - |
| DDSFreeText2 | varchar |  |  | SI | - |
| DDSLocationDR | bigint |  | FK | SI | - |
| DDSNoOfCopies | integer |  |  | SI | Number of copies to be printed |
| DDSOrderDR | varchar |  | FK | SI | - |
| DDSPAADMAdmDate | date |  |  | SI | - |
| DDSPAADMDischgDate | date |  |  | SI | - |
| DDSPatientDR | bigint |  | FK | SI | - |
| DDSPrintHistoryDR | bigint |  | FK | SI | - |
| DDSRepositoryMessage | varchar |  |  | SI | Any extra messages returned from the respository w... |
| DDSRepositorySentDate | date |  |  | SI | Date Document Sent to Repository |
| DDSRepositorySentTime | time |  |  | SI | Time Document Sent to Repository |
| DDSRepositoryStatus | varchar |  |  | SI | Status returned from the repository
ToBeSent
Sen... |
| DDSRepositoryUID | varchar |  |  | SI | Unique Identifier Returned from the Repository (un... |
| DDSResourceDR | bigint |  | FK | SI | - |
| DDSSignCPDR | varchar |  | FK | SI | - |
| DDSSignDate | date |  |  | SI | - |
| DDSSignDocStream | longvarbinary |  |  | SI | Signed Report Document as a stream; |
| DDSSignTime | time |  |  | SI | - |
| DDSSignUserDR | bigint |  | FK | SI | - |
| DDSSignedByCP | varchar |  |  | SI | Care Providers who have Signed the Document |
| DDSTextResultID | varchar |  |  | SI | TextResultID for the Text Result to be signed |
| DDSUpdateDate | date |  |  | SI | - |
| DDSUpdateTime | time |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*