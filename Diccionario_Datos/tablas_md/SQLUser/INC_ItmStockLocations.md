# SQLUser.INC_ItmStockLocations

**Schema:** SQLUser
**Columnas:** 137
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOC_ParRef | bigint | PK |  | NO | INC_Itm Parent Reference |
| LOC_BarCode | varchar |  |  | SI | Bar Code |
| LOC_Childsub | double |  |  | NO | Childsub |
| LOC_Code | varchar |  |  | SI | Code |
| LOC_CreatedDate | date |  |  | SI | Created Date |
| LOC_CreatedTime | time |  |  | SI | Created Time |
| LOC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOC_Desc | varchar |  |  | SI | Description |
| LOC_Locations | varchar |  |  | SI | Locations |
| LOC_RowId | varchar |  |  | NO | - |
| LOC_StockTakeGroup | varchar |  |  | SI | StockTakeGroup |
| LOC_UpdatedDate | date |  |  | SI | Updated Date |
| LOC_UpdatedTime | time |  |  | SI | Updated Time |
| LOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Regime |
| Q02 | - |  |  | SI | Clinical trial |
| Q03 | - |  |  | SI | Start date |
| Q04 | - |  |  | SI | Frequency / No of cycles |
| Q05 | - |  |  | SI | Blood taken |
| Q06 | - |  |  | SI | Date bloods taken |
| Q07 | - |  |  | SI | Height and weight recorded? |
| Q08 | - |  |  | SI | Allergies / Reaction details reviewed / recorded? |
| Q09 | - |  |  | SI | Venous access assessment |
| Q10 | - |  |  | SI | Action taken if access is poor |
| Q11 | - |  |  | SI | MRSA screen needed |
| Q12 | - |  |  | SI | Date of MRSA screen |
| Q13 | - |  |  | SI | Transport |
| Q14 | - |  |  | SI | If needed, transport booking information given to ... |
| Q15 | - |  |  | SI | Appointment date for consent / prescription |
| Q16 | - |  |  | SI | Has patient had chemotherapy before? |
| Q17 | - |  |  | SI | If yes |
| Q18 | - |  |  | SI | Is the patient still aware of chemotherapy helplin... |
| Q19 | - |  |  | SI | Correct patient contact numbers? |
| Q20 | - |  |  | SI | Own thermometer |
| Q21 | - |  |  | SI | If no |
| Q22 | - |  |  | SI | Give the patient support service information |
| Q23 | - |  |  | SI | Advised re: helpline |
| Q24 | - |  |  | SI | Transport plan |
| Q25 | - |  |  | SI | Advised not to delay calling helpline |
| Q26 | - |  |  | SI | Advised to source own thermometer |
| Q27 | - |  |  | SI | Does the patient know who their key worker is? (If... |
| Q28 | - |  |  | SI | Does the patient understand their diagnosis and tr... |
| Q29 | - |  |  | SI | Verbal information given (Please tick relevant box... |
| Q30 | - |  |  | SI | General |
| Q31 | - |  |  | SI | How therapy works |
| Q32 | - |  |  | SI | How administered |
| Q33 | - |  |  | SI | Inpatient / Outpatient stay |
| Q34 | - |  |  | SI | Day units |
| Q35 | - |  |  | SI | Transport / Parking |
| Q36 | - |  |  | SI | Appointments |
| Q37 | - |  |  | SI | Other, please state |
| Q38 | - |  |  | SI | Specific |
| Q39 | - |  |  | SI | Dental work |
| Q40 | - |  |  | SI | Vaccinations - influenza / pneumococcal (no live v... |
| Q41 | - |  |  | SI | Prescriptions |
| Q42 | - |  |  | SI | Clinical trials |
| Q43 | - |  |  | SI | Diet and alcohol |
| Q44 | - |  |  | SI | Exercise / Swimming (no swimming with Central Veno... |
| Q45 | - |  |  | SI | Personal care - sun protection, tampons, razors |
| Q46 | - |  |  | SI | Barrier contraception |
| Q47 | - |  |  | SI | CVC care |
| Q48 | - |  |  | SI | Extravasation |
| Q49 | - |  |  | SI | Other, please state |
| Q50 | - |  |  | SI | Side effects |
| Q51 | - |  |  | SI | Neutropenia / Sepsis |
| Q52 | - |  |  | SI | Bleeding / Anaemia |
| Q53 | - |  |  | SI | Nausea / Vomiting |
| Q54 | - |  |  | SI | Diarrhoea / Constipation |
| Q55 | - |  |  | SI | Loss of appetite / Taste changes |
| Q56 | - |  |  | SI | Mouth/Gut ulcers |
| Q57 | - |  |  | SI | Gritty eyes / Blurred vision |
| Q58 | - |  |  | SI | Hair loss |
| Q59 | - |  |  | SI | Fatigue |
| Q60 | - |  |  | SI | Skin changes / Rashes (Palmer Planter Syndrome) |
| Q61 | - |  |  | SI | Fertility / Libido |
| Q62 | - |  |  | SI | Neuropathy |
| Q63 | - |  |  | SI | Renal / Liver toxicity |
| Q64 | - |  |  | SI | Cardiac / Lung toxicity |
| Q65 | - |  |  | SI | Bladder irritation / Discoloured urine |
| Q66 | - |  |  | SI | Allergic reaction |
| Q67 | - |  |  | SI | Flu-like symptoms |
| Q68 | - |  |  | SI | Fluid retention |
| Q69 | - |  |  | SI | CNS toxicity / Drowsiness |
| Q70 | - |  |  | SI | Laryngeal spasm |
| Q71 | - |  |  | SI | Other, please state |
| Q72 | - |  |  | SI | Written information provided: |
| Q73 | - |  |  | SI | Pre-Chemotherapy information pack |
| Q74 | - |  |  | SI | Details of any other written information given: |
| Q75 | - |  |  | SI | Does the patient require any MDT referrals, e.g. d... |
| Q76 | - |  |  | SI | Details of referrals made: |
| Q77 | - |  |  | SI | Are there any other issues of concern? |
| Q78 | - |  |  | SI | Please list and take action |
| Q79 | - |  |  | SI | Check against known UK / Overseas list areas of co... |
| Q80 | - |  |  | SI | Are there any outstanding issues for discussion? |
| Q81 | - |  |  | SI | Please list issues and arrangements made to comple... |
| Q82 | - |  |  | SI | Date |
| Q83 | - |  |  | SI | Time |
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