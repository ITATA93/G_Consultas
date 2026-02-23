# questionnaire.QTCBASFI

> BASFI

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(BASFI)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Putting on your socks or tights without help or ai... |
| Q02 | varchar |  |  | SI | Bending forward from the waist to pick up a pen fr... |
| Q03 | varchar |  |  | SI | Reaching up to a high shelf without help or aids (... |
| Q04 | varchar |  |  | SI | Getting up from an armless chair without using you... |
| Q05 | varchar |  |  | SI | Getting up off the floor without any help from lyi... |
| Q06 | varchar |  |  | SI | Standing unsupported for 10 minutes without discom... |
| Q07 | varchar |  |  | SI | Climbing 12-15 steps without using a handrail or w... |
| Q08 | varchar |  |  | SI | Looking over your shoulder without turning your bo... |
| Q09 | varchar |  |  | SI | Doing physically demanding activities (e.g. physio... |
| Q10 | varchar |  |  | SI | Doing a full day activities whether it be at home ... |
| Q11 | varchar |  |  | SI | 10 - High degree of functional limitation  / 0 - L... |
| Q12 | varchar |  |  | SI | A higher number is associated with a higher degree... |
| Q13 | varchar |  |  | SI | Indicate patient's ability with each of the activi... |
| Q14 | varchar |  |  | SI | BASFI (Bath Ankylosing Spondylitis Functional Inde... |
| Q15 | varchar |  |  | SI | Easy |
| Q16 | varchar |  |  | SI | Easy |
| Q17 | varchar |  |  | SI | Easy |
| Q18 | varchar |  |  | SI | Easy |
| Q19 | varchar |  |  | SI | Easy |
| Q20 | varchar |  |  | SI | Easy |
| Q21 | varchar |  |  | SI | Easy |
| Q22 | varchar |  |  | SI | Easy |
| Q23 | varchar |  |  | SI | Easy |
| Q24 | varchar |  |  | SI | Easy |
| Q25 | varchar |  |  | SI | Impossible |
| Q26 | varchar |  |  | SI | Impossible |
| Q27 | varchar |  |  | SI | Impossible |
| Q28 | varchar |  |  | SI | Impossible |
| Q29 | varchar |  |  | SI | Impossible |
| Q30 | varchar |  |  | SI | Impossible |
| Q31 | varchar |  |  | SI | Impossible |
| Q32 | varchar |  |  | SI | Impossible |
| Q33 | varchar |  |  | SI | Impossible |
| Q34 | varchar |  |  | SI | Impossible |
| Q35 | date |  |  | SI | Date |
| Q36 | time |  |  | SI | Time |
| Q37 | varchar |  |  | SI | Putting on your socks or tights without help or ai... |
| Q38 | varchar |  |  | SI | Bending forward from the waist to pick up a pen fr... |
| Q39 | varchar |  |  | SI | Reaching up to a high shelf without help or aids (... |
| Q40 | varchar |  |  | SI | Getting up from an armless chair without using you... |
| Q41 | varchar |  |  | SI | Getting up off the floor without any help from lyi... |
| Q42 | varchar |  |  | SI | Standing unsupported for 10 minutes without discom... |
| Q43 | varchar |  |  | SI | Climbing 12-15 steps without using a handrail or w... |
| Q44 | varchar |  |  | SI | Looking over your shoulder without turning your bo... |
| Q45 | varchar |  |  | SI | Doing physically demanding activities (e.g. physio... |
| Q46 | varchar |  |  | SI | Doing a full day activities whether it be at home ... |
| Q47 | varchar |  |  | SI | Please answer the following questions where 0= Eas... |
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