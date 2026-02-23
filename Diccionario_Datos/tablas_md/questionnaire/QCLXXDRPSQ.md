# questionnaire.QCLXXDRPSQ

> Datos Relevantes para la Solicitud Quirúrgica

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Datos Relevantes para la Solicitud Quirúrgica

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Equipo |
| Q02 | varchar |  |  | SI | Parámetros Antropométricos |
| Q03 | varchar |  |  | SI | Peso y Talla |
| Q04 | varchar |  |  | SI | Antecedentes Farmacológicos |
| Q05 | varchar |  |  | SI | Paciente actualmente bajo tratamiento: |
| Q06 | varchar |  |  | SI | Antiagregante |
| Q07 | varchar |  |  | SI | Anticoagulante |
| Q08 | varchar |  |  | SI | Requerimientos para la realización del acto quirúr... |
| Q10 | numeric |  |  | SI | Talla |
| Q11 | numeric |  |  | SI | Peso |
| Q12 | varchar |  |  | SI | IMC_old |
| Q13 | varchar |  |  | SI | Antecedentes Farmacológicos |
| Q14 | varchar |  |  | SI | Requerimientos para la realización del acto quirúr... |
| Q16 | varchar |  |  | SI | Tipo de cama |
| Q17 | varchar |  |  | SI | Insumos de Especialidad |
| Q18 | varchar |  |  | SI | Instrumental Externo |
| Q19 | varchar |  |  | SI | Instrumental Quirúrgico Especial  |
| Q20 | varchar |  |  | SI | Apoyo de Imagenología |
| Q21 | varchar |  |  | SI | Hemorreserva  |
| Q22 | varchar |  |  | SI | IMC |
| Q23 | varchar |  |  | SI | Modalidad |
| Q25 | bit |  |  | SI | Cirugías Adicionales |
| Q27 | varchar |  |  | SI | Convenio |
| Q28 | varchar |  |  | SI | Requiere Hemocomponentes |
| Q29 | numeric |  |  | SI | Cantidad |
| Q30 | varchar |  |  | SI | Comentarios&nbsp;Hemocomponentes |
| Q31 | varchar |  |  | SI | Precauciones adicionales |
| Q32 | varchar |  |  | SI | Preparación Especial |
| Q33 | varchar |  |  | SI | Alergias |
| Q34 | varchar |  |  | SI | Comentarios Alergias |
| Q35 | varchar |  |  | SI | Complejidad |
| Q36 | varchar |  |  | SI | Equipamiento |
| Q37 | varchar |  |  | SI | Observaciones Generales |
| Q38 | varchar |  |  | SI | Proveedor |
| Q39 | varchar |  |  | SI | Cirugías Adicionales |
| Q40 | varchar |  |  | SI | Información Complementaria |
| Q41 | varchar |  |  | SI | Estadía Hospitalaria |
| Q42 | varchar |  |  | SI | Observaciones |
| Q43 | varchar |  |  | SI | Implantes/Insumos |
| Q44 | varchar |  |  | SI | Instrumental |
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