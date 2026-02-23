# SQLUser.PAC_AgedCareAssessServDet

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PAC_AgedCareAssessServ Parent Reference |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | DateFrom |
| DET_DateTo | date |  |  | SI | DateTo |
| DET_RowId | varchar |  |  | NO | - |
| DET_SepRef | varchar |  |  | SI | SepRef |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Monoaural hearing loss formula:[([500Hz+1000Hz+200... |
| Q02 | - |  |  | SI | Left ear (X) |
| Q03 | - |  |  | SI | Right Ear (O) |
| Q04 | - |  |  | SI | 500 Hz |
| Q05 | - |  |  | SI | 1000 Hz |
| Q06 | - |  |  | SI | 2000 Hz |
| Q07 | - |  |  | SI | 3000 Hz |
| Q08 | - |  |  | SI | Total |
| Q09 | - |  |  | SI | Stop here if total is 100 or less |
| Q10 | - |  |  | SI | 500 Hz |
| Q11 | - |  |  | SI | 1000 Hz |
| Q12 | - |  |  | SI | 2000 Hz |
| Q13 | - |  |  | SI | 3000 Hz |
| Q14 | - |  |  | SI | Total |
| Q15 | - |  |  | SI | Average threshold for 4 frequencies (/ 4) = |
| Q16 | - |  |  | SI | Less threshold fence of 25 dB (- 25) = |
| Q17 | - |  |  | SI | Multiplied by 1.5 equals the % of monoaural loss (... |
| Q18 | - |  |  | SI | Total percent monoaural hearing loss |
| Q19 | - |  |  | SI | L ear avg |
| Q20 | - |  |  | SI | R ear avg |
| Q21 | - |  |  | SI | Less 25 L |
| Q22 | - |  |  | SI | Less 25 R |
| Q23 | - |  |  | SI | by1.5 L |
| Q24 | - |  |  | SI | by1.5 R |
| Q25 | - |  |  | SI | Total L |
| Q26 | - |  |  | SI | Total R |
| Q27 | - |  |  | SI | Stop here if either of the monoaural hearing loss ... |
| Q28 | - |  |  | SI | Combined hearing loss formula: |
| Q29 | - |  |  | SI | ([% better ear x 5] + [% worse ear]) / 6 = % of lo... |
| Q30 | - |  |  | SI | % better ear x 5 = |
| Q31 | - |  |  | SI | (+) Plus % worse ear = |
| Q32 | - |  |  | SI | Sub total = |
| Q33 | - |  |  | SI | Sub-total divided by 6 (/6) = |
| Q34 | - |  |  | SI | % Binaural hearing loss |
| Q35 | - |  |  | SI | Comments |
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