# web_Msg.PAAdmDischargeSummaryRecipients

**Schema:** web_Msg
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| DischID | varchar |  |  | SI | PAAdmDischargeSummary ID |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| RecipientAddress | varchar |  |  | SI | Recipient Address |
| RecipientDesc | varchar |  |  | SI | Recipient Description |
| RecipientID | varchar |  |  | SI | Recipient ID |
| RecipientType | varchar |  |  | SI | Recipient Type |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*