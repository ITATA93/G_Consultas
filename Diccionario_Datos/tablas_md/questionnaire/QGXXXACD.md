# questionnaire.QGXXXACD

> Advanced Care Directive

**Schema:** questionnaire
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Advanced Care Directive

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | A record of my future health care wishes |
| Q02 | varchar |  |  | SI | I declare that: |
| Q03 | varchar |  |  | SI | 1.  My current health problems include  |
| Q04 | varchar |  |  | SI | If you have some specific health problems you may ... |
| Q05 | varchar |  |  | SI | Refer to Advance Care Plan Information Sheet. |
| Q06 | varchar |  |  | SI | 2.  This document has been explained to me and I u... |
| Q07 | varchar |  |  | SI |  It will only be used if I am unable to make decis... |
| Q08 | varchar |  |  | SI | 3.  I understand that it is important to discuss m... |
| Q09 | varchar |  |  | SI | 4.  I request that my wishes, and the beliefs and ... |
| Q10 | varchar |  |  | SI | I have written on page 2 of this form the things t... |
| Q11 | varchar |  |  | SI | 5.  I understand that doctors will only provide tr... |
| Q12 | varchar |  |  | SI | I also understand that irrespective of any decisio... |
| Q13 | varchar |  |  | SI | CPR |
| Q14 | varchar |  |  | SI | Life Prolonging Treatments  |
| Q15 | varchar |  |  | SI | To me, a reasonable outcome means: |
| Q16 | varchar |  |  | SI | Decisions regarding CPR will be made by: |
| Q17 | varchar |  |  | SI | I choose to delegate decisions regarding CPR and l... |
| Q18 | varchar |  |  | SI | Medical Enduring Power of Attorney Name and Contac... |
| Q19 | varchar |  |  | SI | Name and relationship |
| Q20 | varchar |  |  | SI | The things that I most value in my life are  (e.g.... |
| Q21 | varchar |  |  | SI | Future situations that I would find unacceptable i... |
| Q22 | varchar |  |  | SI | Specific treatments that I would NOT want consider... |
| Q23 | varchar |  |  | SI | Other things that I would like known, which may he... |
| Q24 | varchar |  |  | SI | I ask that, if possible, my Medical Enduring Power... |
| Q25 | varchar |  |  | SI | If I am nearing death I would like the following  ... |
| Q26 | bit |  |  | SI | Refusal of Treatment Certificate (RTC) exists |
| Q27 | varchar |  |  | SI | This is a true record of my wishes on this date |
| Q28 | varchar |  |  | SI | Signature provided by |
| Q29 | longvarbinary |  |  | SI | Patient |
| Q29UDt | date |  |  | SI | Patient Last Updated Date |
| Q29UTm | time |  |  | SI | Patient Last Updated Time |
| Q30 | longvarbinary |  |  | SI | If the patient is unable to sign but has indicated... |
| Q30UDt | date |  |  | SI | If the patient is unable to sign but has indicated... |
| Q30UTm | time |  |  | SI | If the patient is unable to sign but has indicated... |
| Q31 | varchar |  |  | SI | Name of witness |
| Q32 | longvarbinary |  |  | SI | I believe that the person is competent and underst... |
| Q32UDt | date |  |  | SI | I believe that the person is competent and underst... |
| Q32UTm | time |  |  | SI | I believe that the person is competent and underst... |
| Q33 | varchar |  |  | SI | The contents of this Statement of Choices have als... |
| Q34 | date |  |  | SI | Date |
| Q35 | varchar |  |  | SI | Name |
| Q36 | varchar |  |  | SI | Relationship |
| Q37 | longvarbinary |  |  | SI | Signature Person 1 |
| Q37UDt | date |  |  | SI | Signature Person 1 Last Updated Date |
| Q37UTm | time |  |  | SI | Signature Person 1 Last Updated Time |
| Q38 | date |  |  | SI | Date |
| Q39 | varchar |  |  | SI | Name |
| Q40 | varchar |  |  | SI | Relationship |
| Q41 | longvarbinary |  |  | SI | Signature Person 2 |
| Q41UDt | date |  |  | SI | Signature Person 2 Last Updated Date |
| Q41UTm | time |  |  | SI | Signature Person 2 Last Updated Time |
| Q42 | varchar |  |  | SI | Care Provider |
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