# SQLUser.OEC_ActivityType

**Schema:** SQLUser
**Columnas:** 133
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACTIV_RowId | bigint | PK |  | NO | - |
| ACTIV_Code | varchar |  |  | NO | Code |
| ACTIV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACTIV_CreatedDate | date |  |  | SI | Created Date |
| ACTIV_CreatedTime | time |  |  | SI | Created Time |
| ACTIV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACTIV_DateFrom | date |  |  | SI | Date From |
| ACTIV_DateTo | date |  |  | SI | Date To |
| ACTIV_Desc | varchar |  |  | NO | Description |
| ACTIV_Owner | varchar |  |  | SI | Owner |
| ACTIV_UpdatedDate | date |  |  | SI | Updated Date |
| ACTIV_UpdatedTime | time |  |  | SI | Updated Time |
| ACTIV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Lethal congenital anomaly |
| Q01ObsDR | - |  |  | SI | Lethal congenital anomaly DR |
| Q02 | - |  |  | SI | Infection - chronic |
| Q02ObsDR | - |  |  | SI | Infection - chronic DR |
| Q03 | - |  |  | SI | Infection - acute |
| Q03ObsDR | - |  |  | SI | Infection - acute DR |
| Q04 | - |  |  | SI | Non-immune hydrops fetalis |
| Q04ObsDR | - |  |  | SI | Non-immune hydrops fetalis DR |
| Q05 | - |  |  | SI | Rhesus isoimmunisation |
| Q05ObsDR | - |  |  | SI | Rhesus isoimmunisation DR |
| Q06 | - |  |  | SI | Fetomaternal haemorrhage |
| Q06ObsDR | - |  |  | SI | Fetomaternal haemorrhage DR |
| Q07 | - |  |  | SI | Twin-twin transfusion |
| Q07ObsDR | - |  |  | SI | Twin-twin transfusion DR |
| Q08 | - |  |  | SI | Fetal growth restriction |
| Q08ObsDR | - |  |  | SI | Fetal growth restriction DR |
| Q09 | - |  |  | SI | Prolapse |
| Q09ObsDR | - |  |  | SI | Prolapse DR |
| Q10 | - |  |  | SI | Constricting loop or knot |
| Q10ObsDR | - |  |  | SI | Constricting loop or knot DR |
| Q11 | - |  |  | SI | Velamentous insertion |
| Q11ObsDR | - |  |  | SI | Velamentous insertion DR |
| Q12 | - |  |  | SI | Abruption |
| Q12ObsDR | - |  |  | SI | Abruption DR |
| Q13 | - |  |  | SI | Praevia |
| Q13ObsDR | - |  |  | SI | Praevia DR |
| Q14 | - |  |  | SI | Vasa praevia |
| Q14ObsDR | - |  |  | SI | Vasa praevia DR |
| Q15 | - |  |  | SI | Chorioamnionitis |
| Q15ObsDR | - |  |  | SI | Chorioamnionitis DR |
| Q16 | - |  |  | SI | Oligohydramnios |
| Q16ObsDR | - |  |  | SI | Oligohydramnios DR |
| Q17 | - |  |  | SI | Polyhydramnios |
| Q17ObsDR | - |  |  | SI | Polyhydramnios DR |
| Q18 | - |  |  | SI | Rupture |
| Q18ObsDR | - |  |  | SI | Rupture DR |
| Q19 | - |  |  | SI | Uterine anomalies |
| Q19ObsDR | - |  |  | SI | Uterine anomalies DR |
| Q20 | - |  |  | SI | Diabetes |
| Q20ObsDR | - |  |  | SI | Diabetes DR |
| Q21 | - |  |  | SI | Thyroid disease |
| Q21ObsDR | - |  |  | SI | Thyroid disease DR |
| Q22 | - |  |  | SI | Essential hypertension |
| Q22ObsDR | - |  |  | SI | Essential hypertension DR |
| Q23 | - |  |  | SI | Hypertensive disease in pregnancy |
| Q23ObsDR | - |  |  | SI | Hypertensive disease in pregnancy DR |
| Q24 | - |  |  | SI | Lupus or antiphospholipid syndrome |
| Q24ObsDR | - |  |  | SI | Lupus or antiphospholipid syndrome DR |
| Q25 | - |  |  | SI | Cholestasis |
| Q25ObsDR | - |  |  | SI | Cholestasis DR |
| Q26 | - |  |  | SI | Drug misuse |
| Q26ObsDR | - |  |  | SI | Drug misuse DR |
| Q27 | - |  |  | SI | Asphyxia |
| Q27ObsDR | - |  |  | SI | Asphyxia DR |
| Q28 | - |  |  | SI | Birth trauma |
| Q28ObsDR | - |  |  | SI | Birth trauma DR |
| Q29 | - |  |  | SI | External trauma |
| Q29ObsDR | - |  |  | SI | External trauma DR |
| Q30 | - |  |  | SI | Latrogenic trauma |
| Q30ObsDR | - |  |  | SI | Latrogenic trauma DR |
| Q31 | - |  |  | SI | No relevant condition identified |
| Q31ObsDR | - |  |  | SI | No relevant condition identified DR |
| Q32 | - |  |  | SI | No information available |
| Q32ObsDR | - |  |  | SI | No information available DR |
| Q33 | - |  |  | SI | Comments |
| Q34 | - |  |  | SI | Termination under the abortion act |
| Q34ObsDR | - |  |  | SI | Termination under the abortion act DR |
| Q35 | - |  |  | SI | Breech presentation |
| Q35ObsDR | - |  |  | SI | Breech presentation DR |
| Q36 | - |  |  | SI | Abdominal surgery in pregnancy |
| Q36ObsDR | - |  |  | SI | Abdominal surgery in pregnancy DR |
| Q37 | - |  |  | SI | Chromosome results |
| Q38 | - |  |  | SI | Death before labour |
| Q38ObsDR | - |  |  | SI | Death before labour DR |
| Q39 | - |  |  | SI | Death during labour |
| Q39ObsDR | - |  |  | SI | Death during labour DR |
| Q40 | - |  |  | SI | Post mortem performed |
| Q40ObsDR | - |  |  | SI | Post mortem performed DR |
| Q41 | - |  |  | SI | Placental insufficiency |
| Q41ObsDR | - |  |  | SI | Placental insufficiency DR |
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