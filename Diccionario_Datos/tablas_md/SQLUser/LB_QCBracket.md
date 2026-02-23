# SQLUser.LB_QCBracket

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBQCB_RowID | bigint | PK |  | NO | - |
| LBQCB_AllQCRequiredToPass | varchar |  |  | SI | QC from all other test items in the group must pas... |
| LBQCB_BracketID | varchar |  |  | SI | Bracket number 
Unique per instrument |
| LBQCB_ClosedDate | date |  |  | SI | Date closed |
| LBQCB_ClosedTime | time |  |  | SI | Time closed |
| LBQCB_CreatedDate | date |  |  | SI | Date created |
| LBQCB_CreatedTime | time |  |  | SI | Time created |
| LBQCB_Instrument_DR | bigint |  | FK | SI | Instrument |
| LBQCB_Number | numeric |  |  | SI | Bracket number 
Unique per instrument |
| LBQCB_QCMode | varchar |  |  | SI | Instrument QC Mode
Standard type: LabInstrumentQC... |
| LBQCB_Status | varchar |  |  | SI | Bracket Status Status
StandardType: LabQCRunStatu... |
| LBQCB_TestItem_DR | bigint |  | FK | SI | Test Item Link |
| LBQCB_WorksheetDef_DR | bigint |  | FK | SI | Worksheet Definition for all LBQCBWorksheets |
| LBQCB_Worksheet_DR | bigint |  | FK | SI | Worksheet with the QC (can also have patient resul... |
| LBQCB_Worksheets | varchar |  |  | SI | Worksheets with the patient results (for QC Only w... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*