# SQLUser.CT_LocLabDoctorReport

**Schema:** SQLUser
**Columnas:** 34
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLOCLBDR_ParRef | bigint | PK |  | NO | CT_CareProv Parent Reference |
| CTLOCLBDR_CareProvCourier_DR | bigint |  | FK | SI | For PatientLocation: Not used
For LabSite: The de... |
| CTLOCLBDR_Childsub | double |  |  | NO | Childsub |
| CTLOCLBDR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTLOCLBDR_CumulativeEpisodes | integer |  |  | SI | Cumulatives Maximum Number of Episodes
The maximu... |
| CTLOCLBDR_CumulativeOrder | varchar |  |  | SI | Doctors Reports Cumulative Order
The Careprovider... |
| CTLOCLBDR_CumulativePreference | varchar |  |  | SI | Doctors Reports Cumulative Preference
The CarePro... |
| CTLOCLBDR_DateFrom | date |  |  | SI | DateFrom |
| CTLOCLBDR_DateTo | date |  |  | SI | DateTo |
| CTLOCLBDR_DeliverySort | varchar |  |  | SI | Doctors Reports Delivery Sort
The sort key to use... |
| CTLOCLBDR_DoctorsReportsType | varchar |  |  | SI | Report Type
The ReportType to use for Doctors Rep... |
| CTLOCLBDR_ExtInterfaceQueue_DR | bigint |  | FK | SI | External Interface Queue |
| CTLOCLBDR_IncludeConfidentialTest | varchar |  |  | SI | Include Confidential Test |
| CTLOCLBDR_Language_DR | bigint |  | FK | SI | Doctors Reports Language
The language in which th... |
| CTLOCLBDR_LocCourierCopies | numeric |  |  | SI | The default #copies to use with CTLOCLBDRLocCourie... |
| CTLOCLBDR_LocCourier_DR | bigint |  | FK | SI | For PatientLocation: The default Courier to use fo... |
| CTLOCLBDR_ManualPrint | varchar |  |  | SI | Manual Print
Flag to show if Doctors Reports to t... |
| CTLOCLBDR_RefDoctorCourier_DR | bigint |  | FK | SI | For PatientLocation: Not used
For LabSite: The de... |
| CTLOCLBDR_ReportMode | varchar |  |  | SI | Report Mode |
| CTLOCLBDR_RowId | varchar |  |  | NO | - |
| CTLOCLBDR_TestSets | varchar |  |  | SI | Test Set Restriction |
| CTLOCLBDR_ThirdPartyCourier_DR | bigint |  | FK | SI | For PatientLocation: Not used
For LabSite: The de... |
| CTLOCLBDR_UpdatedDate | date |  |  | SI | Updated Date |
| CTLOCLBDR_UpdatedTime | time |  |  | SI | Updated Time |
| CTLOCLBDR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CTLOCLBDR_UseCurrentPatientLocation | varchar |  |  | SI | Report To Current Patient Location |
| Q17Q1 | - |  |  | SI | Agente anestésico |
| Q17Q2 | - |  |  | SI | Otro (Texto Libre) |
| Q17Q3 | - |  |  | SI | Dosis |
| Q17Q4 | - |  |  | SI | Unidad de medida |
| Q17Q5 | - |  |  | SI | Dilución (ml) |
| Q17Q6 | - |  |  | SI | Modelo |
| Q17Q7 | - |  |  | SI | Comentario / Observaciones |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*