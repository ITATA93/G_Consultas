# web_Msg.LBDR_OutstandingReferringDoctor

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
| LBDRORD_Clinic_DR | bigint |  | FK | SI | - |
| LBDRORD_ConfidentalCourier | varchar |  |  | SI | - |
| LBDRORD_Courier_DR | bigint |  | FK | SI | - |
| LBDRORD_ReferringDoctor_DR | bigint |  | FK | SI | - |
| LBDRORD_Selected | varchar |  |  | SI | - |
| LBDRORD_TestSet_DR | bigint |  | FK | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*