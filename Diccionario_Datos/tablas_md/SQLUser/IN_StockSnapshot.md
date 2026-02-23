# SQLUser.IN_StockSnapshot

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STKSNAP_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | 1A: Is the Patient different than his/her baseline... |
| Q02 | - |  |  | SI | 1B: Has the patient had any fluctuation in mental ... |
| Q03 | - |  |  | SI | (e.g Richmond Agitation and Sedation Scale (RASS))... |
| Q04 | - |  |  | SI | Acute Onset or fluctuating course (positive if  'Y... |
| Q05 | - |  |  | SI | Attempt the Attention Screening Examination (ASE) ... |
| Q06 | - |  |  | SI | If patient is unable to perform this test or the s... |
| Q07 | - |  |  | SI | 2A: ASE Letters test ? |
| Q08 | - |  |  | SI | S A V E A H A A R T |
| Q09 | - |  |  | SI | Direction: Say to the patient 'I am going to read ... |
| Q10 | - |  |  | SI | Score for ASE Letters |
| Q11 | - |  |  | SI | 2B: ASE Pictures test? |
| Q12 | - |  |  | SI | Score for ASE Pictures |
| Q13 | - |  |  | SI | Confirm patient response for Feature 2 |
| Q14 | - |  |  | SI | 3A: Use either Set A or Set B,  alternate on conse... |
| Q15 | - |  |  | SI | Positive if combined score is less than 4	 |
| Q16 | - |  |  | SI | Set A: |
| Q17 | - |  |  | SI | 1. Will a stone float on water? |
| Q18 | - |  |  | SI | 2. Are there fish in the sea? |
| Q19 | - |  |  | SI | 3. Does one pound weigh more than two pounds? |
| Q20 | - |  |  | SI | 4. Can you use a hammer to pound a nail? |
| Q21 | - |  |  | SI | Set B: |
| Q22 | - |  |  | SI | 1. Will a leaf float on water? |
| Q23 | - |  |  | SI | 2. Are there Elephants in the sea? |
| Q24 | - |  |  | SI | 3. Do two pounds weigh more than one pound? |
| Q25 | - |  |  | SI | 4. Can you use a hammer to cut wood? |
| Q26 | - |  |  | SI | 3B: Command: Say to the patient ''Hold up this man... |
| Q27 | - |  |  | SI | Confirm name of set used |
| Q28 | - |  |  | SI | Label A	 |
| Q29 | - |  |  | SI | Label B |
| Q30 | - |  |  | SI | Confirm score for set used 	 |
| Q31 | - |  |  | SI | Confirm score for command used	 |
| Q32 | - |  |  | SI | Total score for Set and  Command |
| Q33 | - |  |  | SI | Confirm patient's response for Feature 3	 |
| Q34 | - |  |  | SI | Please select Positive if the actual Richmond Agit... |
| Q35 | - |  |  | SI | Overall CAM-ICU |
| Q36 | - |  |  | SI | Instructions for completing form: |
| Q37 | - |  |  | SI | Instructions for Feature 2 - Inattention:	 |
| Q38 | - |  |  | SI | Positive if either score for 2A or 2 B is less tha... |
| Q39 | - |  |  | SI | 2A: ASE Letters:	 |
| Q40 | - |  |  | SI | Read letters from the following letter list in a n... |
| Q41 | - |  |  | SI | S A V E A H A A R T	 |
| Q42 | - |  |  | SI | Scoring: Errors are counted when patient fails to ... |
| Q43 | - |  |  | SI | Score 1 point for each error |
| Q44 | - |  |  | SI | 2B: ASE Pictures:	 |
| Q45 | - |  |  | SI | Directions are included on the picture packets (pl... |
| Q46 | - |  |  | SI | Instructions for Feature 3 - Disorganised thinking... |
| Q47 | - |  |  | SI | 3B: Command:(examiner holds two fingers in front o... |
| Q48 | - |  |  | SI | **if the patient is unable to move both arms, for ... |
| Q49 | - |  |  | SI | Patient earns 1 point if able to successfully comp... |
| Q50 | - |  |  | SI | Overall CAM-ICU:(Feature 1 Plus 2 AND either 3 or ... |
| Q51 | - |  |  | SI | Confirm score for set used |
| Q52 | - |  |  | SI | Confirm score for command used	 |
| Q53 | - |  |  | SI | Or |
| Q54 | - |  |  | SI | Confirm patient's response for Feature 3	 |
| Q55 | - |  |  | SI | Date |
| Q56 | - |  |  | SI | Time |
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
| STKSNAP_BaseUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| STKSNAP_Date | date |  |  | SI | Date of snapshot |
| STKSNAP_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| STKSNAP_Item_DR | bigint |  | FK | SI | Des Ref INCItm |
| STKSNAP_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| STKSNAP_LogQty | double |  |  | SI | Logical Quantity |
| STKSNAP_Period | varchar |  |  | SI | Reporting Period |
| STKSNAP_PurchaseUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| STKSNAP_ServTax_DR | bigint |  | FK | SI | Des Ref ARCServTax |
| STKSNAP_Time | time |  |  | SI | Time of snapshot |
| STKSNAP_UnitCost | double |  |  | SI | Unit Cost |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*