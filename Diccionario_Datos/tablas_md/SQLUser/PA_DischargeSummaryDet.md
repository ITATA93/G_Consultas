# SQLUser.PA_DischargeSummaryDet

**Schema:** SQLUser
**Columnas:** 38
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PA_DischargeSummary Parent Reference |
| ChildQ71DR | - |  |  | SI | Child Reference: Sinus Tract, Tunneling, Undermini... |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_LabResult_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| DET_MRDiagnos_DR | varchar |  | FK | SI | Des Ref MRDiagnos |
| DET_MREncEntry_DR | bigint |  | FK | SI | Des Ref to MREncEntry |
| DET_MRMedication_DR | varchar |  | FK | SI | Des Ref MRMedication |
| DET_MRNursingNotes_DR | varchar |  | FK | SI | Des Ref MRNursingNotes |
| DET_MRPictures_DR | varchar |  | FK | SI | Des Ref to MRPictures |
| DET_MRPresentIllness_DR | varchar |  | FK | SI | Des Ref MRPresentIllness |
| DET_MRProcedures_DR | varchar |  | FK | SI | Des Ref MRProcedures |
| DET_MRReasonForEnc_DR | varchar |  | FK | SI | Des Ref to MRReasonForEnc |
| DET_MRSubFind_DR | varchar |  | FK | SI | Des Ref MRSubFind |
| DET_OEOrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| DET_ORAnaestOperation_DR | varchar |  | FK | SI | Des Ref to ORAnaestOperation |
| DET_ORAnaesthesia_DR | varchar |  | FK | SI | Des Ref ORAnaesthesia |
| DET_PAAlertMsg_DR | varchar |  | FK | SI | Des Ref PAAlertMsg |
| DET_PAAllergy_DR | varchar |  | FK | SI | Des Ref PAAllergy |
| DET_PAFamily_DR | varchar |  | FK | SI | Des Ref PAFamily |
| DET_PAOperation_DR | varchar |  | FK | SI | Des Ref PAOperation |
| DET_PAProblem_DR | varchar |  | FK | SI | Des Ref to PAProblem |
| DET_PASocHist_DR | varchar |  | FK | SI | Des Ref PASocHist |
| DET_QuestCode | varchar |  |  | SI | DETQuestCode |
| DET_QuestID | varchar |  |  | SI | DETQuestCode |
| DET_RowId | varchar |  |  | NO | - |
| DET_TextResult_DR | bigint |  | FK | SI | Des Ref OETextResult |
| DET_WordResult_DR | varchar |  | FK | SI | Des Ref OEOrdResult |
| Q70Q1 | - |  |  | SI | Date |
| Q70Q10 | - |  |  | SI | Entered by |
| Q70Q2 | - |  |  | SI | Max length (cm) |
| Q70Q3 | - |  |  | SI | Max width (cm) |
| Q70Q4 | - |  |  | SI | Max depth (cm) |
| Q70Q5 | - |  |  | SI | Sinus Tract |
| Q70Q6 | - |  |  | SI | Tunnelling / Undermining |
| Q70Q7 | - |  |  | SI | Pressure injury stage |
| Q70Q8 | - |  |  | SI | Add image |
| Q70Q9 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*