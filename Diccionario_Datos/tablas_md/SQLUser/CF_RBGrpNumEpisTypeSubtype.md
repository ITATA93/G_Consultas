# SQLUser.CF_RBGrpNumEpisTypeSubtype

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GRPNUM_ParRef | bigint | PK |  | NO | - |
| GRPNUM_Childsub | double |  |  | NO | CF_RB Parent Reference
Childsub |
| GRPNUM_EpisSubtype_DR | bigint |  | FK | SI | Des Ref Episode Subtype |
| GRPNUM_EpisType_DR | varchar |  | FK | SI | Episode Type |
| GRPNUM_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Tipo de quemadura |
| Q02 | - |  |  | SI | Porcentaje de quemadura |
| Q03 | - |  |  | SI | Cultivo |
| Q04 | - |  |  | SI | Resultado Cultivo |
| Q05 | - |  |  | SI | Valoración de Heridas / Úlceras |
| Q06 | - |  |  | SI | Aspecto de la herida |
| Q07 | - |  |  | SI | Profundidad |
| Q08 | - |  |  | SI | Exudado cantidad |
| Q09 | - |  |  | SI | Exudado calidad |
| Q10 | - |  |  | SI | Tejido esfacelado o necrótico |
| Q11 | - |  |  | SI | Tejido granulatorio |
| Q12 | - |  |  | SI | Edema |
| Q13 | - |  |  | SI | Escala del dolor |
| Q14 | - |  |  | SI | Piel circundante |
| Q15 | - |  |  | SI | Acciones realizadas en la quemadura |
| Q16 | - |  |  | SI | Limpieza con agua destilada estéril |
| Q17 | - |  |  | SI | Limpieza con suero fisiológico 0,9% |
| Q18 | - |  |  | SI | Limpieza con Prontosan |
| Q19 | - |  |  | SI | Limpieza con Vashe |
| Q20 | - |  |  | SI | cantidad utilizada |
| Q21 | - |  |  | SI | Curación Avanzada de Heridas |
| Q22 | - |  |  | SI | Detalle |
| Q23 | - |  |  | SI | Otras acciones realizadas en la quemadura |
| Q24 | - |  |  | SI | Cobertura utilizada |
| Q25 | - |  |  | SI | Otra cobertura utilizada |
| Q26 | - |  |  | SI | Apósito interactivo |
| Q27 | - |  |  | SI | Otro apósito interactivo |
| Q28 | - |  |  | SI | Apósito bioactivo |
| Q29 | - |  |  | SI | Otro apósito bioactivo |
| Q30 | - |  |  | SI | Apósito mixo |
| Q31 | - |  |  | SI | Otro apósito mixto |
| Q32 | - |  |  | SI | Protector cutáneo |
| Q33 | - |  |  | SI | Otro protector cutáneo |
| Q34 | - |  |  | SI | Vendaje de fijación |
| Q35 | - |  |  | SI | Otro vendaje de fijación |
| Q36 | - |  |  | SI | Terapia de Presión Negativa (TPN) /&nbsp |
| Q37 | - |  |  | SI | cantidad utilizada |
| Q38 | - |  |  | SI | Detalle |
| Q39 | - |  |  | SI | cantidad utilizada |
| Q40 | - |  |  | SI | Detalle |
| Q41 | - |  |  | SI | cantidad utilizada |
| Q42 | - |  |  | SI | Detalle |
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