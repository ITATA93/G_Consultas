# questionnaire.QCLXXISRAPO

> Informe Social y de Redes de Apoyo

**Schema:** questionnaire
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Informe Social y de Redes de Apoyo

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha  de Registro del Informe |
| Q02 | time |  |  | SI | Hora de Registro del Informe |
| Q03 | varchar |  |  | SI | Responsable del Registro del Informe |
| Q04 | varchar |  |  | SI | I. Datos de Identificación del paciente |
| Q05 | varchar |  |  | SI | Teléfono Celular |
| Q06 | varchar |  |  | SI | Correo Electrónico |
| Q07 | varchar |  |  | SI | Domicilio Villa / Población |
| Q08 | varchar |  |  | SI | Número  |
| Q09 | varchar |  |  | SI | Comuna |
| Q10 | varchar |  |  | SI | Estado civil |
| Q11 | varchar |  |  | SI | Sistema de Salud |
| Q12 | varchar |  |  | SI | Motivo de solicitud de certificación  |
| Q13 | varchar |  |  | SI | II. Datos de Identificación del representante |
| Q14 | varchar |  |  | SI | Representante |
| Q15 | varchar |  |  | SI | Nombres y Apellidos |
| Q16 | varchar |  |  | SI | R.U.N.  (99.999.999-9) |
| Q17 | varchar |  |  | SI | Correo Electrónico |
| Q18 | varchar |  |  | SI | Teléfono |
| Q19 | varchar |  |  | SI | Relación con el interesado |
| Q20 | varchar |  |  | SI | III. Situación escolar y laboral del Paciente |
| Q21 | varchar |  |  | SI | Nivel de escolaridad alcanzado |
| Q22 | varchar |  |  | SI | Actividad o actividades que desempeña actualmente ... |
| Q23 | varchar |  |  | SI | Estudia |
| Q24 | varchar |  |  | SI | Trabaja |
| Q25 | varchar |  |  | SI | Rubro en que se desempeña |
| Q26 | varchar |  |  | SI | Dificultades que presenta en el trabajo |
| Q27 | varchar |  |  | SI | Situación ocupacional |
| Q28 | varchar |  |  | SI | Tipo de pensión |
| Q29 | varchar |  |  | SI | Tipo de jubilación |
| Q30 | varchar |  |  | SI | PIE: Programa de Integración Escolar |
| Q31 | varchar |  |  | SI | IV. Identificación con quienes cohabita paciente |
| Q33 | varchar |  |  | SI | Describa situación familiar actual  |
| Q34 | varchar |  |  | SI | Paciente ¿tiene cuidador? |
| Q35 | varchar |  |  | SI | V. Descripción del cuidador(a) |
| Q36 | varchar |  |  | SI | Descripción cuidador/a principal |
| Q38 | varchar |  |  | SI | VI. Identificación de redes de apoyo y nivel de pa... |
| Q39 | varchar |  |  | SI | Red de apoyo principal con la que cuenta el pacien... |
| Q40 | varchar |  |  | SI | Primarias |
| Q41 | varchar |  |  | SI | Relación con interesado (Primarias) |
| Q42 | varchar |  |  | SI | Tipo de apoyo (Primarias) |
| Q43 | varchar |  |  | SI | Secundarias (clubes, agrupaciones, iglesia) |
| Q44 | varchar |  |  | SI | Relación con interesado (Secundarias) |
| Q45 | varchar |  |  | SI | Tipo de apoyo (Secundarias) |
| Q46 | varchar |  |  | SI | Institucionales (municipalidad, servicio salud, in... |
| Q47 | varchar |  |  | SI | Relación con interesado (Institucionales) |
| Q48 | varchar |  |  | SI | Tipo de apoyo (Institucionales) |
| Q49 | varchar |  |  | SI | Valoración general de la red de apoyo  |
| Q50 | varchar |  |  | SI | Participación en actividades sociales (culturales,... |
| Q51 | varchar |  |  | SI | Participación en actividades sociales (Texto) |
| Q52 | varchar |  |  | SI | VII. Información sobre vivienda y entorno |
| Q53 | varchar |  |  | SI | Tipo de domicilio del paciente |
| Q54 | varchar |  |  | SI | Tipo de domicilio (Texto) |
| Q55 | varchar |  |  | SI | Sector |
| Q56 | varchar |  |  | SI | Identificación de barreras ambientales |
| Q57 | varchar |  |  | SI | Barreras al interior de la vivienda |
| Q58 | varchar |  |  | SI | Barreras del entorno de la vivienda |
| Q59 | varchar |  |  | SI | Habitación independiente |
| Q60 | varchar |  |  | SI | Baño dentro de la vivienda |
| Q61 | varchar |  |  | SI | Baño adaptado |
| Q62 | varchar |  |  | SI | Estado general de vivienda |
| Q63 | varchar |  |  | SI | Paciente tiene acceso a transporte |
| Q64 | varchar |  |  | SI | Tipo de transporte Publico |
| Q65 | varchar |  |  | SI | ¿El interesado tiene algún grado de limitación en ... |
| Q66 | varchar |  |  | SI | Comentarios |
| Q67 | varchar |  |  | SI | VIII. Datos de identificación de Asistente o Traba... |
| Q68 | varchar |  |  | SI | Nombre completo |
| Q69 | varchar |  |  | SI | R.U.N. (99.999.999-9) |
| Q70 | varchar |  |  | SI | Institución |
| Q71 | varchar |  |  | SI | Correo electrónico |
| Q72 | varchar |  |  | SI | Teléfono |
| Q73 | date |  |  | SI | Fecha Informe |
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