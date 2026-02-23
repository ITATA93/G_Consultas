# questionnaire.QGXXXMANI

> Intrapartum Assessment

**Schema:** questionnaire
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intrapartum Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Gestation: Weeks |
| Q01ObsDR | varchar |  | FK | SI | Gestation: Weeks DR |
| Q02 | varchar |  |  | SI | Reason for admission |
| Q03 | varchar |  |  | SI | Systolic BP |
| Q03ObsDR | varchar |  | FK | SI | Systolic BP DR |
| Q04 | varchar |  |  | SI | Diastolic BP |
| Q04ObsDR | varchar |  | FK | SI | Diastolic BP DR |
| Q05 | varchar |  |  | SI | Temperature |
| Q05ObsDR | varchar |  | FK | SI | Temperature DR |
| Q06 | varchar |  |  | SI | Pulse |
| Q06ObsDR | varchar |  | FK | SI | Pulse DR |
| Q07 | varchar |  |  | SI | Urinalysis |
| Q07ObsDR | varchar |  | FK | SI | Urinalysis DR |
| Q08 | varchar |  |  | SI | Urinalysis abnormalites |
| Q08ObsDR | varchar |  | FK | SI | Urinalysis abnormalites DR |
| Q09 | varchar |  |  | SI | Oedema |
| Q09ObsDR | varchar |  | FK | SI | Oedema DR |
| Q10 | varchar |  |  | SI | Fundal height |
| Q10ObsDR | varchar |  | FK | SI | Fundal height DR |
| Q11 | varchar |  |  | SI | Lie |
| Q11ObsDR | varchar |  | FK | SI | Lie DR |
| Q12 | varchar |  |  | SI | Presentation |
| Q12ObsDR | varchar |  | FK | SI | Presentation DR |
| Q13 | varchar |  |  | SI | Position |
| Q13ObsDR | varchar |  | FK | SI | Position DR |
| Q14 | varchar |  |  | SI | Presentation / 5ths palpable |
| Q14ObsDR | varchar |  | FK | SI | Presentation / 5ths palpable DR |
| Q15 | varchar |  |  | SI | Fetal heart rate |
| Q15ObsDR | varchar |  | FK | SI | Fetal heart rate DR |
| Q16 | varchar |  |  | SI | Fetal movement felt |
| Q16ObsDR | varchar |  | FK | SI | Fetal movement felt DR |
| Q17 | varchar |  |  | SI | Antenatal steroids given |
| Q17ObsDR | varchar |  | FK | SI | Antenatal steroids given DR |
| Q18 | varchar |  |  | SI | Fundal height |
| Q18ObsDR | varchar |  | FK | SI | Fundal height DR |
| Q19 | varchar |  |  | SI | IV cannula |
| Q19ObsDR | varchar |  | FK | SI | IV cannula DR |
| Q20 | varchar |  |  | SI | IV fluids prescribed |
| Q20ObsDR | varchar |  | FK | SI | IV fluids prescribed DR |
| Q21 | varchar |  |  | SI | IV cannula site check |
| Q21ObsDR | varchar |  | FK | SI | IV cannula site check DR |
| Q22 | varchar |  |  | SI | IV cannula flush |
| Q22ObsDR | varchar |  | FK | SI | IV cannula flush DR |
| Q23 | varchar |  |  | SI | IV cannula change (48hrs) |
| Q23ObsDR | varchar |  | FK | SI | IV cannula change (48hrs) DR |
| Q24 | varchar |  |  | SI | Antenatal steroids given |
| Q24ObsDR | varchar |  | FK | SI | Antenatal steroids given DR |
| Q25 | varchar |  |  | SI | Antenatal steroids 2nd dose given |
| Q25ObsDR | varchar |  | FK | SI | Antenatal steroids 2nd dose given DR |
| Q26 | varchar |  |  | SI | Medicines required |
| Q26ObsDR | varchar |  | FK | SI | Medicines required DR |
| Q27 | varchar |  |  | SI | Medicines prescribed |
| Q27ObsDR | varchar |  | FK | SI | Medicines prescribed DR |
| Q28 | varchar |  |  | SI | Prescribed medicines review |
| Q28ObsDR | varchar |  | FK | SI | Prescribed medicines review DR |
| Q29 | varchar |  |  | SI | PV loss |
| Q29ObsDR | varchar |  | FK | SI | PV loss DR |
| Q30 | varchar |  |  | SI | Bleeding |
| Q30ObsDR | varchar |  | FK | SI | Bleeding DR |
| Q31 | date |  |  | SI | SRM date |
| Q32 | time |  |  | SI | SRM time |
| Q33 | varchar |  |  | SI | SRM |
| Q33ObsDR | varchar |  | FK | SI | SRM DR |
| Q34 | varchar |  |  | SI | Liquor clear |
| Q34ObsDR | varchar |  | FK | SI | Liquor clear DR |
| Q35 | varchar |  |  | SI | Liquor blood stained |
| Q35ObsDR | varchar |  | FK | SI | Liquor blood stained DR |
| Q36 | varchar |  |  | SI | Liquor meconium stained |
| Q36ObsDR | varchar |  | FK | SI | Liquor meconium stained DR |
| Q37 | varchar |  |  | SI | Liquor odourless |
| Q37ObsDR | varchar |  | FK | SI | Liquor odourless DR |
| Q38 | varchar |  |  | SI | Plan of care |
| Q39 | varchar |  |  | SI | Midwife countersigning |
| Q41 | varchar |  |  | SI | Comments |
| Q42 | varchar |  |  | SI | Estimated blood loss |
| Q42ObsDR | varchar |  | FK | SI | Estimated blood loss DR |
| Q43 | varchar |  |  | SI | Gestation: Days |
| Q43ObsDR | varchar |  | FK | SI | Gestation: Days DR |
| Q44 | date |  |  | SI | Date |
| Q45 | time |  |  | SI | Time |
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