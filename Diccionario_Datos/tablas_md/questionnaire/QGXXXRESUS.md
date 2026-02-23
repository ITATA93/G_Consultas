# questionnaire.QGXXXRESUS

> Resuscitation Report

**Schema:** questionnaire
**Columnas:** 149
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Resuscitation Report

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date event recognised |
| Q02 | time |  |  | SI | Time event recognised |
| Q03 | varchar |  |  | SI | Location of event |
| Q04 | varchar |  |  | SI | Witnessed |
| Q05 | varchar |  |  | SI | Pre arrest diagnosis |
| Q06 | varchar |  |  | SI | Estimated duration of arrest prior to CPR |
| Q07 | varchar |  |  | SI | CPR commenced by |
| Q08 | date |  |  | SI | Date |
| Q09 | time |  |  | SI | Time |
| Q10 | varchar |  |  | SI | Intubation by  |
| Q100 | varchar |  |  | SI | Additional persons present |
| Q101 | varchar |  |  | SI | Medical Emergency Team Evaluation |
| Q102 | varchar |  |  | SI | All necessary personnel attended? |
| Q103 | varchar |  |  | SI | One person assumed team leader role? |
| Q104 | varchar |  |  | SI | All equipment functioned properly? |
| Q105 | varchar |  |  | SI | Doctor identified to notify family of event? |
| Q106 | varchar |  |  | SI | If family present, staff member assigned to provid... |
| Q107 | varchar |  |  | SI | Evaluation notes |
| Q108 | varchar |  |  | SI | Scribe |
| Q109 | date |  |  | SI | Date |
| Q11 | date |  |  | SI | Date |
| Q110 | longvarbinary |  |  | SI | Signature |
| Q110UDt | date |  |  | SI | Signature Last Updated Date |
| Q110UTm | time |  |  | SI | Signature Last Updated Time |
| Q111 | varchar |  |  | SI | Designation |
| Q112 | varchar |  |  | SI | Primary Survey |
| Q113 | varchar |  |  | SI | Defibrillation |
| Q114 | date |  |  | SI | Date |
| Q115 | time |  |  | SI | Time |
| Q116 | numeric |  |  | SI | Tube size (mm) |
| Q117 | date |  |  | SI | Date |
| Q118 | time |  |  | SI | Time |
| Q119 | varchar |  |  | SI | Monitoring in place at onset of event |
| Q12 | time |  |  | SI | Time |
| Q13 | numeric |  |  | SI | Tube size (mm) |
| Q14 | varchar |  |  | SI | Staff present at arrest |
| Q15 | varchar |  |  | SI | Staff present at arrest 2 |
| Q16 | varchar |  |  | SI | Staff present at arrest 3 |
| Q17 | varchar |  |  | SI | Staff present at arrest 4 |
| Q19 | varchar |  |  | SI | Procedures |
| Q20 | varchar |  |  | SI | Resuscitation notes |
| Q21 | varchar |  |  | SI | Resuscitation stopped by |
| Q22 | date |  |  | SI | Resuscitation ceased date |
| Q23 | time |  |  | SI | Resuscitation ceased time |
| Q24 | varchar |  |  | SI | Family notified |
| Q39 | varchar |  |  | SI | Resuscitation result |
| Q40 | varchar |  |  | SI | Hospital-wide resuscitation response activated? |
| Q41 | date |  |  | SI | Date |
| Q42 | time |  |  | SI | Time |
| Q43 | varchar |  |  | SI | Hospital / Facility |
| Q44 | varchar |  |  | SI | Location details |
| Q45 | varchar |  |  | SI | Type of event |
| Q46 | varchar |  |  | SI | Other event |
| Q47 | varchar |  |  | SI | Witness details |
| Q48 | varchar |  |  | SI | Main illness category |
| Q49 | varchar |  |  | SI | Other illness category |
| Q50 | varchar |  |  | SI | Visiting medical officer notified |
| Q51 | varchar |  |  | SI | Coroners |
| Q52 | varchar |  |  | SI | Transferred |
| Q53 | varchar |  |  | SI | To |
| Q54 | varchar |  |  | SI | Pulse at onset of event |
| Q55 | date |  |  | SI | Date |
| Q56 | time |  |  | SI | Time |
| Q57 | varchar |  |  | SI | Care Provider 1 |
| Q58 | varchar |  |  | SI | Care Provider 2 |
| Q59 | date |  |  | SI | Date |
| Q60 | date |  |  | SI | Date |
| Q61 | longvarbinary |  |  | SI | Signature |
| Q61UDt | date |  |  | SI | Signature Last Updated Date |
| Q61UTm | time |  |  | SI | Signature Last Updated Time |
| Q62 | longvarbinary |  |  | SI | Signature |
| Q62UDt | date |  |  | SI | Signature Last Updated Date |
| Q62UTm | time |  |  | SI | Signature Last Updated Time |
| Q63 | varchar |  |  | SI | Designation |
| Q64 | varchar |  |  | SI | Designation |
| Q65 | varchar |  |  | SI | Patient monitored |
| Q66 | varchar |  |  | SI | Monitoring in place at onset of event |
| Q67 | varchar |  |  | SI | Conscious at onset of event |
| Q68 | varchar |  |  | SI | Breathing at onset of event |
| Q69 | varchar |  |  | SI | Condition when need for chest compressions / defib... |
| Q70 | varchar |  |  | SI | Initial rhythm |
| Q71 | varchar |  |  | SI | Other rhythm |
| Q72 | varchar |  |  | SI | First documented pulseless rhythm |
| Q73 | varchar |  |  | SI | Interventions already in place |
| Q74 | varchar |  |  | SI | Other interventions in place |
| Q75 | varchar |  |  | SI | Resuscitation attempted |
| Q76 | varchar |  |  | SI | Resuscitation intervention summary |
| Q77 | varchar |  |  | SI | Reason for not commencing resuscitation |
| Q78 | varchar |  |  | SI | Compressions |
| Q79 | varchar |  |  | SI | Compression method used |
| Q80 | varchar |  |  | SI | Other compression method used |
| Q81 | varchar |  |  | SI | CPR performance monitored or guidance used |
| Q82 | varchar |  |  | SI | Other monitor / guidance method |
| Q83 | varchar |  |  | SI | Defibrillator application |
| Q84 | date |  |  | SI | Date applied |
| Q85 | time |  |  | SI | Time applied |
| Q86 | varchar |  |  | SI | Defibrillation given |
| Q88 | varchar |  |  | SI | Airway and Ventilation |
| Q89 | date |  |  | SI | First assisted ventilation |
| Q90 | time |  |  | SI | Time of first assisted ventilation |
| Q91 | varchar |  |  | SI | Ventilation method |
| Q92 | varchar |  |  | SI | Other ventilation |
| Q93 | varchar |  |  | SI | Invasive airway |
| Q94 | varchar |  |  | SI | Airway patency confirmed with |
| Q95 | varchar |  |  | SI | Additional Details |
| Q96 | varchar |  |  | SI | Resuscitation outcome |
| Q97 | varchar |  |  | SI | Transfer status |
| Q98 | varchar |  |  | SI | Other transfer location |
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