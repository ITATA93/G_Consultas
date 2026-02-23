# SQLUser.MRC_ReviewOfSystem

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REV_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | 1. Vestirse, incluyendo amararse los zapatos y abr... |
| Q02 | - |  |  | SI | 2. Acostarse y levantarse de la cama |
| Q03 | - |  |  | SI | 3. Levantar hasta su boca una taza o vaso lleno |
| Q04 | - |  |  | SI | 4. Caminar al aire libre en terreno plano |
| Q05 | - |  |  | SI | 5. Bañarse y secarse todo el cuerpo |
| Q06 | - |  |  | SI | 6. Agacharse para recoger la ropa del piso |
| Q07 | - |  |  | SI | 7. Abrir y cerrar las llaves del agua |
| Q08 | - |  |  | SI | 8. Subir y bajar del auto, el colectivo, el bus o ... |
| Q09 | - |  |  | SI | 9. Recibir un recado o mensaje y entregarlo a otra... |
| Q10 | - |  |  | SI | 10. Salir de la casa y comprar en un almacén o neg... |
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
| REV_Code | varchar |  |  | SI | Code |
| REV_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| REV_CreatedDate | date |  |  | SI | Created Date |
| REV_CreatedTime | time |  |  | SI | Created Time |
| REV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REV_DateFrom | date |  |  | SI | Date From |
| REV_DateTo | date |  |  | SI | Date To |
| REV_Desc | varchar |  |  | SI | Description |
| REV_Owner | varchar |  |  | SI | Owner |
| REV_UpdatedDate | date |  |  | SI | Updated Date |
| REV_UpdatedTime | time |  |  | SI | Updated Time |
| REV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*