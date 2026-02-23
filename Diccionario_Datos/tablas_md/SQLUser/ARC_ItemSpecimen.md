# SQLUser.ARC_ItemSpecimen

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPEC_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| Q01 | - |  |  | SI | Solicitud de Procedimiento |
| Q02 | - |  |  | SI | Ayunas |
| Q03 | - |  |  | SI | Comentario Ayunas |
| Q04 | - |  |  | SI | Exámenes preoperatorios |
| Q05 | - |  |  | SI | PCR Covid |
| Q06 | - |  |  | SI | Fecha |
| Q07 | - |  |  | SI | Resultado |
| Q08 | - |  |  | SI | Estudio imagenológico previo |
| Q09 | - |  |  | SI | Brazalete |
| Q10 | - |  |  | SI | Retiro prótesis dental |
| Q11 | - |  |  | SI | Rasurado |
| Q12 | - |  |  | SI | Ubicación |
| Q13 | - |  |  | SI | Pase anestésico |
| Q14 | - |  |  | SI | Pase especialidad |
| Q15 | - |  |  | SI | Comentario pase especialidad |
| Q16 | - |  |  | SI | Información al usuario de servicio o familiar |
| Q17 | - |  |  | SI | Consentimiento informado |
| Q18 | - |  |  | SI | Cama de egreso |
| Q19 | - |  |  | SI | Comentario cama de egreso |
| Q20 | - |  |  | SI | Alergias |
| Q21 | - |  |  | SI | Comentario alergias |
| Q22 | - |  |  | SI | FUR |
| Q23 | - |  |  | SI | Fecha FUR |
| Q24 | - |  |  | SI | Motivo de Atraso |
| Q25 | - |  |  | SI | Motivo de Atraso |
| Q26 | - |  |  | SI | Otro motivo |
| Q27 | - |  |  | SI | Responsable |
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
| SPEC_Childsub | double |  |  | NO | Childsub |
| SPEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SPEC_CreatedDate | date |  |  | SI | Created Date |
| SPEC_CreatedTime | time |  |  | SI | Created Time |
| SPEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SPEC_DateFrom | date |  |  | SI | Date From |
| SPEC_DateTo | date |  |  | SI | Date To |
| SPEC_Default | varchar |  |  | SI | Default |
| SPEC_RowId | varchar |  |  | NO | - |
| SPEC_Specimen_DR | varchar |  | FK | SI | Des Ref Specimen |
| SPEC_UpdatedDate | date |  |  | SI | Updated Date |
| SPEC_UpdatedTime | time |  |  | SI | Updated Time |
| SPEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*