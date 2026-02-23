# questionnaire.QTCERAPH

**Schema:** questionnaire
**Columnas:** 123
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CQ1 | varchar | PK |  | SI | - |
| CQINCIDENTE | varchar | PK |  | SI | - |
| CQRAPH10 | varchar | PK |  | SI | - |
| CQRAPH14 | varchar | PK |  | SI | - |
| CQRAPH15 | varchar | PK |  | SI | - |
| CQRAPH17 | varchar | PK |  | SI | - |
| CQRAPH18 | varchar | PK |  | SI | - |
| CQRAPH2 | varchar | PK |  | SI | - |
| CQRAPH20 | varchar | PK |  | SI | - |
| CQRAPH3 | varchar | PK |  | SI | - |
| CQRAPH32 | varchar | PK |  | SI | - |
| CQRCP | varchar | PK |  | SI | - |
| CQViaVenosa | varchar | PK |  | SI | - |
| CQaspiracion | varchar | PK |  | SI | - |
| CQct | varchar | PK |  | SI | - |
| CQcur | varchar | PK |  | SI | - |
| CQinm | varchar | PK |  | SI | - |
| CQosteoclisis | varchar | PK |  | SI | - |
| CQovace | varchar | PK |  | SI | - |
| CQtorax | varchar | PK |  | SI | - |
| ID | bigint | PK |  | NO | - |
| Q1 | varchar | PK |  | SI | OVACE |
| QFiO2 | bit | PK |  | SI | FiO2 |
| QINCIDENTE | varchar | PK |  | SI | Incidente |
| QObservacion | varchar | PK |  | SI | Observación |
| QRAPH1 | varchar | PK |  | SI | Cod.Ambulancia |
| QRAPH10 | varchar | PK |  | SI | Condición del Paciente |
| QRAPH11 | bit | PK |  | SI | Intubación  |
| QRAPH12 | bit | PK |  | SI | Ventilación mecanica |
| QRAPH13 | bit | PK |  | SI | Ventilación Asistida |
| QRAPH14 | varchar | PK |  | SI | Manejo de la Vía Aérea |
| QRAPH15 | varchar | PK |  | SI | Monitorización |
| QRAPH16 | bit | PK |  | SI | Saturometria |
| QRAPH17 | varchar | PK |  | SI | Infusión de volúmen |
| QRAPH18 | varchar | PK |  | SI | Infusión de drogas |
| QRAPH19 | varchar | PK |  | SI | Descripción |
| QRAPH2 | varchar | PK |  | SI | Tipo de Accidente |
| QRAPH20 | varchar | PK |  | SI | Desfribilación/Cardioversión < 24horas |
| QRAPH21 | bit | PK |  | SI | Marcapasos Externo |
| QRAPH22 | bit | PK |  | SI | Drenajes Pleurales |
| QRAPH23 | varchar | PK |  | SI | Lugar de Origen |
| QRAPH25 | bit | PK |  | SI | CSV |
| QRAPH27 | bit | PK |  | SI | HGT |
| QRAPH28 | bit | PK |  | SI | Collar Cervical |
| QRAPH29 | bit | PK |  | SI | Ferulas |
| QRAPH3 | varchar | PK |  | SI | Accidente |
| QRAPH30 | bit | PK |  | SI | NBZ |
| QRAPH31 | bit | PK |  | SI | Tabla |
| QRAPH32 | varchar | PK |  | SI | Monitor Desfibrilador |
| QRAPH33 | bit | PK |  | SI | Marcapaso |
| QRAPH34 | bit | PK |  | SI | Marcarilla O2 |
| QRAPH35 | bit | PK |  | SI | Aspiración |
| QRAPH36 | bit | PK |  | SI | Vías IV |
| QRAPH37 | bit | PK |  | SI | Infución de drogas |
| QRAPH38 | varchar | PK |  | SI | Hora |
| QRAPH39 | varchar | PK |  | SI | Dosis |
| QRAPH4 | varchar | PK |  | SI | Dirección |
| QRAPH40 | varchar | PK |  | SI | Medicamento |
| QRAPH41 | varchar | PK |  | SI | Vía de Administración |
| QRAPH42 | varchar | PK |  | SI | Medico Receptor |
| QRAPH5 | varchar | PK |  | SI | Comuna |
| QRAPH6 | varchar | PK |  | SI | Región |
| QRAPH7 | varchar | PK |  | SI | Motivo de Atención |
| QRAPH8 | varchar | PK |  | SI | Hipótesis diagnóstica  |
| QRAPH9 | varchar | PK |  | SI | Observación |
| QRCP | varchar | PK |  | SI | RCP Básica |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |
| QViaVenosa | varchar | PK |  | SI | Vía Venosa |
| Qaspiracion | varchar | PK |  | SI | Aspiración |
| Qcapnografia | bit | PK |  | SI | Capnografia |
| Qct | varchar | PK |  | SI | Categorización post evaluación |
| Qcur | varchar | PK |  | SI | Curación |
| Qdinamica | bit | PK |  | SI | Dinámica Uterina |
| Qecg | bit | PK |  | SI | Electrocardiograma |
| Qinm | varchar | PK |  | SI | Inmobilización |
| Qosteoclisis | varchar | PK |  | SI | Osteoclisis |
| Qotro | varchar | PK |  | SI | Otro procedimiento |
| Qovace | varchar | PK |  | SI | OVACE |
| Qpr | varchar | PK |  | SI | Protocolo |
| Qra | varchar | PK |  | SI | Reacción Adversa |
| Qresponsable | varchar | PK |  | SI | Responsable |
| Qtorax | varchar | PK |  | SI | Tórax |
| Qtto1 | bit | PK |  | SI | Tratamiento Inyectable IM |
| Qtto2 | bit | PK |  | SI | Tratamiento Inyectable ev |
| Qtto3 | bit | PK |  | SI | Tratamiento Vía Oral |
| Qtto4 | bit | PK |  | SI | Tratamiento Sublingual |
| Qtto5 | bit | PK |  | SI | Tratamiento Rectal |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*