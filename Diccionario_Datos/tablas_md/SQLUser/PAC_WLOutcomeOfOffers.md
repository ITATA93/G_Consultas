# SQLUser.PAC_WLOutcomeOfOffers

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLOOF_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Ventilation Day |
| Q03ObsDR | - |  |  | SI | Ventilation Day DR |
| Q04 | - |  |  | SI | Total Invasive Ventilation Days |
| Q04ObsDR | - |  |  | SI | Total Invasive Ventilation Days DR |
| Q05 | - |  |  | SI | Total Non Invasive Ventilation Days |
| Q05ObsDR | - |  |  | SI | Total Non Invasive Ventilation Days DR |
| Q06 | - |  |  | SI | Devices present and functioning at time of assessm... |
| Q07 | - |  |  | SI | Aerosol Set-up Date |
| Q08 | - |  |  | SI | Bacteria Filter |
| Q09 | - |  |  | SI | Heat and Moisture Exchanger |
| Q10 | - |  |  | SI | In Line Suction Catheter |
| Q11 | - |  |  | SI | Ventilator Circuit |
| Q12 | - |  |  | SI | Bag Valve Mask |
| Q13 | - |  |  | SI | Endotracheal Tube retie / retape date |
| Q13ObsDR | - |  |  | SI | Endotracheal Tube retie / retape date DR |
| Q14 | - |  |  | SI | Endotracheal Tube retie / retape time |
| Q14ObsDR | - |  |  | SI | Endotracheal Tube retie / retape time DR |
| Q15 | - |  |  | SI | Endotracheal Tube Position |
| Q15ObsDR | - |  |  | SI | Endotracheal Tube Position DR |
| Q16 | - |  |  | SI | Endotracheal Tube Position on XRAY |
| Q16ObsDR | - |  |  | SI | Endotracheal Tube Position on XRAY DR |
| Q17 | - |  |  | SI | Date of Endotracheal Tube Xray |
| Q17ObsDR | - |  |  | SI | Date of Endotracheal Tube Xray DR |
| Q18 | - |  |  | SI | Airway above carina (cm) |
| Q19 | - |  |  | SI | Adjusted by |
| Q20 | - |  |  | SI | If Pushed / Pulled, how much adjusted? (cm) |
| Q21 | - |  |  | SI | Lip Condition |
| Q22 | - |  |  | SI | Pressure on nasal bridge |
| Q23 | - |  |  | SI | Pressure on nostril or septum |
| Q24 | - |  |  | SI | Pressure on forehead |
| Q25 | - |  |  | SI | Airway security |
| Q26 | - |  |  | SI | Respiratory Therapy Checks completed |
| Q27 | - |  |  | SI | Patient's appearance |
| Q28 | - |  |  | SI | Sedation / Paralysis |
| Q29 | - |  |  | SI | Cardiopulmonary Support |
| Q30 | - |  |  | SI | RT Device and Safety Check Comments |
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
| WLOOF_Accepted | varchar |  |  | SI | Accepted |
| WLOOF_Code | varchar |  |  | NO | Code |
| WLOOF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLOOF_CreatedDate | date |  |  | SI | Created Date |
| WLOOF_CreatedTime | time |  |  | SI | Created Time |
| WLOOF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLOOF_DateFrom | date |  |  | SI | DateFrom |
| WLOOF_DateTo | date |  |  | SI | DateTo |
| WLOOF_Desc | varchar |  |  | NO | Description |
| WLOOF_DisplayOnAdmission | varchar |  |  | SI | DisplayOnAdmission |
| WLOOF_FieldToDenote | varchar |  |  | SI | FieldToDenote |
| WLOOF_OutcomeOfferReasonable | varchar |  |  | SI | OutcomeOfferReasonable |
| WLOOF_Owner | varchar |  |  | SI | Owner |
| WLOOF_ResetOutComeFrom | varchar |  |  | SI | ResetOutComeFrom |
| WLOOF_ResetOutComeTo | varchar |  |  | SI | ResetOutComeTo |
| WLOOF_StopWaitTime | varchar |  |  | SI | StopWaitTime |
| WLOOF_UpdatedDate | date |  |  | SI | Updated Date |
| WLOOF_UpdatedTime | time |  |  | SI | Updated Time |
| WLOOF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*