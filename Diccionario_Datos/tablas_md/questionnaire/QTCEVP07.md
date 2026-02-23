# questionnaire.QTCEVP07

> Antecedentes Ginecológicos

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Antecedentes Ginecológicos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | MENARQUIA |
| Q02 | numeric |  |  | SI | MENOPAUSIA |
| Q03 | varchar |  |  | SI | Terapia de Reemplazo Hormonal |
| Q04 | varchar |  |  | SI | Ciclo |
| Q05 | numeric |  |  | SI | Frecuencia del ciclo |
| Q06 | numeric |  |  | SI | Duración |
| Q07 | date |  |  | SI | FUR |
| Q08 | varchar |  |  | SI | Observaciones Ciclo Menstrual |
| Q09 | numeric |  |  | SI | Edad de inicio |
| Q10 | varchar |  |  | SI | Actividad Actual |
| Q11 | varchar |  |  | SI | Método Anticonceptivo |
| Q12 | date |  |  | SI | Fecha último PAP |
| Q13 | varchar |  |  | SI | Resultado PAP |
| Q14 | varchar |  |  | SI | Observaciones PAP |
| Q15 | date |  |  | SI | Fecha última mamografía |
| Q16 | varchar |  |  | SI | Resultado Mamografía |
| Q17 | varchar |  |  | SI | ¿Requirió ECO Mamaria complementaria? |
| Q18 | varchar |  |  | SI | Resultado ECO mamaria |
| Q19 | varchar |  |  | SI | Observaciones ECO Mamaria |
| Q20 | varchar |  |  | SI | Observaciones Mamografia |
| Q21 | varchar |  |  | SI | Observaciones Actividad Sexual |
| Q22 | numeric |  |  | SI | Numero de parejas sexuales |
| Q23 | varchar |  |  | SI | Conducta sexual de riesgo |
| Q24 | varchar |  |  | SI | Desea agregar observaciones? (Ciclo Menstrual) |
| Q25 | varchar |  |  | SI | Desea agregar observaciones? (Actividad Sexual) |
| Q26 | varchar |  |  | SI | Desea agregar Observaciones? (PAP) |
| Q27 | varchar |  |  | SI | Desea agregar Observaciones? (Mamografia) |
| Q28 | varchar |  |  | SI | Orgasmo |
| Q29 | varchar |  |  | SI | Frecuencia |
| Q30 | varchar |  |  | SI | Actividad Sexual-Líbido |
| Q31 | varchar |  |  | SI | Antecedente de Incontinencia Urinaria |
| Q32 | varchar |  |  | SI | Alteración Intervalo/Duración |
| Q33 | varchar |  |  | SI | Alteración de la cantidad |
| Q34 | varchar |  |  | SI | Otras Alteraciones |
| Q35 | varchar |  |  | SI | Alteraciones del Coito |
| Q36 | varchar |  |  | SI | Método Anticonceptivo |
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