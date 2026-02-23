# questionnaire.QTCCDP

> Cardiac Disease in Pregnancy - Labour / Birth Care Plan

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiac Disease in Pregnancy - Labour / Birth Care Plan

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Level of care for birth |
| Q04 | varchar |  |  | SI | Transfer location |
| Q05 | varchar |  |  | SI | Planned gestation at transfer |
| Q06 | numeric |  |  | SI | Planned gestation at transfer |
| Q07 | numeric |  |  | SI | Planned gestation at transfer (days) |
| Q08 | varchar |  |  | SI | weeks |
| Q09 | varchar |  |  | SI | days |
| Q10 | varchar |  |  | SI | Planned method of birth |
| Q11 | varchar |  |  | SI | Planned onset of labour |
| Q12 | numeric |  |  | SI | Recommended Prostaglandin E2 dose for induction of... |
| Q13 | varchar |  |  | SI | Planned onset of labour notes |
| Q14 | varchar |  |  | SI | Recommended intervention(s) and monitoring |
| Q15 | varchar |  |  | SI | Recommended anaesthetic technique |
| Q16 | varchar |  |  | SI | Recommendations for 1st stage |
| Q17 | varchar |  |  | SI | Special circumstances |
| Q18 | varchar |  |  | SI | Is patient on low molecular weight heparin |
| Q19 | varchar |  |  | SI | Inform ANAESTHETIST (epidural can be administered ... |
| Q20 | varchar |  |  | SI | Oxytocin augmentation |
| Q21 | varchar |  |  | SI | Preterm labour tocolysis notes |
| Q22 | varchar |  |  | SI | Preterm labour tocolysis |
| Q23 | varchar |  |  | SI | Oxytocin augmentation notes |
| Q24 | varchar |  |  | SI | Recommendations for 2nd stage |
| Q25 | numeric |  |  | SI | Assist if not birthed in |
| Q26 | varchar |  |  | SI | minutes |
| Q27 | varchar |  |  | SI | Recommendations for 3rd stage |
| Q28 | varchar |  |  | SI | Recommended oxytocin protocol |
| Q29 | varchar |  |  | SI | Oxytocin protocol notes |
| Q30 | varchar |  |  | SI | Special consideration(s) in post partum haemorrhag... |
| Q31 | varchar |  |  | SI | Recommendation(s) for post birth |
| Q32 | numeric |  |  | SI | LMWH duration |
| Q33 | varchar |  |  | SI | days for post birth |
| Q34 | numeric |  |  | SI | Postnatal stay for |
| Q35 | varchar |  |  | SI | days |
| Q36 | numeric |  |  | SI | Cardiac review required |
| Q37 | varchar |  |  | SI | weeks post-discharge |
| Q38 | varchar |  |  | SI | Contraceptive method notes |
| Q39 | varchar |  |  | SI | Notes |
| Q41 | varchar |  |  | SI | Onset of Labour |
| Q42 | varchar |  |  | SI | Intervention(s) and Monitoring |
| Q43 | varchar |  |  | SI | Anaesthesia |
| Q44 | varchar |  |  | SI | First Stage |
| Q45 | varchar |  |  | SI | Special Circumstances |
| Q46 | varchar |  |  | SI | Second Stage |
| Q47 | varchar |  |  | SI | Third Stage |
| Q48 | varchar |  |  | SI | Post Partum |
| Q49 | varchar |  |  | SI | Care provider(s) contributing to plan |
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