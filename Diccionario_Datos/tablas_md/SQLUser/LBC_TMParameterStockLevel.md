# SQLUser.LBC_TMParameterStockLevel

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTMPSL_ParRef | bigint | PK |  | NO | Tranfusion Medicine Parameter Parent  |
| LBCTMPSL_BloodGroup_DR | bigint |  | FK | NO | Blood Group |
| LBCTMPSL_BloodProductGroup_DR | bigint |  | FK | SI | Blood Product Group |
| LBCTMPSL_BloodProduct_DR | bigint |  | FK | SI | Blood Product |
| LBCTMPSL_DefaultQuantity | numeric |  |  | SI | Default quantity |
| LBCTMPSL_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Nombre |
| Q02 | - |  |  | SI | Apellido Paterno |
| Q03 | - |  |  | SI | Apellido Materno |
| Q04 | - |  |  | SI | N° Ced. Identidad |
| Q05 | - |  |  | SI | Fecha de Nacimiento |
| Q06 | - |  |  | SI | Domicilio |
| Q07 | - |  |  | SI | Tutor Responsable |
| Q08 | - |  |  | SI | Teléfono |
| Q09 | - |  |  | SI | Motivo de Consulta |
| Q10 | - |  |  | SI | Resumen História Clínica Relevante |
| Q11 | - |  |  | SI | Antecedentes Mórbidos Familiares (Especialmente En... |
| Q12 | - |  |  | SI | Otros Antecedentes de Importancia (Incluir Anteced... |
| Q13 | - |  |  | SI | Fármacos Usados |
| Q14 | - |  |  | SI | Número de la Dirección |
| Q15 | - |  |  | SI | Etnia |
| Q16 | - |  |  | SI | Edad |
| Q17 | - |  |  | SI | Inserción en Sistema Escolar |
| Q18 | - |  |  | SI | Años de Deserción |
| Q19 | - |  |  | SI | Último Curso Rendido |
| Q20 | - |  |  | SI | Tipo de Vivienda |
| Q21 | - |  |  | SI | ¿Con quién vive? |
| Q22 | - |  |  | SI | Teléfono Contacto |
| Q23 | - |  |  | SI | Estado Conyugal |
| Q24 | - |  |  | SI | Hijos |
| Q25 | - |  |  | SI | Estado Ocupacional |
| Q26 | - |  |  | SI | Antecedentes Mórbidos (Enfermedades de Importancia... |
| Q27 | - |  |  | SI | Hipótesis diagnóstica (CIE-10) |
| Q28 | - |  |  | SI | Objetivos de Derivación |
| Q29 | - |  |  | SI | Centro de Referencia |
| Q30 | - |  |  | SI | Fecha de Derivación |
| Q31 | - |  |  | SI | Profesional que Deriva |
| Q32 | - |  |  | SI | Teléfono Celular |
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