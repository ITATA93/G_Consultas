# SQLUser.LBC_BPSplitTypeOutputProduct

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPSTOP_ParRef | bigint | PK |  | NO | Parent Split Type |
| LBCBPSTOP_BloodProduct_DR | bigint |  | FK | NO | Blood Product |
| LBCBPSTOP_ExpiryOffset | integer |  |  | SI | Default expiry offset of the newly created blood p... |
| LBCBPSTOP_ExpiryOffsetUnit | varchar |  |  | SI | Unit of the default expiry offset of the newly cre... |
| LBCBPSTOP_RowID | varchar |  |  | NO | - |
| QAtencionCons | - |  |  | SI | Atención en Consultorio |
| QBDD | - |  |  | SI | Budesonida (dosis) |
| QComuna | - |  |  | SI | Comuna |
| QConsultorio | - |  |  | SI | Consultorio |
| QDomic | - |  |  | SI | Domicilio |
| QEvalOxig | - |  |  | SI | 6. Evaluación de Oxigenoterapia |
| QExistenciaAct | - |  |  | SI | 5. Existencia Actual de |
| QFactores | - |  |  | SI | 1. Factores ambientales de Riesgo actuales |
| QFechaReg | - |  |  | SI | Fecha Registro |
| QFuente | - |  |  | SI | Fuente del Suministro O2 |
| QHoraReg | - |  |  | SI | Hora Registro |
| QIPD | - |  |  | SI | Ipatropio (dosis) |
| QMantFlujo | - |  |  | SI | Mantener Flujo O2 |
| QNombre | - |  |  | SI | Nombre |
| QNombreInf | - |  |  | SI | Nombre del Informantr |
| QNumVisita | - |  |  | SI | 3. Número de Visitas a consultorio en últimos 3 me... |
| QNumVisitaUrg | - |  |  | SI | 4. Número Visitas a Urgencia en últimos 3 meses |
| QNumeroReg | - |  |  | SI | N° Registro O2 |
| QOTD | - |  |  | SI | Otro (dosis) |
| QPrev | - |  |  | SI | Previsión |
| QPuntajeCuest | - |  |  | SI | 10. Puntaje Cuestionario de calida de Vida (CRQ) |
| QPuntajeEs | - |  |  | SI | 9. Puntaje Escala de Disnea |
| QRegion | - |  |  | SI | Región |
| QRut | - |  |  | SI | Rut |
| QSTD | - |  |  | SI | Salbutamol (dosis) |
| QSalaEra | - |  |  | SI | Sala ERA Consultorio |
| QServicio | - |  |  | SI | Servicio de Salud |
| QTelef | - |  |  | SI | Teléfono |
| QTiempo | - |  |  | SI | Tiempo Diario de uso |
| QTutorRes | - |  |  | SI | 7. Tutor Responsable y Capacitado |
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
| QUsoBron | - |  |  | SI | 2. Uso Broncodilatadores (Dosis) |
| QVisitaDom | - |  |  | SI | Visita Domiciliaria |
| Qservoxig | - |  |  | SI | 8. Servicio de oxigenoterapia continuo |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*