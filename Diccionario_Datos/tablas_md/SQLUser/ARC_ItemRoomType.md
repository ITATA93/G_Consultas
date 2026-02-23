# SQLUser.ARC_ItemRoomType

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROOMT_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| Q01 | - |  |  | SI | Chequeo Pre By-pass |
| Q02 | - |  |  | SI | Módulos |
| Q03 | - |  |  | SI | Oclusividad Art - CP - V - A |
| Q04 | - |  |  | SI | Conexión Eléctrica |
| Q05 | - |  |  | SI | Conexión 02-Aire |
| Q06 | - |  |  | SI | Centrífuga Bioprofe |
| Q07 | - |  |  | SI | Oxigenador |
| Q08 | - |  |  | SI | Modelo |
| Q09 | - |  |  | SI | Integridad Envoltorios |
| Q10 | - |  |  | SI | Salida Gas Libre |
| Q11 | - |  |  | SI | Líneas |
| Q12 | - |  |  | SI | Dirección Correcta |
| Q13 | - |  |  | SI | Conexiones Aseguradas |
| Q14 | - |  |  | SI | Circuito Desburbujado |
| Q15 | - |  |  | SI | Fuente de Gas |
| Q16 | - |  |  | SI | Flujómetro - Blender |
| Q17 | - |  |  | SI | Cardioplejía |
| Q18 | - |  |  | SI | Solución Chequeada |
| Q19 | - |  |  | SI | Intercambiador |
| Q20 | - |  |  | SI | Probe Temperatura |
| Q21 | - |  |  | SI | Conexión Plejía |
| Q22 | - |  |  | SI | Drogas |
| Q23 | - |  |  | SI | Heparina Circuito |
| Q24 | - |  |  | SI | Antibiótico |
| Q25 | - |  |  | SI | Comentario Antibiótico |
| Q26 | - |  |  | SI | Antifibrinolítico |
| Q27 | - |  |  | SI | Comentario Antifibrinolítico |
| Q28 | - |  |  | SI | Relajante |
| Q29 | - |  |  | SI | Comentario Relajante |
| Q30 | - |  |  | SI | Seguridad |
| Q31 | - |  |  | SI | Oxigenador de Repuesto |
| Q32 | - |  |  | SI | Líneas de Repuesto |
| Q33 | - |  |  | SI | Clamp |
| Q34 | - |  |  | SI | Manivelas |
| Q35 | - |  |  | SI | Linterna |
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
| ROOMT_Childsub | double |  |  | NO | Childsub |
| ROOMT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ROOMT_CreatedDate | date |  |  | SI | Created Date |
| ROOMT_CreatedTime | time |  |  | SI | Created Time |
| ROOMT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ROOMT_Days | double |  |  | NO | Days |
| ROOMT_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| ROOMT_RowId | varchar |  |  | NO | - |
| ROOMT_UpdatedDate | date |  |  | SI | Updated Date |
| ROOMT_UpdatedTime | time |  |  | SI | Updated Time |
| ROOMT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*