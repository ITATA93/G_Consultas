# SQLUser.CT_CareProvLabDoctorReport

**Schema:** SQLUser
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Profesionales**. Médicos y personal de salud.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPCPLBDR_ParRef | varchar | PK |  | NO | CT_CareProv Parent Reference |
| CTPCPLBDR_Childsub | double |  |  | NO | Childsub |
| CTPCPLBDR_CourierCopies | numeric |  |  | SI | The default number of copies of Lab Doctors Report... |
| CTPCPLBDR_Courier_DR | bigint |  | FK | SI | The default Courier to use for Lab Doctors Reports... |
| CTPCPLBDR_CumulativeEpisodes | integer |  |  | SI | Cumulatives Maximum Number of Episodes
The maximu... |
| CTPCPLBDR_CumulativeOrder | varchar |  |  | SI | Doctors Reports Cumulative Order
The Careprovider... |
| CTPCPLBDR_CumulativePreference | varchar |  |  | SI | Doctors Reports Cumulative Preference
The CarePro... |
| CTPCPLBDR_DateFrom | date |  |  | SI | DateFrom |
| CTPCPLBDR_DateTo | date |  |  | SI | DateTo |
| CTPCPLBDR_DeliverySort | varchar |  |  | SI | Doctors Reports Delivery Sort
The sort key to use... |
| CTPCPLBDR_DoctorsReportsType | varchar |  |  | SI | Report Type
The ReportType to use for Doctors Rep... |
| CTPCPLBDR_ExtInterfaceQueue_DR | bigint |  | FK | SI | External Interface Queue |
| CTPCPLBDR_IncludeConfidentialTest | varchar |  |  | SI | Include Confidential Test |
| CTPCPLBDR_Language_DR | bigint |  | FK | SI | Doctors Reports Language
The language in which th... |
| CTPCPLBDR_ManualPrint | varchar |  |  | SI | Manual Print
Flag to show if Doctors Reports to t... |
| CTPCPLBDR_ReportMode | varchar |  |  | SI | Report Mode |
| CTPCPLBDR_RowId | varchar |  |  | NO | - |
| CTPCPLBDR_TestSets | varchar |  |  | SI | Test Set Restriction |
| CTPCPLBDR_UpdatedDate | date |  |  | SI | Updated Date |
| CTPCPLBDR_UpdatedTime | time |  |  | SI | Updated Time |
| CTPCPLBDR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q22Q1 | - |  |  | SI | Hemoglucotest |
| Q22Q2 | - |  |  | SI | Comida |
| Q22Q3 | - |  |  | SI | Fecha |
| Q22Q4 | - |  |  | SI | Hora |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*