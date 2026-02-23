# SQLUser.ARC_PayRefStatus

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRST_RowId | bigint | PK |  | NO | - |
| PRST_Code | varchar |  |  | NO | Code |
| PRST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRST_CreatedDate | date |  |  | SI | Created Date |
| PRST_CreatedTime | time |  |  | SI | Created Time |
| PRST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRST_DateFrom | date |  |  | SI | Date From |
| PRST_DateTo | date |  |  | SI | Date To |
| PRST_Desc | varchar |  |  | NO | Description |
| PRST_Initial | varchar |  |  | SI | Initial |
| PRST_Owner | varchar |  |  | SI | Owner |
| PRST_PartialProcessed | varchar |  |  | SI | Partially Processed |
| PRST_Processed | varchar |  |  | SI | Processed |
| PRST_UpdatedDate | date |  |  | SI | Updated Date |
| PRST_UpdatedTime | time |  |  | SI | Updated Time |
| PRST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Peso |
| Q01ObsDR | - |  |  | SI | Peso DR |
| Q02 | - |  |  | SI | Talla |
| Q02ObsDR | - |  |  | SI | Talla DR |
| Q03 | - |  |  | SI | Perímetro de Cintura |
| Q03ObsDR | - |  |  | SI | Perímetro de Cintura DR |
| Q04 | - |  |  | SI | IMC |
| Q05 | - |  |  | SI | Estatura Madre |
| Q05ObsDR | - |  |  | SI | Estatura Madre DR |
| Q06 | - |  |  | SI | Estatura Padre |
| Q06ObsDR | - |  |  | SI | Estatura Padre DR |
| Q07 | - |  |  | SI | Talla Diana Hombres |
| Q08 | - |  |  | SI | Talla Diana Mujeres |
| Q09 | - |  |  | SI | Talla por Edad |
| Q09ObsDR | - |  |  | SI | Talla por Edad DR |
| Q10 | - |  |  | SI | IMC por Edad |
| Q10ObsDR | - |  |  | SI | IMC por Edad DR |
| Q11 | - |  |  | SI | Puntaje Z Talla/Edad |
| Q11ObsDR | - |  |  | SI | Puntaje Z Talla/Edad DR |
| Q12 | - |  |  | SI | Puntaje Z IMC/Edad |
| Q12ObsDR | - |  |  | SI | Puntaje Z IMC/Edad DR |
| Q13 | - |  |  | SI | Ingresar información en forma manual (deshabilita ... |
| Q14 | - |  |  | SI | Calificación Estatura |
| Q14ObsDR | - |  |  | SI | Calificación Estatura DR |
| Q15 | - |  |  | SI | Tanner Genitales |
| Q15ObsDR | - |  |  | SI | Tanner Genitales DR |
| Q16 | - |  |  | SI | Tanner Mamas |
| Q16ObsDR | - |  |  | SI | Tanner Mamas DR |
| Q17 | - |  |  | SI | Tanner Vello Púbico |
| Q17ObsDR | - |  |  | SI | Tanner Vello Púbico DR |
| Q18 | - |  |  | SI | Percentil de Cicunferencia Cintura |
| Q18ObsDR | - |  |  | SI | Percentil de Cicunferencia Cintura DR |
| Q19 | - |  |  | SI | Indice Cintura/Estatura |
| Q20 | - |  |  | SI | Obesidad Abdominal Según Circunferencia de Cintura |
| Q20ObsDR | - |  |  | SI | Obesidad Abdominal Según Circunferencia de Cintura... |
| Q21 | - |  |  | SI | Diagnóstico Nutricional |
| Q21ObsDR | - |  |  | SI | Diagnóstico Nutricional DR |
| Q22 | - |  |  | SI | Corregir cálculos según edad biológica |
| Q23 | - |  |  | SI | Edad (Años) |
| Q24 | - |  |  | SI | Edad (Meses) |
| Q25 | - |  |  | SI | Ingrese edad biológica estimada |
| QSEN | - |  |  | SI | Usuario bajo algún programa del SENAME [REM] |
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