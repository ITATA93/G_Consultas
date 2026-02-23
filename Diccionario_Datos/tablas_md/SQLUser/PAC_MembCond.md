# SQLUser.PAC_MembCond

**Schema:** SQLUser
**Columnas:** 146
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MEMBCOND_RowId | bigint | PK |  | NO | - |
| MEMBCOND_Active | varchar |  |  | SI | Active |
| MEMBCOND_Code | varchar |  |  | NO | Code |
| MEMBCOND_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MEMBCOND_CreatedDate | date |  |  | SI | Created Date |
| MEMBCOND_CreatedTime | time |  |  | SI | Created Time |
| MEMBCOND_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MEMBCOND_DateFrom | date |  |  | SI | Date From |
| MEMBCOND_DateTo | date |  |  | SI | Date To  |
| MEMBCOND_Desc | varchar |  |  | NO | Description |
| MEMBCOND_NationalCode | varchar |  |  | SI | National Code |
| MEMBCOND_Owner | varchar |  |  | SI | Owner |
| MEMBCOND_UpdatedDate | date |  |  | SI | Updated Date |
| MEMBCOND_UpdatedTime | time |  |  | SI | Updated Time |
| MEMBCOND_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Safety checks |
| Q02 | - |  |  | SI | Invasive lines |
| Q03 | - |  |  | SI | Patient identification |
| Q04 | - |  |  | SI | Fluids and medications |
| Q05 | - |  |  | SI | Drains and tubes |
| Q06 | - |  |  | SI | Remarks |
| Q07 | - |  |  | SI | Skin |
| Q07ObsDR | - |  |  | SI | Skin DR |
| Q08 | - |  |  | SI | Cord |
| Q08ObsDR | - |  |  | SI | Cord DR |
| Q09 | - |  |  | SI | Eyes |
| Q09ObsDR | - |  |  | SI | Eyes DR |
| Q10 | - |  |  | SI | Mouth |
| Q10ObsDR | - |  |  | SI | Mouth DR |
| Q11 | - |  |  | SI | Buttocks |
| Q11ObsDR | - |  |  | SI | Buttocks DR |
| Q12 | - |  |  | SI | Invasive lines |
| Q13 | - |  |  | SI | Date |
| Q14 | - |  |  | SI | Time |
| Q15 | - |  |  | SI | Clinical handover received from |
| Q16 | - |  |  | SI | 2 x identification bands in situ |
| Q17 | - |  |  | SI | Baby weighed |
| Q19 | - |  |  | SI | Air entry |
| Q19ObsDR | - |  |  | SI | Air entry DR |
| Q20 | - |  |  | SI | Work of breathing (Qualitative) |
| Q20ObsDR | - |  |  | SI | Work of breathing (Qualitative) DR |
| Q21 | - |  |  | SI | Breathing patterns |
| Q21ObsDR | - |  |  | SI | Breathing patterns DR |
| Q22 | - |  |  | SI | Air entry / Breath sounds notes |
| Q23 | - |  |  | SI | T-piece circuit, bag and mask present and function... |
| Q24 | - |  |  | SI | Suction equipment present and functional |
| Q25 | - |  |  | SI | Electrocardiogram (ECG) monitor settings and alarm... |
| Q26 | - |  |  | SI | Ventilation settings and alarms checked |
| Q27 | - |  |  | SI | Humidifier settings and bag checked |
| Q28 | - |  |  | SI | Isolette humidity checked |
| Q29 | - |  |  | SI | Notes |
| Q30 | - |  |  | SI | Equipment |
| Q31 | - |  |  | SI | Date due for change |
| Q32 | - |  |  | SI | Change every |
| Q33 | - |  |  | SI | Ventilation circuit |
| Q34 | - |  |  | SI | Ventilation circuit - Date due for change (change ... |
| Q35 | - |  |  | SI | Every 7 days |
| Q36 | - |  |  | SI | Suction |
| Q37 | - |  |  | SI | Suction - Date due for change (change every day) |
| Q38 | - |  |  | SI | Every day |
| Q39 | - |  |  | SI | Closed circuit tracheostomy care |
| Q40 | - |  |  | SI | Closed circuit tracheostomy care - Date due for ch... |
| Q41 | - |  |  | SI | Every day |
| Q42 | - |  |  | SI | Continuous Positive Airway Pressure (CPAP) circuit |
| Q43 | - |  |  | SI | CPAP circuit - Date due for change (change every 7... |
| Q44 | - |  |  | SI | Every 7 days |
| Q45 | - |  |  | SI | High flow circuit |
| Q46 | - |  |  | SI | High flow circuit - Date due for change (change ev... |
| Q47 | - |  |  | SI | Every 7 days |
| Q48 | - |  |  | SI | Isolette |
| Q49 | - |  |  | SI | Isolette - Date due for change (change every 7 day... |
| Q50 | - |  |  | SI | Every 7 days |
| Q51 | - |  |  | SI | Nasogastric tube (NG) |
| Q52 | - |  |  | SI | NG - Date due for change (change per protocol) |
| Q53 | - |  |  | SI | Per protocol |
| Q54 | - |  |  | SI | Electrocardiogram (ECG) dots |
| Q55 | - |  |  | SI | ECG dots - Date due for change (change every day) |
| Q56 | - |  |  | SI | Every day |
| Q57 | - |  |  | SI | Notes |
| Q58 | - |  |  | SI | Equipment |
| Q59 | - |  |  | SI | Equipment |
| Q60 | - |  |  | SI | Equipment |
| Q61 | - |  |  | SI | Equipment |
| Q62 | - |  |  | SI | Equipment |
| Q63 | - |  |  | SI | Equipment |
| Q64 | - |  |  | SI | Equipment |
| Q65 | - |  |  | SI | Equipment |
| Q66 | - |  |  | SI | Equipment |
| Q67 | - |  |  | SI | Date due for change |
| Q68 | - |  |  | SI | Date due for change |
| Q69 | - |  |  | SI | Date due for change |
| Q70 | - |  |  | SI | Date due for change |
| Q71 | - |  |  | SI | Date due for change |
| Q72 | - |  |  | SI | Date due for change |
| Q73 | - |  |  | SI | Date due for change |
| Q74 | - |  |  | SI | Date due for change |
| Q75 | - |  |  | SI | Date due for change |
| Q76 | - |  |  | SI | Change every |
| Q77 | - |  |  | SI | Change every |
| Q78 | - |  |  | SI | Change every |
| Q79 | - |  |  | SI | Change every |
| Q80 | - |  |  | SI | Change every |
| Q81 | - |  |  | SI | Change every |
| Q82 | - |  |  | SI | Change every |
| Q83 | - |  |  | SI | Change every |
| Q84 | - |  |  | SI | Change every |
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