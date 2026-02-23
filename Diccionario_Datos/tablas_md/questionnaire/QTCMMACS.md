# questionnaire.QTCMMACS

> Mini-Manual Ability Classification System (Mini-MACS)

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mini-Manual Ability Classification System (Mini-MACS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Eliasson A, Ullenhag A, Wahlström U, Krumlinde‐Sun... |
| Q04 | varchar |  |  | SI | Dev Med Child Neurol 2017;59:7278. |
| Q05 | varchar |  |  | SI | Mini-MACS levels of childrens self-initiated abili... |
| Q06 | varchar |  |  | SI | Instructions |
| Q07 | varchar |  |  | SI | I. Handles objects easily and successfully. |
| Q08 | varchar |  |  | SI | The child may have a slight limitation in performi... |
| Q09 | varchar |  |  | SI | The child may need somewhat more adult assistance ... |
| Q10 | varchar |  |  | SI | II. Handles most objects, but with somewhat reduce... |
| Q11 | varchar |  |  | SI | Some actions can only be performed and accomplishe... |
| Q12 | varchar |  |  | SI | The child needs adult assistance to handle objects... |
| Q13 | varchar |  |  | SI | III. Handles objects with difficulty. |
| Q14 | varchar |  |  | SI | Performance is slow, with limited variation and qu... |
| Q15 | varchar |  |  | SI | Easily managed objects are handled independently f... |
| Q16 | varchar |  |  | SI | The child often needs adult help and support to ha... |
| Q17 | varchar |  |  | SI | IV. handles a limited selection of easily managed ... |
| Q18 | varchar |  |  | SI | The actions are performed slowly, with exertion an... |
| Q19 | varchar |  |  | SI | The child needs constant adult help and support to... |
| Q20 | varchar |  |  | SI | V. Does not handle objects and has severely limite... |
| Q21 | varchar |  |  | SI | At best, the child can push, touch, press, or hold... |
| Q22 | varchar |  |  | SI | Distinctions between levels I and II |
| Q23 | varchar |  |  | SI | Children in level I may have slightly more difficu... |
| Q24 | varchar |  |  | SI | Children in level II handle essentially the same o... |
| Q25 | varchar |  |  | SI | Functional differences between hands may cause per... |
| Q26 | varchar |  |  | SI | They may need more guidance and practice to learn ... |
| Q27 | varchar |  |  | SI | Distinctions between levels II and III |
| Q28 | varchar |  |  | SI | Children in level II can handle most objects, thou... |
| Q29 | varchar |  |  | SI | Level III children manage to use easily handled ob... |
| Q30 | varchar |  |  | SI | They perform actions with few subcomponents. Perfo... |
| Q31 | varchar |  |  | SI | Distinctions between levels III and IV |
| Q32 | varchar |  |  | SI | Children in level III manage to use easily handled... |
| Q33 | varchar |  |  | SI | They perform actions with few subcomponents, and t... |
| Q34 | varchar |  |  | SI | At best, children in level IV can perform simple a... |
| Q35 | varchar |  |  | SI | They need constant help. |
| Q36 | varchar |  |  | SI | Distinctions between levels IV and V |
| Q37 | varchar |  |  | SI | Children in level IV perform individual actions wi... |
| Q38 | varchar |  |  | SI | At best, children in level V perform simple moveme... |
| Q39 | varchar |  |  | SI | For example, they can press a simple button or hol... |
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