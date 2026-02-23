# SQLUser.ARC_ItemKeywords

**Schema:** SQLUser
**Columnas:** 157
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_RowId | bigint | PK |  | NO | - |
| KEYW_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| KEYW_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| KEYW_Agent_DR | bigint |  | FK | SI | Des Ref MHCAgent |
| KEYW_AuxilInsurType_DR | bigint |  | FK | SI | Des Ref ARCAuxilInsurType |
| KEYW_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| KEYW_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| KEYW_Desc | varchar |  |  | SI | Description |
| KEYW_GenKey | varchar |  |  | SI | GenKey |
| KEYW_Generic_DR | bigint |  | FK | SI | Des Ref Generic |
| KEYW_INCI_DR | bigint |  | FK | SI | Des Ref INCI |
| KEYW_InsuranceType1_DR | bigint |  | FK | SI | Des Ref ARCInsuranceType |
| KEYW_InsuranceType_DR | bigint |  | FK | SI | Des Ref ARCInsuranceType |
| KEYW_Keyword | varchar |  |  | SI | Keyword |
| KEYW_OrderCateg_DR | bigint |  | FK | SI | Des Ref OrderCateg |
| KEYW_OrderSubCat_DR | bigint |  | FK | SI | Des Ref OrderSubCat |
| KEYW_Region | varchar |  |  | SI | Region |
| KEYW_TransferDestination_DR | bigint |  | FK | SI | Des Ref PACTransferDestination |
| KEYW_Type | varchar |  |  | SI | Type |
| KEYW_Vendor_DR | bigint |  | FK | SI | Des Ref Vendor |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Day of care |
| Q04 | - |  |  | SI | Plan of Care |
| Q05 | - |  |  | SI | Central Nervous System |
| Q06 | - |  |  | SI | Alert and oriented - Glasgow coma scale  15/15 |
| Q07 | - |  |  | SI | Variance |
| Q08 | - |  |  | SI | Cardiovascular System |
| Q09 | - |  |  | SI | Observations are within acceptable limits and stab... |
| Q10 | - |  |  | SI | Variance |
| Q11 | - |  |  | SI | Chest pain free |
| Q12 | - |  |  | SI | Variance |
| Q13 | - |  |  | SI | Cardiac rhythm monitored and all arrhythmias repor... |
| Q14 | - |  |  | SI | Variance |
| Q15 | - |  |  | SI | Cardiac rhythm monitored and all arrhythmias repor... |
| Q16 | - |  |  | SI | Variance |
| Q17 | - |  |  | SI | 12 lead ECG conducted and reviewed by medical offi... |
| Q18 | - |  |  | SI | Variance |
| Q19 | - |  |  | SI | Blood and test results reviewed as clinically indi... |
| Q20 | - |  |  | SI | Variance |
| Q21 | - |  |  | SI | Medications are reviewed and considered for best p... |
| Q22 | - |  |  | SI | Variance |
| Q23 | - |  |  | SI | Review ECHO results for appropriate heart failure ... |
| Q24 | - |  |  | SI | Variance |
| Q25 | - |  |  | SI | Limbs are warm and perfused |
| Q26 | - |  |  | SI | Variance |
| Q27 | - |  |  | SI | VTE prophylaxis prescribed and administered |
| Q28 | - |  |  | SI | Variance |
| Q29 | - |  |  | SI | IV access assessed |
| Q30 | - |  |  | SI | Variance |
| Q31 | - |  |  | SI | Respiratory System |
| Q32 | - |  |  | SI | Respiratory rate less than 20 bpm |
| Q33 | - |  |  | SI | Variance |
| Q34 | - |  |  | SI | Oxygen saturations ≥95% as clinically indicated |
| Q35 | - |  |  | SI | Variance |
| Q36 | - |  |  | SI | Auscultation of chest, clear and air entry equal |
| Q37 | - |  |  | SI | Variance |
| Q38 | - |  |  | SI | Metabolic |
| Q39 | - |  |  | SI | Normothermia maintained |
| Q40 | - |  |  | SI | Variance |
| Q41 | - |  |  | SI | Blood glucose level maintained between 4-8 mmol/L. |
| Q42 | - |  |  | SI | Variance |
| Q43 | - |  |  | SI | Gastrointestinal / Elimination |
| Q44 | - |  |  | SI | Euvolemia maintained |
| Q45 | - |  |  | SI | Euvolemia maintained |
| Q45a | - |  |  | SI | Variance |
| Q46 | - |  |  | SI | Tolerating oral diet |
| Q47 | - |  |  | SI | Variance |
| Q48 | - |  |  | SI | Strict fluid balance chart maintained |
| Q49 | - |  |  | SI | Variance |
| Q50 | - |  |  | SI | Urine output > 30 mls per hour |
| Q51 | - |  |  | SI | Variance |
| Q52 | - |  |  | SI | All bowel motions documented |
| Q53 | - |  |  | SI | Variance |
| Q54 | - |  |  | SI | Monitor for fluid retention |
| Q55 | - |  |  | SI | Variance |
| Q56 | - |  |  | SI | Skin Care and Hygiene |
| Q57 | - |  |  | SI | Skin remains intact |
| Q58 | - |  |  | SI | Variance |
| Q59 | - |  |  | SI | Personal hygiene attended |
| Q60 | - |  |  | SI | Variance |
| Q61 | - |  |  | SI | Wounds and insertion sites are assessed |
| Q62 | - |  |  | SI | Variance |
| Q63 | - |  |  | SI | Pressure relieving devices in situ as needed |
| Q64 | - |  |  | SI | Variance |
| Q65 | - |  |  | SI | Physiotherapy and Mobilisation |
| Q66 | - |  |  | SI | Supportive mobilisation commenced |
| Q67 | - |  |  | SI | Variance |
| Q68 | - |  |  | SI | Cardiac Education |
| Q69 | - |  |  | SI | Cardiac education commenced |
| Q70 | - |  |  | SI | Variance |
| Q71 | - |  |  | SI | Cardiac education continued |
| Q72 | - |  |  | SI | Variance |
| Q73 | - |  |  | SI | Assess for fitness for discharge, aim for day 3 |
| Q74 | - |  |  | SI | Variance |
| Q75 | - |  |  | SI | Referral to Cardiac Rehabilitation Phase 2 |
| Q76 | - |  |  | SI | Variance |
| Q77 | - |  |  | SI | Cardiac Education Phase 1 completed |
| Q78 | - |  |  | SI | Variance |
| Q79 | - |  |  | SI | Social |
| Q80 | - |  |  | SI | Next of kin / significant other notified of patien... |
| Q81 | - |  |  | SI | Variance |
| Q82 | - |  |  | SI | Problems, barriers to discharge assessed |
| Q83 | - |  |  | SI | Variance |
| Q84 | - |  |  | SI | Estimated date of discharge documented and discuss... |
| Q85 | - |  |  | SI | Variance |
| Q86 | - |  |  | SI | Patient has an estimated date of discharge recorde... |
| Q87 | - |  |  | SI | Variance |
| Q88 | - |  |  | SI | Accessed interpreter service as required |
| Q89 | - |  |  | SI | Variance |
| Q90 | - |  |  | SI | Referral to allied health if required |
| Q91 | - |  |  | SI | Variance |
| Q92 | - |  |  | SI | Dummy1 |
| Q93 | - |  |  | SI | Dummy2 |
| Q94 | - |  |  | SI | Referred to cardiac clinical nurse consultant |
| Q95 | - |  |  | SI | Variance |
| Q96 | - |  |  | SI | Other patient specific needs addressed as required |
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