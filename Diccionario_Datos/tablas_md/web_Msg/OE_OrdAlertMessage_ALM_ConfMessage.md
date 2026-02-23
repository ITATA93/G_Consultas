# web_Msg.OE_OrdAlertMessage_ALM_ConfMessage

**Schema:** web_Msg
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OE_OrdAlertMessage | varchar | PK |  | NO | Parent reference |
| ALM_ConfMessage | varchar |  |  | SI | ALM_ConfMessage |
| ID | varchar |  |  | NO | - |
| element_key | varchar |  |  | NO | ALMConfMessage array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*