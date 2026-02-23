# questionnaire.QCLXXCACU

> Boletin de Notificación Obligatoria Cánceres de Cuello Uterino y/o Mama

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Boletin de Notificación Obligatoria Cánceres de Cuello Uterino y/o Mama

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Servicio de Salud |
| Q02 | varchar |  |  | SI | Establecimiento |
| Q03 | date |  |  | SI | Fecha Notificación |
| Q04 | varchar |  |  | SI | Número de Informe |
| Q05 | varchar |  |  | SI | Ficha Clínica |
| Q06 | varchar |  |  | SI | RUN |
| Q07 | varchar |  |  | SI | Nombre Paciente |
| Q08 | varchar |  |  | SI | Apellido Paterno |
| Q09 | varchar |  |  | SI | Apellido Materno |
| Q10 | varchar |  |  | SI | Sexo |
| Q11 | varchar |  |  | SI | Fecha de Nacimiento |
| Q12 | varchar |  |  | SI | Previsión |
| Q13 | varchar |  |  | SI | Domicilio |
| Q14 | varchar |  |  | SI | Número Domicilio |
| Q15 | varchar |  |  | SI | Comuna |
| Q16 | varchar |  |  | SI | Ciudad |
| Q17 | varchar |  |  | SI | Centro de Salud |
| Q18 | varchar |  |  | SI | Localización |
| Q19 | varchar |  |  | SI | Lateralidad |
| Q20 | varchar |  |  | SI | Cuadrante |
| Q21 | varchar |  |  | SI | Etapa Clínica |
| Q22 | varchar |  |  | SI | Código CIE |
| Q23 | varchar |  |  | SI | Cídigo CIE - 0 |
| Q24 | varchar |  |  | SI | Método Diagnóstico |
| Q25 | date |  |  | SI | Fecha Diagnóstico |
| Q26 | varchar |  |  | SI | Nombre Profesional |
| Q27 | varchar |  |  | SI | Firma |
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