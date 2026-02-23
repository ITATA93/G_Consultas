# SQLUser.PAC_DischargeDestinationKeyw

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ParRef | bigint | PK |  | NO | PAC_DischargeDestination Parent Reference |
| KEYW_Childsub | double |  |  | NO | Childsub |
| KEYW_Description | varchar |  |  | SI | Description |
| KEYW_RowId | varchar |  |  | NO | - |
| KEYW_Text | varchar |  |  | SI | Name |
| Q01 | - |  |  | SI | Child's ability to handle objects in important dai... |
| Q02 | - |  |  | SI | 1 - Handles objects easily and successfully. |
| Q03 | - |  |  | SI | At most, limitations in the ease of performing man... |
| Q04 | - |  |  | SI | 2 - Handles most objects but with somewhat reduced... |
| Q05 | - |  |  | SI | Certain activities may be avoided or be achieved w... |
| Q06 | - |  |  | SI | 3 - Handles objects with difficulty |
| Q07 | - |  |  | SI | The performance is slow and achieved with limited ... |
| Q08 | - |  |  | SI | 4 - Handles a limited selection of easily managed ... |
| Q09 | - |  |  | SI | Performs parts of activities with effort and with ... |
| Q10 | - |  |  | SI | 5 - Does not handle objects and has severely limit... |
| Q11 | - |  |  | SI | Requires total assistance. |
| Q12 | - |  |  | SI | Distinctions between Levels 1 and 2: |
| Q13 | - |  |  | SI | Children in Level 1 may have limitations in handli... |
| Q14 | - |  |  | SI | Limitations may also involve performance in new an... |
| Q15 | - |  |  | SI | Children in Level 2 perform almost the same activi... |
| Q16 | - |  |  | SI | Functional differences between hands can limit eff... |
| Q17 | - |  |  | SI | Children in Level 2 commonly try to simplify handl... |
| Q18 | - |  |  | SI | Distinctions between Levels 2 and 3: |
| Q19 | - |  |  | SI | Children in Level 2 handle most objects, although ... |
| Q20 | - |  |  | SI | Children in Level 3 commonly need help to prepare ... |
| Q21 | - |  |  | SI | They cannot perform certain activities and their d... |
| Q22 | - |  |  | SI | Distinction between Levels 3 and 4: |
| Q23 | - |  |  | SI | Children in Level 3 can perform selected activitie... |
| Q24 | - |  |  | SI | Children in Level 4 need continuous help during th... |
| Q25 | - |  |  | SI | Distinctions between Levels 4 and 5: |
| Q26 | - |  |  | SI | Children in Level 4 perform part of an activity, h... |
| Q27 | - |  |  | SI | Children in Level 5 might at best participate with... |
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