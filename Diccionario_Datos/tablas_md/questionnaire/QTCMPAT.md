# questionnaire.QTCMPAT

> Modified Pain Assessment Tool (mPAT)

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Modified Pain Assessment Tool (mPAT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Posture / Tone	 |
| Q04 | varchar |  |  | SI | Cry |
| Q05 | varchar |  |  | SI | Sleep pattern |
| Q06 | varchar |  |  | SI | Expression |
| Q07 | varchar |  |  | SI | Color |
| Q08 | varchar |  |  | SI | Respirations |
| Q09 | varchar |  |  | SI | Heart rate |
| Q10 | varchar |  |  | SI | Oxygen saturation |
| Q11 | varchar |  |  | SI | Blood pressure |
| Q12 | varchar |  |  | SI | Nurse perception |
| Q13 | varchar |  |  | SI | Hodgkinson K, Bear M, Thorn J, Blaricum SV. Measur... |
| Q14 | varchar |  |  | SI | O’Sullivan AT, Rowley S, Ellis S, Faasse K, Petrie... |
| Q15 | varchar |  |  | SI | Clin J Pain 2016;32:51–57. |
| Q16 | varchar |  |  | SI | Comfort Measures |
| Q17 | varchar |  |  | SI | Gently repositioning the neonate to make him/her m... |
| Q18 | varchar |  |  | SI | Wrapping / containment of the infant to provide su... |
| Q19 | varchar |  |  | SI | Decreasing environmental stressors; reducing noise... |
| Q20 | varchar |  |  | SI | Tactile soothing; stroking the baby gently, suppor... |
| Q21 | varchar |  |  | SI | Talking softly to the baby. |
| Q22 | varchar |  |  | SI | Changing the baby's nappy. |
| Q23 | varchar |  |  | SI | Using a pacifier/dummy to provide non-nutritive su... |
| Q24 | varchar |  |  | SI | The mPAT is an observational scale designed to ass... |
| Q25 | varchar |  |  | SI | It is recommended that mPAT can be utilised for bo... |
| Q26 | varchar |  |  | SI | The mPAT scale focuses on behavioural and physiolo... |
| Q27 | varchar |  |  | SI | > 5 |
| Q28 | varchar |  |  | SI | > 10 |
| Q29 | varchar |  |  | SI | Recommend comfort measures such as soothing, use o... |
| Q30 | varchar |  |  | SI | Recommend analgesia |
| Q31 | varchar |  |  | SI | Dummy1 |
| Q32 | varchar |  |  | SI | Dummy2 |
| Q33 | varchar |  |  | SI | Dummy3 |
| Q34 | varchar |  |  | SI | Dummy4 |
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