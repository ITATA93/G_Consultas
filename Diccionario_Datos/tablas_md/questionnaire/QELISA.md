# questionnaire.QELISA

> Solicitud de Exámenes Microbiológicos método presuntivo no confirmatorio (ELISA)

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Solicitud de Exámenes Microbiológicos método presuntivo no confirmatorio (ELISA)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q005 | varchar |  |  | SI | Diagnóstico Clínico |
| Q01 | bit |  |  | SI | VIH |
| Q02 | bit |  |  | SI | HBsAg |
| Q03 | bit |  |  | SI | HVC |
| Q04 | varchar |  |  | SI | OTRAS ESPECIFICACIONES: |
| Q05 | varchar |  |  | SI | DIAGNÓSTICO CLÍNICO |
| Q06 | varchar |  |  | SI | Condición de riesgo |
| Q07 | date |  |  | SI | Fecha de Examen |
| Q08 | varchar |  |  | SI | Responsable |
| Q09 | varchar |  |  | SI | Sexo |
| Q10 | varchar |  |  | SI | Procedencia |
| Q11 | varchar |  |  | SI | Servicio |
| Q12 | date |  |  | SI | FECHA DE NACIMIENTO |
| Q13 | varchar |  |  | SI | Nombre |
| Q14 | varchar |  |  | SI | NACIONALIDAD |
| Q15 | bit |  |  | SI | F |
| Q16 | bit |  |  | SI | M |
| Q17 | varchar |  |  | SI | N° Ficha |
| Q18 | varchar |  |  | SI | Código SURVIH |
| Q19 | varchar |  |  | SI | RUN |
| Q20 | varchar |  |  | SI | DIRECCIÓN |
| Q21 | varchar |  |  | SI | COMUNA |
| Q22 | varchar |  |  | SI | Fono Paciente |
| Q23 | varchar |  |  | SI | N° Embarazo |
| Q24 | varchar |  |  | SI | Semanas de gestación |
| Q25 | varchar |  |  | SI | NOMBRE Y FIRMA DEL MÉDICO / MATRONA  |
| Q27 | varchar |  |  | SI | Sexo |
| Q28 | varchar |  |  | SI | Fecha de Nacimiento |
| Q29 | varchar |  |  | SI | Nombre |
| Q30 | varchar |  |  | SI | Nacionalidad |
| Q31 | varchar |  |  | SI | Apellido paterno |
| Q32 | varchar |  |  | SI | Apellido materno |
| Q33 | varchar |  |  | SI | RUN |
| Q34 | varchar |  |  | SI | Dirección |
| Q35 | bit |  |  | SI | VIH Embarazada (1°) |
| Q36 | bit |  |  | SI | VIH Embarazada (2°) |
| Q37 | bit |  |  | SI | Chagas |
| Q38 | varchar |  |  | SI | Sala |
| Q39 | varchar |  |  | SI | Comuna |
| Q40 | varchar |  |  | SI | Nº Ficha |
| Q41 | varchar |  |  | SI | Servicio |
| Q42 | varchar |  |  | SI | Clave1 |
| Q43 | varchar |  |  | SI | Clave2 |
| Q44 | varchar |  |  | SI | Clave3 |
| Q45 | varchar |  |  | SI | Clave4 |
| Q46 | varchar |  |  | SI | Prueba de identidad |
| Q47 | varchar |  |  | SI | Sintomático |
| Q48 | varchar |  |  | SI | Factores de riesgo |
| Q49 | varchar |  |  | SI | Otro factor |
| Q50 | varchar |  |  | SI | Grupo de pesquisa |
| Q51 | time |  |  | SI | Hora de examen |
| Q52 | varchar |  |  | SI | Observaciones |
| Q53 | varchar |  |  | SI | Profesional solicitante |
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