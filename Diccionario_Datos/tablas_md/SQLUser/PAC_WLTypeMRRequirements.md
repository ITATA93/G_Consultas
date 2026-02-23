# SQLUser.PAC_WLTypeMRRequirements

**Schema:** SQLUser
**Columnas:** 147
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MR_ParRef | bigint | PK |  | NO | PAC_WaitingListType Parent Reference |
| MR_AllVolumes | varchar |  |  | SI | All Volumes |
| MR_Childsub | double |  |  | NO | Childsub |
| MR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MR_CreatedDate | date |  |  | SI | Created Date |
| MR_CreatedTime | time |  |  | SI | Created Time |
| MR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MR_LastTwoVolumes | varchar |  |  | SI | Last Two Volumes |
| MR_LatestVolumeOnly | varchar |  |  | SI | Latest Volume Only |
| MR_LeadTime | double |  |  | SI | Lead Time |
| MR_RecordType_DR | bigint |  | FK | SI | Des Ref RecordType |
| MR_RowId | varchar |  |  | NO | - |
| MR_UpdatedDate | date |  |  | SI | Updated Date |
| MR_UpdatedTime | time |  |  | SI | Updated Time |
| MR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Stroke pathway day |
| Q04 | - |  |  | SI | Central Nervous System |
| Q05 | - |  |  | SI | Patient has attended all required investigative pr... |
| Q06 | - |  |  | SI | Variance |
| Q07 | - |  |  | SI | Patient remained neurologically stable with no fur... |
| Q08 | - |  |  | SI | Variance |
| Q09 | - |  |  | SI | Patient remained seizure free |
| Q10 | - |  |  | SI | Variance |
| Q11 | - |  |  | SI | Patient had no further deterioration in language, ... |
| Q12 | - |  |  | SI | Variance |
| Q13 | - |  |  | SI | Patient able to communication basic needs |
| Q14 | - |  |  | SI | Variance |
| Q15 | - |  |  | SI | All neurological deficits documented and reported ... |
| Q16 | - |  |  | SI | Variance |
| Q17 | - |  |  | SI | Cardiovascular System |
| Q18 | - |  |  | SI | Patient remained hemodynamically stable and observ... |
| Q19 | - |  |  | SI | Variance |
| Q20 | - |  |  | SI | Cardiac rhythm monitoring in place and all arrhyth... |
| Q21 | - |  |  | SI | Variance |
| Q22 | - |  |  | SI | Cardiac rhythm monitoring ceased as per medical in... |
| Q23 | - |  |  | SI | Variance |
| Q24 | - |  |  | SI | 12 lead electrocardiogram conducted and reviewed b... |
| Q25 | - |  |  | SI | Variance |
| Q26 | - |  |  | SI | All ordered blood tests taken and results reviewed... |
| Q27 | - |  |  | SI | Variance |
| Q28 | - |  |  | SI | Medications reviewed and considered for best pract... |
| Q29 | - |  |  | SI | Variance |
| Q30 | - |  |  | SI | Appropriate venous thrombosis therapy prophylaxis ... |
| Q31 | - |  |  | SI | Variance |
| Q32 | - |  |  | SI | Respiratory System |
| Q33 | - |  |  | SI | Respiratory rate less than 20 bpm |
| Q34 | - |  |  | SI | Variance |
| Q35 | - |  |  | SI | Oxygen saturations ≥ 95% or 88 - 92% for CO2 retai... |
| Q36 | - |  |  | SI | Variance |
| Q37 | - |  |  | SI | Airway remained patent and all secretions managed ... |
| Q38 | - |  |  | SI | Variance |
| Q39 | - |  |  | SI | Lung fields clear and air entry equal |
| Q40 | - |  |  | SI | Variance |
| Q41 | - |  |  | SI | Patient nursed in 30° upright position or as clini... |
| Q42 | - |  |  | SI | Variance |
| Q43 | - |  |  | SI | Metabolic |
| Q44 | - |  |  | SI | Patient remained normothermic |
| Q45 | - |  |  | SI | Variance |
| Q46 | - |  |  | SI | Blood glucose level maintained between 4 - 8 mmol/... |
| Q47 | - |  |  | SI | Variance |
| Q48 | - |  |  | SI | Elimination / Fluid Balance |
| Q49 | - |  |  | SI | Urine output > 30 mLs per hour |
| Q50 | - |  |  | SI | Variance |
| Q51 | - |  |  | SI | Strict fluid balance chart maintained |
| Q52 | - |  |  | SI | Variance |
| Q53 | - |  |  | SI | Patient assessed for dysphagia |
| Q54 | - |  |  | SI | Variance |
| Q55 | - |  |  | SI | Patient is receiving adequate nutrition |
| Q56 | - |  |  | SI | Variance |
| Q57 | - |  |  | SI | All bowel motions document. If bowels not open for... |
| Q58 | - |  |  | SI | Variance |
| Q59 | - |  |  | SI | Patient remained continent of both urine and faece... |
| Q60 | - |  |  | SI | Variance |
| Q61 | - |  |  | SI | Skin Care and Hygiene |
| Q62 | - |  |  | SI | Skin remains intact and free from pressure injurie... |
| Q63 | - |  |  | SI | Variance |
| Q64 | - |  |  | SI | Patient has received regular pressure area care |
| Q65 | - |  |  | SI | Variance |
| Q66 | - |  |  | SI | Pressure relieving devices in situ as needed |
| Q67 | - |  |  | SI | Variance |
| Q68 | - |  |  | SI | Personal hygiene attended |
| Q69 | - |  |  | SI | Variance |
| Q70 | - |  |  | SI | Patient received mouth and eye care as clinically ... |
| Q71 | - |  |  | SI | Variance |
| Q72 | - |  |  | SI | Mobilisation / Physiotherapy |
| Q73 | - |  |  | SI | Mobility has been assessed and documented |
| Q74 | - |  |  | SI | Variance |
| Q75 | - |  |  | SI | Patient mobilising as tolerated |
| Q76 | - |  |  | SI | Variance |
| Q77 | - |  |  | SI | Stroke Education |
| Q78 | - |  |  | SI | Patient commenced on stroke education |
| Q79 | - |  |  | SI | Variance |
| Q80 | - |  |  | SI | Patient continuing with stroke education |
| Q81 | - |  |  | SI | Variance |
| Q82 | - |  |  | SI | Social |
| Q83 | - |  |  | SI | Problems, barriers to discharge assessed |
| Q84 | - |  |  | SI | Variance |
| Q85 | - |  |  | SI | Estimated date of discharge recorded |
| Q86 | - |  |  | SI | Variance |
| Q87 | - |  |  | SI | Estimated date of discharge reviewed and updated i... |
| Q88 | - |  |  | SI | Variance |
| Q89 | - |  |  | SI | Referred to allied health services as clinically i... |
| Q90 | - |  |  | SI | Variance |
| Q91 | - |  |  | SI | Referred to appropriate rehabilitation services as... |
| Q92 | - |  |  | SI | Variance |
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