# SQLUser.LBC_InstrumentEventTypeRec

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCIETR_ParRef | bigint | PK |  | NO | Parent instrument DR |
| CQ05ADE1 | - |  |  | SI | (null) |
| CQ11ADE1 | - |  |  | SI | (null) |
| CQ16ADE1 | - |  |  | SI | (null) |
| CQ18ADE1 | - |  |  | SI | (null) |
| CQ20ADE1 | - |  |  | SI | (null) |
| CQ22ADE1 | - |  |  | SI | (null) |
| CQ23ADE1 | - |  |  | SI | (null) |
| CQ29 | - |  |  | SI | (null) |
| LBCIETR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCIETR_DateFrom | date |  |  | SI | Date From |
| LBCIETR_DateTo | date |  |  | SI | Date To |
| LBCIETR_InstrumentEventRecord_DR | bigint |  | FK | NO | Instrument Event Record |
| LBCIETR_Mandatory | varchar |  |  | SI | Mandatory Flag |
| LBCIETR_RowID | varchar |  |  | NO | - |
| Q01ADE1 | - |  |  | SI | Esp_Codigo |
| Q02ADE1 | - |  |  | SI | Fecha |
| Q03ADE1 | - |  |  | SI | Lugar |
| Q04ADE1 | - |  |  | SI | Area_old |
| Q05ADE1 | - |  |  | SI | Protegido |
| Q06ADE1 | - |  |  | SI | Documentado |
| Q07ADE1 | - |  |  | SI | Localidad |
| Q08ADE1 | - |  |  | SI | Hora |
| Q09ADE1 | - |  |  | SI | Colegio |
| Q10ADE1 | - |  |  | SI | Curso |
| Q11ADE1 | - |  |  | SI | Accidente |
| Q12ADE1 | - |  |  | SI | Lugar del Accidente |
| Q13ADE1 | - |  |  | SI | Region |
| Q14ADE1 | - |  |  | SI | Servicio de Salud |
| Q15ADE1 | - |  |  | SI | Comuna |
| Q16ADE1 | - |  |  | SI | Tipo Accidente |
| Q17ADE1 | - |  |  | SI | Horario |
| Q18ADE1 | - |  |  | SI | Dia |
| Q19ADE1 | - |  |  | SI | Parte del Cuerpo Afectada |
| Q20ADE1 | - |  |  | SI | Incapacidad |
| Q21ADE1 | - |  |  | SI | Total Dias Incapacidad |
| Q22ADE1 | - |  |  | SI | Tipo de Incapacidad |
| Q23ADE1 | - |  |  | SI | Causa de Cierre del Caso |
| Q24 | - |  |  | SI | N° |
| Q25 | - |  |  | SI | Testigo1 |
| Q26 | - |  |  | SI | Testigo2 |
| Q27 | - |  |  | SI | Circunstancia del accidente |
| Q28 | - |  |  | SI | Fecha cierre de caso |
| Q29 | - |  |  | SI | Hospitalizacion |
| Q30 | - |  |  | SI | Total dias de Hospitalizacion |
| Q31 | - |  |  | SI | Ciudad |
| Q32 | - |  |  | SI | Testigos: (En caso de Trayecto) |
| Q33 | - |  |  | SI | Nombre Apellido  /  C.NAC de ID |
| Q34 | - |  |  | SI | Nombre Apellido  /  C.NAC de ID |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*