# SQLUser.LBC_ThirdPartyLabDoctorReport

**Schema:** SQLUser
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTPLBDR_ParRef | bigint | PK |  | NO | Parent Third Party DR |
| ChildQ21DR | - |  |  | SI | Child Reference: Ojos |
| LBCTPLBDR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTPLBDR_CourierCopies | numeric |  |  | SI | The default number of copies of Lab Doctors Report... |
| LBCTPLBDR_Courier_DR | bigint |  | FK | SI | The default Courier to use for Lab Doctors Reports... |
| LBCTPLBDR_CumulativeEpisodes | integer |  |  | SI | Cumulatives Maximum Number of Episodes
The maximu... |
| LBCTPLBDR_CumulativeOrder | varchar |  |  | SI | Doctors Reports Cumulative Order
The Careprovider... |
| LBCTPLBDR_CumulativePreference | varchar |  |  | SI | Doctors Reports Cumulative Preference
The CarePro... |
| LBCTPLBDR_DateFrom | date |  |  | SI | DateFrom |
| LBCTPLBDR_DateTo | date |  |  | SI | DateTo |
| LBCTPLBDR_DeliverySort | varchar |  |  | SI | Doctors Reports Delivery Sort
The sort key to use... |
| LBCTPLBDR_DoctorsReportsType | varchar |  |  | SI | Report Type
The ReportType to use for Doctors Rep... |
| LBCTPLBDR_ExtInterfaceQueue_DR | bigint |  | FK | SI | External Interface Queue |
| LBCTPLBDR_IncludeConfidentialTest | varchar |  |  | SI | Include Confidential Test |
| LBCTPLBDR_Language_DR | bigint |  | FK | SI | Doctors Reports Language
The language in which th... |
| LBCTPLBDR_ManualPrint | varchar |  |  | SI | Manual Print
Flag to show if Doctors Reports to t... |
| LBCTPLBDR_ReportMode | varchar |  |  | SI | Report Mode |
| LBCTPLBDR_RowID | varchar |  |  | NO | - |
| LBCTPLBDR_TestSets | varchar |  |  | SI | Test Set Restriction |
| LBCTPLBDR_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTPLBDR_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTPLBDR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q83Q1 | - |  |  | SI | Reflejos |
| Q83Q2 | - |  |  | SI | Estado |
| Q83Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*