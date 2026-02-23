# SQLUser.PAC_ContractSpokIdentifier

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CSI_RowId | bigint | PK |  | NO | - |
| CSI_Code | varchar |  |  | NO | Code |
| CSI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CSI_CreatedDate | date |  |  | SI | Created Date |
| CSI_CreatedTime | time |  |  | SI | Created Time |
| CSI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CSI_DateFrom | date |  |  | SI | Date From |
| CSI_DateTo | date |  |  | SI | Date To |
| CSI_Default | varchar |  |  | SI | Default |
| CSI_Desc | varchar |  |  | NO | Description |
| CSI_NationCode | varchar |  |  | SI | National Code |
| CSI_Owner | varchar |  |  | SI | Owner |
| CSI_UpdatedDate | date |  |  | SI | Updated Date |
| CSI_UpdatedTime | time |  |  | SI | Updated Time |
| CSI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Procedure |
| Q02 | - |  |  | SI | Number of oocytes recieved |
| Q03 | - |  |  | SI | Catheter type |
| Q03A | - |  |  | SI | Other catheter type |
| Q04 | - |  |  | SI | Uterine length (cm) |
| Q05 | - |  |  | SI | Embryo transfer |
| Q06 | - |  |  | SI | Uterus position |
| Q07 | - |  |  | SI | Ultrasound guided |
| Q07ObsDR | - |  |  | SI | Ultrasound guided DR |
| Q08 | - |  |  | SI | Tenaculum used |
| Q09 | - |  |  | SI | Sedation |
| Q09ObsDR | - |  |  | SI | Sedation DR |
| Q10 | - |  |  | SI | Uterine sound used |
| Q11 | - |  |  | SI | Cervical dilatation |
| Q12 | - |  |  | SI | Pain reaction |
| Q13 | - |  |  | SI | Cell stage |
| Q14 | - |  |  | SI | Embryo grade |
| Q15 | - |  |  | SI | Number of embryos transfered |
| Q16 | - |  |  | SI | Number of embryos cryopreserved |
| Q17 | - |  |  | SI | Comments |
| Q19 | - |  |  | SI | Date |
| Q20 | - |  |  | SI | Time |
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