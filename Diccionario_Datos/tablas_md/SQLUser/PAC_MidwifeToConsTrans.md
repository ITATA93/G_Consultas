# SQLUser.PAC_MidwifeToConsTrans

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIDW_RowId | bigint | PK |  | NO | - |
| MIDW_Code | varchar |  |  | NO | Code |
| MIDW_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MIDW_CreatedDate | date |  |  | SI | Created Date |
| MIDW_CreatedTime | time |  |  | SI | Created Time |
| MIDW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MIDW_DateFrom | date |  |  | SI | Date From |
| MIDW_DateTo | date |  |  | SI | Date To |
| MIDW_Desc | varchar |  |  | NO | Description |
| MIDW_Owner | varchar |  |  | SI | Owner |
| MIDW_UpdatedDate | date |  |  | SI | Updated Date |
| MIDW_UpdatedTime | time |  |  | SI | Updated Time |
| MIDW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Assessment criteria |
| Q02 | - |  |  | SI | Sedation |
| Q03 | - |  |  | SI | Normal |
| Q04 | - |  |  | SI | Pain / Agitation |
| Q05 | - |  |  | SI | -2 |
| Q06 | - |  |  | SI | -1 |
| Q07 | - |  |  | SI | 0 |
| Q08 | - |  |  | SI | 1 |
| Q09 | - |  |  | SI | 2 |
| Q10 | - |  |  | SI | Crying irritability |
| Q11 | - |  |  | SI | Behavior state |
| Q12 | - |  |  | SI | Facial expression |
| Q13 | - |  |  | SI | Extremities tone |
| Q14 | - |  |  | SI | Vital signs: HR, RR, BP, SaO2 |
| Q15 | - |  |  | SI | Premature pain assessment |
| Q16 | - |  |  | SI | Every 8 hours, 30 minutes after each intervention ... |
| Q17 | - |  |  | SI | Sedation |
| Q18 | - |  |  | SI | Deeply |
| Q19 | - |  |  | SI | Lightly |
| Q20 | - |  |  | SI | Normal |
| Q21 | - |  |  | SI | Pain / Agitation |
| Q22 | - |  |  | SI | Mild |
| Q23 | - |  |  | SI | Severe |
| Q24 | - |  |  | SI | -10 to -6 |
| Q25 | - |  |  | SI | -5 to -2 |
| Q26 | - |  |  | SI | -1 to +3 |
| Q27 | - |  |  | SI | +4 to +7 |
| Q28 | - |  |  | SI | +8 to +10 |
| Q29 | - |  |  | SI | Consider reduction of sedative / analgesic therapy... |
| Q30 | - |  |  | SI | Nonpharmalogic intervention (non-nutritive sucking... |
| Q31 | - |  |  | SI | If after 2 interventions N-PASS still +4 to +7: in... |
| Q32 | - |  |  | SI | Initiation / escalation of sedative and/or analges... |
| Q33 | - |  |  | SI | Reduction of sedative analgesic therapy needed |
| Q34 | - |  |  | SI | Deeply: -10 to -6 |
| Q35 | - |  |  | SI | Lightly: -5 to -2 |
| Q36 | - |  |  | SI | Normal: -1 to +3 |
| Q37 | - |  |  | SI | Mild: +4 to +7 |
| Q38 | - |  |  | SI | Severe: +8 to +10 |
| Q39 | - |  |  | SI | N-PASS assessment for pain, agitation, and sedatio... |
| Q40 | - |  |  | SI | The N-PASS allows assessment of both sedation and ... |
| Q41 | - |  |  | SI | The 5 parameters of the N-PASS are crying / irrita... |
| Q42 | - |  |  | SI | Score |
| Q43 | - |  |  | SI | Classification |
| Q44 | - |  |  | SI | Date |
| Q45 | - |  |  | SI | Time |
| Q46 | - |  |  | SI | Sedation |
| Q47 | - |  |  | SI | Sedation |
| Q48 | - |  |  | SI | Sedation |
| Q49 | - |  |  | SI | Pain / Agitation |
| Q50 | - |  |  | SI | Pain / Agitation |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*