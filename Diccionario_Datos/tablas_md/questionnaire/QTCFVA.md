# questionnaire.QTCFVA

> Domestic and Family Violence Assessment

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Domestic and Family Violence Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Domestic and family violence alert completed |
| Q02 | varchar |  |  | SI | Interpreter required |
| Q03 | varchar |  |  | SI | Preferred language spoken |
| Q04 | varchar |  |  | SI | Preferred interpreter |
| Q05 | varchar |  |  | SI | Type of domestic & family violence (D&FV) |
| Q06 | varchar |  |  | SI | Other type |
| Q07 | varchar |  |  | SI | Alleged perpetrator relationship to patient |
| Q08 | varchar |  |  | SI | Other perpetrator |
| Q09 | varchar |  |  | SI | Patient's report of situation |
| Q10 | varchar |  |  | SI | Clinician's assessment of situation |
| Q11 | varchar |  |  | SI | Children / Other in the family |
| Q12 | varchar |  |  | SI | Location / Residence of children |
| Q13 | varchar |  |  | SI | Legal status |
| Q14 | varchar |  |  | SI | Date and time of incident |
| Q15 | date |  |  | SI | Date |
| Q16 | time |  |  | SI | Time |
| Q17 | bit |  |  | SI | Unknown |
| Q18 | bit |  |  | SI | N/A |
| Q19 | varchar |  |  | SI | History of FV |
| Q20 | varchar |  |  | SI | Client's living arrangements |
| Q21 | varchar |  |  | SI | Identified risks |
| Q22 | varchar |  |  | SI | Patient / Client |
| Q23 | varchar |  |  | SI | Perpetrator risks (e.g. use of weapons, threats to... |
| Q24 | varchar |  |  | SI | Relationship |
| Q25 | varchar |  |  | SI | Other relationship |
| Q26 | varchar |  |  | SI | Safety |
| Q27 | varchar |  |  | SI | Clinician assessed urgency for action |
| Q28 | varchar |  |  | SI | Safety threat to treating team identified (Inform ... |
| Q29 | varchar |  |  | SI | Referral consent |
| Q30 | varchar |  |  | SI | Consent obtained to provide details to external se... |
| Q31 | varchar |  |  | SI | Internal referral |
| Q32 | varchar |  |  | SI | External referrals |
| Q33 | varchar |  |  | SI | Information (brochures / numbers) provided |
| Q34 | varchar |  |  | SI | Safety plan |
| Q35 | varchar |  |  | SI | Client discharged to |
| Q36 | varchar |  |  | SI | Client wishes considered in discharge planning |
| Q37 | varchar |  |  | SI | Notes |
| Q38 | varchar |  |  | SI | If other, please specify |
| Q39 | varchar |  |  | SI | Other agency |
| Q40 | varchar |  |  | SI | Other living arrangements |
| Q41 | varchar |  |  | SI | Interpreter required |
| Q42 | varchar |  |  | SI | Preferred language spoken |
| Q43 | varchar |  |  | SI | Other internal referral |
| Q44 | varchar |  |  | SI | Name |
| Q45 | varchar |  |  | SI | Designation / Service |
| Q46 | varchar |  |  | SI | Secondary Consultation Sought |
| Q47 | date |  |  | SI | Date |
| Q48 | time |  |  | SI | Time |
| Q49 | varchar |  |  | SI | External link |
| Q50 | varchar |  |  | SI | Unknown |
| Q51 | varchar |  |  | SI | N/A |
| Q52 | varchar |  |  | SI | Children / other in the family notes |
| Q53 | varchar |  |  | SI | Family safety framework assessment required |
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