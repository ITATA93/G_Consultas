# questionnaire.QTCPSCED

> Procedure Sedation Checklist Emergency Department

**Schema:** questionnaire
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Procedure Sedation Checklist Emergency Department

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Procedure |
| Q02 | date |  |  | SI | Date |
| Q03 | time |  |  | SI | Time |
| Q04 | varchar |  |  | SI | Doctor performing sedation |
| Q05 | longvarbinary |  |  | SI | Signature |
| Q05UDt | date |  |  | SI | Signature Last Updated Date |
| Q05UTm | time |  |  | SI | Signature Last Updated Time |
| Q06 | varchar |  |  | SI | Supervising consultant |
| Q07 | longvarbinary |  |  | SI | Signature |
| Q07UDt | date |  |  | SI | Signature Last Updated Date |
| Q07UTm | time |  |  | SI | Signature Last Updated Time |
| Q08 | varchar |  |  | SI | Overnight, registrars must be specifically credent... |
| Q09 | varchar |  |  | SI | Is procedural sedation really necessary? |
| Q10 | varchar |  |  | SI | Is the procedure definitely indicated (eg. Forearm... |
| Q11 | varchar |  |  | SI | Are there sufficient consultants / registrars / nu... |
| Q12 | varchar |  |  | SI | Is there a potential resus cubicle available to co... |
| Q13 | varchar |  |  | SI | Would a biers block or nerve block or nitrous work... |
| Q14 | varchar |  |  | SI | Is the emergency department the correct place for ... |
| Q15 | varchar |  |  | SI | Consider and indicate if any of the following:- |
| Q16 | varchar |  |  | SI | These cases may be better transferred to theatre a... |
| Q17 | varchar |  |  | SI | Obtain senior ED or anaesthetic advice if at risk ... |
| Q18 | varchar |  |  | SI | Predictors of difficult bag mask ventilation |
| Q19 | varchar |  |  | SI | Poor mask seal? (eg beard, facial trauma) |
| Q20 | varchar |  |  | SI | Obesity / Obstruction? (eg tonsillitis, croup, etc... |
| Q21 | varchar |  |  | SI | Age > 55? |
| Q22 | varchar |  |  | SI | No teeth? |
| Q23 | varchar |  |  | SI | Stiff lungs (eg asthma)? |
| Q24 | varchar |  |  | SI | Predictors of difficult intubation |
| Q25 | varchar |  |  | SI | Look (does it look difficult) |
| Q26 | varchar |  |  | SI | Inadequate 3-3-2? |
| Q27 | varchar |  |  | SI | Mallampati score 3 or 4? |
| Q28 | varchar |  |  | SI | Obstruction? - FB, tonsillitis, croup etc |
| Q29 | varchar |  |  | SI | Poor neck mobility |
| Q30 | varchar |  |  | SI | History and examination |
| Q31 | varchar |  |  | SI | Hours since last ate (ideally >4 hours) |
| Q32 | varchar |  |  | SI | Hours since last drank (ideally >2 hours) |
| Q33 | varchar |  |  | SI | Consent - Verbal |
| Q34 | varchar |  |  | SI | IV access - Adequate |
| Q35 | varchar |  |  | SI | Airway |
| Q36 | varchar |  |  | SI | Suction |
| Q37 | varchar |  |  | SI | Oral airways |
| Q38 | varchar |  |  | SI | Bag and mask |
| Q39 | varchar |  |  | SI | Oxygen |
| Q40 | varchar |  |  | SI | Monitoring / Equipment |
| Q41 | varchar |  |  | SI | ECG monitoring |
| Q42 | varchar |  |  | SI | SaO2 monitoring |
| Q43 | varchar |  |  | SI | NIBP |
| Q44 | varchar |  |  | SI | Resus trolley |
| Q45 | varchar |  |  | SI | Capnography |
| Q46 | varchar |  |  | SI | Drugs during procedure |
| Q47 | varchar |  |  | SI | Side effects / Complications |
| Q48 | varchar |  |  | SI | Lowest SpO2 recorded |
| Q49 | varchar |  |  | SI | Lowest BP recorded |
| Q50 | varchar |  |  | SI | Nasal / Oral airway required |
| Q51 | varchar |  |  | SI | Jaw thrust / Chin lift required |
| Q52 | varchar |  |  | SI | Vomiting? |
| Q53 | varchar |  |  | SI | Other |
| Q54 | varchar |  |  | SI | Procedure successfully carried out? |
| Q55 | varchar |  |  | SI | Comment - If no, why not? |
| Q56 | varchar |  |  | SI | Nursing signoff |
| Q57 | date |  |  | SI | Date |
| Q58 | varchar |  |  | SI | Name |
| Q59 | longvarbinary |  |  | SI | Signature |
| Q59UDt | date |  |  | SI | Signature Last Updated Date |
| Q59UTm | time |  |  | SI | Signature Last Updated Time |
| Q60 | varchar |  |  | SI | Comments |
| Q61 | varchar |  |  | SI | Comment |
| Q62 | varchar |  |  | SI | Comment |
| Q63 | varchar |  |  | SI | Comment |
| Q64 | varchar |  |  | SI | Comment |
| Q65 | varchar |  |  | SI | Comment |
| Q66 | varchar |  |  | SI | • 3 fingers between teeth, |
| Q67 | varchar |  |  | SI | • 3 under chin, |
| Q68 | varchar |  |  | SI | • 2 above thyroid |
| Q69 | varchar |  |  | SI | Relevant cardiovascular history |
| Q70 | varchar |  |  | SI | Cardiovascular exam prior to sedation |
| Q71 | varchar |  |  | SI | Relevant respiratory history |
| Q72 | varchar |  |  | SI | Respiratory exam prior to sedation |
| Q74 | date |  |  | SI | Date |
| Q75 | time |  |  | SI | Time |
| Q76 | varchar |  |  | SI | Relevant cardiovascular history |
| Q77 | varchar |  |  | SI | Cardiovascular exam prior to sedation |
| Q78 | varchar |  |  | SI | Relevant respiratory history |
| Q79 | varchar |  |  | SI | Respiratory exam prior to sedation |
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