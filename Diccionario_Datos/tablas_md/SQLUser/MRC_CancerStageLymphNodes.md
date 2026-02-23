# SQLUser.MRC_CancerStageLymphNodes

**Schema:** SQLUser
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NODE_ParRef | bigint | PK |  | NO | Parent Reference |
| NODE_Childsub | double |  |  | NO | Childsub |
| NODE_CodeTableTags | varchar |  |  | SI | List of Code Table Tags |
| NODE_CreatedDate | date |  |  | SI | Created Date |
| NODE_CreatedTime | time |  |  | SI | Created Time |
| NODE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NODE_DateFrom | date |  |  | SI | Date From |
| NODE_DateTo | date |  |  | SI | Date To |
| NODE_Desc | varchar |  |  | SI | Description |
| NODE_RowId | varchar |  |  | NO | - |
| NODE_Stage | varchar |  |  | SI | Nodal Stage |
| NODE_UpdatedDate | date |  |  | SI | Updated Date |
| NODE_UpdatedTime | time |  |  | SI | Updated Time |
| NODE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Clave Definitiva |
| Q02 | - |  |  | SI | RUT |
| Q03 | - |  |  | SI | Clave Recién Nacido |
| Q04 | - |  |  | SI | Sexo |
| Q05 | - |  |  | SI | Edad |
| Q06 | - |  |  | SI | Años |
| Q07 | - |  |  | SI | Días |
| Q08 | - |  |  | SI | Clave Materna |
| Q09 | - |  |  | SI | N° ISP Materno |
| Q10 | - |  |  | SI | Cod. Establecimiento |
| Q11 | - |  |  | SI | Profesional Responsable |
| Q12 | - |  |  | SI | Hospital / Laboratorio |
| Q13 | - |  |  | SI | Unidad |
| Q14 | - |  |  | SI | RUT Profesional |
| Q15 | - |  |  | SI | Dirección |
| Q16 | - |  |  | SI | Región |
| Q17 | - |  |  | SI | Comuna |
| Q18 | - |  |  | SI | Fono |
| Q19 | - |  |  | SI | Fax |
| Q20 | - |  |  | SI | Mail |
| Q21 | - |  |  | SI | Fecha de Obtención |
| Q22 | - |  |  | SI | Hora |
| Q23 | - |  |  | SI | Tipo de Muestra |
| Q24 | - |  |  | SI | N° de Muestra |
| Q25 | - |  |  | SI | Otro |
| Q26 | - |  |  | SI | Cod.SurVIH |
| Q27 | - |  |  | SI | Datos Clínicos |
| Q28 | - |  |  | SI | Diagnóstico |
| Q29 | - |  |  | SI | Protocolo de transmisión vertical |
| Q30 | - |  |  | SI | Terapia |
| Q31 | - |  |  | SI | Madre VIH (+) |
| Q32 | - |  |  | SI | Otro Factor |
| Q33 | - |  |  | SI | Clave 2 |
| Q34 | - |  |  | SI | Clave 3 |
| Q35 | - |  |  | SI | Clave 4 |
| Q36 | - |  |  | SI | Meses |
| Q37 | - |  |  | SI | Años |
| Q38 | - |  |  | SI | Sexo |
| Q39 | - |  |  | SI | RUT de la madre |
| Q40 | - |  |  | SI | Nacionalidad de la madre |
| Q41 | - |  |  | SI | 4.1 Técnica Visual |
| Q42 | - |  |  | SI | Otra |
| Q43 | - |  |  | SI | Lote |
| Q44 | - |  |  | SI | Vencimiento |
| Q45 | - |  |  | SI | 4.2 Técnica Instrumental |
| Q46 | - |  |  | SI | Otra |
| Q47 | - |  |  | SI | Reactividad |
| Q48 | - |  |  | SI | Cut-Off |
| Q49 | - |  |  | SI | Reactividad 2 |
| Q50 | - |  |  | SI | Cut-Off 2 |
| Q51 | - |  |  | SI | Reactividad 3 |
| Q52 | - |  |  | SI | Cut-Off 3 |
| Q53 | - |  |  | SI | Lote |
| Q54 | - |  |  | SI | Vencimiento |
| Q55 | - |  |  | SI | Hijo de Madre en Proceso de Confirmación VIH |
| Q56 | - |  |  | SI | Nacionalidad |
| Q57 | - |  |  | SI | N° Solicitud |
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