# TCDS_Cubes_RBOperatingRoom_Version73.Fact

**Schema:** TCDS_Cubes_RBOperatingRoom_Version73
**Columnas:** 37
**Actualizado:** 2026-01-30 15:32:02

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx102792014 | varchar |  |  | SI | Dimension: Dx102792014<br/>
Source: RBOPDateArriv... |
| Dx1255190232 | varchar |  |  | SI | Dimension: Dx1255190232<br/>
Source: RBOPDateOper |
| Dx1723263099 | varchar |  |  | SI | Dimension: Dx1723263099<br/>
Source: RBOPDateArri... |
| Dx1913907599 | varchar |  |  | SI | Dimension: Dx1913907599<br/>
Source: RBOPDateArri... |
| Dx2321484328 | varchar |  |  | SI | Dimension: Dx2321484328<br/>
Source: RBOPDateArri... |
| Dx2743488044 | varchar |  |  | SI | Dimension: Dx2743488044<br/>
Source: RBOPDateArri... |
| Dx3358230890 | varchar |  |  | SI | Dimension: Dx3358230890<br/>
Source: RBOPDateOper |
| DxAdmissionToSurgeryDays | bigint |  |  | SI | Dimension: DxAdmissionToSurgeryDays
Expression: "... |
| DxAnaestheticMethod | bigint |  |  | SI | Dimension: DxAnaestheticMethod<br/>
Source: RBOPA... |
| DxAnaesthetist | bigint |  |  | SI | Dimension: DxAnaesthetist<br/>
Source: RBOPAnaest... |
| DxBookingPriority | bigint |  |  | SI | Dimension: DxBookingPriority<br/>
Source: RBOPPri... |
| DxBookingStatus | bigint |  |  | SI | Dimension: DxBookingStatus
Expression: %expressio... |
| DxConsultant | bigint |  |  | SI | Dimension: DxConsultant
Expression: "sourceConsul... |
| DxDSSEpisodeID | bigint |  |  | SI | Dimension: DxDSSEpisodeID<br/>
Source: RBOPPAADMD... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: RBOPPAADMD... |
| DxDaySurgery | bigint |  |  | SI | Dimension: DxDaySurgery<br/>
Source: RBOPDaySurge... |
| DxEndoscopy | bigint |  |  | SI | Dimension: DxEndoscopy<br/>
Source: RBOPEndoscopy |
| DxEstimatedTime | bigint |  |  | SI | Dimension: DxEstimatedTime<br/>
Source: RBOPEstim... |
| DxIntendedOperation | bigint |  |  | SI | Dimension: DxIntendedOperation<br/>
Source: RBOPO... |
| DxIntendedProcedure | bigint |  |  | SI | Dimension: DxIntendedProcedure<br/>
Source: RBOPS... |
| DxOriginalOperation | bigint |  |  | SI | Dimension: DxOriginalOperation
Expression: %expre... |
| DxRBOPDateArrived | date |  |  | SI | Dimension: DxRBOPDateArrived<br/>
Source: RBOPDat... |
| DxRBOPDateArrivedFxYear | varchar |  |  | SI | Dimension: DxRBOPDateArrivedFxYear<br/>
Source: R... |
| DxRBOPDateOper | date |  |  | SI | Dimension: DxRBOPDateOper<br/>
Source: RBOPDateOp... |
| DxRBOPDateOperFxMonthNumber | varchar |  |  | SI | Dimension: DxRBOPDateOperFxMonthNumber<br/>
Sourc... |
| DxRBOPDateOperFxMonthYear | varchar |  |  | SI | Dimension: DxRBOPDateOperFxMonthYear<br/>
Source:... |
| DxRBOPDateOperFxQuarterYear | varchar |  |  | SI | Dimension: DxRBOPDateOperFxQuarterYear<br/>
Sourc... |
| DxRBOPDateOperFxYear | varchar |  |  | SI | Dimension: DxRBOPDateOperFxYear<br/>
Source: RBOP... |
| DxReasonReturnToTheatre | bigint |  |  | SI | Dimension: DxReasonReturnToTheatre<br/>
Source: R... |
| DxReferralLetterToOperation | bigint |  |  | SI | Dimension: DxReferralLetterToOperation
Expression... |
| DxResource | bigint |  |  | SI | Dimension: DxResource<br/>
Source: RBOPResourceDR... |
| DxSurgeon | bigint |  |  | SI | Dimension: DxSurgeon<br/>
Source: RBOPSurgeonDR.C... |
| DxSurgeryToDischargeDays | bigint |  |  | SI | Dimension: DxSurgeryToDischargeDays
Expression: "... |
| DxSuspendReason | bigint |  |  | SI | Dimension: DxSuspendReason<br/>
Source: RBOPReaso... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*