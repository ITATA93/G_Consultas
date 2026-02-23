# questionnaire.QGXXXMPERMO

> Perinatal mortality - Obstetric

**Schema:** questionnaire
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perinatal mortality - Obstetric

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Lethal congenital anomaly |
| Q01ObsDR | varchar |  | FK | SI | Lethal congenital anomaly DR |
| Q02 | varchar |  |  | SI | Infection - chronic |
| Q02ObsDR | varchar |  | FK | SI | Infection - chronic DR |
| Q03 | varchar |  |  | SI | Infection - acute |
| Q03ObsDR | varchar |  | FK | SI | Infection - acute DR |
| Q04 | varchar |  |  | SI | Non-immune hydrops fetalis |
| Q04ObsDR | varchar |  | FK | SI | Non-immune hydrops fetalis DR |
| Q05 | varchar |  |  | SI | Rhesus isoimmunisation |
| Q05ObsDR | varchar |  | FK | SI | Rhesus isoimmunisation DR |
| Q06 | varchar |  |  | SI | Fetomaternal haemorrhage |
| Q06ObsDR | varchar |  | FK | SI | Fetomaternal haemorrhage DR |
| Q07 | varchar |  |  | SI | Twin-twin transfusion |
| Q07ObsDR | varchar |  | FK | SI | Twin-twin transfusion DR |
| Q08 | varchar |  |  | SI | Fetal growth restriction |
| Q08ObsDR | varchar |  | FK | SI | Fetal growth restriction DR |
| Q09 | varchar |  |  | SI | Prolapse |
| Q09ObsDR | varchar |  | FK | SI | Prolapse DR |
| Q10 | varchar |  |  | SI | Constricting loop or knot |
| Q10ObsDR | varchar |  | FK | SI | Constricting loop or knot DR |
| Q11 | varchar |  |  | SI | Velamentous insertion |
| Q11ObsDR | varchar |  | FK | SI | Velamentous insertion DR |
| Q12 | varchar |  |  | SI | Abruption |
| Q12ObsDR | varchar |  | FK | SI | Abruption DR |
| Q13 | varchar |  |  | SI | Praevia |
| Q13ObsDR | varchar |  | FK | SI | Praevia DR |
| Q14 | varchar |  |  | SI | Vasa praevia |
| Q14ObsDR | varchar |  | FK | SI | Vasa praevia DR |
| Q15 | varchar |  |  | SI | Chorioamnionitis |
| Q15ObsDR | varchar |  | FK | SI | Chorioamnionitis DR |
| Q16 | varchar |  |  | SI | Oligohydramnios |
| Q16ObsDR | varchar |  | FK | SI | Oligohydramnios DR |
| Q17 | varchar |  |  | SI | Polyhydramnios |
| Q17ObsDR | varchar |  | FK | SI | Polyhydramnios DR |
| Q18 | varchar |  |  | SI | Rupture |
| Q18ObsDR | varchar |  | FK | SI | Rupture DR |
| Q19 | varchar |  |  | SI | Uterine anomalies |
| Q19ObsDR | varchar |  | FK | SI | Uterine anomalies DR |
| Q20 | varchar |  |  | SI | Diabetes |
| Q20ObsDR | varchar |  | FK | SI | Diabetes DR |
| Q21 | varchar |  |  | SI | Thyroid disease |
| Q21ObsDR | varchar |  | FK | SI | Thyroid disease DR |
| Q22 | varchar |  |  | SI | Essential hypertension |
| Q22ObsDR | varchar |  | FK | SI | Essential hypertension DR |
| Q23 | varchar |  |  | SI | Hypertensive disease in pregnancy |
| Q23ObsDR | varchar |  | FK | SI | Hypertensive disease in pregnancy DR |
| Q24 | varchar |  |  | SI | Lupus or antiphospholipid syndrome |
| Q24ObsDR | varchar |  | FK | SI | Lupus or antiphospholipid syndrome DR |
| Q25 | varchar |  |  | SI | Cholestasis |
| Q25ObsDR | varchar |  | FK | SI | Cholestasis DR |
| Q26 | varchar |  |  | SI | Drug misuse |
| Q26ObsDR | varchar |  | FK | SI | Drug misuse DR |
| Q27 | varchar |  |  | SI | Asphyxia |
| Q27ObsDR | varchar |  | FK | SI | Asphyxia DR |
| Q28 | varchar |  |  | SI | Birth trauma |
| Q28ObsDR | varchar |  | FK | SI | Birth trauma DR |
| Q29 | varchar |  |  | SI | External trauma |
| Q29ObsDR | varchar |  | FK | SI | External trauma DR |
| Q30 | varchar |  |  | SI | Latrogenic trauma |
| Q30ObsDR | varchar |  | FK | SI | Latrogenic trauma DR |
| Q31 | varchar |  |  | SI | No relevant condition identified |
| Q31ObsDR | varchar |  | FK | SI | No relevant condition identified DR |
| Q32 | varchar |  |  | SI | No information available |
| Q32ObsDR | varchar |  | FK | SI | No information available DR |
| Q33 | varchar |  |  | SI | Comments |
| Q34 | varchar |  |  | SI | Termination under the abortion act |
| Q34ObsDR | varchar |  | FK | SI | Termination under the abortion act DR |
| Q35 | varchar |  |  | SI | Breech presentation |
| Q35ObsDR | varchar |  | FK | SI | Breech presentation DR |
| Q36 | varchar |  |  | SI | Abdominal surgery in pregnancy |
| Q36ObsDR | varchar |  | FK | SI | Abdominal surgery in pregnancy DR |
| Q37 | varchar |  |  | SI | Chromosome results |
| Q38 | varchar |  |  | SI | Death before labour |
| Q38ObsDR | varchar |  | FK | SI | Death before labour DR |
| Q39 | varchar |  |  | SI | Death during labour |
| Q39ObsDR | varchar |  | FK | SI | Death during labour DR |
| Q40 | varchar |  |  | SI | Post mortem performed |
| Q40ObsDR | varchar |  | FK | SI | Post mortem performed DR |
| Q41 | varchar |  |  | SI | Placental insufficiency |
| Q41ObsDR | varchar |  | FK | SI | Placental insufficiency DR |
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