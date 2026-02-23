# SQLUser.OR_AnaestSurgPathwaySkinPrep

**Schema:** SQLUser
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SKINPREP_ParRef | varchar | PK |  | NO | OR_AnaestSurgPathway Parent Reference |
| ChildQ68DR | - |  |  | SI | Child Reference: Staff Member Attending To The Ass... |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Following completion of the Falls Risk Screen, imp... |
| Q04 | - |  |  | SI | Completed on |
| Q05 | - |  |  | SI | 1. History of Falls |
| Q06 | - |  |  | SI | Obtained details about previous fall in the last 6... |
| Q07 | - |  |  | SI | Actions |
| Q08 | - |  |  | SI | Patient describes : loss of consciousness, syncope... |
| Q09 | - |  |  | SI | Does the patient have postural hypotension? Refer ... |
| Q10 | - |  |  | SI | Additional history notes |
| Q11 | - |  |  | SI | 2. Mental Status |
| Q12 | - |  |  | SI | Patient is confused, disorientated, agitated or de... |
| Q13 | - |  |  | SI | Actions |
| Q14 | - |  |  | SI | Conduct or refer for a cognitive screen (e.g. AMTS... |
| Q15 | - |  |  | SI | Consider delirium. Complete or refer for a Confusi... |
| Q16 | - |  |  | SI | If possible causes of delirium (e.g. sepsis, pain,... |
| Q17 | - |  |  | SI | Implement a Delirium Care Pathway (as per local pr... |
| Q18 | - |  |  | SI | Commence communication plan with family / carers |
| Q19 | - |  |  | SI | Patient requires increased observation (avoid use ... |
| Q20 | - |  |  | SI | Patient with confusion NOT to be left alone during... |
| Q21 | - |  |  | SI | Locate patient near nurses' station if possible or... |
| Q22 | - |  |  | SI | Consider use of behaviour chart - if patient’s beh... |
| Q23 | - |  |  | SI | Provide bed at appropriate patient height and/or f... |
| Q24 | - |  |  | SI | Provide bed at appropriate patient height and/or f... |
| Q25 | - |  |  | SI | Provide bed/chair alarm (if available / appropriat... |
| Q26 | - |  |  | SI | Refer to allied health / medical team for review (... |
| Q27 | - |  |  | SI | Other health care for review |
| Q28 | - |  |  | SI | Additional mental status notes |
| Q29 | - |  |  | SI | 3. Vision |
| Q30 | - |  |  | SI | Patient has visual impairment (e.g. cataract, glau... |
| Q31 | - |  |  | SI | Actions |
| Q32 | - |  |  | SI | Ensure easy access to bathroom and toilet |
| Q33 | - |  |  | SI | Direct patient to seek assistance when mobilising |
| Q34 | - |  |  | SI | Ensure adequate night lighting in ward (e.g. leave... |
| Q35 | - |  |  | SI | Refer to allied health / medical team for review (... |
| Q36 | - |  |  | SI | Other health care for review |
| Q37 | - |  |  | SI | Additional vision notes |
| Q38 | - |  |  | SI | 4. Toileting |
| Q39 | - |  |  | SI | Patient has confusion, urinary or faecal frequency... |
| Q40 | - |  |  | SI | Actions |
| Q41 | - |  |  | SI | Provide patient with individualised (supervision /... |
| Q42 | - |  |  | SI | Patient to be always supervised when mobilising to... |
| Q43 | - |  |  | SI | Patient to be supervised in toilet / bathroom |
| Q44 | - |  |  | SI | Refer to continence nurse and/or allied health rev... |
| Q45 | - |  |  | SI | Other health care for review |
| Q46 | - |  |  | SI | Additional toileting notes |
| Q47 | - |  |  | SI | 5. Transfer / Mobility |
| Q48 | - |  |  | SI | Patient has issues that affect balance / mobility ... |
| Q49 | - |  |  | SI | Actions |
| Q50 | - |  |  | SI | Referral to physiotherapist for mobility assessmen... |
| Q51 | - |  |  | SI | Referral to occupational therapist for functional ... |
| Q52 | - |  |  | SI | Provide patient with equipment to assist mobility ... |
| Q53 | - |  |  | SI | Provide patient with assistance / supervision to m... |
| Q54 | - |  |  | SI | Provide patient with assistance for personal care |
| Q55 | - |  |  | SI | Provide patient with assistance / supervision in b... |
| Q56 | - |  |  | SI | Ensure patient has access to non-slip footwear (e.... |
| Q57 | - |  |  | SI | Additional transfer / mobility notes |
| Q58 | - |  |  | SI | 6. Medications |
| Q59 | - |  |  | SI | Patient is taking antipsychotics, antidepressants,... |
| Q60 | - |  |  | SI | Actions |
| Q61 | - |  |  | SI | Refer to treating medical officer for medication r... |
| Q62 | - |  |  | SI | Additional medications notes |
| Q63 | - |  |  | SI | Follow up Interventions |
| Q64 | - |  |  | SI | Ensure Falls Risk Alert is added |
| Q65 | - |  |  | SI | Ensure all actions are identified and noted |
| Q66 | - |  |  | SI | Falls risk discussed and intervention developed in... |
| Q67 | - |  |  | SI | Intervention details |
| Q69 | - |  |  | SI | Notes |
| Q70 | - |  |  | SI | Flag and communicate falls risk status and interve... |
| Q71 | - |  |  | SI | Refer to allied health / medical team for review (... |
| Q72 | - |  |  | SI | Refer to continence nurse and/or allied health rev... |
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
| SKINPREP_Antisepsis_DR | bigint |  | FK | SI |  Des Ref ORCAntisepsis |
| SKINPREP_Childsub | numeric |  |  | NO | Childsub |
| SKINPREP_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*