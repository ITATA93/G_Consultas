# SQLUser.CT_WeightConFactor

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTWCF_RowId | bigint | PK |  | NO | - |
| CTWCF_ConFactor | double |  |  | NO | Factor |
| CTWCF_CreatedDate | date |  |  | SI | Created Date |
| CTWCF_CreatedTime | time |  |  | SI | Created Time |
| CTWCF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTWCF_Unit | varchar |  |  | NO | Unit |
| CTWCF_UpdatedDate | date |  |  | SI | Updated Date |
| CTWCF_UpdatedTime | time |  |  | SI | Updated Time |
| CTWCF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | INTENSITY AND DURATION OF PRESSURE |
| Q02 | - |  |  | SI | General Physical Condition |
| Q03 | - |  |  | SI | MOBILITY - The Ability to Change and Control Body ... |
| Q04 | - |  |  | SI | ACTIVITY - The degree of physical activity |
| Q05 | - |  |  | SI | SENSORY PERCEPTION - Ability to respond in a devel... |
| Q06 | - |  |  | SI | TOLERANCE OF THE SKIN AND SUPPORTING STRUCTURE |
| Q07 | - |  |  | SI | MOISTURE - Degree to which skin is exposed to mois... |
| Q08 | - |  |  | SI | FRICTION AND SHEAR - Friction: occurs when skin mo... |
| Q09 | - |  |  | SI | NUTRITION - Usual food intake pattern |
| Q10 | - |  |  | SI | Tissue perfusion and oxygenation |
| Q11 | - |  |  | SI | Remarks |
| Q12 | - |  |  | SI | < 20 |
| Q13 | - |  |  | SI | At Risk |
| Q14 | - |  |  | SI | ≥ 20 |
| Q15 | - |  |  | SI | Low Risk |
| Q16 | - |  |  | SI | The Braden scale assesses a patient's risk of deve... |
| Q17 | - |  |  | SI | Score |
| Q18 | - |  |  | SI | Classification |
| Q19 | - |  |  | SI | ≥ 20 : Low Risk |
| Q20 | - |  |  | SI | < 20 : At Risk |
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