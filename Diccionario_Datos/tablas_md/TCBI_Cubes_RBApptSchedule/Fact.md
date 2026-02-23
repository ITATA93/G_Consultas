# TCBI_Cubes_RBApptSchedule.Fact

**Schema:** TCBI_Cubes_RBApptSchedule
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxASDate | date |  |  | SI | Dimension: DxASDate<br/>
Source: ASDate |
| DxASDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxASDateFxDayMonthYear<br/>
Source: AS... |
| DxASDateFxMonthNumber | varchar |  |  | SI | Dimension: DxASDateFxMonthNumber<br/>
Source: ASD... |
| DxASDateFxMonthYear | varchar |  |  | SI | Dimension: DxASDateFxMonthYear<br/>
Source: ASDat... |
| DxASDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxASDateFxQuarterNumber<br/>
Source: A... |
| DxASDateFxQuarterYear | varchar |  |  | SI | Dimension: DxASDateFxQuarterYear<br/>
Source: ASD... |
| DxASDateFxYear | varchar |  |  | SI | Dimension: DxASDateFxYear<br/>
Source: ASDate |
| DxAppointmentDayOfWeek | bigint |  |  | SI | Dimension: DxAppointmentDayOfWeek
Expression: $sy... |
| DxCareProvider | bigint |  |  | SI | Dimension: DxCareProvider<br/>
Source: ASRESParRe... |
| DxCareProviderType | bigint |  |  | SI | Dimension: DxCareProviderType<br/>
Source: ASRESP... |
| DxClinic | bigint |  |  | SI | Dimension: DxClinic<br/>
Source: ASRBEffDateSessi... |
| DxDepartment | bigint |  |  | SI | Dimension: DxDepartment<br/>
Source: ASRESParRef.... |
| DxDepartmentCode | bigint |  |  | SI | Dimension: DxDepartmentCode<br/>
Source: ASRESPar... |
| DxEquipment | bigint |  |  | SI | Dimension: DxEquipment<br/>
Source: ASRESParRef.R... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: ASRESParRef.RE... |
| DxIrregularFlag | bigint |  |  | SI | Dimension: DxIrregularFlag<br/>
Source: ASIrregul... |
| DxLinkedCareProvider | bigint |  |  | SI | Dimension: DxLinkedCareProvider<br/>
Source: ASRE... |
| DxLinkedCareProviderType | bigint |  |  | SI | Dimension: DxLinkedCareProviderType<br/>
Source: ... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: ASRESParRef.RE... |
| DxLocationCode | bigint |  |  | SI | Dimension: DxLocationCode<br/>
Source: ASRESParRe... |
| DxLocationType | bigint |  |  | SI | Dimension: DxLocationType
Expression: %expression... |
| DxResource | bigint |  |  | SI | Dimension: DxResource<br/>
Source: ASRESParRef.RE... |
| DxRoom | bigint |  |  | SI | Dimension: DxRoom<br/>
Source: ASRBEffDateSession... |
| DxSessionType | bigint |  |  | SI | Dimension: DxSessionType<br/>
Source: ASRBEffDate... |
| DxSessionTypeOverride | bigint |  |  | SI | Dimension: DxSessionTypeOverride
Expression: "sou... |
| MxHolidaySlot | double |  |  | SI | Measure: MxHolidaySlot
Expression: %cube.GetPubli... |
| MxNotAvailableSessionScheduleSlots | double |  |  | SI | Measure: MxNotAvailableSessionScheduleSlots
Expre... |
| MxNotAvailableSlot | double |  |  | SI | Measure: MxNotAvailableSlot
Expression: %source.A... |
| MxNumberBookedSlots | double |  |  | SI | Measure: MxNumberBookedSlots<br/>
Source: ASBooke... |
| MxNumberSessionSlots | double |  |  | SI | Measure: MxNumberSessionSlots<br/>
Source: ASNoAp... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*