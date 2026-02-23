# questionnaire.QTCQDASH

> Quick Discapacidad de Brazo, Hombro y Mano (DASH)

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Quick Discapacidad de Brazo, Hombro y Mano (DASH)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Please rate your ability to do the following activ... |
| Q04 | varchar |  |  | SI | Open a tight or new jar |
| Q05 | varchar |  |  | SI | Do heavy household chores (e.g., wash walls, wash ... |
| Q06 | varchar |  |  | SI | Carry a shopping bag or briefcase |
| Q07 | varchar |  |  | SI | Wash your back |
| Q08 | varchar |  |  | SI | Use a knife to cut food |
| Q09 | varchar |  |  | SI | Recreational activities in which you take some for... |
| Q10 | varchar |  |  | SI | During the past week, to what extent has your arm,... |
| Q11 | varchar |  |  | SI | During the past week, were you limited in your wor... |
| Q12 | varchar |  |  | SI | Please rate the severity of the following symptoms... |
| Q13 | varchar |  |  | SI | Arm, shoulder or hand pain |
| Q14 | varchar |  |  | SI | Tingling (pins and needles) in your arm, shoulder ... |
| Q15 | varchar |  |  | SI | During the past week, how much difficulty have you... |
| Q16 | varchar |  |  | SI | Quick DASH Disability / Symptom Score |
| Q17 | varchar |  |  | SI | The following questions ask about the impact of yo... |
| Q18 | varchar |  |  | SI | Do you work? |
| Q19 | varchar |  |  | SI | Please indicate what your job / work is |
| Q20 | varchar |  |  | SI | Using your usual technique for your work? |
| Q21 | varchar |  |  | SI | Doing your usual work because of arm, shoulder or ... |
| Q22 | varchar |  |  | SI | Doing your work as well as you would like? |
| Q23 | varchar |  |  | SI | Spending your usual amount of time doing your work... |
| Q24 | varchar |  |  | SI | Work Module Score |
| Q25 | varchar |  |  | SI | The following questions relate to the impact of yo... |
| Q26 | varchar |  |  | SI | respect to that activity which is most important t... |
| Q27 | varchar |  |  | SI | Do you play one sport or instrument (or both) |
| Q28 | varchar |  |  | SI | Please indicate the sport or instrument which is m... |
| Q29 | varchar |  |  | SI | Using your usual technique for playing your instru... |
| Q30 | varchar |  |  | SI | Playing your musical instrument or sport because o... |
| Q31 | varchar |  |  | SI | Playing your musical instrument or sport as well a... |
| Q32 | varchar |  |  | SI | Spending your usual amount of time practicing or p... |
| Q33 | varchar |  |  | SI | Sport / Performing Art Module Score |
| Q34 | varchar |  |  | SI | The QUICK-DASH questionnaire expresses a value (in... |
| Q35 | varchar |  |  | SI | Score |
| Q36 | varchar |  |  | SI | Classification |
| Q37 | varchar |  |  | SI | 0 - 100 |
| Q38 | varchar |  |  | SI | Lower scores indicate better quality of life |
| Q39 | varchar |  |  | SI | 0 - 100: Lower scores indicate better quality of l... |
| Q40 | varchar |  |  | SI | This questionnaire asks about your symptoms as wel... |
| Q41 | varchar |  |  | SI | If you did not have the opportunity to perform an ... |
| Q42 | varchar |  |  | SI | It doesn't matter which hand or arm you use to per... |
| Q43 | varchar |  |  | SI | Work Module Score |
| Q44 | varchar |  |  | SI | Sport / Performing Art Module Score |
| Q45 | varchar |  |  | SI | Quick DASH Disability / Symptom Score Caption |
| Q46 | varchar |  |  | SI | Work Module Score Caption |
| Q47 | varchar |  |  | SI | Sport / Performing Art Module Score Caption |
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