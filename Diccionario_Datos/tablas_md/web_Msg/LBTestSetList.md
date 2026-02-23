# web_Msg.LBTestSetList

**Schema:** web_Msg
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AdmissionType | varchar |  |  | SI | - |
| BloodProductIssueSearch | bit |  |  | SI | - |
| CTSRCH | varchar |  |  | SI | - |
| CareProvider | varchar |  |  | SI | - |
| CareProviders | varchar |  |  | SI | - |
| CreateWorkList | bit |  |  | SI | Message classes are to be created and saved |
| DateFrom | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| DepartmentList | varchar |  |  | SI | - |
| Departments | varchar |  |  | SI | - |
| EpisodeNo | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| IncompleteLabEpisode | varchar |  |  | SI | - |
| IsStoredList | bit |  |  | SI | Indicates message classes have been created and sa... |
| LBCDynamicFunctionTestList | varchar |  |  | SI | - |
| LBEPExternalReferralFrom | bigint |  |  | SI | - |
| LBEPExternalReferralNumber | varchar |  |  | SI | - |
| LBEPLabSite | bigint |  |  | SI | - |
| LBEPLabSiteList | varchar |  |  | SI | - |
| LBEPPAPERID | varchar |  |  | SI | Derived from the entered URN |
| LBEPSubjectIdentificationNumber | varchar |  |  | SI | - |
| LBEpisodeGroupNumber | varchar |  |  | SI | - |
| LBEpisodeNo | varchar |  |  | SI | - |
| LBEpisodeStatusList | varchar |  |  | SI | - |
| LabSiteList | varchar |  |  | SI | - |
| LabSites | varchar |  |  | SI | - |
| MRN | varchar |  |  | SI | - |
| MaterialNumber | varchar |  |  | SI | [DEPRICATED] |
| PAPERID | varchar |  |  | SI | - |
| PackingListNumber | varchar |  |  | SI | - |
| PatientLocationList | varchar |  |  | SI | - |
| PatientLocations | varchar |  |  | SI | - |
| PatientTypeList | varchar |  |  | SI | - |
| PriorityList | varchar |  |  | SI | - |
| QueueAllAny | varchar |  |  | SI | - |
| QueueList | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| ReasonNotPerformedList | varchar |  |  | SI | - |
| ReceivedDateFrom | date |  |  | SI | - |
| ReceivedDateTo | date |  |  | SI | - |
| ReceivedTimeFrom | time |  |  | SI | - |
| ReceivedTimeTo | time |  |  | SI | - |
| RefDocID | varchar |  |  | SI | - |
| ReferralLabList | varchar |  |  | SI | - |
| ReferralLaboratory | bigint |  |  | SI | - |
| ResultFlagList | varchar |  |  | SI | - |
| ResultInquiryMode | bit |  |  | SI | - |
| SRCHMsgID | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| ShowOnlyPatients | bit |  |  | SI | - |
| SignificantResults | bit |  |  | SI | - |
| Specimen | bigint |  |  | SI | - |
| SpecimenGroup | bigint |  |  | SI | - |
| SpecimenNumber | varchar |  |  | SI | Now searches for specimen and material number |
| SubjectID | varchar |  |  | SI | - |
| SubjectType | bigint |  |  | SI | - |
| TSRTITM | varchar |  |  | SI | - |
| TSRTORD | varchar |  |  | SI | - |
| TestSetActiveTransferLimitation | varchar |  |  | SI | - |
| TestSetList | varchar |  |  | SI | - |
| TestSetStatusList | varchar |  |  | SI | - |
| TotalEpisodeRowCount | integer |  |  | SI | - |
| TotalRowCount | integer |  |  | SI | - |
| TransferFromLabSite | bigint |  |  | SI | - |
| TransferStatus | varchar |  |  | SI | - |
| TransferStatusList | varchar |  |  | SI | - |
| TransferToLabSite | bigint |  |  | SI | - |
| TransferToReferralLab | bigint |  |  | SI | - |
| TurnaroundTimeExceeded | varchar |  |  | SI | - |
| URN | varchar |  |  | SI | - |
| Worksheet | bigint |  |  | SI | - |
| WorksheetNumber | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| currentCTSRCH | varchar |  |  | SI | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*