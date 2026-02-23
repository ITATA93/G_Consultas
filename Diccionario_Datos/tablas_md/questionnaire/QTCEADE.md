# questionnaire.QTCEADE

> Declaracion Individual de Accidente Escolar

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Declaracion Individual de Accidente Escolar

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ05ADE1 | varchar |  |  | SI | - |
| CQ11ADE1 | varchar |  |  | SI | - |
| CQ16ADE1 | varchar |  |  | SI | - |
| CQ18ADE1 | varchar |  |  | SI | - |
| CQ20ADE1 | varchar |  |  | SI | - |
| CQ22ADE1 | varchar |  |  | SI | - |
| CQ23ADE1 | varchar |  |  | SI | - |
| CQ29 | varchar |  |  | SI | - |
| Q01ADE1 | varchar |  |  | SI | Esp_Codigo |
| Q02ADE1 | date |  |  | SI | Fecha |
| Q03ADE1 | varchar |  |  | SI | Lugar |
| Q04ADE1 | varchar |  |  | SI | Area_old |
| Q05ADE1 | varchar |  |  | SI | Protegido |
| Q06ADE1 | varchar |  |  | SI | Documentado |
| Q07ADE1 | varchar |  |  | SI | Localidad |
| Q08ADE1 | time |  |  | SI | Hora |
| Q09ADE1 | varchar |  |  | SI | Colegio |
| Q10ADE1 | varchar |  |  | SI | Curso |
| Q11ADE1 | varchar |  |  | SI | Accidente |
| Q12ADE1 | varchar |  |  | SI | Lugar del Accidente |
| Q13ADE1 | varchar |  |  | SI | Region |
| Q14ADE1 | varchar |  |  | SI | Servicio de Salud |
| Q15ADE1 | varchar |  |  | SI | Comuna |
| Q16ADE1 | varchar |  |  | SI | Tipo Accidente |
| Q17ADE1 | time |  |  | SI | Horario |
| Q18ADE1 | varchar |  |  | SI | Dia |
| Q19ADE1 | varchar |  |  | SI | Parte del Cuerpo Afectada |
| Q20ADE1 | varchar |  |  | SI | Incapacidad |
| Q21ADE1 | numeric |  |  | SI | Total Dias Incapacidad |
| Q22ADE1 | varchar |  |  | SI | Tipo de Incapacidad |
| Q23ADE1 | varchar |  |  | SI | Causa de Cierre del Caso |
| Q24 | varchar |  |  | SI | N° |
| Q25 | varchar |  |  | SI | Testigo1 |
| Q26 | varchar |  |  | SI | Testigo2 |
| Q27 | varchar |  |  | SI | Circunstancia del accidente |
| Q28 | date |  |  | SI | Fecha cierre de caso |
| Q29 | varchar |  |  | SI | Hospitalizacion |
| Q30 | numeric |  |  | SI | Total dias de Hospitalizacion |
| Q31 | varchar |  |  | SI | Ciudad |
| Q32 | varchar |  |  | SI | Testigos: (En caso de Trayecto) |
| Q33 | varchar |  |  | SI | Nombre Apellido  /  C.NAC de ID |
| Q34 | varchar |  |  | SI | Nombre Apellido  /  C.NAC de ID |
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