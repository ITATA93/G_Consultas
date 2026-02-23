# SQLUser.MRC_PhyESystemFinding

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPhyEF_ParRef | varchar | PK |  | NO | OEC_ConsultCateg Parent Reference |
| CTPhyEF_Childsub | double |  |  | NO | Childsub |
| CTPhyEF_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| CTPhyEF_CreatedDate | date |  |  | SI | Created Date |
| CTPhyEF_CreatedTime | time |  |  | SI | Created Time |
| CTPhyEF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTPhyEF_DateFrom | date |  |  | SI | Date From |
| CTPhyEF_DateTo | date |  |  | SI | Date To |
| CTPhyEF_ICDCode_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| CTPhyEF_ICPCCode_DR | bigint |  | FK | SI | Des Ref PACICPCCode |
| CTPhyEF_RowId | varchar |  |  | NO | - |
| CTPhyEF_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| CTPhyEF_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| CTPhyEF_UpdatedDate | date |  |  | SI | Updated Date |
| CTPhyEF_UpdatedTime | time |  |  | SI | Updated Time |
| CTPhyEF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Inquieto, demasiado activo |
| Q02 | - |  |  | SI | Excitable, Impulsivo |
| Q03 | - |  |  | SI | Molesta a otros niños |
| Q04 | - |  |  | SI | No termina lo que comienza |
| Q05 | - |  |  | SI | Se mueve constantemente |
| Q06 | - |  |  | SI | Se distrae con facilidad |
| Q07 | - |  |  | SI | Hay que satisfacerle de inmediato |
| Q08 | - |  |  | SI | Llora con facilidad |
| Q09 | - |  |  | SI | Cambia de humor bruscamente |
| Q10 | - |  |  | SI | Pataletas |
| Q11 | - |  |  | SI | RESPECTO A SU APRENDIZAJE |
| Q12 | - |  |  | SI | ¿Su lectura es poco fluida o silabeante? |
| Q13 | - |  |  | SI | ¿Le cuesta comprender lo que ha leído? |
| Q14 | - |  |  | SI | ¿Le cuesta escribir al dictado? |
| Q15 | - |  |  | SI | ¿Tiene dificultades para copiar a tiempo lo leído ... |
| Q16 | - |  |  | SI | ¿Comete muchas faltas de ortografía? |
| Q17 | - |  |  | SI | ¿Le cuesta demasiado el cálculo matemático? |
| Q18 | - |  |  | SI | POR FAVOR INDÍQUENOS |
| Q19 | - |  |  | SI | ¿Recibe medicación en la escuela? |
| Q20 | - |  |  | SI | ¿Ha notado mejoría en conducta? |
| Q21 | - |  |  | SI | PONGA NOTA DE 1 A 7 |
| Q22 | - |  |  | SI | A su conducta |
| Q23 | - |  |  | SI | A su rendimiento |
| Q24 | - |  |  | SI | A la relación con sus profesores |
| Q25 | - |  |  | SI | A la relación con sus compañeros |
| Q26 | - |  |  | SI | Resultado Test de Conners |
| Q26ObsDR | - |  |  | SI | Resultado Test de Conners DR |
| Q27 | - |  |  | SI | Nivel Educacional |
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