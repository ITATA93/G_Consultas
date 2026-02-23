# epr_Pref.ObservationItemEWS

**Schema:** epr_Pref
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| EWSPREFActiveFor | double |  |  | SI | Active For (Hours) |
| EWSPREFAgeFromDays | integer |  |  | SI | Age From Days |
| EWSPREFAgeFromMonths | integer |  |  | SI | Age From Months |
| EWSPREFAgeFromYears | integer |  |  | SI | Age From Years |
| EWSPREFAgeToDays | integer |  |  | SI | Age To Days |
| EWSPREFAgeToMonths | integer |  |  | SI | Age To Months |
| EWSPREFAgeToYears | integer |  |  | SI | Age To Years |
| EWSPREFCTLocDR | bigint |  | FK | SI | Des Ref to Location CT |
| EWSPREFDateFrom | date |  |  | NO | Date From |
| EWSPREFDateTo | date |  |  | SI | Date To |
| EWSPREFDisplayWarning | varchar |  |  | SI | Display Warning |
| EWSPREFEarlyWarningScoringSystem | bigint |  |  | SI | Early Warning Scoring System |
| EWSPREFFrom | double |  |  | SI | Range From |
| EWSPREFObsItemDR | bigint |  | FK | NO | Reference to Observation Item |
| EWSPREFObsItemLookupValueDR | varchar |  | FK | SI | Des Ref to Observation Item Lookup Values CT  |
| EWSPREFObsLookupItemDR | bigint |  | FK | SI | Des Ref to Observation Item CT (lookup only) |
| EWSPREFPAADMDR | bigint |  | FK | NO | Reference to Episode |
| EWSPREFPatientAlertDR | bigint |  | FK | SI | Des Ref to Patient Alert CT |
| EWSPREFPregnancyEvent | varchar |  |  | SI | Applies to Pregnancy Event ONLY |
| EWSPREFRangeDR | bigint |  | FK | SI | EWS Score |
| EWSPREFSexDR | bigint |  | FK | SI | Reference to Sex |
| EWSPREFTimeFrom | time |  |  | SI | Time From |
| EWSPREFTimeTo | time |  |  | SI | Time To |
| EWSPREFTo | double |  |  | SI | Range To |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*