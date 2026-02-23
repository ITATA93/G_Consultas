# SQLUser.PAC_Stage

**Schema:** SQLUser
**Columnas:** 135
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STG_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Procedure |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Doctor performing sedation |
| Q05 | - |  |  | SI | Signature |
| Q05UDt | - |  |  | SI | Signature Last Updated Date |
| Q05UTm | - |  |  | SI | Signature Last Updated Time |
| Q06 | - |  |  | SI | Supervising consultant |
| Q07 | - |  |  | SI | Signature |
| Q07UDt | - |  |  | SI | Signature Last Updated Date |
| Q07UTm | - |  |  | SI | Signature Last Updated Time |
| Q08 | - |  |  | SI | Overnight, registrars must be specifically credent... |
| Q09 | - |  |  | SI | Is procedural sedation really necessary? |
| Q10 | - |  |  | SI | Is the procedure definitely indicated (eg. Forearm... |
| Q11 | - |  |  | SI | Are there sufficient consultants / registrars / nu... |
| Q12 | - |  |  | SI | Is there a potential resus cubicle available to co... |
| Q13 | - |  |  | SI | Would a biers block or nerve block or nitrous work... |
| Q14 | - |  |  | SI | Is the emergency department the correct place for ... |
| Q15 | - |  |  | SI | Consider and indicate if any of the following:- |
| Q16 | - |  |  | SI | These cases may be better transferred to theatre a... |
| Q17 | - |  |  | SI | Obtain senior ED or anaesthetic advice if at risk ... |
| Q18 | - |  |  | SI | Predictors of difficult bag mask ventilation |
| Q19 | - |  |  | SI | Poor mask seal? (eg beard, facial trauma) |
| Q20 | - |  |  | SI | Obesity / Obstruction? (eg tonsillitis, croup, etc... |
| Q21 | - |  |  | SI | Age > 55? |
| Q22 | - |  |  | SI | No teeth? |
| Q23 | - |  |  | SI | Stiff lungs (eg asthma)? |
| Q24 | - |  |  | SI | Predictors of difficult intubation |
| Q25 | - |  |  | SI | Look (does it look difficult) |
| Q26 | - |  |  | SI | Inadequate 3-3-2? |
| Q27 | - |  |  | SI | Mallampati score 3 or 4? |
| Q28 | - |  |  | SI | Obstruction? - FB, tonsillitis, croup etc |
| Q29 | - |  |  | SI | Poor neck mobility |
| Q30 | - |  |  | SI | History and examination |
| Q31 | - |  |  | SI | Hours since last ate (ideally >4 hours) |
| Q32 | - |  |  | SI | Hours since last drank (ideally >2 hours) |
| Q33 | - |  |  | SI | Consent - Verbal |
| Q34 | - |  |  | SI | IV access - Adequate |
| Q35 | - |  |  | SI | Airway |
| Q36 | - |  |  | SI | Suction |
| Q37 | - |  |  | SI | Oral airways |
| Q38 | - |  |  | SI | Bag and mask |
| Q39 | - |  |  | SI | Oxygen |
| Q40 | - |  |  | SI | Monitoring / Equipment |
| Q41 | - |  |  | SI | ECG monitoring |
| Q42 | - |  |  | SI | SaO2 monitoring |
| Q43 | - |  |  | SI | NIBP |
| Q44 | - |  |  | SI | Resus trolley |
| Q45 | - |  |  | SI | Capnography |
| Q46 | - |  |  | SI | Drugs during procedure |
| Q47 | - |  |  | SI | Side effects / Complications |
| Q48 | - |  |  | SI | Lowest SpO2 recorded |
| Q49 | - |  |  | SI | Lowest BP recorded |
| Q50 | - |  |  | SI | Nasal / Oral airway required |
| Q51 | - |  |  | SI | Jaw thrust / Chin lift required |
| Q52 | - |  |  | SI | Vomiting? |
| Q53 | - |  |  | SI | Other |
| Q54 | - |  |  | SI | Procedure successfully carried out? |
| Q55 | - |  |  | SI | Comment - If no, why not? |
| Q56 | - |  |  | SI | Nursing signoff |
| Q57 | - |  |  | SI | Date |
| Q58 | - |  |  | SI | Name |
| Q59 | - |  |  | SI | Signature |
| Q59UDt | - |  |  | SI | Signature Last Updated Date |
| Q59UTm | - |  |  | SI | Signature Last Updated Time |
| Q60 | - |  |  | SI | Comments |
| Q61 | - |  |  | SI | Comment |
| Q62 | - |  |  | SI | Comment |
| Q63 | - |  |  | SI | Comment |
| Q64 | - |  |  | SI | Comment |
| Q65 | - |  |  | SI | Comment |
| Q66 | - |  |  | SI | • 3 fingers between teeth, |
| Q67 | - |  |  | SI | • 3 under chin, |
| Q68 | - |  |  | SI | • 2 above thyroid |
| Q69 | - |  |  | SI | Relevant cardiovascular history |
| Q70 | - |  |  | SI | Cardiovascular exam prior to sedation |
| Q71 | - |  |  | SI | Relevant respiratory history |
| Q72 | - |  |  | SI | Respiratory exam prior to sedation |
| Q74 | - |  |  | SI | Date |
| Q75 | - |  |  | SI | Time |
| Q76 | - |  |  | SI | Relevant cardiovascular history |
| Q77 | - |  |  | SI | Cardiovascular exam prior to sedation |
| Q78 | - |  |  | SI | Relevant respiratory history |
| Q79 | - |  |  | SI | Respiratory exam prior to sedation |
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
| STG_Code | varchar |  |  | NO | Code |
| STG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| STG_CreatedDate | date |  |  | SI | Created Date |
| STG_CreatedTime | time |  |  | SI | Created Time |
| STG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STG_Desc | varchar |  |  | NO | Description |
| STG_Owner | varchar |  |  | SI | Owner |
| STG_UpdatedDate | date |  |  | SI | Updated Date |
| STG_UpdatedTime | time |  |  | SI | Updated Time |
| STG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*