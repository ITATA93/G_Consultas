# SQLUser.LBC_TestSetRevisionProfile

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRPR_ParRef | bigint | PK |  | NO | Parent Revision |
| LBCTSRPR_CareProviders | varchar |  |  | SI | Care provider |
| LBCTSRPR_ClinicalConditions | varchar |  |  | SI | Clinical Conditions |
| LBCTSRPR_Code | varchar |  |  | NO | Code |
| LBCTSRPR_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| LBCTSRPR_Desc | varchar |  |  | NO | Description |
| LBCTSRPR_LabSiteLocations | varchar |  |  | SI | Lab Episode Locations |
| LBCTSRPR_PatientLocations | varchar |  |  | SI | Patient Locations |
| LBCTSRPR_ReferringDoctors | varchar |  |  | SI | Referring Doctors |
| LBCTSRPR_RowID | varchar |  |  | NO | - |
| LBCTSRPR_Sequence | double |  |  | SI | Profile Sequence |
| LBCTSRPR_Species | varchar |  |  | SI | Species |
| LBCTSRPR_SpeciesBreeds | varchar |  |  | SI | Breeds |
| LBCTSRPR_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| Q005 | - |  |  | SI | Diagnóstico Clínico |
| Q01 | - |  |  | SI | VIH |
| Q02 | - |  |  | SI | HBsAg |
| Q03 | - |  |  | SI | HVC |
| Q04 | - |  |  | SI | OTRAS ESPECIFICACIONES: |
| Q05 | - |  |  | SI | DIAGNÓSTICO CLÍNICO |
| Q06 | - |  |  | SI | Condición de riesgo |
| Q07 | - |  |  | SI | Fecha de Examen |
| Q08 | - |  |  | SI | Responsable |
| Q09 | - |  |  | SI | Sexo |
| Q10 | - |  |  | SI | Procedencia |
| Q11 | - |  |  | SI | Servicio |
| Q12 | - |  |  | SI | FECHA DE NACIMIENTO |
| Q13 | - |  |  | SI | Nombre |
| Q14 | - |  |  | SI | NACIONALIDAD |
| Q15 | - |  |  | SI | F |
| Q16 | - |  |  | SI | M |
| Q17 | - |  |  | SI | N° Ficha |
| Q18 | - |  |  | SI | Código SURVIH |
| Q19 | - |  |  | SI | RUN |
| Q20 | - |  |  | SI | DIRECCIÓN |
| Q21 | - |  |  | SI | COMUNA |
| Q22 | - |  |  | SI | Fono Paciente |
| Q23 | - |  |  | SI | N° Embarazo |
| Q24 | - |  |  | SI | Semanas de gestación |
| Q25 | - |  |  | SI | NOMBRE Y FIRMA DEL MÉDICO / MATRONA |
| Q27 | - |  |  | SI | Sexo |
| Q28 | - |  |  | SI | Fecha de Nacimiento |
| Q29 | - |  |  | SI | Nombre |
| Q30 | - |  |  | SI | Nacionalidad |
| Q31 | - |  |  | SI | Apellido paterno |
| Q32 | - |  |  | SI | Apellido materno |
| Q33 | - |  |  | SI | RUN |
| Q34 | - |  |  | SI | Dirección |
| Q35 | - |  |  | SI | VIH Embarazada (1°) |
| Q36 | - |  |  | SI | VIH Embarazada (2°) |
| Q37 | - |  |  | SI | Chagas |
| Q38 | - |  |  | SI | Sala |
| Q39 | - |  |  | SI | Comuna |
| Q40 | - |  |  | SI | Nº Ficha |
| Q41 | - |  |  | SI | Servicio |
| Q42 | - |  |  | SI | Clave1 |
| Q43 | - |  |  | SI | Clave2 |
| Q44 | - |  |  | SI | Clave3 |
| Q45 | - |  |  | SI | Clave4 |
| Q46 | - |  |  | SI | Prueba de identidad |
| Q47 | - |  |  | SI | Sintomático |
| Q48 | - |  |  | SI | Factores de riesgo |
| Q49 | - |  |  | SI | Otro factor |
| Q50 | - |  |  | SI | Grupo de pesquisa |
| Q51 | - |  |  | SI | Hora de examen |
| Q52 | - |  |  | SI | Observaciones |
| Q53 | - |  |  | SI | Profesional solicitante |
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