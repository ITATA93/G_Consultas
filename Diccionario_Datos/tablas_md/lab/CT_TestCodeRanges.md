# lab.CT_TestCodeRanges

**Schema:** lab
**Columnas:** 35
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTCR_ParRef | varchar | PK |  | NO | CT_TestCode Parent Reference |
| CTTCR_Age | varchar |  |  | SI | Age |
| CTTCR_Altitude_DR | varchar |  | FK | SI | Altitude DR |
| CTTCR_AutoHighRange | varchar |  |  | SI | Auto High Range |
| CTTCR_AutoLowRange | varchar |  |  | SI | Auto Low Range |
| CTTCR_ClinicalConditions_DR | varchar |  | FK | SI | Clinical Conditions DR |
| CTTCR_Comments | varchar |  |  | SI | Comments |
| CTTCR_Date | date |  |  | NO | Effective Date |
| CTTCR_DateEnd | date |  |  | SI | End Date |
| CTTCR_Ethnicity_DR | varchar |  | FK | SI | Ethnicity DR |
| CTTCR_HighRange | varchar |  |  | SI | High Range |
| CTTCR_LowRange | varchar |  |  | SI | Low Range |
| CTTCR_Order | double |  |  | NO | Order |
| CTTCR_PanicHigh | varchar |  |  | SI | Panic High |
| CTTCR_PanicLow | varchar |  |  | SI | Panic Low |
| CTTCR_PathHigh | varchar |  |  | SI | Path High |
| CTTCR_PathLow | varchar |  |  | SI | Path Low |
| CTTCR_PatientLocation_DR | varchar |  | FK | SI | Patient Location DR |
| CTTCR_PregnantAutoHighRange | varchar |  |  | SI | Pregnant Auto High Range |
| CTTCR_PregnantAutoLowRange | varchar |  |  | SI | Pregnant Auto Low Range |
| CTTCR_PregnantHighRange | varchar |  |  | SI | Pregnant High Range |
| CTTCR_PregnantLowRange | varchar |  |  | SI | Pregnant Low Range |
| CTTCR_PregnantPanicHighRange | varchar |  |  | SI | Pregnant Panic High Range |
| CTTCR_PregnantPanicLowRange | varchar |  |  | SI | Pregnant Panic Low Range |
| CTTCR_PregnantPathHigh | varchar |  |  | SI | Pregnant Path High |
| CTTCR_PregnantPathLow | varchar |  |  | SI | Pregnant Path Low |
| CTTCR_PregnantUnacceptHigh | varchar |  |  | SI | Pregnant Unaccept High |
| CTTCR_PregnantUnacceptLow | varchar |  |  | SI | Pregnant Unaccept Low |
| CTTCR_RangesType | varchar |  |  | NO | Ranges Type |
| CTTCR_RowId | varchar |  |  | NO | - |
| CTTCR_Species_DR | varchar |  | FK | SI | Des Ref Species |
| CTTCR_UnacceptHigh | varchar |  |  | SI | Unaccept High |
| CTTCR_UnacceptLow | varchar |  |  | SI | Unaccept Low |
| CTTCR_UserSite_DR | varchar |  | FK | SI | User Site |
| CTTCR_WeeksOfPregnancy | varchar |  |  | SI | Weeks Of Pregnancy |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*