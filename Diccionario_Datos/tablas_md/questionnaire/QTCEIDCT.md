# questionnaire.QTCEIDCT

> Informe de Derivación Centros de Tratamiento

**Schema:** questionnaire
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Informe de Derivación Centros de Tratamiento

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombre  |
| Q02 | varchar |  |  | SI | Apellido Paterno |
| Q03 | varchar |  |  | SI | Apellido Materno |
| Q04 | varchar |  |  | SI | N° Cédula de Identidad |
| Q05 | varchar |  |  | SI | Etnia |
| Q06 | varchar |  |  | SI | Fecha de Nacimiento |
| Q07 | varchar |  |  | SI | Edad |
| Q08 | varchar |  |  | SI | Inserción en sistema escolar |
| Q09 | numeric |  |  | SI | Años de deserción |
| Q10 | varchar |  |  | SI | Último curso rendido |
| Q11 | varchar |  |  | SI | Domicilio |
| Q12 | varchar |  |  | SI | Tipo de Vivienda |
| Q13 | varchar |  |  | SI | ¿Con quién vive? |
| Q14 | varchar |  |  | SI | Teléfono Contacto |
| Q15 | varchar |  |  | SI | Estado conyugal |
| Q16 | varchar |  |  | SI | Hijos |
| Q17 | numeric |  |  | SI | N° de hijos |
| Q18 | varchar |  |  | SI | Estado ocupacional |
| Q19 | varchar |  |  | SI | Tutor responsable |
| Q20 | varchar |  |  | SI | Teléfono Tutor |
| Q22 | varchar |  |  | SI | Centro de Referencia |
| Q23 | varchar |  |  | SI | Profesional que deriva |
| Q24 | date |  |  | SI | Fecha derivación |
| Q25 | varchar |  |  | SI | Número Dirección |
| Q26 | varchar |  |  | SI | Celular  |
| Q27 | varchar |  |  | SI | Motivo de Consulta |
| Q28 | varchar |  |  | SI | Resumen Historia Clínica Reciente |
| Q30 | numeric |  |  | SI | Número de Tratamientos Anteriores |
| Q31 | numeric |  |  | SI | Número Hospitalizaciones Anteriores |
| Q32 | numeric |  |  | SI | Número de Medidas Anteriores |
| Q33 | numeric |  |  | SI | Número de Sanciones |
| Q34 | varchar |  |  | SI | Edad de Primera Detención |
| Q35 | numeric |  |  | SI | Número de veces ingresado a CIP |
| Q36 | numeric |  |  | SI | Número de veces Ingresado a CRC |
| Q37 | numeric |  |  | SI | Número de Meses privado de Libertad |
| Q38 | varchar |  |  | SI | Embarazo |
| Q39 | varchar |  |  | SI | Embarazo ¿Por qué? |
| Q40 | varchar |  |  | SI | Parto |
| Q41 | varchar |  |  | SI | Parto ¿Por qué? |
| Q42 | varchar |  |  | SI | Patología Perinatal |
| Q43 | varchar |  |  | SI | Patología Perinatal ¿Cuál? |
| Q44 | varchar |  |  | SI | Desarrollo Psicomotor |
| Q45 | varchar |  |  | SI | De ser Anormal (Describa) |
| Q46 | varchar |  |  | SI | Antecedentes Mórbidos (Enfermedades de Importancia... |
| Q47 | varchar |  |  | SI | Otros Antecedentes de Importancia (Incluir anteced... |
| Q48 | varchar |  |  | SI | Antecedentes mórbidos familiares (Especialmente en... |
| Q49 | varchar |  |  | SI | Fármacos Usados |
| Q50 | bigint |  |  | SI | Genograma |
| Q50TxtOnly | bigint |  |  | SI | Genograma Plain Text Only |
| Q51 | varchar |  |  | SI | Trastornos Psiquiátricos |
| Q52 | varchar |  |  | SI | Nivel Intelectual |
| Q53 | varchar |  |  | SI | Patología Medica Asociada |
| Q54 | varchar |  |  | SI | Situación Psicosocial Asociada |
| Q55 | varchar |  |  | SI | CBPS |
| Q56 | varchar |  |  | SI | DLC |
| Q57 | varchar |  |  | SI | Estado Motivacional |
| Q58 | varchar |  |  | SI | Individual - Grupal |
| Q59 | varchar |  |  | SI | Familiar |
| Q60 | varchar |  |  | SI | Escolar |
| Q61 | varchar |  |  | SI | Social |
| Q62 | varchar |  |  | SI | Derivado a  |
| Q63 | varchar |  |  | SI | Derivado por  |
| Q64 | varchar |  |  | SI | Objetivo General de Derivación |
| Q65 | varchar |  |  | SI | Objetivos Específicos de Derivación |
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