# SQLUser.ARC_ItemQtyAllowed

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QTYAL_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| Q01 | - |  |  | SI | Servicio de Salud |
| Q02 | - |  |  | SI | Establecimiento |
| Q03 | - |  |  | SI | Fecha Notificación |
| Q04 | - |  |  | SI | Número de Informe |
| Q05 | - |  |  | SI | Ficha Clínica |
| Q06 | - |  |  | SI | RUN |
| Q07 | - |  |  | SI | Nombre Paciente |
| Q08 | - |  |  | SI | Apellido Paterno |
| Q09 | - |  |  | SI | Apellido Materno |
| Q10 | - |  |  | SI | Sexo |
| Q11 | - |  |  | SI | Fecha de Nacimiento |
| Q12 | - |  |  | SI | Previsión |
| Q13 | - |  |  | SI | Domicilio |
| Q14 | - |  |  | SI | Número Domicilio |
| Q15 | - |  |  | SI | Comuna |
| Q16 | - |  |  | SI | Ciudad |
| Q17 | - |  |  | SI | Centro de Salud |
| Q18 | - |  |  | SI | Localización |
| Q19 | - |  |  | SI | Lateralidad |
| Q20 | - |  |  | SI | Cuadrante |
| Q21 | - |  |  | SI | Etapa Clínica |
| Q22 | - |  |  | SI | Código CIE |
| Q23 | - |  |  | SI | Cídigo CIE - 0 |
| Q24 | - |  |  | SI | Método Diagnóstico |
| Q25 | - |  |  | SI | Fecha Diagnóstico |
| Q26 | - |  |  | SI | Nombre Profesional |
| Q27 | - |  |  | SI | Firma |
| QTYAL_ARCQtyAll_DR | bigint |  | FK | NO | Des Ref to ARCQtyAll |
| QTYAL_Childsub | double |  |  | NO | Childsub |
| QTYAL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| QTYAL_CreatedDate | date |  |  | SI | Created Date |
| QTYAL_CreatedTime | time |  |  | SI | Created Time |
| QTYAL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| QTYAL_DateFrom | date |  |  | NO | Eff. Date From |
| QTYAL_DateTo | date |  |  | SI | Eff. Date To |
| QTYAL_InsType_DR | bigint |  | FK | SI | Des Ref to ARCInsType |
| QTYAL_RowId | varchar |  |  | NO | - |
| QTYAL_UpdatedDate | date |  |  | SI | Updated Date |
| QTYAL_UpdatedTime | time |  |  | SI | Updated Time |
| QTYAL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
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