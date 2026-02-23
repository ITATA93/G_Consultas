# questionnaire.QTCNNSC

> Neonatal Safety Checks

**Schema:** questionnaire
**Columnas:** 132
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neonatal Safety Checks

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Safety checks |
| Q02 | varchar |  |  | SI | Invasive lines |
| Q03 | varchar |  |  | SI | Patient identification |
| Q04 | varchar |  |  | SI | Fluids and medications |
| Q05 | varchar |  |  | SI | Drains and tubes |
| Q06 | varchar |  |  | SI | Remarks |
| Q07 | varchar |  |  | SI | Skin |
| Q07ObsDR | varchar |  | FK | SI | Skin DR |
| Q08 | varchar |  |  | SI | Cord |
| Q08ObsDR | varchar |  | FK | SI | Cord DR |
| Q09 | varchar |  |  | SI | Eyes |
| Q09ObsDR | varchar |  | FK | SI | Eyes DR |
| Q10 | varchar |  |  | SI | Mouth |
| Q10ObsDR | varchar |  | FK | SI | Mouth DR |
| Q11 | varchar |  |  | SI | Buttocks |
| Q11ObsDR | varchar |  | FK | SI | Buttocks DR |
| Q12 | varchar |  |  | SI | Invasive lines |
| Q13 | date |  |  | SI | Date |
| Q14 | time |  |  | SI | Time |
| Q15 | varchar |  |  | SI | Clinical handover received from |
| Q16 | varchar |  |  | SI | 2 x identification bands in situ |
| Q17 | varchar |  |  | SI | Baby weighed |
| Q19 | varchar |  |  | SI | Air entry |
| Q19ObsDR | varchar |  | FK | SI | Air entry DR |
| Q20 | varchar |  |  | SI | Work of breathing (Qualitative) |
| Q20ObsDR | varchar |  | FK | SI | Work of breathing (Qualitative) DR |
| Q21 | varchar |  |  | SI | Breathing patterns |
| Q21ObsDR | varchar |  | FK | SI | Breathing patterns DR |
| Q22 | varchar |  |  | SI | Air entry / Breath sounds notes |
| Q23 | varchar |  |  | SI | T-piece circuit, bag and mask present and function... |
| Q24 | varchar |  |  | SI | Suction equipment present and functional |
| Q25 | varchar |  |  | SI | Electrocardiogram (ECG) monitor settings and alarm... |
| Q26 | varchar |  |  | SI | Ventilation settings and alarms checked |
| Q27 | varchar |  |  | SI | Humidifier settings and bag checked |
| Q28 | varchar |  |  | SI | Isolette humidity checked |
| Q29 | varchar |  |  | SI | Notes |
| Q30 | varchar |  |  | SI | Equipment |
| Q31 | varchar |  |  | SI | Date due for change |
| Q32 | varchar |  |  | SI | Change every |
| Q33 | varchar |  |  | SI | Ventilation circuit |
| Q34 | date |  |  | SI | Ventilation circuit - Date due for change (change ... |
| Q35 | varchar |  |  | SI | Every 7 days |
| Q36 | varchar |  |  | SI | Suction |
| Q37 | date |  |  | SI | Suction - Date due for change (change every day) |
| Q38 | varchar |  |  | SI | Every day |
| Q39 | varchar |  |  | SI | Closed circuit tracheostomy care |
| Q40 | date |  |  | SI | Closed circuit tracheostomy care - Date due for ch... |
| Q41 | varchar |  |  | SI | Every day |
| Q42 | varchar |  |  | SI | Continuous Positive Airway Pressure (CPAP) circuit |
| Q43 | date |  |  | SI | CPAP circuit - Date due for change (change every 7... |
| Q44 | varchar |  |  | SI | Every 7 days |
| Q45 | varchar |  |  | SI | High flow circuit |
| Q46 | date |  |  | SI | High flow circuit - Date due for change (change ev... |
| Q47 | varchar |  |  | SI | Every 7 days |
| Q48 | varchar |  |  | SI | Isolette |
| Q49 | date |  |  | SI | Isolette - Date due for change (change every 7 day... |
| Q50 | varchar |  |  | SI | Every 7 days |
| Q51 | varchar |  |  | SI | Nasogastric tube (NG) |
| Q52 | date |  |  | SI | NG - Date due for change (change per protocol) |
| Q53 | varchar |  |  | SI | Per protocol |
| Q54 | varchar |  |  | SI | Electrocardiogram (ECG) dots |
| Q55 | date |  |  | SI | ECG dots - Date due for change (change every day) |
| Q56 | varchar |  |  | SI | Every day |
| Q57 | varchar |  |  | SI | Notes |
| Q58 | varchar |  |  | SI | Equipment |
| Q59 | varchar |  |  | SI | Equipment |
| Q60 | varchar |  |  | SI | Equipment |
| Q61 | varchar |  |  | SI | Equipment |
| Q62 | varchar |  |  | SI | Equipment |
| Q63 | varchar |  |  | SI | Equipment |
| Q64 | varchar |  |  | SI | Equipment |
| Q65 | varchar |  |  | SI | Equipment |
| Q66 | varchar |  |  | SI | Equipment |
| Q67 | varchar |  |  | SI | Date due for change |
| Q68 | varchar |  |  | SI | Date due for change |
| Q69 | varchar |  |  | SI | Date due for change |
| Q70 | varchar |  |  | SI | Date due for change |
| Q71 | varchar |  |  | SI | Date due for change |
| Q72 | varchar |  |  | SI | Date due for change |
| Q73 | varchar |  |  | SI | Date due for change |
| Q74 | varchar |  |  | SI | Date due for change |
| Q75 | varchar |  |  | SI | Date due for change |
| Q76 | varchar |  |  | SI | Change every |
| Q77 | varchar |  |  | SI | Change every |
| Q78 | varchar |  |  | SI | Change every |
| Q79 | varchar |  |  | SI | Change every |
| Q80 | varchar |  |  | SI | Change every |
| Q81 | varchar |  |  | SI | Change every |
| Q82 | varchar |  |  | SI | Change every |
| Q83 | varchar |  |  | SI | Change every |
| Q84 | varchar |  |  | SI | Change every |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*