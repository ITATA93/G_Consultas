# questionnaire.QTCNPASS

> Neonatal Pain, Agitation and Sedation Scale

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neonatal Pain, Agitation and Sedation Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Assessment criteria |
| Q02 | varchar |  |  | SI | Sedation |
| Q03 | varchar |  |  | SI | Normal |
| Q04 | varchar |  |  | SI | Pain / Agitation |
| Q05 | varchar |  |  | SI | -2 |
| Q06 | varchar |  |  | SI | -1 |
| Q07 | varchar |  |  | SI | 0 |
| Q08 | varchar |  |  | SI | 1 |
| Q09 | varchar |  |  | SI | 2 |
| Q10 | varchar |  |  | SI | Crying irritability |
| Q11 | varchar |  |  | SI | Behavior state |
| Q12 | varchar |  |  | SI | Facial expression |
| Q13 | varchar |  |  | SI | Extremities tone |
| Q14 | varchar |  |  | SI | Vital signs: HR, RR, BP, SaO2 |
| Q15 | varchar |  |  | SI | Premature pain assessment |
| Q16 | varchar |  |  | SI | Every 8 hours, 30 minutes after each intervention ... |
| Q17 | varchar |  |  | SI | Sedation |
| Q18 | varchar |  |  | SI | Deeply |
| Q19 | varchar |  |  | SI | Lightly |
| Q20 | varchar |  |  | SI | Normal |
| Q21 | varchar |  |  | SI | Pain / Agitation |
| Q22 | varchar |  |  | SI | Mild |
| Q23 | varchar |  |  | SI | Severe |
| Q24 | varchar |  |  | SI | -10 to -6 |
| Q25 | varchar |  |  | SI | -5 to -2 |
| Q26 | varchar |  |  | SI | -1 to +3 |
| Q27 | varchar |  |  | SI | +4 to +7 |
| Q28 | varchar |  |  | SI | +8 to +10 |
| Q29 | varchar |  |  | SI | Consider reduction of sedative / analgesic therapy... |
| Q30 | varchar |  |  | SI | Nonpharmalogic intervention (non-nutritive sucking... |
| Q31 | varchar |  |  | SI | If after 2 interventions N-PASS still +4 to +7: in... |
| Q32 | varchar |  |  | SI | Initiation / escalation of sedative and/or analges... |
| Q33 | varchar |  |  | SI | Reduction of sedative analgesic therapy needed |
| Q34 | varchar |  |  | SI | Deeply: -10 to -6 |
| Q35 | varchar |  |  | SI | Lightly: -5 to -2 |
| Q36 | varchar |  |  | SI | Normal: -1 to +3 |
| Q37 | varchar |  |  | SI | Mild: +4 to +7 |
| Q38 | varchar |  |  | SI | Severe: +8 to +10 |
| Q39 | varchar |  |  | SI | N-PASS assessment for pain, agitation, and sedatio... |
| Q40 | varchar |  |  | SI | The N-PASS allows assessment of both sedation and ... |
| Q41 | varchar |  |  | SI | The 5 parameters of the N-PASS are crying / irrita... |
| Q42 | varchar |  |  | SI | Score |
| Q43 | varchar |  |  | SI | Classification |
| Q44 | date |  |  | SI | Date |
| Q45 | time |  |  | SI | Time |
| Q46 | varchar |  |  | SI | Sedation |
| Q47 | varchar |  |  | SI | Sedation |
| Q48 | varchar |  |  | SI | Sedation |
| Q49 | varchar |  |  | SI | Pain / Agitation |
| Q50 | varchar |  |  | SI | Pain / Agitation |
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