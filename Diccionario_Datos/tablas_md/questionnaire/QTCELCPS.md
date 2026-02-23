# questionnaire.QTCELCPS

**Schema:** questionnaire
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bit | PK |  | SI | Identidad |
| Q02 | bit | PK |  | SI | Brazalete |
| Q03 | bit | PK |  | SI | Ficha |
| Q04 | bit | PK |  | SI | Area Operatoria |
| Q05 | bit | PK |  | SI | Procedimiento Quirurgico |
| Q06 | bit | PK |  | SI | Consentimiento Quirurgico |
| Q07 | bit | PK |  | SI | Area Operatoria Marcada |
| Q08 | bit | PK |  | SI | No Aplica |
| Q09 | bit | PK |  | SI | Medias Antiembolicas |
| Q10 | bit | PK |  | SI | No aplica |
| Q11 | bit | PK |  | SI | Chequeo Seguridad Anestesica |
| Q12 | bit | PK |  | SI | Consentimiento Anestesico |
| Q13 | bit | PK |  | SI | Oximetro de Pulso instalado y funcionando |
| Q14 | varchar | PK |  | SI | Alergias conocidas |
| Q15 | varchar | PK |  | SI | Via aerea dificil |
| Q16 | varchar | PK |  | SI | Riesgo de Aspiracion |
| Q17 | varchar | PK |  | SI | Riesgo sangramiento > 500 ml.  ( 7ML/KG en niños) |
| Q18 | bit | PK |  | SI | Confirmacion miembros del equipo |
| Q19 | bit | PK |  | SI | Identidad del paciente |
| Q20 | bit | PK |  | SI | Area Operatoria |
| Q21 | bit | PK |  | SI | Procedimiento quirúrgico |
| Q22 | bit | PK |  | SI | Escenarios Imprevistos |
| Q23 | bit | PK |  | SI | Duración estimada cirugía |
| Q24 | bit | PK |  | SI | Pérdidas de sangres estimadas |
| Q25 | bit | PK |  | SI | Otros |
| Q26 | bit | PK |  | SI |  Equipo Anestesia revisa |
| Q27 | bit | PK |  | SI | Ropa |
| Q28 | bit | PK |  | SI | Instrumental |
| Q29 | bit | PK |  | SI | Funcionamiento correcto de equipos |
| Q30 | varchar | PK |  | SI | ¿ Se realizó profilaxis antibiótica? |
| Q31 | varchar | PK |  | SI | ¿Se ha desplegado la imagenología necesaria?  |
| Q32 | bit | PK |  | SI | El nombre del procedimiento realizado |
| Q33 | bit | PK |  | SI | Conteo instrumental correcto |
| Q34 | varchar | PK |  | SI | Conteo compresas correcto |
| Q35 | bit | PK |  | SI | Conteo agujas correcto |
| Q36 | bit | PK |  | SI | No Aplica        |
| Q37 | bit | PK |  | SI | No Aplica |
| Q38 | bit | PK |  | SI | Nombre completo del paciente |
| Q39 | bit | PK |  | SI | RUT del paciente |
| Q40 | bit | PK |  | SI |  Fecha de toma de la muestra |
| Q41 | bit | PK |  | SI | Identificación clara del tejido u órgano y  locali... |
| Q42 | bit | PK |  | SI | Numeración de la muestra en caso de haber más de u... |
| Q43 | varchar | PK |  | SI | Problema Equipamiento |
| Q44 | varchar | PK |  | SI | Revision datos importantes para la recuperacion |
| Q45 | varchar | PK |  | SI | Se confirma que todos los miembros del equipo se h... |
| Q46 | varchar | PK |  | SI | El nombre del procedimiento realizado |
| Q47 | varchar | PK |  | SI | Conteo instrumental correcto |
| Q48 | varchar | PK |  | SI | Conteo agujas correcto |
| Q49 | varchar | PK |  | SI | Nombre completo del paciente  |
| Q50 | varchar | PK |  | SI | RUT del paciente |
| Q51 | varchar | PK |  | SI | Fecha de toma de la muestra |
| Q52 | varchar | PK |  | SI | Identificación clara del tejido u órgano y localiz... |
| Q53 | varchar | PK |  | SI | Numeración de la muestra en caso de haber más de u... |
| Q54 | varchar | PK |  | SI | Problema Equipamiento |
| Q55 | varchar | PK |  | SI | Revision datos importantes para la recuperacion |
| Q56 | varchar | PK |  | SI | Conteo de Compresas |
| Q57 | varchar | PK |  | SI | Observaciones |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*