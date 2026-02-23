# questionnaire.QTCCATR

> Chemotherapy Assessment and Treatment Record

**Schema:** questionnaire
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Chemotherapy Assessment and Treatment Record

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Regime |
| Q02 | varchar |  |  | SI | Clinical trial |
| Q03 | date |  |  | SI | Start date |
| Q04 | varchar |  |  | SI | Frequency / No of cycles |
| Q05 | varchar |  |  | SI | Blood taken |
| Q06 | date |  |  | SI | Date bloods taken |
| Q07 | varchar |  |  | SI | Height and weight recorded?  |
| Q08 | varchar |  |  | SI | Allergies / Reaction details reviewed / recorded? |
| Q09 | varchar |  |  | SI | Venous access assessment |
| Q10 | varchar |  |  | SI | Action taken if access is poor |
| Q11 | varchar |  |  | SI | MRSA screen needed |
| Q12 | date |  |  | SI | Date of MRSA screen |
| Q13 | varchar |  |  | SI | Transport  |
| Q14 | varchar |  |  | SI | If needed, transport booking information given to ... |
| Q15 | date |  |  | SI | Appointment date for consent / prescription |
| Q16 | varchar |  |  | SI | Has patient had chemotherapy before? |
| Q17 | varchar |  |  | SI | If yes |
| Q18 | varchar |  |  | SI | Is the patient still aware of chemotherapy helplin... |
| Q19 | varchar |  |  | SI | Correct patient contact numbers?  |
| Q20 | varchar |  |  | SI | Own thermometer |
| Q21 | varchar |  |  | SI | If no |
| Q22 | varchar |  |  | SI | Give the patient support service information |
| Q23 | varchar |  |  | SI | Advised re: helpline |
| Q24 | varchar |  |  | SI | Transport plan |
| Q25 | varchar |  |  | SI | Advised not to delay calling helpline |
| Q26 | varchar |  |  | SI | Advised to source own thermometer |
| Q27 | varchar |  |  | SI | Does the patient know who their key worker is? (If... |
| Q28 | varchar |  |  | SI | Does the patient understand their diagnosis and tr... |
| Q29 | varchar |  |  | SI | Verbal information given (Please tick relevant box... |
| Q30 | varchar |  |  | SI | General |
| Q31 | varchar |  |  | SI | How therapy works |
| Q32 | varchar |  |  | SI | How administered |
| Q33 | varchar |  |  | SI | Inpatient / Outpatient stay |
| Q34 | varchar |  |  | SI | Day units |
| Q35 | varchar |  |  | SI | Transport / Parking |
| Q36 | varchar |  |  | SI | Appointments |
| Q37 | varchar |  |  | SI | Other, please state |
| Q38 | varchar |  |  | SI | Specific |
| Q39 | varchar |  |  | SI | Dental work |
| Q40 | varchar |  |  | SI | Vaccinations - influenza / pneumococcal (no live v... |
| Q41 | varchar |  |  | SI | Prescriptions |
| Q42 | varchar |  |  | SI | Clinical trials |
| Q43 | varchar |  |  | SI | Diet and alcohol |
| Q44 | varchar |  |  | SI | Exercise / Swimming (no swimming with Central Veno... |
| Q45 | varchar |  |  | SI | Personal care - sun protection, tampons, razors |
| Q46 | varchar |  |  | SI | Barrier contraception |
| Q47 | varchar |  |  | SI | CVC care |
| Q48 | varchar |  |  | SI | Extravasation |
| Q49 | varchar |  |  | SI | Other, please state |
| Q50 | varchar |  |  | SI | Side effects |
| Q51 | varchar |  |  | SI | Neutropenia / Sepsis |
| Q52 | varchar |  |  | SI | Bleeding / Anaemia |
| Q53 | varchar |  |  | SI | Nausea / Vomiting |
| Q54 | varchar |  |  | SI | Diarrhoea / Constipation |
| Q55 | varchar |  |  | SI | Loss of appetite / Taste changes |
| Q56 | varchar |  |  | SI | Mouth/Gut ulcers |
| Q57 | varchar |  |  | SI | Gritty eyes / Blurred vision |
| Q58 | varchar |  |  | SI | Hair loss |
| Q59 | varchar |  |  | SI | Fatigue |
| Q60 | varchar |  |  | SI | Skin changes / Rashes (Palmer Planter Syndrome) |
| Q61 | varchar |  |  | SI | Fertility / Libido |
| Q62 | varchar |  |  | SI | Neuropathy |
| Q63 | varchar |  |  | SI | Renal / Liver toxicity |
| Q64 | varchar |  |  | SI | Cardiac / Lung toxicity |
| Q65 | varchar |  |  | SI | Bladder irritation / Discoloured urine |
| Q66 | varchar |  |  | SI | Allergic reaction |
| Q67 | varchar |  |  | SI | Flu-like symptoms |
| Q68 | varchar |  |  | SI | Fluid retention |
| Q69 | varchar |  |  | SI | CNS toxicity / Drowsiness |
| Q70 | varchar |  |  | SI | Laryngeal spasm |
| Q71 | varchar |  |  | SI | Other, please state |
| Q72 | varchar |  |  | SI | Written information provided: |
| Q73 | varchar |  |  | SI | Pre-Chemotherapy information pack |
| Q74 | varchar |  |  | SI | Details of any other written information given: |
| Q75 | varchar |  |  | SI | Does the patient require any MDT referrals, e.g. d... |
| Q76 | varchar |  |  | SI | Details of referrals made: |
| Q77 | varchar |  |  | SI | Are there any other issues of concern? |
| Q78 | varchar |  |  | SI | Please list and take action |
| Q79 | varchar |  |  | SI | Check against known UK / Overseas list areas of co... |
| Q80 | varchar |  |  | SI | Are there any outstanding issues for discussion? |
| Q81 | varchar |  |  | SI | Please list issues and arrangements made to comple... |
| Q82 | date |  |  | SI | Date |
| Q83 | time |  |  | SI | Time |
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