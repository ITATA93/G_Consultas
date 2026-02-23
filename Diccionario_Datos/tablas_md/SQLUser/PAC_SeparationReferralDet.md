# SQLUser.PAC_SeparationReferralDet

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PAC_SeparationReferral Parent Reference |
| DET_ACASStatus | varchar |  |  | SI | ACASStatus |
| DET_CareType | varchar |  |  | SI | CareType |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | DateFrom |
| DET_DateTo | date |  |  | SI | DateTo |
| DET_DischargeType | varchar |  |  | SI | DischargeType |
| DET_RowId | varchar |  |  | NO | - |
| DET_Sex | varchar |  |  | SI | Sex |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Weight |
| Q01ObsDR | - |  |  | SI | Weight DR |
| Q02 | - |  |  | SI | Patient has read and understands patient informati... |
| Q03 | - |  |  | SI | Have the following side effects been discussed in ... |
| Q04 | - |  |  | SI | 1 - Potential risk of depression and/or mood swing... |
| Q05 | - |  |  | SI | 2 - Hyperlipidaemia |
| Q06 | - |  |  | SI | 3 - Teratogenic risk (in females) |
| Q07 | - |  |  | SI | Patient advised to ask someone close to them to ob... |
| Q08 | - |  |  | SI | If there are any concerns Isotretinoin treatment s... |
| Q09 | - |  |  | SI | Have the following results been recorded and check... |
| Q10 | - |  |  | SI | The importance of not becoming pregnant for one mo... |
| Q11 | - |  |  | SI | Read and understood patient information leaflet on... |
| Q12 | - |  |  | SI | If patient is female and is of child bearing age a... |
| Q13 | - |  |  | SI | If sexually active the patient has been advised to... |
| Q14 | - |  |  | SI | If not sexually active and of child bearing age pa... |
| Q15 | - |  |  | SI | continue with it regularly until one month after s... |
| Q16 | - |  |  | SI | If patient is female and sexually active and not u... |
| Q17 | - |  |  | SI | Patient has been advised to attend Family Planning... |
| Q18 | - |  |  | SI | Acknowledgement form has been signed |
| Q19 | - |  |  | SI | Patient has been given the telephone number of the... |
| Q20 | - |  |  | SI | Completed blood form given to patient for repeat b... |
| Q21 | - |  |  | SI | Notes |
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