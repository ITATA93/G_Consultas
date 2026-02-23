# SQLUser.LB_TestSetSnomedGroup

**Schema:** SQLUser
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTSSG_ParRef | bigint | PK |  | NO | - |
| ChildQ21DR | - |  |  | SI | Child Reference: Causas Pendientes |
| LBTSSG_FullySpecifiedName | varchar |  |  | SI | Fully Specified Name |
| LBTSSG_RowID | varchar |  |  | NO | - |
| LBTSSG_SnomedTermDR | bigint |  | FK | SI | referance to PACSnomedTerms(SNOMED CT)  |
| Q01 | - |  |  | SI | Nombre |
| Q02 | - |  |  | SI | Apellido Paterno |
| Q03 | - |  |  | SI | Apellido Materno |
| Q04 | - |  |  | SI | N° Cédula de Identidad |
| Q05 | - |  |  | SI | Etnia |
| Q06 | - |  |  | SI | Fecha de Nacimiento |
| Q07 | - |  |  | SI | Edad |
| Q08 | - |  |  | SI | Inserción en sistema escolar |
| Q09 | - |  |  | SI | Años de deserción |
| Q10 | - |  |  | SI | Último curso rendido |
| Q11 | - |  |  | SI | Domicilio |
| Q12 | - |  |  | SI | Tipo de Vivienda |
| Q13 | - |  |  | SI | ¿Con quién vive? |
| Q14 | - |  |  | SI | Teléfono Contacto |
| Q15 | - |  |  | SI | Estado conyugal |
| Q16 | - |  |  | SI | Hijos |
| Q17 | - |  |  | SI | N° de hijos |
| Q18 | - |  |  | SI | Estado ocupacional |
| Q19 | - |  |  | SI | Tutor responsable |
| Q20 | - |  |  | SI | Teléfono Tutor |
| Q22 | - |  |  | SI | Centro de Referencia |
| Q23 | - |  |  | SI | Profesional que deriva |
| Q24 | - |  |  | SI | Fecha derivación |
| Q25 | - |  |  | SI | Número Dirección |
| Q26 | - |  |  | SI | Celular |
| Q27 | - |  |  | SI | Motivo de Consulta |
| Q28 | - |  |  | SI | Resumen Historia Clínica Reciente |
| Q30 | - |  |  | SI | Número de Tratamientos Anteriores |
| Q31 | - |  |  | SI | Número Hospitalizaciones Anteriores |
| Q32 | - |  |  | SI | Número de Medidas Anteriores |
| Q33 | - |  |  | SI | Número de Sanciones |
| Q34 | - |  |  | SI | Edad de Primera Detención |
| Q35 | - |  |  | SI | Número de veces ingresado a CIP |
| Q36 | - |  |  | SI | Número de veces Ingresado a CRC |
| Q37 | - |  |  | SI | Número de Meses privado de Libertad |
| Q38 | - |  |  | SI | Embarazo |
| Q39 | - |  |  | SI | Embarazo ¿Por qué? |
| Q40 | - |  |  | SI | Parto |
| Q41 | - |  |  | SI | Parto ¿Por qué? |
| Q42 | - |  |  | SI | Patología Perinatal |
| Q43 | - |  |  | SI | Patología Perinatal ¿Cuál? |
| Q44 | - |  |  | SI | Desarrollo Psicomotor |
| Q45 | - |  |  | SI | De ser Anormal (Describa) |
| Q46 | - |  |  | SI | Antecedentes Mórbidos (Enfermedades de Importancia... |
| Q47 | - |  |  | SI | Otros Antecedentes de Importancia (Incluir anteced... |
| Q48 | - |  |  | SI | Antecedentes mórbidos familiares (Especialmente en... |
| Q49 | - |  |  | SI | Fármacos Usados |
| Q50 | - |  |  | SI | Genograma |
| Q50TxtOnly | - |  |  | SI | Genograma Plain Text Only |
| Q51 | - |  |  | SI | Trastornos Psiquiátricos |
| Q52 | - |  |  | SI | Nivel Intelectual |
| Q53 | - |  |  | SI | Patología Medica Asociada |
| Q54 | - |  |  | SI | Situación Psicosocial Asociada |
| Q55 | - |  |  | SI | CBPS |
| Q56 | - |  |  | SI | DLC |
| Q57 | - |  |  | SI | Estado Motivacional |
| Q58 | - |  |  | SI | Individual - Grupal |
| Q59 | - |  |  | SI | Familiar |
| Q60 | - |  |  | SI | Escolar |
| Q61 | - |  |  | SI | Social |
| Q62 | - |  |  | SI | Derivado a |
| Q63 | - |  |  | SI | Derivado por |
| Q64 | - |  |  | SI | Objetivo General de Derivación |
| Q65 | - |  |  | SI | Objetivos Específicos de Derivación |
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