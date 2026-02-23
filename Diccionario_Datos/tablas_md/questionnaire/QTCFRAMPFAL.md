# questionnaire.QTCFRAMPFAL

> Falls Risk Assessment and Management Plan (FRAMP)

**Schema:** questionnaire
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Falls Risk Assessment and Management Plan (FRAMP)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Following completion of the Falls Risk Screen, imp... |
| Q04 | varchar |  |  | SI | Completed on |
| Q05 | varchar |  |  | SI | 1. History of Falls |
| Q06 | varchar |  |  | SI | Obtained details about previous fall in the last 6... |
| Q07 | varchar |  |  | SI | Actions |
| Q08 | varchar |  |  | SI | Patient describes : loss of consciousness, syncope... |
| Q09 | varchar |  |  | SI | Does the patient have postural hypotension? Refer ... |
| Q10 | varchar |  |  | SI | Additional history notes |
| Q11 | varchar |  |  | SI | 2. Mental Status |
| Q12 | varchar |  |  | SI | Patient is confused, disorientated, agitated or de... |
| Q13 | varchar |  |  | SI | Actions |
| Q14 | varchar |  |  | SI | Conduct or refer for a cognitive screen (e.g. AMTS... |
| Q15 | varchar |  |  | SI | Consider delirium. Complete or refer for a Confusi... |
| Q16 | varchar |  |  | SI | If possible causes of delirium (e.g. sepsis, pain,... |
| Q17 | varchar |  |  | SI | Implement a Delirium Care Pathway (as per local pr... |
| Q18 | varchar |  |  | SI | Commence communication plan with family / carers |
| Q19 | varchar |  |  | SI | Patient requires increased observation (avoid use ... |
| Q20 | varchar |  |  | SI | Patient with confusion NOT to be left alone during... |
| Q21 | varchar |  |  | SI | Locate patient near nurses' station if possible or... |
| Q22 | varchar |  |  | SI | Consider use of behaviour chart - if patient’s beh... |
| Q23 | varchar |  |  | SI | Provide bed at appropriate patient height and/or f... |
| Q24 | varchar |  |  | SI | Provide bed at appropriate patient height and/or f... |
| Q25 | varchar |  |  | SI | Provide bed/chair alarm (if available / appropriat... |
| Q26 | varchar |  |  | SI | Refer to allied health / medical team for review (... |
| Q27 | varchar |  |  | SI | Other health care for review |
| Q28 | varchar |  |  | SI | Additional mental status notes |
| Q29 | varchar |  |  | SI | 3. Vision |
| Q30 | varchar |  |  | SI | Patient has visual impairment (e.g. cataract, glau... |
| Q31 | varchar |  |  | SI | Actions |
| Q32 | varchar |  |  | SI | Ensure easy access to bathroom and toilet |
| Q33 | varchar |  |  | SI | Direct patient to seek assistance when mobilising |
| Q34 | varchar |  |  | SI | Ensure adequate night lighting in ward (e.g. leave... |
| Q35 | varchar |  |  | SI | Refer to allied health / medical team for review (... |
| Q36 | varchar |  |  | SI | Other health care for review |
| Q37 | varchar |  |  | SI | Additional vision notes |
| Q38 | varchar |  |  | SI | 4. Toileting |
| Q39 | varchar |  |  | SI | Patient has confusion, urinary or faecal frequency... |
| Q40 | varchar |  |  | SI | Actions |
| Q41 | varchar |  |  | SI | Provide patient with individualised (supervision /... |
| Q42 | varchar |  |  | SI | Patient to be always supervised when mobilising to... |
| Q43 | varchar |  |  | SI | Patient to be supervised in toilet / bathroom |
| Q44 | varchar |  |  | SI | Refer to continence nurse and/or allied health rev... |
| Q45 | varchar |  |  | SI | Other health care for review |
| Q46 | varchar |  |  | SI | Additional toileting notes |
| Q47 | varchar |  |  | SI | 5. Transfer / Mobility |
| Q48 | varchar |  |  | SI | Patient has issues that affect balance / mobility ... |
| Q49 | varchar |  |  | SI | Actions |
| Q50 | varchar |  |  | SI | Referral to physiotherapist for mobility assessmen... |
| Q51 | varchar |  |  | SI | Referral to occupational therapist for functional ... |
| Q52 | varchar |  |  | SI | Provide patient with equipment to assist mobility ... |
| Q53 | varchar |  |  | SI | Provide patient with assistance / supervision to m... |
| Q54 | varchar |  |  | SI | Provide patient with assistance for personal care |
| Q55 | varchar |  |  | SI | Provide patient with assistance / supervision in b... |
| Q56 | varchar |  |  | SI | Ensure patient has access to non-slip footwear (e.... |
| Q57 | varchar |  |  | SI | Additional transfer / mobility notes |
| Q58 | varchar |  |  | SI | 6. Medications |
| Q59 | varchar |  |  | SI | Patient is taking antipsychotics, antidepressants,... |
| Q60 | varchar |  |  | SI | Actions |
| Q61 | varchar |  |  | SI | Refer to treating medical officer for medication r... |
| Q62 | varchar |  |  | SI | Additional medications notes |
| Q63 | varchar |  |  | SI | Follow up Interventions |
| Q64 | varchar |  |  | SI | Ensure Falls Risk Alert is added |
| Q65 | varchar |  |  | SI | Ensure all actions are identified and noted |
| Q66 | varchar |  |  | SI | Falls risk discussed and intervention developed in... |
| Q67 | varchar |  |  | SI | Intervention details |
| Q69 | varchar |  |  | SI | Notes |
| Q70 | varchar |  |  | SI | Flag and communicate falls risk status and interve... |
| Q71 | varchar |  |  | SI | Refer to allied health / medical team for review (... |
| Q72 | varchar |  |  | SI | Refer to continence nurse and/or allied health rev... |
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