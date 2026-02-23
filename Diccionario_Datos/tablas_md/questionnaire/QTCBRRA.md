# questionnaire.QTCBRRA

> Bed Rails Risk Assessment

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Bed Rails Risk Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Maintaining patient safety with use of bedrails ou... |
| Q02 | varchar |  |  | SI | Please state who the discussion / decision has bee... |
| Q03 | varchar |  |  | SI | Ensure patient information leaflet is given |
| Q04 | varchar |  |  | SI | State reason as to why bedrails are being used on ... |
| Q05 | varchar |  |  | SI | The use of bedrails will be reviewed on a daily ba... |
| Q06 | varchar |  |  | SI | Ensure the need for the use of bedrails is communi... |
| Q07 | varchar |  |  | SI | Please state the reason why the use of bedrails is... |
| Q08 | varchar |  |  | SI | Ensure that the appropriate use of bed rails is as... |
| Q09 | varchar |  |  | SI | Mental State |
| Q10 | varchar |  |  | SI | Patient is confused and disorientated |
| Q11 | varchar |  |  | SI | Patient is drowsy |
| Q12 | varchar |  |  | SI | Patient is orientated and alert |
| Q13 | varchar |  |  | SI | Patient is unconscious |
| Q14 | varchar |  |  | SI | Mobility |
| Q15 | varchar |  |  | SI | Patient is very immobile (bedfast or hoist depende... |
| Q16 | varchar |  |  | SI | Patient is neither independent nor immobile |
| Q17 | varchar |  |  | SI | Patient can mobilise without help from staff |
| Q18 | varchar |  |  | SI | Use bedrails with care |
| Q19 | varchar |  |  | SI | Bedrails NOT recommended (use low profile bed) |
| Q20 | varchar |  |  | SI | Bedrails NOT recommended (use low profile bed) |
| Q21 | varchar |  |  | SI | Bedrails recommended |
| Q22 | varchar |  |  | SI | Use bedrails with care |
| Q23 | varchar |  |  | SI | Bedrails NOT recommended |
| Q24 | varchar |  |  | SI | Bedrails recommended |
| Q25 | varchar |  |  | SI | Bedrails recommended |
| Q26 | varchar |  |  | SI | Bedrails recommended |
| Q27 | varchar |  |  | SI | Bedrails NOT recommended |
| Q28 | varchar |  |  | SI | Bedrails NOT recommended |
| Q29 | varchar |  |  | SI | N/A |
| Q30 | varchar |  |  | SI | N/A |
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