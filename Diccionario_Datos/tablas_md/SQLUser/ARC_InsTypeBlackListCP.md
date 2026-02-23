# SQLUser.ARC_InsTypeBlackListCP

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BLCP_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| BLCP_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| BLCP_Childsub | double |  |  | NO | Childsub |
| BLCP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BLCP_CreatedDate | date |  |  | SI | Created Date |
| BLCP_CreatedTime | time |  |  | SI | Created Time |
| BLCP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BLCP_DateFrom | date |  |  | SI | Date From |
| BLCP_DateTo | date |  |  | SI | Date To |
| BLCP_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| BLCP_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| BLCP_RowId | varchar |  |  | NO | - |
| BLCP_UpdatedDate | date |  |  | SI | Updated Date |
| BLCP_UpdatedTime | time |  |  | SI | Updated Time |
| BLCP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ04DR | - |  |  | SI | Child Reference: Vulva |
| Q01 | - |  |  | SI | Comentario Examen Ginecológico |
| Q02 | - |  |  | SI | Resto del Examen Ginecológico realizado, sin alter... |
| Q03 | - |  |  | SI | Inspección |
| Q05 | - |  |  | SI | Tacto Vaginal |
| Q06 | - |  |  | SI | Residuo Vaginal |
| Q07 | - |  |  | SI | Paredes vaginales elásticas. Mucosa vaginal normal... |
| Q08 | - |  |  | SI | Saco de Douglas libre |
| Q09 | - |  |  | SI | Cuello uterino de consistencia y tamaño normal |
| Q10 | - |  |  | SI | Útero en antero versión, de tamaño y consistencia ... |
| Q11 | - |  |  | SI | Flujo Vaginal normal |
| Q12 | - |  |  | SI | Anexos libres e indoloros |
| Q13 | - |  |  | SI | Parámetros normales |
| Q14 | - |  |  | SI | Labios mayores y menores de tamaño y aspecto norma... |
| Q15 | - |  |  | SI | Clítoris de tamaño y aspecto normal |
| Q16 | - |  |  | SI | Glándulas de Bartolino normales |
| Q17 | - |  |  | SI | Descripción Tacto Vaginal |
| Q18 | - |  |  | SI | Descripción Especuloscopía |
| Q19 | - |  |  | SI | Vagina de elasticidad conservada |
| Q20 | - |  |  | SI | Cuello central de coloración normal, sin lesiones ... |
| Q21 | - |  |  | SI | Descripción Examen Mamas |
| Q22 | - |  |  | SI | Mamas de tamaño y desarrollo normal, simétricas |
| Q23 | - |  |  | SI | No se palpan masas ni adenopatías locales |
| Q24 | - |  |  | SI | Pezones sin lesiones ni secreción anormal |
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