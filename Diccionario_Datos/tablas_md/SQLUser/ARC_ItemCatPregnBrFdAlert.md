# SQLUser.ARC_ItemCatPregnBrFdAlert

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBA_ParRef | bigint | PK |  | NO | ARC_ItemCat Parent Reference |
| PBA_Childsub | double |  |  | NO | Childsub |
| PBA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBA_CreatedDate | date |  |  | SI | Created Date |
| PBA_CreatedTime | time |  |  | SI | Created Time |
| PBA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBA_DateFrom | date |  |  | SI | DateFrom |
| PBA_DateTo | date |  |  | SI | DateTo |
| PBA_Message | varchar |  |  | SI | Message |
| PBA_Options | varchar |  |  | SI | Options |
| PBA_RowId | varchar |  |  | NO | - |
| PBA_UpdatedDate | date |  |  | SI | Updated Date |
| PBA_UpdatedTime | time |  |  | SI | Updated Time |
| PBA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of Recording |
| Q02 | - |  |  | SI | Date of Analysis |
| Q03 | - |  |  | SI | Monitor ID |
| Q04 | - |  |  | SI | SUCCESS RATE (%) |
| Q05 | - |  |  | SI | Height |
| Q05ObsDR | - |  |  | SI | Height DR |
| Q06 | - |  |  | SI | Weight |
| Q06ObsDR | - |  |  | SI | Weight DR |
| Q07 | - |  |  | SI | Diabetes |
| Q08 | - |  |  | SI | Systolic min / max (mmHg) |
| Q08ObsDR | - |  |  | SI | Systolic min / max (mmHg) DR |
| Q09 | - |  |  | SI | Systolic min / max 2 |
| Q09ObsDR | - |  |  | SI | Systolic min / max 2 DR |
| Q10 | - |  |  | SI | mmHg |
| Q11 | - |  |  | SI | Diastolic min / max (mmHg) |
| Q11ObsDR | - |  |  | SI | Diastolic min / max (mmHg) DR |
| Q12 | - |  |  | SI | Diastolic min / max 2 |
| Q12ObsDR | - |  |  | SI | Diastolic min / max 2 DR |
| Q13 | - |  |  | SI | mmHg |
| Q14 | - |  |  | SI | 24 Hour Average BP (mmHg) |
| Q14ObsDR | - |  |  | SI | 24 Hour Average BP (mmHg) DR |
| Q15 | - |  |  | SI | Daytime Average (mmHg) |
| Q15ObsDR | - |  |  | SI | Daytime Average (mmHg) DR |
| Q16 | - |  |  | SI | Percentage of systolic readings > 120 mmHG |
| Q16ObsDR | - |  |  | SI | Percentage of systolic readings > 120 mmHG DR |
| Q17 | - |  |  | SI | Percentage of diastolic readings > 80 mmHG |
| Q17ObsDR | - |  |  | SI | Percentage of diastolic readings > 80 mmHG DR |
| Q18 | - |  |  | SI | Nocturnal Average (mmHg) |
| Q18ObsDR | - |  |  | SI | Nocturnal Average (mmHg) DR |
| Q19 | - |  |  | SI | Nocturnal Dipper (mmHg) |
| Q19ObsDR | - |  |  | SI | Nocturnal Dipper (mmHg) DR |
| Q20 | - |  |  | SI | Percentage of nocturnal systolic readings > 120 mm... |
| Q20ObsDR | - |  |  | SI | Percentage of nocturnal systolic readings > 120 mm... |
| Q21 | - |  |  | SI | Percentage of nocturnal diastolic readings > 80 mm... |
| Q21ObsDR | - |  |  | SI | Percentage of nocturnal diastolic readings > 80 mm... |
| Q22 | - |  |  | SI | Comments |
| Q23 | - |  |  | SI | Conclusion |
| Q24 | - |  |  | SI | Reported by |
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