# SQLUser.ARC_ActivityClaimStatus

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACTCLST_RowId | bigint | PK |  | NO | - |
| ACTCLST_Code | varchar |  |  | NO | Code |
| ACTCLST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACTCLST_CreatedDate | date |  |  | SI | Created Date |
| ACTCLST_CreatedTime | time |  |  | SI | Created Time |
| ACTCLST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACTCLST_DateFrom | date |  |  | SI | Date From |
| ACTCLST_DateTo | date |  |  | SI | Date To |
| ACTCLST_Desc | varchar |  |  | NO | Description |
| ACTCLST_Owner | varchar |  |  | SI | Owner |
| ACTCLST_UpdatedDate | date |  |  | SI | Updated Date |
| ACTCLST_UpdatedTime | time |  |  | SI | Updated Time |
| ACTCLST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ17DR | - |  |  | SI | Child Reference: Ropa del Paciente |
| Q01 | - |  |  | SI | Almohada |
| Q02 | - |  |  | SI | Jabón |
| Q03 | - |  |  | SI | Shampoo |
| Q04 | - |  |  | SI | Desodorante |
| Q05 | - |  |  | SI | Colonia |
| Q06 | - |  |  | SI | Crema |
| Q07 | - |  |  | SI | Cepillo de Dientes |
| Q08 | - |  |  | SI | Pasta de Dientes |
| Q09 | - |  |  | SI | Toalla |
| Q10 | - |  |  | SI | Peineta/Cepillo |
| Q11 | - |  |  | SI | Máquina de Afeitar |
| Q12 | - |  |  | SI | Pijama |
| Q13 | - |  |  | SI | Zapatillas de Levantar |
| Q14 | - |  |  | SI | Bata de Levantar |
| Q15 | - |  |  | SI | Pañales |
| Q16 | - |  |  | SI | Toallas Higiénicas |
| Q18 | - |  |  | SI | Zapatos/Zapatillas |
| Q19 | - |  |  | SI | Lentes |
| Q20 | - |  |  | SI | Audifonos |
| Q21 | - |  |  | SI | Prótesis Dental |
| Q22 | - |  |  | SI | Cortauñas |
| Q23 | - |  |  | SI | Pinzas |
| Q25 | - |  |  | SI | Responsable |
| Q26 | - |  |  | SI | Observaciones |
| Q27 | - |  |  | SI | Destino |
| Q28 | - |  |  | SI | Estado Paciente |
| Q34 | - |  |  | SI | Personal del Servicio Clínico |
| Q35 | - |  |  | SI | Personal Seguridad |
| Q36 | - |  |  | SI | Recibe Pertenencias y/o Valores |
| Q37 | - |  |  | SI | Nombre Completo |
| Q38 | - |  |  | SI | Parentesco Paciente |
| Q40 | - |  |  | SI | Fecha Recepción/Entrega |
| Q41 | - |  |  | SI | Hora Recepción/Entrega |
| Q42 | - |  |  | SI | Servicio/Unidad de (Recepción/Entrega) |
| Q43 | - |  |  | SI | Sin Prótesis Dental |
| Q44 | - |  |  | SI | Sin Lentes |
| Q45 | - |  |  | SI | Sin Audífonos |
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