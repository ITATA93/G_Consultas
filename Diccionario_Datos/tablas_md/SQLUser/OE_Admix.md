# SQLUser.OE_Admix

**Schema:** SQLUser
**Columnas:** 244
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AM_RowId | bigint | PK |  | NO | - |
| AM_AddedAdditiveFlg | varchar |  |  | SI | AMAddedAdditiveFlg |
| AM_AdditiveVolume | double |  |  | SI | Additive Volume (mL) |
| AM_AdmixManufLock | bit |  |  | SI | Lock By Admixture Manufacture |
| AM_AdmixType | varchar |  |  | NO | Admixture Type |
| AM_AllowToModify | varchar |  |  | SI | Allow to Modify Recipe |
| AM_BulkAdmixtureRecipe_DR | bigint |  | FK | SI | Des Ref Bulk Admixture Recipe |
| AM_BulkQuantity | double |  |  | SI | Bulk Quantity |
| AM_BulkRecLoc_DR | bigint |  | FK | SI | Bulk Receiving Location |
| AM_Date | date |  |  | SI | Date |
| AM_DefineTheFinalVolume | varchar |  |  | SI | Define the Final Volume |
| AM_DrgHistDesc_DR | varchar |  | FK | SI | Des Ref PHCDrgHistDesc |
| AM_FinalForm_DR | bigint |  | FK | SI | Final Form |
| AM_GenericHistDesc_DR | varchar |  | FK | SI | Des Ref PHCGenericHistDesc |
| AM_IncludeAdditiveVolume | varchar |  |  | SI | Include Additive Volume |
| AM_IncludeOverfillVolume | varchar |  |  | SI | Include Overfill Volume |
| AM_MainItem | varchar |  |  | SI | Main Item |
| AM_ManufInstruction | varchar |  |  | SI | Manufacture Instruction |
| AM_ManufactureStatus | varchar |  |  | SI | AMManufactureStatus |
| AM_MaxFlowRate | double |  |  | SI | Max Flow Rate |
| AM_MinFlowRate | double |  |  | SI | Min Flow Rate |
| AM_NurseInstructions | varchar |  |  | SI | Nurse Instructions |
| AM_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| AM_OrderedBagVolume | double |  |  | SI | Volume Per Bag (mL) from Order Entry |
| AM_OverfillVolume | double |  |  | SI | Overfill Volume (mL) |
| AM_PCALoadingVolume | double |  |  | SI | PCA Loading Volume |
| AM_PCALoadingVolumeUOM_DR | bigint |  | FK | SI | PCA Loading Volume UOM |
| AM_Quantity | double |  |  | SI | Quantity |
| AM_ReleaseSpecification | varchar |  |  | SI | Release Specification |
| AM_RemainInProgress | varchar |  |  | SI | Remain In progress when is quantity fulfilled |
| AM_ResolvedSolv_DR | varchar |  | FK | SI | Resolved Solvent |
| AM_SolventBagVolume | double |  |  | SI | Solvent Bag Volume (mL) |
| AM_SolventVolumeBeforeMixing | double |  |  | SI | Solvent Volume Before Mixing (mL) |
| AM_Solvent_DR | varchar |  | FK | SI | Solvent |
| AM_StartingSolventVolume | double |  |  | SI | Starting Solvent Volume (mL) |
| AM_SubtractAdditive | varchar |  |  | SI | Subtract Additive Volumes from Solvent |
| AM_Time | time |  |  | SI | Time |
| AM_TotalBagVolume | double |  |  | SI | Total Final Volume Per Bag (mL) |
| AM_TotalFlowRate | double |  |  | SI | Total Flow Rate |
| AM_TotalFlowRatePerUOM | varchar |  |  | SI | Total Flow Rate Per UOM |
| AM_TotalFlowRateUOM_DR | bigint |  | FK | SI | Total Flow Rate UOM |
| AM_TransactionNo | varchar |  |  | SI | AMTransactionNo |
| AM_UOM_DR | bigint |  | FK | SI | UOM |
| AM_VolumeCalculatorUsed | varchar |  |  | SI | Volume Calculator Used |
| AM_WithdrawVolume | double |  |  | SI | Withdraw Volume (mL) |
| AM_WithoutSolvent | varchar |  |  | SI | Admixture ordered without a solvent |
| Q01 | - |  |  | SI | Cerebellar |
| Q02 | - |  |  | SI | Mood |
| Q03 | - |  |  | SI | Headache |
| Q04 | - |  |  | SI | Constipation |
| Q05 | - |  |  | SI | Hearing |
| Q06 | - |  |  | SI | Vision |
| Q07 | - |  |  | SI | Skin |
| Q08 | - |  |  | SI | Allergy |
| Q09 | - |  |  | SI | Fever/No infection |
| Q10 | - |  |  | SI | Local tissue |
| Q100 | - |  |  | SI | Grade 4 |
| Q101 | - |  |  | SI | Grade 4 |
| Q102 | - |  |  | SI | Grade 4 |
| Q103 | - |  |  | SI | Grade 4 |
| Q104 | - |  |  | SI | Grade 4 |
| Q105 | - |  |  | SI | Grade 4 |
| Q106 | - |  |  | SI | Grade 4 |
| Q107 | - |  |  | SI | Grade 0 |
| Q108 | - |  |  | SI | Grade 0 |
| Q109 | - |  |  | SI | Grade 0 |
| Q11 | - |  |  | SI | Weight gain/loss |
| Q110 | - |  |  | SI | Grade 0 |
| Q111 | - |  |  | SI | Grade 0 |
| Q112 | - |  |  | SI | Grade 0 |
| Q113 | - |  |  | SI | Grade 0 |
| Q114 | - |  |  | SI | Grade 0 |
| Q115 | - |  |  | SI | Grade 1 |
| Q116 | - |  |  | SI | Grade 1 |
| Q117 | - |  |  | SI | Grade 1 |
| Q118 | - |  |  | SI | Grade 1 |
| Q119 | - |  |  | SI | Grade 1 |
| Q12 | - |  |  | SI | Hyperglycaemia |
| Q120 | - |  |  | SI | Grade 1 |
| Q121 | - |  |  | SI | Grade 1 |
| Q122 | - |  |  | SI | Grade 1 |
| Q123 | - |  |  | SI | Grade 1 |
| Q124 | - |  |  | SI | Grade 2 |
| Q125 | - |  |  | SI | Grade 2 |
| Q126 | - |  |  | SI | Grade 2 |
| Q127 | - |  |  | SI | Grade 2 |
| Q128 | - |  |  | SI | Grade 2 |
| Q129 | - |  |  | SI | Grade 2 |
| Q13 | - |  |  | SI | Hypoglycaemia |
| Q130 | - |  |  | SI | Grade 2 |
| Q131 | - |  |  | SI | Grade 2 |
| Q132 | - |  |  | SI | Grade 2 |
| Q133 | - |  |  | SI | Grade 3 |
| Q134 | - |  |  | SI | Grade 3 |
| Q135 | - |  |  | SI | Grade 3 |
| Q136 | - |  |  | SI | Grade 3 |
| Q137 | - |  |  | SI | Grade 3 |
| Q138 | - |  |  | SI | Grade 3 |
| Q139 | - |  |  | SI | Grade 3 |
| Q14 | - |  |  | SI | Amylase |
| Q140 | - |  |  | SI | Grade 3 |
| Q141 | - |  |  | SI | Grade 3 |
| Q142 | - |  |  | SI | Grade 4 |
| Q143 | - |  |  | SI | Grade 4 |
| Q144 | - |  |  | SI | Grade 4 |
| Q145 | - |  |  | SI | Grade 4 |
| Q146 | - |  |  | SI | Grade 4 |
| Q147 | - |  |  | SI | Grade 4 |
| Q148 | - |  |  | SI | Grade 4 |
| Q149 | - |  |  | SI | Grade 4 |
| Q15 | - |  |  | SI | Hypercalcaemia |
| Q150 | - |  |  | SI | Grade 0 |
| Q151 | - |  |  | SI | Degree of severity definition |
| Q152 | - |  |  | SI | Grade 1: Mild, with no or mild symptoms |
| Q153 | - |  |  | SI | Grade 2: Moderate |
| Q154 | - |  |  | SI | Grade 3: Severe but not life-threatening |
| Q155 | - |  |  | SI | Grade 4: Life-threatening |
| Q156 | - |  |  | SI | Grade 0: No adverse reactions related to treatment... |
| Q157 | - |  |  | SI | Date |
| Q158 | - |  |  | SI | Time |
| Q16 | - |  |  | SI | Hypocalcaemia |
| Q17 | - |  |  | SI | Hypomagnesemia |
| Q18 | - |  |  | SI | Pulmonary |
| Q19 | - |  |  | SI | Dysrhythmias |
| Q20 | - |  |  | SI | Function |
| Q21 | - |  |  | SI | Ischaemia |
| Q22 | - |  |  | SI | Pericardial |
| Q23 | - |  |  | SI | Hypertension |
| Q24 | - |  |  | SI | Hypotension |
| Q25 | - |  |  | SI | Sensory |
| Q26 | - |  |  | SI | Motor |
| Q27 | - |  |  | SI | WBC (x1000/mm3) |
| Q28 | - |  |  | SI | PLT (x1000/mm3) |
| Q29 | - |  |  | SI | Hgb (gm/dl) |
| Q30 | - |  |  | SI | ANC (x1000/mm3) |
| Q31 | - |  |  | SI | Lymph (x1000/mm3) |
| Q32 | - |  |  | SI | Haemorrhage |
| Q33 | - |  |  | SI | Infection |
| Q34 | - |  |  | SI | Nausea |
| Q35 | - |  |  | SI | Vomiting |
| Q36 | - |  |  | SI | Diarrhoea |
| Q37 | - |  |  | SI | Stomatitis |
| Q38 | - |  |  | SI | Bilirubin |
| Q39 | - |  |  | SI | SGOT/SGPT |
| Q40 | - |  |  | SI | Alkaline Phosphatase (ALP) / 5'Nucleotidase |
| Q41 | - |  |  | SI | Clinical |
| Q42 | - |  |  | SI | Creatinine |
| Q43 | - |  |  | SI | Proteinuria |
| Q44 | - |  |  | SI | Haematuria |
| Q45 | - |  |  | SI | Alopecia |
| Q46 | - |  |  | SI | Cortical |
| Q47 | - |  |  | SI | Fibrinogen |
| Q48 | - |  |  | SI | Prothrombin |
| Q49 | - |  |  | SI | Partial thromboplastin time |
| Q50 | - |  |  | SI | Grades |
| Q51 | - |  |  | SI | Grade 0 |
| Q52 | - |  |  | SI | Grade 1 |
| Q53 | - |  |  | SI | Grade 2 |
| Q54 | - |  |  | SI | Grade 3 |
| Q55 | - |  |  | SI | Grade 4 |
| Q56 | - |  |  | SI | Grade 0 |
| Q57 | - |  |  | SI | Grade 0 |
| Q58 | - |  |  | SI | Grade 0 |
| Q59 | - |  |  | SI | Grade 0 |
| Q60 | - |  |  | SI | Grade 0 |
| Q61 | - |  |  | SI | Grade 0 |
| Q62 | - |  |  | SI | Grade 0 |
| Q63 | - |  |  | SI | Grade 0 |
| Q64 | - |  |  | SI | Grade 0 |
| Q65 | - |  |  | SI | Grade 0 |
| Q66 | - |  |  | SI | Grade 1 |
| Q67 | - |  |  | SI | Grade 1 |
| Q68 | - |  |  | SI | Grade 1 |
| Q69 | - |  |  | SI | Grade 1 |
| Q70 | - |  |  | SI | Grade 1 |
| Q71 | - |  |  | SI | Grade 1 |
| Q72 | - |  |  | SI | Grade 1 |
| Q73 | - |  |  | SI | Grade 1 |
| Q74 | - |  |  | SI | Grade 1 |
| Q75 | - |  |  | SI | Grade 1 |
| Q76 | - |  |  | SI | Grade 2 |
| Q77 | - |  |  | SI | Grade 2 |
| Q78 | - |  |  | SI | Grade 2 |
| Q79 | - |  |  | SI | Grade 2 |
| Q80 | - |  |  | SI | Grade 2 |
| Q81 | - |  |  | SI | Grade 2 |
| Q82 | - |  |  | SI | Grade 2 |
| Q83 | - |  |  | SI | Grade 2 |
| Q84 | - |  |  | SI | Grade 2 |
| Q85 | - |  |  | SI | Grade 2 |
| Q86 | - |  |  | SI | Grade 3 |
| Q87 | - |  |  | SI | Grade 3 |
| Q88 | - |  |  | SI | Grade 3 |
| Q89 | - |  |  | SI | Grade 3 |
| Q90 | - |  |  | SI | Grade 3 |
| Q91 | - |  |  | SI | Grade 3 |
| Q92 | - |  |  | SI | Grade 3 |
| Q93 | - |  |  | SI | Grade 3 |
| Q94 | - |  |  | SI | Grade 3 |
| Q95 | - |  |  | SI | Grade 3 |
| Q96 | - |  |  | SI | Grade 4 |
| Q97 | - |  |  | SI | Grade 4 |
| Q98 | - |  |  | SI | Grade 4 |
| Q99 | - |  |  | SI | Grade 4 |
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