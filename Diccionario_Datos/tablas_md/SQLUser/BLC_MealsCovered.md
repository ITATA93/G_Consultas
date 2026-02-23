# SQLUser.BLC_MealsCovered

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MEALC_RowId | bigint | PK |  | NO | - |
| MEALC_CreatedDate | date |  |  | SI | Created Date |
| MEALC_CreatedTime | time |  |  | SI | Created Time |
| MEALC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MEALC_DateFrom | date |  |  | SI | Date From |
| MEALC_DateTo | date |  |  | SI | Date To |
| MEALC_DietType | varchar |  |  | SI | Not Used Diet Type |
| MEALC_InsType_DR | bigint |  | FK | SI | Des Ref InsType_DR |
| MEALC_Number_of_Meals | double |  |  | SI | Number of Meals |
| MEALC_UpdatedDate | date |  |  | SI | Updated Date |
| MEALC_UpdatedTime | time |  |  | SI | Updated Time |
| MEALC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Antecedentes Quirúrgicos |
| Q02 | - |  |  | SI | Diagnóstico Preoperatorio |
| Q03 | - |  |  | SI | Nombre Cirugía |
| Q04 | - |  |  | SI | Prestación |
| Q05 | - |  |  | SI | Prestación (Descripción) |
| Q06 | - |  |  | SI | Cirugía programada |
| Q07 | - |  |  | SI | Cirujano |
| Q08 | - |  |  | SI | Ayudante |
| Q09 | - |  |  | SI | Arsenalera |
| Q10 | - |  |  | SI | Tipo de Anestesia |
| Q11 | - |  |  | SI | Anestésico utilizado |
| Q12 | - |  |  | SI | Uso de Sedación |
| Q13 | - |  |  | SI | Fecha Inicio |
| Q14 | - |  |  | SI | Hora Inicio |
| Q15 | - |  |  | SI | Protocolo Quirúrgico |
| Q16 | - |  |  | SI | Biopsia |
| Q17 | - |  |  | SI | Tejido, órgano o localización |
| Q18 | - |  |  | SI | Número de Frascos |
| Q19 | - |  |  | SI | Fecha Fin |
| Q20 | - |  |  | SI | Hora Fin |
| Q21 | - |  |  | SI | Diagnóstico Postoperatorio |
| Q22 | - |  |  | SI | 1. Antecedentes |
| Q23 | - |  |  | SI | 2. Detalles de la Cirugía |
| Q24 | - |  |  | SI | Operación |
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