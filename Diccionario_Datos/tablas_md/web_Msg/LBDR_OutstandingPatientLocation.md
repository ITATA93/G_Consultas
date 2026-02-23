# web_Msg.LBDR_OutstandingPatientLocation

**Schema:** web_Msg
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBDROPL_ConfidentalCourier | varchar |  |  | SI | - |
| LBDROPL_Courier_DR | bigint |  | FK | SI | - |
| LBDROPL_NumberOfJobs | integer |  |  | SI | - |
| LBDROPL_PatientLocation_DR | bigint |  | FK | SI | - |
| LBDROPL_Selected | varchar |  |  | SI | - |
| LBDROPL_TestSet_DR | bigint |  | FK | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*