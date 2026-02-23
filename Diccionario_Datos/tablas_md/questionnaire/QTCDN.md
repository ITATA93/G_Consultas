# questionnaire.QTCDN

> Death Notification

**Schema:** questionnaire
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Death Notification

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Ward / department |
| Q02 | varchar |  |  | SI | Parent unit Hospital Medical Officer (HMO)	 |
| Q03 | date |  |  | SI | Date of death	 |
| Q04 | time |  |  | SI | Time of death	 |
| Q05 | varchar |  |  | SI | Hospital Medical Officer (HMO) declaring death	 |
| Q06 | varchar |  |  | SI | Death certificate completed	 |
| Q07 | varchar |  |  | SI | Relatives / next of kin notified  |
| Q08 | varchar |  |  | SI | By whom	 |
| Q09 | date |  |  | SI | Date |
| Q10 | time |  |  | SI | Time |
| Q11 | varchar |  |  | SI | Relatives / next of kin name(s)	 |
| Q12 | varchar |  |  | SI | General Practitioner (GP) notified |
| Q13 | varchar |  |  | SI | General Practitioner (GP) name	 |
| Q14 | date |  |  | SI | Date notified	 |
| Q15 | time |  |  | SI | Time notified	 |
| Q16 | varchar |  |  | SI | Please indicate when notified by Hospital Medical ... |
| Q17 | varchar |  |  | SI | Please indicate when completed |
| Q18 | varchar |  |  | SI | Left on deceased (please list)	 |
| Q19 | varchar |  |  | SI | Sent home with relative / next of kin |
| Q20 | varchar |  |  | SI | Name(s)	 |
| Q21 | varchar |  |  | SI | Nurse's name	 |
| Q22 | longvarbinary |  |  | SI | Witness signature (relative / next of kin)	 |
| Q22UDt | date |  |  | SI | Witness signature (relative / next of kin)	 Last U... |
| Q22UTm | time |  |  | SI | Witness signature (relative / next of kin)	 Last U... |
| Q23 | varchar |  |  | SI | Witness name (relative / next of kin)	 |
| Q24 | varchar |  |  | SI | Pacemaker insitu |
| Q25 | varchar |  |  | SI | Incomplete actions referred to Medical Officer (MO... |
| Q26 | longvarbinary |  |  | SI | Signature	 |
| Q26UDt | date |  |  | SI | Signature	 Last Updated Date |
| Q26UTm | time |  |  | SI | Signature	 Last Updated Time |
| Q27 | varchar |  |  | SI | Name |
| Q28 | date |  |  | SI | Date |
| Q29 | longvarbinary |  |  | SI | Signature	 |
| Q29UDt | date |  |  | SI | Signature	 Last Updated Date |
| Q29UTm | time |  |  | SI | Signature	 Last Updated Time |
| Q30 | varchar |  |  | SI | Name |
| Q31 | date |  |  | SI | Date |
| Q32 | varchar |  |  | SI | Valuables sent home |
| Q34 | varchar |  |  | SI | Reason for not calling |
| Q35 | varchar |  |  | SI | Room number |
| Q36 | varchar |  |  | SI | Bed number |
| Q37 | varchar |  |  | SI | Comments |
| Q38 | varchar |  |  | SI | Name of Member Representative of Patient (MRP) |
| Q39 | varchar |  |  | SI | ID ( Member Representative of Patient (MRP)) |
| Q40 | numeric |  |  | SI | Contact number |
| Q41 | date |  |  | SI | Date |
| Q42 | longvarbinary |  |  | SI | Signature |
| Q42UDt | date |  |  | SI | Signature Last Updated Date |
| Q42UTm | time |  |  | SI | Signature Last Updated Time |
| Q43 | varchar |  |  | SI | Name of patient experience officer |
| Q44 | varchar |  |  | SI | ID |
| Q45 | date |  |  | SI | Date |
| Q46 | longvarbinary |  |  | SI | Signature |
| Q46UDt | date |  |  | SI | Signature Last Updated Date |
| Q46UTm | time |  |  | SI | Signature Last Updated Time |
| Q47 | varchar |  |  | SI | Dummy 1 |
| Q48 | varchar |  |  | SI | Dummy 2 |
| Q49 | varchar |  |  | SI | Dummy 3 |
| Q50 | varchar |  |  | SI | Dummy 4 |
| Q51 | varchar |  |  | SI | Dummy 5 |
| Q52 | varchar |  |  | SI | Dummy 6 |
| Q53 | varchar |  |  | SI | Dummy 7 |
| Q54 | varchar |  |  | SI | Dummy 8 |
| Q55 | varchar |  |  | SI | Dummy 9 |
| Q56 | varchar |  |  | SI | Dummy 10 |
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