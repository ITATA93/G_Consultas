# SQLUser.IN_Request

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INRQ_RowId | bigint | PK |  | NO | - |
| INRQ_Date | date |  |  | NO | Date When Request Made |
| INRQ_DateLastUpdated | date |  |  | SI | DateLastUpdated |
| INRQ_No | varchar |  |  | NO | Request Reference Number |
| INRQ_RBOperRoom_DR | bigint |  | FK | SI | Des Ref to RBOperatingRoom |
| INRQ_RecLoc_DR | bigint |  | FK | NO | Des Ref to CTLOC |
| INRQ_Remarks | varchar |  |  | SI | Remarks |
| INRQ_ReqLoc_DR | bigint |  | FK | NO | Des Ref to CTLOC |
| INRQ_SSUSR_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| INRQ_Status | varchar |  |  | SI | Status (C)lose,(O)pen,(X)cancel |
| INRQ_SterileReqStatus | varchar |  |  | SI | SterileReqStatus |
| INRQ_Time | time |  |  | NO | Request Time |
| INRQ_TimeLastUpdated | time |  |  | SI | TimeLastUpdated |
| INRQ_UserCompleted | varchar |  |  | SI | User Completed |
| INRQ_UserLastUpdated_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Level of conciousness |
| Q04 | - |  |  | SI | Mobility |
| Q05 | - |  |  | SI | Haemodynamic |
| Q06 | - |  |  | SI | Oxygenation |
| Q07 | - |  |  | SI | Nutrition |
| Q08 | - |  |  | SI | Level of consciousness |
| Q09 | - |  |  | SI | 1. Awake and alert: RASS 0 to + 1. The patient is ... |
| Q10 | - |  |  | SI | 2. Agitated / restless / confused: RASS > 1. The p... |
| Q11 | - |  |  | SI | 3. Sedated but responsive: RASS -1 to -3. The pati... |
| Q12 | - |  |  | SI | 4. Coma, sedated and unresponsive: RASS -4 to -5. ... |
| Q13 | - |  |  | SI | Mobility |
| Q14 | - |  |  | SI | 1. Independent / walking with help. The patient wa... |
| Q15 | - |  |  | SI | 2. Limited / bed-armchair activity. The patient is... |
| Q16 | - |  |  | SI | 3. Very limited but tolerates change in position. ... |
| Q17 | - |  |  | SI | 4. Unable to change position or lying prone. The p... |
| Q18 | - |  |  | SI | Haemodynamic |
| Q19 | - |  |  | SI | 1. No haemodynamic support. The patient does not r... |
| Q20 | - |  |  | SI | 2. Volume expanders. The patient requires use of b... |
| Q21 | - |  |  | SI | 3. Dopamine or norepinephrine or adrenaline or car... |
| Q22 | - |  |  | SI | 4. Needing two of the above. The patient requires ... |
| Q23 | - |  |  | SI | Oxygenation |
| Q24 | - |  |  | SI | 1. Spontaneous breathing and low FiO2 (< 0.4). The... |
| Q25 | - |  |  | SI | 2. Spontaneous breathing and high FiO2 (>= 0.4). T... |
| Q26 | - |  |  | SI | 3. Non-invasive mechanical ventilation. The patien... |
| Q27 | - |  |  | SI | 4. Invasive mechanical ventilation. The patient re... |
| Q28 | - |  |  | SI | Nutrition |
| Q29 | - |  |  | SI | 1. Full oral diet. The patient tolerates liquids a... |
| Q30 | - |  |  | SI | 2. Enteral nutrition / parenteral feeding. The pat... |
| Q31 | - |  |  | SI | 3. Oral fluids. Incomplete oral feeding. The patie... |
| Q32 | - |  |  | SI | 4. No feeding. The patient is not being fed at all... |
| Q33 | - |  |  | SI | The COMHON index assesses a patient's risk of deve... |
| Q34 | - |  |  | SI | RASS = Richmond Agitation Sedation Scale |
| Q35 | - |  |  | SI | World Federation of Critical Care Nurses. COHMON I... |
| Q36 | - |  |  | SI | https://wfccn.org/wp-content/uploads/2022/03/COMHO... |
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