# lab.EP_VisitTestSetData

**Schema:** lab
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISTD_ParRef | varchar | PK |  | NO | EP_VisitTestSet Parent Reference |
| VISTD_Abnormal | varchar |  |  | SI | - |
| VISTD_ClinicallySignificant | varchar |  |  | SI | Clinically Significant |
| VISTD_Comments | varchar |  |  | SI | Comments |
| VISTD_DisplaySequence | double |  |  | SI | Display Sequence |
| VISTD_HL7CodedCECode | varchar |  |  | SI | HL7 Coded CE Code |
| VISTD_HL7DataType | varchar |  |  | SI | HL7 Data Type |
| VISTD_HL7ReferenceComment | varchar |  |  | SI | HL7 Reference Comment |
| VISTD_ICD10List | varchar |  |  | SI | ICD10 list |
| VISTD_InstrumentDate | date |  |  | SI | Instrument Date |
| VISTD_InstrumentFlags | varchar |  |  | SI | Instrument Flags |
| VISTD_InstrumentTime | time |  |  | SI | Instrument Time |
| VISTD_Machine_DR | varchar |  | FK | SI | Machine DR |
| VISTD_ManualFlag | varchar |  |  | SI | Manual Flag |
| VISTD_PreviousResult | varchar |  |  | SI | Previous Result |
| VISTD_PrimaryResult | varchar |  |  | SI | Primary Result |
| VISTD_RepeatRequired | varchar |  |  | SI | Repeat Required |
| VISTD_ResultRefRangeHigh | varchar |  |  | SI | Reference Range High |
| VISTD_ResultRefRangeLow | varchar |  |  | SI | Reference Range Low |
| VISTD_ResultStatus | varchar |  |  | SI | Test item result status |
| VISTD_RowId | varchar |  |  | NO | - |
| VISTD_SupressReport | varchar |  |  | SI | Supress Report |
| VISTD_TestCode_DR | varchar |  | FK | NO | Des Ref TestCode |
| VISTD_TestData | varchar |  |  | SI | Test Data |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*