# SQLUser.ARC_PaymentAgreementRCM

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRCM_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| PRCM_AutoECPharmDisp | varchar |  |  | SI | Auto e-Claim Pharmacy Dispatch |
| PRCM_AutoECPharmDispFreq | varchar |  |  | SI | Auto e-Claim Pharmacy Dispatch Frequency |
| PRCM_Childsub | double |  |  | NO | Childsub |
| PRCM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRCM_CreatedDate | date |  |  | SI | Created Date |
| PRCM_CreatedTime | time |  |  | SI | Created Time |
| PRCM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRCM_DateFrom | date |  |  | SI | Date From |
| PRCM_DateTo | date |  |  | SI | Date To |
| PRCM_EClaims | varchar |  |  | SI | eClaims |
| PRCM_EClaimsPharmacy | varchar |  |  | SI | eClaims Pharmacy |
| PRCM_EpisSubType_DR | bigint |  | FK | SI | Des Ref PACEpisodeSubType |
| PRCM_EpisodeType | varchar |  |  | SI | Episode Type |
| PRCM_Erx | varchar |  |  | SI | eRx |
| PRCM_FacilityType_DR | bigint |  | FK | SI | Facility Type |
| PRCM_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| PRCM_NewBornCovDays | double |  |  | SI | New Born Coverage days |
| PRCM_PostOffice | varchar |  |  | SI | Post Office |
| PRCM_PostOfficeAppPharm | varchar |  |  | SI | Post Office Approvals Pharmacy |
| PRCM_PostOfficeApprovals | varchar |  |  | SI | Post Office Approvals |
| PRCM_PostOffice_DR | bigint |  | FK | SI | Des Ref to ARCPostOffice |
| PRCM_Rank | double |  |  | SI | Rank |
| PRCM_RowId | varchar |  |  | NO | - |
| PRCM_UpdatedDate | date |  |  | SI | Updated Date |
| PRCM_UpdatedTime | time |  |  | SI | Updated Time |
| PRCM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Factores de Riesgo |
| Q02 | - |  |  | SI | Mayor o igual a 65 años o pediátrico |
| Q03 | - |  |  | SI | Caídas Previas |
| Q04 | - |  |  | SI | En algún procedimiento anterior |
| Q05 | - |  |  | SI | Alteraciones Neurológicas |
| Q06 | - |  |  | SI | Epilepsia, convulsiones, paresia, parálisis, Parki... |
| Q07 | - |  |  | SI | Trastornos Psíquicos |
| Q08 | - |  |  | SI | Alcoholismo y/o drogadicción |
| Q09 | - |  |  | SI | Actitud resistente, agresiva o temerosa, crisis de... |
| Q10 | - |  |  | SI | Depresión, trastorno bipolar en etapa aguda |
| Q11 | - |  |  | SI | Defectos Visión /Audición |
| Q12 | - |  |  | SI | Cataratas, glaucoma, retinopatía y trastornos vest... |
| Q13 | - |  |  | SI | Alteraciones de conciencia |
| Q14 | - |  |  | SI | Confuso, desorientado, agitación psicomotora |
| Q15 | - |  |  | SI | Uso de Fármacos |
| Q16 | - |  |  | SI | Tranquilizantes-sedantes |
| Q17 | - |  |  | SI | Diuréticos |
| Q18 | - |  |  | SI | Hipotensores (No diuréticos) |
| Q19 | - |  |  | SI | Antiparkinsonianos |
| Q20 | - |  |  | SI | Antidepresivos |
| Q21 | - |  |  | SI | Otros |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*