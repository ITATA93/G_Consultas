# SQLUser.ARC_ItemCat

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCIC_RowId | bigint | PK |  | NO | - |
| ARCIC_AddToDiagnosticStage | varchar |  |  | SI | Add to Diagnostic Stage |
| ARCIC_AllowQuestEditExecOrd | varchar |  |  | SI | Allow Questionnaire to be Edited for Executed Orde... |
| ARCIC_AllowToEnterOneResultOnly | varchar |  |  | SI | Allow ToEnterOneResultOnly |
| ARCIC_AutoOrder | varchar |  |  | SI | Order Automatically from a Clinical Pathway |
| ARCIC_BillingType | varchar |  |  | SI | Billing Type |
| ARCIC_CalcQtyFlag | varchar |  |  | NO | Calculate Qty Flag |
| ARCIC_Code | varchar |  |  | NO | Item Category Code |
| ARCIC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCIC_Commissioning | varchar |  |  | SI | Commissioning  |
| ARCIC_CounterTypeDr | bigint |  |  | SI | Counter type DR |
| ARCIC_CreatedDate | date |  |  | SI | Created Date |
| ARCIC_CreatedTime | time |  |  | SI | Created Time |
| ARCIC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCIC_DateFrom | date |  |  | SI | DateFrom |
| ARCIC_DateTo | date |  |  | SI | DateTo |
| ARCIC_Desc | varchar |  |  | NO | Item Category Description |
| ARCIC_DiagnosticWaitTime | double |  |  | SI | DiagnosticWaitTime |
| ARCIC_DicomResult | varchar |  |  | SI | Dicom Result |
| ARCIC_DirectlyExecute | varchar |  |  | SI | Directly Execute from a Clinical Pathway |
| ARCIC_DisplayOPWhiteboard | varchar |  |  | SI | DisplayOPWhiteboard |
| ARCIC_DontCreateWL | varchar |  |  | SI | DontCreateWL |
| ARCIC_DoseType | varchar |  |  | SI | Dose Type |
| ARCIC_ExecCateg_DR | bigint |  | FK | SI | Des Ref ExecCateg |
| ARCIC_ExecDose | varchar |  |  | SI | Executable Dosage Dependant |
| ARCIC_ExecFlag | varchar |  |  | SI | Execution Flag |
| ARCIC_ExecFreq | varchar |  |  | SI | Executable Frequency Dependant |
| ARCIC_ExecQuestionnaire_DR | bigint |  | FK | SI | Des Ref Execution Questionnaire |
| ARCIC_ExpiryDays | double |  |  | SI | ExpiryDays |
| ARCIC_FreqGroup_DR | bigint |  | FK | SI | Des Ref to OECFrequencyGroup |
| ARCIC_HL7ResultType | varchar |  |  | SI | HL7 Result Type |
| ARCIC_IVExpiry | double |  |  | SI | IV Expiry |
| ARCIC_IgnoreDiscOrdItmInOrdSet | varchar |  |  | SI | Do Not Ignore Discountinued Order Items if in an O... |
| ARCIC_InhaledMedGas | varchar |  |  | SI | Inhaled Medical Gas |
| ARCIC_IsCarePlanGoal | varchar |  |  | SI | Is a Care Plan Goal |
| ARCIC_IsTest | varchar |  |  | SI | Is Test  |
| ARCIC_LaboratoryCodes | varchar |  |  | SI | Laboratory Codes |
| ARCIC_LateralityReq | varchar |  |  | SI | Laterality Required - Radiology  |
| ARCIC_LetterType_DR | bigint |  | FK | SI | Letter Type |
| ARCIC_MarkReadyForInv | varchar |  |  | SI | MarkReadyForInv |
| ARCIC_NonReviewable | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2020+ (JRIA: T... |
| ARCIC_NurseWorkBench | varchar |  |  | SI | Show in Nurses WorkBench |
| ARCIC_OnlyShowVerRes | varchar |  |  | SI | Only Show Verified Results |
| ARCIC_OrdCat_DR | bigint |  | FK | SI | Des Ref to OrdCateg |
| ARCIC_OrderType | varchar |  |  | NO | Order Type |
| ARCIC_OverridePrice | varchar |  |  | SI | OverridePrice |
| ARCIC_Owner | varchar |  |  | SI | Owner |
| ARCIC_PhoneOrderReviewTime | double |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2020+ (JRIA: T... |
| ARCIC_PrescrExpDays | double |  |  | SI | PrescrExpDays |
| ARCIC_PrescrRepeatDays | double |  |  | SI | PrescrRepeatDays |
| ARCIC_Questionnaire_DR | bigint |  | FK | SI | Des Ref Questionnaire |
| ARCIC_ReadyForInvoiceOnPack | varchar |  |  | SI | Mark Ready for Invoice on Packing |
| ARCIC_RecieveSpecimens | varchar |  |  | SI | Recieve Specimens |
| ARCIC_RenderingTrigger | varchar |  |  | SI | Rendering Trigger |
| ARCIC_RestrictedOrder | varchar |  |  | SI | Restricted Order |
| ARCIC_ResultCategories | varchar |  |  | SI | Result Categories |
| ARCIC_ResultEPRChart_DR | bigint |  | FK | SI | Result Entry EPR Chart |
| ARCIC_ReviewRequired | varchar |  |  | SI | ReviewRequired |
| ARCIC_SecSignForAdm | varchar |  |  | SI | SecSignForAdm |
| ARCIC_Template | varchar |  |  | SI | Template |
| ARCIC_TextResultType_DR | bigint |  | FK | SI | Des Ref TextResultType |
| ARCIC_UpdatedDate | date |  |  | SI | Updated Date |
| ARCIC_UpdatedTime | time |  |  | SI | Updated Time |
| ARCIC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ARCIC_UseODBCforWord | varchar |  |  | SI | Use ODBC for Word |
| ARCIC_UserDefWindow_DR | bigint |  | FK | SI | Des Ref UserDefWindow |
| ARCIC_WarningNonVerResult | varchar |  |  | SI | WarningNonVerResult |
| ChildQ100DR | - |  |  | SI | Child Reference: Fuerza y resistencia |
| Q73Q1 | - |  |  | SI | Ojo |
| Q73Q10 | - |  |  | SI | Nistagmo |
| Q73Q11 | - |  |  | SI | Motilidad supranuclear |
| Q73Q2 | - |  |  | SI | Estrabismo |
| Q73Q3 | - |  |  | SI | Paresia plano vertical |
| Q73Q4 | - |  |  | SI | Paresia plano horizontal |
| Q73Q5 | - |  |  | SI | Tamaño pupilar |
| Q73Q6 | - |  |  | SI | Reflejo pupilar directo |
| Q73Q7 | - |  |  | SI | Reflejo pupilar consensuado |
| Q73Q8 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*