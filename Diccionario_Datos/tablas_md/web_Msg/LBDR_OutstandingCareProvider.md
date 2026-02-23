# web_Msg.LBDR_OutstandingCareProvider

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
| LBDROCP_CareProvider_DR | varchar |  | FK | SI | - |
| LBDROCP_ConfidentalCourier | varchar |  |  | SI | - |
| LBDROCP_Courier_DR | bigint |  | FK | SI | - |
| LBDROCP_Selected | varchar |  |  | SI | - |
| LBDROCP_TestSet_DR | bigint |  | FK | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*