# SQLUser.ARC_OrdSetDateItem

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | varchar | PK |  | NO | ARC_OrdSetDate Parent Reference |
| ITM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ITM_AddUpToQty | double |  |  | SI | Add Up To Qty |
| ITM_AdminRoute_DR | bigint |  | FK | SI | Des Ref PHCAdministrationRoute |
| ITM_ApprovalMainOrder | varchar |  |  | SI | [DEPRECATED]Change of logic by TC-395628[/DEPRECAT... |
| ITM_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITM_CompService_DR | varchar |  | FK | SI | Complementary Service |
| ITM_Conditional | varchar |  |  | SI | Conditional |
| ITM_CreatedDate | date |  |  | SI | Created Date |
| ITM_CreatedTime | time |  |  | SI | Created Time |
| ITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITM_DayIncrement | numeric |  |  | SI | Start date increment |
| ITM_DoseQty | double |  |  | SI | Dose Qty |
| ITM_Durat_DR | bigint |  | FK | SI | Des Ref Duration |
| ITM_Freq_DR | bigint |  | FK | SI | Des Ref Freq |
| ITM_IVType | varchar |  |  | SI | IVType |
| ITM_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| ITM_Instruc_DR | bigint |  | FK | SI | Des Ref Instruc |
| ITM_Line | varchar |  |  | SI | Line No |
| ITM_LinkDoctor | double |  |  | SI | Link for Doctor |
| ITM_LinkToVisibleItem | double |  |  | SI | Linked To Visible Item |
| ITM_NeedleGauge_DR | bigint |  | FK | SI | Des Ref NeedleGauge |
| ITM_NeedleType_DR | bigint |  | FK | SI | Des Ref NeedleType |
| ITM_Notes | varchar |  |  | SI | Notes |
| ITM_Number | double |  |  | SI | Item Number |
| ITM_ParentSection_DR | varchar |  | FK | SI | Parent Section |
| ITM_PrefParams_DR | bigint |  | FK | SI | Des Ref epr.OEOrder.PrefItem
Default Parameters |
| ITM_Price | double |  |  | SI | Price |
| ITM_Qty | double |  |  | SI | Quantity |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_SectionDesc | varchar |  |  | SI | Section Header Description |
| ITM_SelectionDefault | varchar |  |  | SI | Order Selection Default uses Standard Type 'Select... |
| ITM_SequenceFlag | varchar |  |  | SI | [DEPRECATED]Storage for the sequence flag is being... |
| ITM_UOM_DR | bigint |  | FK | SI | Des Ref UOM |
| ITM_UpdatedDate | date |  |  | SI | Updated Date |
| ITM_UpdatedTime | time |  |  | SI | Updated Time |
| ITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ITM_Visible | varchar |  |  | NO | Visible |
| Q01 | - |  |  | SI | Fuerza |
| Q02 | - |  |  | SI | ¿Cuánta dificultad tiene para levantar y cargar 4,... |
| Q03 | - |  |  | SI | Asistencia para caminar |
| Q04 | - |  |  | SI | ¿Cuánta dificultad tiene para caminar por la habit... |
| Q05 | - |  |  | SI | Levantarse de la silla |
| Q06 | - |  |  | SI | ¿Cuánta dificultad tiene para levantarse desde una... |
| Q07 | - |  |  | SI | Subir escaleras |
| Q08 | - |  |  | SI | ¿Cuánta dificultad tiene para subir un tramo de 10... |
| Q09 | - |  |  | SI | Caídas |
| Q10 | - |  |  | SI | ¿Cuántas veces se ha caído al suelo en el último a... |
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