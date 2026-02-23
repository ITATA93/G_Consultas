# questionnaire.QTCPTADIC

> Patient Transfer and Discharge Checklist

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Transfer and Discharge Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Is the patient being discharged / transferred dire... |
| Q02 | varchar |  |  | SI | Destination |
| Q03 | varchar |  |  | SI | Observations breaching clinical review criteria? |
| Q04 | varchar |  |  | SI | Please specify plan |
| Q05 | varchar |  |  | SI | Receiving unit medical officer notified ? |
| Q06 | varchar |  |  | SI | Name of medical officer |
| Q07 | varchar |  |  | SI | Dressing(s) checked and/or changed? |
| Q08 | varchar |  |  | SI | ID / Allergy bands in-situ? |
| Q09 | varchar |  |  | SI | Indwelling catheter and drainage bags emptied? |
| Q10 | varchar |  |  | SI | Care and treatment plan communicated and accepted ... |
| Q11 | varchar |  |  | SI | Details |
| Q12 | varchar |  |  | SI | Post discharge action plan completed? |
| Q13 | varchar |  |  | SI | Medical limitations of treatment completed? |
| Q14 | varchar |  |  | SI | Follow up appointments arranged and provided to pa... |
| Q15 | varchar |  |  | SI | Inter-hospital / facility transfer letter complete... |
| Q16 | varchar |  |  | SI | Discharge / Transfer summary complete? |
| Q17 | varchar |  |  | SI | Discharge summary provided to |
| Q18 | varchar |  |  | SI | Nursing note complete and copy provided to patient... |
| Q19 | varchar |  |  | SI | Medical certificate completed and provided? |
| Q20 | varchar |  |  | SI | Education material provided? |
| Q21 | varchar |  |  | SI | Additional details |
| Q22 | varchar |  |  | SI | Facility notified of discharge time? |
| Q23 | varchar |  |  | SI | Relatives informed of discharge / transfer?  |
| Q24 | varchar |  |  | SI | Pre admission services notified? |
| Q25 | varchar |  |  | SI | Please specify |
| Q26 | varchar |  |  | SI | Medication chart completed? |
| Q27 | varchar |  |  | SI | Pharmacy review complete? |
| Q28 | varchar |  |  | SI | Medications arranged with appropriate pharmacy? |
| Q29 | varchar |  |  | SI | Discharge medications completed? |
| Q30 | varchar |  |  | SI | Own medications returned? |
| Q31 | varchar |  |  | SI | Transport arranged and confirmed? |
| Q32 | varchar |  |  | SI | Patient property and belongings checked and with p... |
| Q33 | varchar |  |  | SI | Intravascular access lines questionnaire updated /... |
| Q34 | varchar |  |  | SI | Allergies up to date? |
| Q35 | varchar |  |  | SI | Alerts up to date? |
| Q36 | varchar |  |  | SI | Problems up to date? |
| Q37 | varchar |  |  | SI | Comment |
| Q38 | varchar |  |  | SI | This checklist can be used for all patient dischar... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*