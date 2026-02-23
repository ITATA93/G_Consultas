# SQLUser.ORC_DiathermyMethod

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIAMET_RowId | bigint | PK |  | NO | - |
| DIAMET_Code | varchar |  |  | NO | Code |
| DIAMET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DIAMET_CreatedDate | date |  |  | SI | Created Date |
| DIAMET_CreatedTime | time |  |  | SI | Created Time |
| DIAMET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DIAMET_DateFrom | date |  |  | SI | Date From |
| DIAMET_DateTo | date |  |  | SI | Date To |
| DIAMET_Desc | varchar |  |  | NO | Description |
| DIAMET_Owner | varchar |  |  | SI | Owner |
| DIAMET_UpdatedDate | date |  |  | SI | Updated Date |
| DIAMET_UpdatedTime | time |  |  | SI | Updated Time |
| DIAMET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Bundle compliance percentage |
| Q04 | - |  |  | SI | Has the patient been identified? |
| Q05 | - |  |  | SI | Has the correct indication of central venous acces... |
| Q06 | - |  |  | SI | Has the patient been informed about the indication... |
| Q07 | - |  |  | SI | Was hand hygiene performed according to protocol? |
| Q08 | - |  |  | SI | Have clean, non-sterile gloves been used? |
| Q09 | - |  |  | SI | Has the insertion site been examined for tendernes... |
| Q10 | - |  |  | SI | Has the old central venous catheter line dressing ... |
| Q11 | - |  |  | SI | Has the insertion site been visually inspected? |
| Q12 | - |  |  | SI | Has the sutureless securement device been removed ... |
| Q13 | - |  |  | SI | Has skin antisepsis been performed with 2% chlorhe... |
| Q14 | - |  |  | SI | Has the material needed for the new dressing been ... |
| Q15 | - |  |  | SI | Have sterile gloves been used, after hand hygiene ... |
| Q16 | - |  |  | SI | Has the new dressing: chlorexidine antiseptic pad ... |
| Q17 | - |  |  | SI | Has the sterile field being maintained for the dur... |
| Q18 | - |  |  | SI | Notes |
| Q19 | - |  |  | SI | 0 - 100 |
| Q20 | - |  |  | SI | Higher percentages represent higher compliance to ... |
| Q21 | - |  |  | SI | 0 - 100: Higher percentages represent higher compl... |
| Q22 | - |  |  | SI | CVCs are the leading cause of device-related bacte... |
| Q23 | - |  |  | SI | The aim of the Central venous catheter (CVC) care ... |
| Q24 | - |  |  | SI | Score |
| Q25 | - |  |  | SI | Classification |
| Q26 | - |  |  | SI | % |
| Q27 | - |  |  | SI | Has all the necessary material for the procedure b... |
| Q28 | - |  |  | SI | Has the correct indication of central venous acces... |
| Q29 | - |  |  | SI | Care Procedure |
| Q30 | - |  |  | SI | Flushing Procedure |
| Q31 | - |  |  | SI | Were clean non-sterile gloves used? |
| Q32 | - |  |  | SI | Has the infusion line been clamped and the needle-... |
| Q33 | - |  |  | SI | Has the connection cone been disinfected? |
| Q34 | - |  |  | SI | Has a new needle-free connector been applied and t... |
| Q35 | - |  |  | SI | Was the pulsatile flush performed with 10ml of sal... |
| Q36 | - |  |  | SI | Has the port protector been applied? |
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