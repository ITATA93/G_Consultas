# SQLUser.ARC_BillClaimStatus

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BILLCLST_RowId | bigint | PK |  | NO | - |
| BILLCLST_Code | varchar |  |  | NO | Code |
| BILLCLST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BILLCLST_CreatedDate | date |  |  | SI | Created Date |
| BILLCLST_CreatedTime | time |  |  | SI | Created Time |
| BILLCLST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BILLCLST_DateFrom | date |  |  | SI | Date From |
| BILLCLST_DateTo | date |  |  | SI | Date To |
| BILLCLST_Desc | varchar |  |  | NO | Description |
| BILLCLST_Owner | varchar |  |  | SI | Owner |
| BILLCLST_UpdatedDate | date |  |  | SI | Updated Date |
| BILLCLST_UpdatedTime | time |  |  | SI | Updated Time |
| BILLCLST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ30DR | - |  |  | SI | Child Reference: Antecedentes del Cuidador |
| Q01 | - |  |  | SI | 1. ANTECEDENTES DEL PACIENTE |
| Q02 | - |  |  | SI | Nombre del Paciente |
| Q03 | - |  |  | SI | Edad del Paciente |
| Q04 | - |  |  | SI | N° Ficha Clínica |
| Q05 | - |  |  | SI | Domicilio del Paciente |
| Q06 | - |  |  | SI | Número Domicilio |
| Q07 | - |  |  | SI | RUN |
| Q08 | - |  |  | SI | Diagnóstico |
| Q09 | - |  |  | SI | Servicio de Origen del Paciente |
| Q10 | - |  |  | SI | Fecha Ingreso Programa H.D. |
| Q11 | - |  |  | SI | Evaluación Paciente o Cuidador al Egreso Hospitala... |
| Q12 | - |  |  | SI | Funcionarios Requeridos en la Visita al Paciente |
| Q13 | - |  |  | SI | 2. ANTECEDENTES CUIDADOR Y FAMILIARES |
| Q14 | - |  |  | SI | Nombre Cuidador |
| Q15 | - |  |  | SI | Parentesco Cuidador |
| Q16 | - |  |  | SI | Teléfono Cuidador |
| Q17 | - |  |  | SI | N° Integrante |
| Q18 | - |  |  | SI | Detalle |
| Q19 | - |  |  | SI | Otros Funcionarios |
| Q20 | - |  |  | SI | 3. FECHA DE TERMINO HOSPITALIZACIÓN DOMICILIARIA |
| Q21 | - |  |  | SI | Días de Estada en Programa H.D. |
| Q22 | - |  |  | SI | Contrareferencia con la Red de salud |
| Q23 | - |  |  | SI | Evaluación Paciente o Cuidador al Egreso H.D. |
| Q24 | - |  |  | SI | Apellido Paterno |
| Q25 | - |  |  | SI | Apellido Materno |
| Q26 | - |  |  | SI | Satifacción Usuario con Programa H.D. |
| Q27 | - |  |  | SI | Nombre de los Profesionales |
| Q28 | - |  |  | SI | Indicación de Nutrición Enteral Domiciliaria (NED) |
| Q29 | - |  |  | SI | 4. REM P3 Sección A |
| Q31 | - |  |  | SI | Tipo de Cupos Asignado |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*