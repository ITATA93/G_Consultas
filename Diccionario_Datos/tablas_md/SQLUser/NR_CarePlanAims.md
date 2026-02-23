# SQLUser.NR_CarePlanAims

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AIM_ParRef | varchar | PK |  | NO | NR_CarePlan Parent Reference |
| AIM_Aims_DR | bigint |  | FK | SI | Des Ref MRCCareAim |
| AIM_Childsub | double |  |  | NO | Childsub |
| AIM_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | No previous uterine incision |
| Q04 | - |  |  | SI | Singleton pregnancy |
| Q05 | - |  |  | SI | ≤4 vaginal births |
| Q06 | - |  |  | SI | No known bleeding disorder |
| Q07 | - |  |  | SI | No history of post-partum haemorrhage |
| Q08 | - |  |  | SI | Prior cesarean(s) or uterine surgery |
| Q09 | - |  |  | SI | Multiple gestation |
| Q10 | - |  |  | SI | > 4 Vaginal births |
| Q11 | - |  |  | SI | Chorioamnionitis |
| Q12 | - |  |  | SI | History of previous postpartum haemorrhage |
| Q13 | - |  |  | SI | Large uterine fibroids |
| Q14 | - |  |  | SI | Platelets 50 to 100 x 10<sup>9</sup>/L |
| Q15 | - |  |  | SI | Haematocrit &lt |
| Q16 | - |  |  | SI | Polyhydramnios |
| Q17 | - |  |  | SI | Gestational age &lt |
| Q18 | - |  |  | SI | Preeclampsia |
| Q19 | - |  |  | SI | Prolonged labor / Induction |
| Q20 | - |  |  | SI | Placenta previa, low lying |
| Q21 | - |  |  | SI | Suspected / known placenta accreta spectrum |
| Q22 | - |  |  | SI | Abruption or active bleeding |
| Q23 | - |  |  | SI | Known coagulopathy |
| Q24 | - |  |  | SI | History of &gt |
| Q25 | - |  |  | SI | HELLP syndrome |
| Q26 | - |  |  | SI | Platelets &lt |
| Q27 | - |  |  | SI | Haematocrit &lt |
| Q28 | - |  |  | SI | Fetal demise |
| Q29 | - |  |  | SI | 2 or more medium risk factors |
| Q30 | - |  |  | SI | Tick the items and the corresponding risk accordin... |
| Q31 | - |  |  | SI | Low |
| Q32 | - |  |  | SI | MONITOR FOR HEMORRHAGE |
| Q33 | - |  |  | SI | Medium |
| Q34 | - |  |  | SI | NOTIFY CARE TEAM |
| Q35 | - |  |  | SI | High |
| Q36 | - |  |  | SI | NOTIFY CARE TEAM |
| Q37 | - |  |  | SI | MOBILIZE RESOURCES |
| Q38 | - |  |  | SI | Score during pregnancy |
| Q39 | - |  |  | SI | Score during delivery |
| Q40 | - |  |  | SI | Score during post-partum |
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