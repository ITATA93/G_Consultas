# questionnaire.QTCNDC

> Nursing Discharge Checklist

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Nursing Discharge Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Relative / carer / other informed of discharge? |
| Q02 | date |  |  | SI | Date Informed	 |
| Q03 | varchar |  |  | SI | Details 	 |
| Q04 | varchar |  |  | SI | Relevant service providers informed of patients di... |
| Q05 | varchar |  |  | SI | Details |
| Q06 | varchar |  |  | SI | Care package complete?  |
| Q07 | varchar |  |  | SI | Detail Rationale	 |
| Q08 | date |  |  | SI | Start Date of Care Package	 |
| Q09 | varchar |  |  | SI | Details of Care Package: Company, How Many Calls P... |
| Q10 | varchar |  |  | SI | Relevant aids ordered? |
| Q11 | varchar |  |  | SI | Details	 |
| Q12 | varchar |  |  | SI | Relevant aids delivered?	 |
| Q13 | varchar |  |  | SI | Details	 |
| Q14 | varchar |  |  | SI | Hospital / patient arranged transport? |
| Q15 | varchar |  |  | SI | Mode of transport |
| Q16 | varchar |  |  | SI | Key / access to home available? |
| Q17 | varchar |  |  | SI | Details	 |
| Q18 | varchar |  |  | SI | Valuables / property returned to patient? |
| Q19 | varchar |  |  | SI | Cannula removed and site healed? |
| Q20 | varchar |  |  | SI | Ensure community IV team referral has been made  |
| Q21 | varchar |  |  | SI | Clinical supplies provided i.e. dressings, nasal g... |
| Q22 | varchar |  |  | SI | Detail items provided |
| Q23 | varchar |  |  | SI | If patient is being discharged with catheter insit... |
| Q24 | varchar |  |  | SI | Does patient require outpatient appointment(OPD)? |
| Q25 | varchar |  |  | SI | Has patient (or carer / relative if appropriate) b... |
| Q26 | varchar |  |  | SI | Details	 |
| Q27 | varchar |  |  | SI | Appointment card given  |
| Q28 | varchar |  |  | SI | Has home oxygen been installed if required |
| Q29 | varchar |  |  | SI | Ensure hospital computer records updated to confir... |
| Q30 | varchar |  |  | SI | Discharge address confirmed as |
| Q31 | varchar |  |  | SI | Details 	 |
| Q32 | varchar |  |  | SI | Heating available at home?	 |
| Q33 | varchar |  |  | SI | Ensure relevant referrals are made |
| Q34 | varchar |  |  | SI | Food available at home? 	 |
| Q35 | varchar |  |  | SI | Supply patient with food pack |
| Q36 | varchar |  |  | SI | Ensure patient is adequately clothed for journey h... |
| Q37 | varchar |  |  | SI | Ensure patient has been given a contact number sho... |
| Q38 | varchar |  |  | SI | Have To Take Out (TTO) medication been supplied	 |
| Q39 | varchar |  |  | SI | Details 	 |
| Q40 | varchar |  |  | SI | Copy of medication given to patient (relative or c... |
| Q41 | varchar |  |  | SI | Ensure you explain to patient (relative or carer i... |
| Q42 | varchar |  |  | SI | Ensure patient (relative or carer if necessary) ar... |
| Q43 | longvarbinary |  |  | SI | I have been given information regarding my operati... |
| Q43UDt | date |  |  | SI | I have been given information regarding my operati... |
| Q43UTm | time |  |  | SI | I have been given information regarding my operati... |
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