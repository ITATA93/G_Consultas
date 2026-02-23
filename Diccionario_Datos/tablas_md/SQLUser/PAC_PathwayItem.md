# SQLUser.PAC_PathwayItem

**Schema:** SQLUser
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPI_ParRef | bigint | PK |  | NO | Parent Reference |
| PACPI_AutoOrder | varchar |  |  | SI | Order Automatically |
| PACPI_CheckFinal | varchar |  |  | SI | End Date the Item only when its Result Status is F... |
| PACPI_Childsub | double |  |  | NO | Childsub |
| PACPI_Code | varchar |  |  | SI | Code |
| PACPI_CodeTableTags | varchar |  |  | SI | List of Code Table Tags |
| PACPI_Consent_DR | bigint |  | FK | SI | Patient Consent |
| PACPI_CreatedDate | date |  |  | SI | Created Date |
| PACPI_CreatedTime | time |  |  | SI | Created Time |
| PACPI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPI_CycleDur | double |  |  | SI | Cycle Period |
| PACPI_CycleDurType | varchar |  |  | SI | Cycle Period Type |
| PACPI_CycleReps | double |  |  | SI | Cycle Repetition |
| PACPI_Desc | varchar |  |  | SI | Description |
| PACPI_DescComputed | bit |  |  | SI | Item Description Computed
1 - the item descriptio... |
| PACPI_DirectlyExecute | varchar |  |  | SI | Directly Execute |
| PACPI_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| PACPI_ICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| PACPI_ItmMast_DR | varchar |  | FK | SI | Order Item |
| PACPI_ListType | varchar |  |  | SI | Type of List |
| PACPI_Note | varchar |  |  | SI | Recommendation Note |
| PACPI_Operation_DR | bigint |  | FK | SI | Procedure |
| PACPI_OrdSets_DR | varchar |  | FK | SI | Order Set |
| PACPI_ParentItem_DR | varchar |  | FK | SI | Parent Item |
| PACPI_PrefParams_DR | bigint |  | FK | SI | Default Parameters |
| PACPI_Protocol_DR | bigint |  | FK | SI | Protocol |
| PACPI_Questionnaire_DR | bigint |  | FK | SI | Questionnaire |
| PACPI_RowId | varchar |  |  | NO | - |
| PACPI_SequenceNumber | numeric |  |  | SI | Sequence Number |
| PACPI_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| PACPI_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| PACPI_StatePPP_DR | bigint |  | FK | SI | State PPP |
| PACPI_Task_DR | bigint |  | FK | SI | Task |
| PACPI_TimeNotAfter | double |  |  | SI | Time Constraint Not After: Offset Time between pre... |
| PACPI_TimeNotAfterType | varchar |  |  | SI | Time Constraint Not After Duration Type |
| PACPI_TimeNotBefore | double |  |  | SI | Time Constraint Not Before: Offset Time between pr... |
| PACPI_TimeNotBeforeType | varchar |  |  | SI | Time Constraint Not Before Duration Type |
| PACPI_TimeStart | varchar |  |  | SI | Time Constraint Starting Point |
| PACPI_UpdatedDate | date |  |  | SI | Updated Date |
| PACPI_UpdatedTime | time |  |  | SI | Updated Time |
| PACPI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PACPI_UseProtTypeOrdWorkflow | varchar |  |  | SI | Use Ordering workflow defined for the Protocol Typ... |
| PACPI_VacDose_DR | bigint |  | FK | SI | Vaccination Dose DR |
| PACPI_VisualRule_DR | bigint |  | FK | SI | Visual Rule |
| Q01 | - |  |  | SI | Use this list to identify fall hazards and accessi... |
| Q02 | - |  |  | SI | Exterior entrances and exit |
| Q02A | - |  |  | SI | Exterior entrances and exit |
| Q03 | - |  |  | SI | Interior doors, stairs, halls |
| Q03A | - |  |  | SI | Interior doors, stairs, halls |
| Q04 | - |  |  | SI | Bathroom |
| Q04A | - |  |  | SI | Bathroom |
| Q05 | - |  |  | SI | Kitchen |
| Q05A | - |  |  | SI | Kitchen |
| Q06 | - |  |  | SI | Living, dining, bedroom |
| Q06A | - |  |  | SI | Living, dining, bedroom |
| Q07 | - |  |  | SI | Laundry |
| Q07A | - |  |  | SI | Laundry |
| Q08 | - |  |  | SI | Telephone and door |
| Q08A | - |  |  | SI | Telephone and door |
| Q09 | - |  |  | SI | Storage space |
| Q09A | - |  |  | SI | Storage space |
| Q10 | - |  |  | SI | Windows |
| Q10A | - |  |  | SI | Windows |
| Q11 | - |  |  | SI | Electrical outlets and controls |
| Q11A | - |  |  | SI | Electrical outlets and controls |
| Q12 | - |  |  | SI | Heat, light, ventilation, security, carbon monoxid... |
| Q12A | - |  |  | SI | Heat, light, ventilation, security, carbon monoxid... |
| Q13 | - |  |  | SI | Comments |
| Q14 | - |  |  | SI | Use this list to prioritize work tasks |
| Q15 | - |  |  | SI | Exterior entrances and exits |
| Q15A | - |  |  | SI | Exterior entrances and exits |
| Q16 | - |  |  | SI | Interior doors, halls, stairs |
| Q16A | - |  |  | SI | Interior doors, halls, stairs |
| Q17 | - |  |  | SI | Bathroom |
| Q17A | - |  |  | SI | Bathroom |
| Q18 | - |  |  | SI | Kitchen |
| Q18A | - |  |  | SI | Kitchen |
| Q19 | - |  |  | SI | Living, dining, bedroom |
| Q19A | - |  |  | SI | Living, dining, bedroom |
| Q20 | - |  |  | SI | Laundry |
| Q20A | - |  |  | SI | Laundry |
| Q21 | - |  |  | SI | Telephone and door |
| Q21A | - |  |  | SI | Telephone and door |
| Q22 | - |  |  | SI | Storage space |
| Q22A | - |  |  | SI | Storage space |
| Q23 | - |  |  | SI | Windows |
| Q23A | - |  |  | SI | Windows |
| Q24 | - |  |  | SI | Electrical outlets and controls |
| Q24A | - |  |  | SI | Electrical outlets and controls |
| Q25 | - |  |  | SI | Heat, light, ventilation, security, carbon monoxid... |
| Q25A | - |  |  | SI | Heat, light, ventilation, security, carbon monoxid... |
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