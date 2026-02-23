# SQLUser.PAC_Synonym

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SYN_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Is the patient being discharged / transferred dire... |
| Q02 | - |  |  | SI | Destination |
| Q03 | - |  |  | SI | Observations breaching clinical review criteria? |
| Q04 | - |  |  | SI | Please specify plan |
| Q05 | - |  |  | SI | Receiving unit medical officer notified ? |
| Q06 | - |  |  | SI | Name of medical officer |
| Q07 | - |  |  | SI | Dressing(s) checked and/or changed? |
| Q08 | - |  |  | SI | ID / Allergy bands in-situ? |
| Q09 | - |  |  | SI | Indwelling catheter and drainage bags emptied? |
| Q10 | - |  |  | SI | Care and treatment plan communicated and accepted ... |
| Q11 | - |  |  | SI | Details |
| Q12 | - |  |  | SI | Post discharge action plan completed? |
| Q13 | - |  |  | SI | Medical limitations of treatment completed? |
| Q14 | - |  |  | SI | Follow up appointments arranged and provided to pa... |
| Q15 | - |  |  | SI | Inter-hospital / facility transfer letter complete... |
| Q16 | - |  |  | SI | Discharge / Transfer summary complete? |
| Q17 | - |  |  | SI | Discharge summary provided to |
| Q18 | - |  |  | SI | Nursing note complete and copy provided to patient... |
| Q19 | - |  |  | SI | Medical certificate completed and provided? |
| Q20 | - |  |  | SI | Education material provided? |
| Q21 | - |  |  | SI | Additional details |
| Q22 | - |  |  | SI | Facility notified of discharge time? |
| Q23 | - |  |  | SI | Relatives informed of discharge / transfer? |
| Q24 | - |  |  | SI | Pre admission services notified? |
| Q25 | - |  |  | SI | Please specify |
| Q26 | - |  |  | SI | Medication chart completed? |
| Q27 | - |  |  | SI | Pharmacy review complete? |
| Q28 | - |  |  | SI | Medications arranged with appropriate pharmacy? |
| Q29 | - |  |  | SI | Discharge medications completed? |
| Q30 | - |  |  | SI | Own medications returned? |
| Q31 | - |  |  | SI | Transport arranged and confirmed? |
| Q32 | - |  |  | SI | Patient property and belongings checked and with p... |
| Q33 | - |  |  | SI | Intravascular access lines questionnaire updated /... |
| Q34 | - |  |  | SI | Allergies up to date? |
| Q35 | - |  |  | SI | Alerts up to date? |
| Q36 | - |  |  | SI | Problems up to date? |
| Q37 | - |  |  | SI | Comment |
| Q38 | - |  |  | SI | This checklist can be used for all patient dischar... |
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
| SYN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SYN_CreatedDate | date |  |  | SI | Created Date |
| SYN_CreatedTime | time |  |  | SI | Created Time |
| SYN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SYN_Owner | varchar |  |  | SI | Owner |
| SYN_Text | varchar |  |  | SI | Text |
| SYN_Type | varchar |  |  | SI | Type |
| SYN_UpdatedDate | date |  |  | SI | Updated Date |
| SYN_UpdatedTime | time |  |  | SI | Updated Time |
| SYN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*