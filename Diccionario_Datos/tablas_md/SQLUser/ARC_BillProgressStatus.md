# SQLUser.ARC_BillProgressStatus

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BLPS_RowId | bigint | PK |  | NO | - |
| BLPS_Cancelled | varchar |  |  | SI | Cancelled |
| BLPS_Code | varchar |  |  | NO | Code |
| BLPS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BLPS_CreatedDate | date |  |  | SI | Created Date |
| BLPS_CreatedTime | time |  |  | SI | Created Time |
| BLPS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BLPS_DateFrom | date |  |  | SI | Date From |
| BLPS_DateTo | date |  |  | SI | Date To |
| BLPS_Desc | varchar |  |  | NO | Description |
| BLPS_Initial | varchar |  |  | SI | Initial |
| BLPS_NoBillAuditEntry | varchar |  |  | SI | Do Not Create Bill Audit Entry |
| BLPS_NoCancelBill | varchar |  |  | SI | Do not allow to Cancel Bill |
| BLPS_NoDiscontOrHoldOrdItem | varchar |  |  | SI | Do not allow to Discontinue or On Hold Order Item |
| BLPS_Owner | varchar |  |  | SI | Owner |
| BLPS_PrelimBatchRequired | varchar |  |  | SI | PrelimBatchRequired |
| BLPS_ResubTotAllOrdItems | varchar |  |  | SI | Resubmission Total - All Order Items |
| BLPS_ResubTotSelOrdItems | varchar |  |  | SI | Resubmission Total - Selected Order Items |
| BLPS_Sequence | double |  |  | SI | Sequence |
| BLPS_UpdatedDate | date |  |  | SI | Updated Date |
| BLPS_UpdatedTime | time |  |  | SI | Updated Time |
| BLPS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. Niña o niño sin control de salud al día. |
| Q02 | - |  |  | SI | 2. Niña o niño con múltiples consultas en SAPU, ot... |
| Q03 | - |  |  | SI | 3. Niña o niño con hospitalización anterior de med... |
| Q04 | - |  |  | SI | 4. Niña o niño con condición médica de base (síndr... |
| Q05 | - |  |  | SI | 5. Niña o niño con madre adolescente. |
| Q06 | - |  |  | SI | 6. Niña o niño cuya madre tiene escolaridad menor ... |
| Q07 | - |  |  | SI | 7. Niña o niño cuya madre presenta escala de Edimb... |
| Q08 | - |  |  | SI | 8. Niña o niño cuyo cuidador/a principal presenta ... |
| Q09 | - |  |  | SI | 9. Niña o niño que vive en familia monoparental si... |
| Q10 | - |  |  | SI | 10. Presencia de cualquier trastorno de salud ment... |
| Q11 | - |  |  | SI | 11. Niña o niño cuyo hermano/a tiene antecedentes ... |
| Q12 | - |  |  | SI | 12. Niña o niño cuyo padre, madre o cuidador/a pri... |
| Q13 | - |  |  | SI | 13. Niña o niño institucionalizado en residencia d... |
| Q14 | - |  |  | SI | 14. Niña o niño que crece en un contexto ambiental... |
| Q15 | - |  |  | SI | 15. Niña o niño que vive en una familia con aislam... |
| Q16 | - |  |  | SI | 16. Violencia intrafamiliar / niña o niña testigo ... |
| Q17 | - |  |  | SI | 17. Maltrato físico o abuso sexual. |
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