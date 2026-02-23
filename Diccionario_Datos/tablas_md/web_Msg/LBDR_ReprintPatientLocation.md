# web_Msg.LBDR_ReprintPatientLocation

**Schema:** web_Msg
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBDRRPL_Batch_DR | bigint |  | FK | SI | - |
| LBDRRPL_ConfidentalCourier | varchar |  |  | SI | - |
| LBDRRPL_NumberOfJobs | integer |  |  | SI | - |
| LBDRRPL_PatientLocation_DR | bigint |  | FK | SI | - |
| LBDRRPL_Selected | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*