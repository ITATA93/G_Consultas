# questionnaire.QFSET

> Formulario de Solicitud de Examen de Tuberculosis

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Solicitud de Examen de Tuberculosis

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Muestra de Expectoración |
| Q02 | varchar |  |  | SI | Sangre |
| Q03 | varchar |  |  | SI | Otra |
| Q04 | varchar |  |  | SI | Virgen a Tratamiento TBC |
| Q05 | varchar |  |  | SI | Antes Tratado TBC |
| Q06 | varchar |  |  | SI | Abandono Tratamiento TBC |
| Q07 | varchar |  |  | SI | Contacto TBC |
| Q08 | varchar |  |  | SI | Extranjero |
| Q09 | varchar |  |  | SI | País |
| Q10 | varchar |  |  | SI | Coinfección Retrovial |
| Q11 | varchar |  |  | SI | Población Cerrada |
| Q12 | varchar |  |  | SI | Hogar |
| Q13 | varchar |  |  | SI | Reo |
| Q14 | varchar |  |  | SI | Otro |
| Q15 | varchar |  |  | SI | Profesional de Salud |
| Q16 | varchar |  |  | SI | N° Meses que esta con tratamiento TBC |
| Q17 | varchar |  |  | SI | Imágenes Pulmonares al RX |
| Q18 | varchar |  |  | SI | Recepción de la muestra  |
| Q19 | date |  |  | SI | Fecha |
| Q20 | time |  |  | SI | Hora |
| Q21 | varchar |  |  | SI | Nombre Responsable Recepción  |
| Q22 | varchar |  |  | SI | Nombre y Firma TM |
| Q23 | varchar |  |  | SI | N° de Cultivo |
| Q24 | varchar |  |  | SI | Resultado BK |
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