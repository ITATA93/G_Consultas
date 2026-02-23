# SQLUser.PAC_ServiceAgreementEpisodeType

**Schema:** SQLUser
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EP_ParRef | bigint | PK |  | NO | PAC_ServiceAgreement Parent Reference |
| EP_Childsub | double |  |  | NO | Childsub |
| EP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EP_CreatedDate | date |  |  | SI | Created Date |
| EP_CreatedTime | time |  |  | SI | Created Time |
| EP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EP_EpisodeType | varchar |  |  | SI | Episode Type |
| EP_RowId | varchar |  |  | NO | - |
| EP_ServiceGroup_DR | bigint |  | FK | SI | Des Ref ServiceGroup |
| EP_UpdatedDate | date |  |  | SI | Updated Date |
| EP_UpdatedTime | time |  |  | SI | Updated Time |
| EP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Pre-procedure Checklist |
| Q04 | - |  |  | SI | Interpreter required |
| Q05 | - |  |  | SI | Variance |
| Q06 | - |  |  | SI | Aboriginal health worker required |
| Q07 | - |  |  | SI | Variance |
| Q08 | - |  |  | SI | Consent signed |
| Q09 | - |  |  | SI | Variance |
| Q10 | - |  |  | SI | Patient armband in place and correct |
| Q11 | - |  |  | SI | Variance |
| Q12 | - |  |  | SI | All allergies documented |
| Q13 | - |  |  | SI | Variance |
| Q14 | - |  |  | SI | Fasting status |
| Q15 | - |  |  | SI | Variance |
| Q16 | - |  |  | SI | Baseline bloods reviewed including potassium level... |
| Q17 | - |  |  | SI | Variance |
| Q18 | - |  |  | SI | Intravascular cannula in situ and patent |
| Q19 | - |  |  | SI | Variance |
| Q20 | - |  |  | SI | Medications reviewed and withheld as ordered by do... |
| Q21 | - |  |  | SI | Variance |
| Q22 | - |  |  | SI | Check pre-medication order |
| Q23 | - |  |  | SI | Variance |
| Q24 | - |  |  | SI | Patient resting comfortably prior to procedure |
| Q25 | - |  |  | SI | Variance |
| Q26 | - |  |  | SI | Education provided regarding device insertion and ... |
| Q27 | - |  |  | SI | Variance |
| Q28 | - |  |  | SI | Day 0 - Post procedure |
| Q29 | - |  |  | SI | Reviewed by cardiologist |
| Q30 | - |  |  | SI | Variance |
| Q31 | - |  |  | SI | Leave patient on continuous monitoring until revie... |
| Q32 | - |  |  | SI | Variance |
| Q33 | - |  |  | SI | Once patient fully awake oral fluids and diet as o... |
| Q34 | - |  |  | SI | Variance |
| Q35 | - |  |  | SI | Rest in bed, can sit up in bed after 4 hours |
| Q36 | - |  |  | SI | Variance |
| Q37 | - |  |  | SI | Post operative procedure information sheet provide... |
| Q38 | - |  |  | SI | Variance |
| Q39 | - |  |  | SI | Day 1 |
| Q40 | - |  |  | SI | Observations remained within normal parameters |
| Q41 | - |  |  | SI | Variance |
| Q42 | - |  |  | SI | Continuous cardiac monitoring until device check a... |
| Q43 | - |  |  | SI | Variance |
| Q44 | - |  |  | SI | 12 lead electrocardiogram (ECG) conducted and revi... |
| Q45 | - |  |  | SI | Variance |
| Q46 | - |  |  | SI | Once device checked by Cardiology reviewed, patien... |
| Q47 | - |  |  | SI | Variance |
| Q48 | - |  |  | SI | Tolerating diet as ordered |
| Q49 | - |  |  | SI | Variance |
| Q50 | - |  |  | SI | Once mobilising, remove Thromboembolic Deterrent S... |
| Q51 | - |  |  | SI | Variance |
| Q52 | - |  |  | SI | Ensure regular medications are charted and reviewe... |
| Q53 | - |  |  | SI | Variance |
| Q54 | - |  |  | SI | If Cardiology review and patient is for discharge,... |
| Q55 | - |  |  | SI | Variance |
| Q56 | - |  |  | SI | Patient provided with post device care education, ... |
| Q57 | - |  |  | SI | Variance |
| Q58 | - |  |  | SI | Contact relevant Cardiac clinical nurse consultant... |
| Q59 | - |  |  | SI | Variance |
| Q60 | - |  |  | SI | Contact Aboriginal health worker if required for a... |
| Q61 | - |  |  | SI | Variance |
| Q62 | - |  |  | SI | Contact Interpreter if required for additional dis... |
| Q63 | - |  |  | SI | Variance |
| Q64 | - |  |  | SI | Cardiology appointment provided to patient |
| Q65 | - |  |  | SI | Variance |
| Q66 | - |  |  | SI | Device card given to the patient |
| Q67 | - |  |  | SI | Variance |
| Q68 | - |  |  | SI | Day of procedure |
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