# SQLUser.OEC_ResultDelivTime

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DLT_Rowid | bigint | PK |  | NO | - |
| DLT_ArriveTime | time |  |  | SI | Arrive Time |
| DLT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DLT_CreatedDate | date |  |  | SI | Created Date |
| DLT_CreatedTime | time |  |  | SI | Created Time |
| DLT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DLT_DateFrom | date |  |  | SI | Date From |
| DLT_DateTo | date |  |  | SI | Date To |
| DLT_LocFrom_DR | bigint |  | FK | SI | Des Ref LocFrom |
| DLT_LocTo_DR | bigint |  | FK | SI | Des Ref LocTo |
| DLT_Owner | varchar |  |  | SI | Owner |
| DLT_StartTime | time |  |  | SI | Start Time |
| DLT_UpdatedDate | date |  |  | SI | Updated Date |
| DLT_UpdatedTime | time |  |  | SI | Updated Time |
| DLT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Incident Category |
| Q03 | - |  |  | SI | Incident Date / Time |
| Q04 | - |  |  | SI | Incident Time |
| Q08 | - |  |  | SI | Narrative around incident |
| Q09 | - |  |  | SI | Inmediate action taken |
| Q10 | - |  |  | SI | Approximate Date / Time |
| Q19 | - |  |  | SI | Incident comments |
| Q27 | - |  |  | SI | Injury details |
| Q31 | - |  |  | SI | Actions taken to prevent incident occurring again |
| Q32 | - |  |  | SI | Escalation |
| Q33 | - |  |  | SI | Outcome & Impact Comments |
| Q34 | - |  |  | SI | Other people Involved? |
| Q35 | - |  |  | SI | Name of others and their roles |
| Q36 | - |  |  | SI | Incident Severity |
| Q37 | - |  |  | SI | Incident Probability |
| Q38 | - |  |  | SI | Former fall reported in the same episode |
| Q39 | - |  |  | SI | Who observed the fall? |
| Q40 | - |  |  | SI | Prior to the fall, what was the patient doing or t... |
| Q41 | - |  |  | SI | Was the fall unassisted or assisted? |
| Q42 | - |  |  | SI | Prior to the fall, was a fall risk assessment docu... |
| Q43 | - |  |  | SI | Applied evaluations |
| Q44 | - |  |  | SI | Required investigations |
| Q45 | - |  |  | SI | Type of investigations |
| Q46 | - |  |  | SI | Investigations outcomes |
| Q47 | - |  |  | SI | Possible clinical risk - Medications |
| Q48 | - |  |  | SI | Possible clinical risk - Sensory deficit |
| Q49 | - |  |  | SI | Sentinel event |
| Q50 | - |  |  | SI | Other documentation available |
| Q51 | - |  |  | SI | Notes on available documentation |
| QINFIN | - |  |  | SI | Finalcial Impact |
| QIRACC | - |  |  | SI | Patient Accident Incident |
| QIRCF | - |  |  | SI | Contributing Factors |
| QIRCF1 | - |  |  | SI | Contributing Factors comments |
| QIRCS | - |  |  | SI | Care Setting |
| QIRDEV | - |  |  | SI | Medical Device / Equipment Incident |
| QIRDEV1 | - |  |  | SI | Description |
| QIRDEV2 | - |  |  | SI | Manufacturer |
| QIRDEV3 | - |  |  | SI | Model |
| QIRDEV4 | - |  |  | SI | Serial Number |
| QIRLoc | - |  |  | SI | Location |
| QIRMED | - |  |  | SI | Medication incident |
| QIRProb | - |  |  | SI | Incident Probability |
| QIRRisk | - |  |  | SI | Risk Assessment previously done |
| QIRRisk2 | - |  |  | SI | Date of last Risk Assessment |
| QIRRisk3 | - |  |  | SI | Score from last Risk Assessment |
| QIRRisk4 | - |  |  | SI | Risk Re-Assessment required |
| QIRRiskGrad | - |  |  | SI | Risk Grading |
| QIRSEV | - |  |  | SI | Incident Severity |
| QIRSecLoc | - |  |  | SI | Secondary Location |
| QIRTTT | - |  |  | SI | Treatment or Procedure Incident |
| QIRTType | - |  |  | SI | Incident Type |
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