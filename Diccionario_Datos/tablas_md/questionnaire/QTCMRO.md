# questionnaire.QTCMRO

> Mechanical Restraint Order

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mechanical Restraint Order

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Duration	 |
| Q02 | varchar |  |  | SI | Restraint to prevent |
| Q03 | varchar |  |  | SI | Prevention strategies attempted |
| Q04 | varchar |  |  | SI | Comments |
| Q05 | varchar |  |  | SI | Is specialling required |
| Q06 | varchar |  |  | SI | Decision discussed with |
| Q07 | date |  |  | SI | Date family involved	 |
| Q08 | time |  |  | SI | Time family involved	 |
| Q09 | varchar |  |  | SI | Staff member advising family	 |
| Q10 | varchar |  |  | SI | Form of restraint to be used |
| Q11 | varchar |  |  | SI | If other, please specify	 |
| Q12 | varchar |  |  | SI | Restraints applied to |
| Q13 | varchar |  |  | SI | Please specify which limbs	 |
| Q14 | date |  |  | SI | Date restraint commenced	 |
| Q15 | time |  |  | SI | Time restraint commenced	 |
| Q16 | varchar |  |  | SI | Nurse in charge when restraint commenced	 |
| Q17 | longvarbinary |  |  | SI | Nurse in charge signature	 |
| Q17UDt | date |  |  | SI | Nurse in charge signature	 Last Updated Date |
| Q17UTm | time |  |  | SI | Nurse in charge signature	 Last Updated Time |
| Q18 | varchar |  |  | SI | Restraint Order (Registrar Level or Above) |
| Q19 | bit |  |  | SI | Medical assessment documented	 |
| Q20 | varchar |  |  | SI | Frequency of Medical Review, maximum of 4 hourly |
| Q21 | varchar |  |  | SI | Frequency of medical review |
| Q22 | varchar |  |  | SI | Specific orders (eg SOOB only)	 |
| Q23 | date |  |  | SI | Review date	 |
| Q24 | varchar |  |  | SI | Medical officer ordering restraint	 |
| Q25 | longvarbinary |  |  | SI | Medical officer signature	 |
| Q25UDt | date |  |  | SI | Medical officer signature	 Last Updated Date |
| Q25UTm | time |  |  | SI | Medical officer signature	 Last Updated Time |
| Q26 | varchar |  |  | SI | Name of the family member advised |
| Q27 | date |  |  | SI | Date |
| Q28 | time |  |  | SI | Time |
| Q29 | date |  |  | SI | Date and time of next medical review |
| Q30 | time |  |  | SI | Time |
| Q31 | varchar |  |  | SI | Frequency of medical review (hrs) |
| Q32 | varchar |  |  | SI | Is the patient under the Mental Health Act |
| Q33 | varchar |  |  | SI | Please complete required forms |
| Q34 | varchar |  |  | SI | Restraint to prevent |
| Q35 | varchar |  |  | SI | Other restraint to prevent |
| Q36 | varchar |  |  | SI | Context of the restraint |
| Q37 | varchar |  |  | SI | Comments |
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