# questionnaire.QTCRSPP

> Record of Sedation for Procedure - Paediatrics

**Schema:** questionnaire
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Record of Sedation for Procedure - Paediatrics

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Procedure to be performed |
| Q02 | varchar |  |  | SI | Clinician performing procedure |
| Q03 | varchar |  |  | SI | Assisting clinician |
| Q04 | date |  |  | SI | Date |
| Q05 | time |  |  | SI | Time |
| Q06 | varchar |  |  | SI | Sedation Agents |
| Q07 | varchar |  |  | SI | Agent(s) to be used |
| Q08 | varchar |  |  | SI | 2 staff required, 1 RN or medical staff member |
| Q09 | varchar |  |  | SI | Fasting: 2 hours solids and liquids |
| Q10 | varchar |  |  | SI | 6 hours solids 4 hours breast feed 2 hours clear f... |
| Q11 | varchar |  |  | SI | 2 staff required, 1 accredited |
| Q12 | varchar |  |  | SI | 2 hours solids |
| Q13 | varchar |  |  | SI | 2 hours breast feed |
| Q14 | varchar |  |  | SI | 2 hours clear fluids |
| Q15 | varchar |  |  | SI | Risk Assessment and Exclusion Criteria for Nitrous... |
| Q16 | varchar |  |  | SI | Prior adverse event |
| Q17 | varchar |  |  | SI | Prior allergic reaction |
| Q18 | varchar |  |  | SI | Significant liver disease / failure |
| Q19 | varchar |  |  | SI | Acute systemic infection |
| Q20 | varchar |  |  | SI | Significant cardiovascular impairment |
| Q21 | varchar |  |  | SI | Immunosuppression |
| Q22 | varchar |  |  | SI | Abnormal conscious state / risk of raised ICP |
| Q23 | varchar |  |  | SI | Significant respiratory disease |
| Q24 | varchar |  |  | SI | Patient receiving opioids or other sedative agents |
| Q25 | varchar |  |  | SI | Age less than or equal to 6 months(for oral agents... |
| Q26 | varchar |  |  | SI | Age less than or equal to 2 years(for nitrous oxid... |
| Q27 | varchar |  |  | SI | Lung cyst |
| Q28 | varchar |  |  | SI | Bowel obstruction |
| Q29 | varchar |  |  | SI | Middle ear disease |
| Q30 | varchar |  |  | SI | Pneumothorax |
| Q31 | varchar |  |  | SI | Recent retinal surgery |
| Q32 | varchar |  |  | SI | If YES answered to any of the above criteria, DO N... |
| Q33 | varchar |  |  | SI | Sedation handout discussed with patient / parent |
| Q34 | varchar |  |  | SI | Informed consent obtained |
| Q35 | varchar |  |  | SI | Indications and possible adverse events discussed |
| Q36 | varchar |  |  | SI | Adequate staff available(minimum of 2 division 1 a... |
| Q37 | varchar |  |  | SI | Baseline observations recorded |
| Q38 | varchar |  |  | SI | Positive patient identification name bands in situ... |
| Q39 | varchar |  |  | SI | Patient fasted as per fasting requirement times |
| Q40 | varchar |  |  | SI | Private area available / treatment area |
| Q41 | varchar |  |  | SI | Suction functioning and connected to wall |
| Q42 | varchar |  |  | SI | Oxygen continuous / wall mounted supply |
| Q43 | varchar |  |  | SI | Pulse oximetry machine |
| Q44 | varchar |  |  | SI | Appropriate sized face masks/bag present |
| Q45 | varchar |  |  | SI | Resuscitation trolley located and available |
| Q46 | varchar |  |  | SI | Minimum staff present / available |
| Q47 | varchar |  |  | SI | Disposable nitrous oxide circuit and nitrous cylin... |
| Q48 | varchar |  |  | SI | Scavenger system attached to circuit |
| Q49 | varchar |  |  | SI | Portable emergency phone in treatment room |
| Q50 | varchar |  |  | SI | Emergency sedation pack / reversal drugs present |
| Q51 | varchar |  |  | SI | Stethoscope and thermometer available |
| Q52 | varchar |  |  | SI | Drugs ordered on medication chart |
| Q53 | varchar |  |  | SI | Line of sight medical / nursing provided constantl... |
| Q54 | varchar |  |  | SI | Observations / Sedation score documented every 5 m... |
| Q55 | varchar |  |  | SI | Delivered 100% oxygen for 5 minutes |
| Q56 | varchar |  |  | SI | Patient returned to baseline sedation score |
| Q57 | varchar |  |  | SI | Observations within normal limits |
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