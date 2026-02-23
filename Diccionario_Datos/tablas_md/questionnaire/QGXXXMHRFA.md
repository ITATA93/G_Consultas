# questionnaire.QGXXXMHRFA

> Obstetric Hemorrhage Risk Factor Assessment

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Obstetric Hemorrhage Risk Factor Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | No previous uterine incision |
| Q04 | varchar |  |  | SI | Singleton pregnancy |
| Q05 | varchar |  |  | SI | ≤4 vaginal births |
| Q06 | varchar |  |  | SI | No known bleeding disorder |
| Q07 | varchar |  |  | SI | No history of post-partum haemorrhage |
| Q08 | varchar |  |  | SI | Prior cesarean(s) or uterine surgery |
| Q09 | varchar |  |  | SI | Multiple gestation |
| Q10 | varchar |  |  | SI | > 4 Vaginal births |
| Q11 | varchar |  |  | SI | Chorioamnionitis |
| Q12 | varchar |  |  | SI | History of previous postpartum haemorrhage |
| Q13 | varchar |  |  | SI | Large uterine fibroids |
| Q14 | varchar |  |  | SI | Platelets 50 to 100 x 10<sup>9</sup>/L |
| Q15 | varchar |  |  | SI | Haematocrit &lt;30% (Hb &lt;10 g/dL) |
| Q16 | varchar |  |  | SI | Polyhydramnios |
| Q17 | varchar |  |  | SI | Gestational age &lt;37 weeks or &gt;41 weeks |
| Q18 | varchar |  |  | SI | Preeclampsia |
| Q19 | varchar |  |  | SI | Prolonged labor / Induction |
| Q20 | varchar |  |  | SI | Placenta previa, low lying |
| Q21 | varchar |  |  | SI | Suspected / known placenta accreta spectrum |
| Q22 | varchar |  |  | SI | Abruption or active bleeding |
| Q23 | varchar |  |  | SI | Known coagulopathy |
| Q24 | varchar |  |  | SI | History of &gt;1 postpartum haemorrhage |
| Q25 | varchar |  |  | SI | HELLP syndrome |
| Q26 | varchar |  |  | SI | Platelets &lt;50 x 10<sup>9</sup>/L |
| Q27 | varchar |  |  | SI | Haematocrit &lt;24% (Hb &lt;8 g/dL) |
| Q28 | varchar |  |  | SI | Fetal demise |
| Q29 | varchar |  |  | SI | 2 or more medium risk factors |
| Q30 | varchar |  |  | SI | Tick the items and the corresponding risk accordin... |
| Q31 | varchar |  |  | SI | Low |
| Q32 | varchar |  |  | SI | MONITOR FOR HEMORRHAGE |
| Q33 | varchar |  |  | SI | Medium |
| Q34 | varchar |  |  | SI | NOTIFY CARE TEAM |
| Q35 | varchar |  |  | SI | High |
| Q36 | varchar |  |  | SI | NOTIFY CARE TEAM  |
| Q37 | varchar |  |  | SI | MOBILIZE RESOURCES |
| Q38 | varchar |  |  | SI | Score during pregnancy |
| Q39 | varchar |  |  | SI | Score during delivery |
| Q40 | varchar |  |  | SI | Score during post-partum |
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