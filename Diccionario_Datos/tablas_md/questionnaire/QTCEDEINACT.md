# questionnaire.QTCEDEINACT

**Schema:** questionnaire
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CQ14 | varchar | PK |  | SI | - |
| CQ20 | varchar | PK |  | SI | - |
| CQ21 | varchar | PK |  | SI | - |
| CQ32 | varchar | PK |  | SI | - |
| CQ33 | varchar | PK |  | SI | - |
| CQ35 | varchar | PK |  | SI | - |
| CQ4 | varchar | PK |  | SI | - |
| CQ43 | varchar | PK |  | SI | - |
| CQ45 | varchar | PK |  | SI | - |
| CQ46 | varchar | PK |  | SI | - |
| CQ47 | varchar | PK |  | SI | - |
| CQ48 | varchar | PK |  | SI | - |
| CQ49 | varchar | PK |  | SI | - |
| CQ50 | varchar | PK |  | SI | - |
| CQ52 | varchar | PK |  | SI | - |
| CQ53 | varchar | PK |  | SI | - |
| CQ59 | varchar | PK |  | SI | - |
| CQ6 | varchar | PK |  | SI | - |
| ID | bigint | PK |  | NO | - |
| Q1 | varchar | PK |  | SI | Nombre o Razón Social |
| Q10 | varchar | PK |  | SI | Departamento |
| Q11 | varchar | PK |  | SI | Población |
| Q12 | varchar | PK |  | SI | Comuna |
| Q13 | varchar | PK |  | SI | Cédula Nacional Identidad |
| Q14 | varchar | PK |  | SI | Carácter de la Actividad |
| Q15 | varchar | PK |  | SI | Régimen Previsional |
| Q16 | varchar | PK |  | SI | N° Insc. |
| Q17 | varchar | PK |  | SI | Años |
| Q18 | varchar | PK |  | SI | Meses |
| Q19 | varchar | PK |  | SI | Días |
| Q2 | varchar | PK |  | SI | Rut Empleador |
| Q20 | varchar | PK |  | SI | Categoría ocupacional del Accidentado |
| Q21 | varchar | PK |  | SI | Profesión u Oficio |
| Q22 | varchar | PK |  | SI | Provincia |
| Q23 | varchar | PK |  | SI | Ciudad |
| Q24 | varchar | PK |  | SI | Calle |
| Q25 | varchar | PK |  | SI | N° |
| Q26 | varchar | PK |  | SI | Provincia |
| Q27 | varchar | PK |  | SI | Ciudad |
| Q28 | varchar | PK |  | SI | Calle |
| Q29 | varchar | PK |  | SI | N° |
| Q3 | varchar | PK |  | SI | Sitio Preciso |
| Q30 | varchar | PK |  | SI | Camino |
| Q31 | varchar | PK |  | SI | Circunstancias (Describa cómo ocurrió) |
| Q32 | varchar | PK |  | SI | Circunstancias |
| Q33 | varchar | PK |  | SI | Agente del Accidente (Causa) |
| Q34 | varchar | PK |  | SI | Otros especificar |
| Q35 | varchar | PK |  | SI | Tipo de  Accidente |
| Q36 | varchar | PK |  | SI | Nombre |
| Q37 | varchar | PK |  | SI | Céd. Nac. Ident. |
| Q38 | varchar | PK |  | SI | Nombre |
| Q39 | varchar | PK |  | SI | Céd. Nac. Ident. |
| Q4 | varchar | PK |  | SI | Rama de la Actividad Económica |
| Q40 | date | PK |  | SI | Fecha en que se registraron estos datos |
| Q41 | varchar | PK |  | SI | Diagnóstico Ingreso |
| Q42 | varchar | PK |  | SI | Diagnóstico Egreso |
| Q43 | varchar | PK |  | SI | Hospitalización |
| Q44 | varchar | PK |  | SI | Total Días |
| Q45 | varchar | PK |  | SI | Intervensión Quirúrgica |
| Q46 | varchar | PK |  | SI | Amputación |
| Q47 | varchar | PK |  | SI | Pérdida Función |
| Q48 | varchar | PK |  | SI | Prótesis |
| Q49 | varchar | PK |  | SI | Presentó Infección Después del Ingreso |
| Q5 | varchar | PK |  | SI | Nombre |
| Q50 | varchar | PK |  | SI | Días de Incapacidad |
| Q51 | varchar | PK |  | SI | Total Días |
| Q52 | varchar | PK |  | SI | Tipo de Incapacidad |
| Q53 | varchar | PK |  | SI | Causa de cierre del Caso |
| Q54 | date | PK |  | SI | Fecha de cierre del Caso |
| Q55 | varchar | PK |  | SI | Establecimiento Asistencial Nombre |
| Q56 | varchar | PK |  | SI | N° Establecimiento Asistencial |
| Q57 | varchar | PK |  | SI | Servicio de Salud |
| Q58 | date | PK |  | SI | Fecha |
| Q59 | varchar | PK |  | SI | Días de la Semana |
| Q6 | varchar | PK |  | SI | Sexo |
| Q60 | time | PK |  | SI | Horas |
| Q61 | varchar | PK |  | SI | N° de horas diarias trabajadas hasta el momento de... |
| Q62 | date | PK |  | SI | Fecha del Accidente |
| Q63 | time | PK |  | SI | Hora del Accidente |
| Q7 | varchar | PK |  | SI | Edad |
| Q8 | varchar | PK |  | SI | Calle |
| Q9 | varchar | PK |  | SI | N° |
| QCM | varchar | PK |  | SI | Comuna |
| QCMB | varchar | PK |  | SI | Comuna |
| QCSS | varchar | PK |  | SI | Código Servicio de Salud |
| QDIAT | bit | PK |  | SI | Declaración individual de Accidente del Trabajo N° |
| QEX | bit | PK |  | SI | Ex S.S.S. |
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
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*