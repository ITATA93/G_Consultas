# questionnaire.QFSECV

> Formulario de Solicitud de Exámenes de Carga Viral VIH-1

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Solicitud de Exámenes de Carga Viral VIH-1

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Sexo |
| Q02 | bit |  |  | SI | Ambulatorio |
| Q03 | bit |  |  | SI | Hospitalizado |
| Q04 | bit |  |  | SI | Embarazada |
| Q05 | bit |  |  | SI | No ha iniciado TARV |
| Q06 | bit |  |  | SI | TRAV Suspendida |
| Q07 | bit |  |  | SI | Actualmente en TARV |
| Q08 | date |  |  | SI | Fecha de Inicio |
| Q09 | varchar |  |  | SI | Marcar drogas de TARV actual: |
| Q10 | varchar |  |  | SI | Otro antiretroviral (indicar) |
| Q11 | date |  |  | SI | Fecha de extracción de muestra |
| Q12 | time |  |  | SI | Hora |
| Q13 | varchar |  |  | SI | Responsable |
| Q14 | date |  |  | SI | Fecha de Lisis |
| Q15 | varchar |  |  | SI | Vol. Plasma en T. Lisis (ml) |
| Q16 | varchar |  |  | SI | Muestra enviada |
| Q17 | varchar |  |  | SI | Establecimiento |
| Q18 | varchar |  |  | SI | Medico Solicitante |
| Q19 | date |  |  | SI | FechaM |
| Q20 | varchar |  |  | SI | Observaciones |
| Q21 | date |  |  | SI | Fecha |
| Q22 | time |  |  | SI | Hora |
| Q23 | varchar |  |  | SI | Responsable |
| Q24 | varchar |  |  | SI | Observación |
| Q29 | varchar |  |  | SI | Inicial del 1° nombre, iniciales 1° y 2° apellido ... |
| Q30 | varchar |  |  | SI | Clasificación |
| Q31 | date |  |  | SI | Fecha de Suspensión |
| Q32 | varchar |  |  | SI | Unidad |
| Q33 | varchar |  |  | SI | Establecimiento |
| Q34 | varchar |  |  | SI | N° Solicitud |
| Q35 | varchar |  |  | SI | N° CONFIRM.ISP |
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