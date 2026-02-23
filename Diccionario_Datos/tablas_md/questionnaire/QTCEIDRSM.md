# questionnaire.QTCEIDRSM

> Informe de Derivación Red Salud Mental

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Informe de Derivación Red Salud Mental

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombre |
| Q02 | varchar |  |  | SI | Apellido Paterno |
| Q03 | varchar |  |  | SI | Apellido Materno |
| Q04 | varchar |  |  | SI | N° Ced. Identidad |
| Q05 | varchar |  |  | SI | Fecha de Nacimiento |
| Q06 | varchar |  |  | SI | Domicilio |
| Q07 | varchar |  |  | SI | Tutor Responsable |
| Q08 | varchar |  |  | SI | Teléfono |
| Q09 | varchar |  |  | SI | Motivo de Consulta |
| Q10 | varchar |  |  | SI | Resumen História Clínica Relevante |
| Q11 | varchar |  |  | SI | Antecedentes Mórbidos Familiares (Especialmente En... |
| Q12 | varchar |  |  | SI | Otros Antecedentes de Importancia (Incluir Anteced... |
| Q13 | varchar |  |  | SI | Fármacos Usados |
| Q14 | varchar |  |  | SI | Número de la Dirección  |
| Q15 | varchar |  |  | SI | Etnia |
| Q16 | varchar |  |  | SI | Edad |
| Q17 | varchar |  |  | SI | Inserción en Sistema Escolar |
| Q18 | numeric |  |  | SI | Años de Deserción |
| Q19 | varchar |  |  | SI | Último Curso Rendido |
| Q20 | varchar |  |  | SI | Tipo de Vivienda |
| Q21 | varchar |  |  | SI | ¿Con quién vive? |
| Q22 | varchar |  |  | SI | Teléfono Contacto |
| Q23 | varchar |  |  | SI | Estado Conyugal |
| Q24 | numeric |  |  | SI | Hijos |
| Q25 | varchar |  |  | SI | Estado Ocupacional |
| Q26 | varchar |  |  | SI | Antecedentes Mórbidos (Enfermedades de Importancia... |
| Q27 | varchar |  |  | SI | Hipótesis diagnóstica (CIE-10) |
| Q28 | varchar |  |  | SI | Objetivos de Derivación |
| Q29 | varchar |  |  | SI | Centro de Referencia |
| Q30 | date |  |  | SI | Fecha de Derivación |
| Q31 | varchar |  |  | SI | Profesional que Deriva |
| Q32 | varchar |  |  | SI | Teléfono Celular |
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