# SQLUser.PAC_FundingArrangement

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FUNDAR_RowId | bigint | PK |  | NO | - |
| FUNDAR_AdmSource | varchar |  |  | SI | AdmSource |
| FUNDAR_Code | varchar |  |  | SI | Code |
| FUNDAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FUNDAR_ContractRole | varchar |  |  | SI | ContractRole |
| FUNDAR_ContractType | varchar |  |  | SI | ContractType |
| FUNDAR_CreatedDate | date |  |  | SI | Created Date |
| FUNDAR_CreatedTime | time |  |  | SI | Created Time |
| FUNDAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FUNDAR_DateFrom | date |  |  | SI | Date From |
| FUNDAR_DateTo | date |  |  | SI | Date To |
| FUNDAR_Default | varchar |  |  | SI | Default |
| FUNDAR_Desc | varchar |  |  | SI | Description |
| FUNDAR_DischDestin | varchar |  |  | SI | DischDestin |
| FUNDAR_NationCode | varchar |  |  | SI | National Code |
| FUNDAR_Owner | varchar |  |  | SI | Owner |
| FUNDAR_UpdatedDate | date |  |  | SI | Updated Date |
| FUNDAR_UpdatedTime | time |  |  | SI | Updated Time |
| FUNDAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Eliasson A, Ullenhag A, Wahlström U, Krumlinde‐Sun... |
| Q04 | - |  |  | SI | Dev Med Child Neurol 2017 |
| Q05 | - |  |  | SI | Mini-MACS levels of childrens self-initiated abili... |
| Q06 | - |  |  | SI | Instructions |
| Q07 | - |  |  | SI | I. Handles objects easily and successfully. |
| Q08 | - |  |  | SI | The child may have a slight limitation in performi... |
| Q09 | - |  |  | SI | The child may need somewhat more adult assistance ... |
| Q10 | - |  |  | SI | II. Handles most objects, but with somewhat reduce... |
| Q11 | - |  |  | SI | Some actions can only be performed and accomplishe... |
| Q12 | - |  |  | SI | The child needs adult assistance to handle objects... |
| Q13 | - |  |  | SI | III. Handles objects with difficulty. |
| Q14 | - |  |  | SI | Performance is slow, with limited variation and qu... |
| Q15 | - |  |  | SI | Easily managed objects are handled independently f... |
| Q16 | - |  |  | SI | The child often needs adult help and support to ha... |
| Q17 | - |  |  | SI | IV. handles a limited selection of easily managed ... |
| Q18 | - |  |  | SI | The actions are performed slowly, with exertion an... |
| Q19 | - |  |  | SI | The child needs constant adult help and support to... |
| Q20 | - |  |  | SI | V. Does not handle objects and has severely limite... |
| Q21 | - |  |  | SI | At best, the child can push, touch, press, or hold... |
| Q22 | - |  |  | SI | Distinctions between levels I and II |
| Q23 | - |  |  | SI | Children in level I may have slightly more difficu... |
| Q24 | - |  |  | SI | Children in level II handle essentially the same o... |
| Q25 | - |  |  | SI | Functional differences between hands may cause per... |
| Q26 | - |  |  | SI | They may need more guidance and practice to learn ... |
| Q27 | - |  |  | SI | Distinctions between levels II and III |
| Q28 | - |  |  | SI | Children in level II can handle most objects, thou... |
| Q29 | - |  |  | SI | Level III children manage to use easily handled ob... |
| Q30 | - |  |  | SI | They perform actions with few subcomponents. Perfo... |
| Q31 | - |  |  | SI | Distinctions between levels III and IV |
| Q32 | - |  |  | SI | Children in level III manage to use easily handled... |
| Q33 | - |  |  | SI | They perform actions with few subcomponents, and t... |
| Q34 | - |  |  | SI | At best, children in level IV can perform simple a... |
| Q35 | - |  |  | SI | They need constant help. |
| Q36 | - |  |  | SI | Distinctions between levels IV and V |
| Q37 | - |  |  | SI | Children in level IV perform individual actions wi... |
| Q38 | - |  |  | SI | At best, children in level V perform simple moveme... |
| Q39 | - |  |  | SI | For example, they can press a simple button or hol... |
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