# web_Msg.LBDR_ReprintReferringDoctor

**Schema:** web_Msg
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBDRRRD_Batch_DR | bigint |  | FK | SI | - |
| LBDRRRD_ConfidentalCourier | varchar |  |  | SI | - |
| LBDRRRD_ReferringDoctor_DR | bigint |  | FK | SI | - |
| LBDRRRD_Selected | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*