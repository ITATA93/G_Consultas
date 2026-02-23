# SQLUser.PAC_InstrText

**Schema:** SQLUser
**Columnas:** 44
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INTX_RowId | bigint | PK |  | NO | - |
| INTX_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| INTX_AnaestMethod_DR | bigint |  | FK | SI | Des Ref Anaesthesia Method |
| INTX_Code | varchar |  |  | SI | Code |
| INTX_CreatedDate | date |  |  | SI | Created Date |
| INTX_CreatedTime | time |  |  | SI | Created Time |
| INTX_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INTX_Desc | varchar |  |  | SI | Description |
| INTX_EpisodeSubtype_DR | bigint |  | FK | SI | Des Ref EpisodeSubtype |
| INTX_HCP_DR | varchar |  | FK | SI | Health Care Provider des ref |
| INTX_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| INTX_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| INTX_ItemCat_DR | bigint |  | FK | SI | Des Ref ItemCat |
| INTX_LetterTypeDR | bigint |  | FK | SI | Letter Type Des Ref |
| INTX_Map | varchar |  |  | SI | Map |
| INTX_ModuleLocation_DR | bigint |  | FK | SI | Des Ref CTLOC |
| INTX_Module_DR | bigint |  | FK | SI | Des Ref Module |
| INTX_OutcomeOfOffer_DR | bigint |  | FK | SI | Des Ref OutcomeOfOffer |
| INTX_Owner | varchar |  |  | SI | Owner |
| INTX_Paragraph | double |  |  | SI | Paragraph |
| INTX_ReasonForCancel_DR | bigint |  | FK | SI | Des Ref Reason For Cancel |
| INTX_ReasonForNotShow_DR | bigint |  | FK | SI | Des Ref Reason For Not Show |
| INTX_ReasonForRemoval_DR | bigint |  | FK | SI | Des Ref ReasonForRemoval |
| INTX_ReasonForTransfer_DR | bigint |  | FK | SI | Des Ref Reason For Transfer |
| INTX_RefPrior_DR | bigint |  | FK | SI | Des Ref RefPrior |
| INTX_RefStatus_DR | bigint |  | FK | SI | Des Ref RefStatus |
| INTX_ReportCode | varchar |  |  | SI | ReportCode |
| INTX_ReportText | varchar |  |  | SI | ReportText |
| INTX_ReportTextHTMLPlainText | longvarchar |  |  | SI | Des Ref websys.Document |
| INTX_ReportTextHTMLRichText | longvarchar |  |  | SI | Des Ref websys.Document |
| INTX_ReportTextRTF | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| INTX_SpecialityLocation_DR | bigint |  | FK | SI | Des Ref SpecialityLocation |
| INTX_StatePPP_DR | bigint |  | FK | SI | Des REf StatePPP |
| INTX_SundryDebtor_DR | bigint |  | FK | SI | Des Ref SundryDebtor |
| INTX_Trust_DR | bigint |  | FK | SI | Des Ref Trust |
| INTX_UpdatedDate | date |  |  | SI | Updated Date |
| INTX_UpdatedTime | time |  |  | SI | Updated Time |
| INTX_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| INTX_WLTypeOfOffer_DR | bigint |  | FK | SI | Des Ref WLTypeOfOffer |
| INTX_WaitingListType_DR | bigint |  | FK | SI | Des Ref WaitingListType |
| Q35Q1 | - |  |  | SI | Goal |
| Q35Q2 | - |  |  | SI | Timing |
| Q35Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*