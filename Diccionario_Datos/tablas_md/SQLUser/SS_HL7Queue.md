# SQLUser.SS_HL7Queue

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7MQ_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7MQ_MSHReceivingApp | varchar |  |  | SI | MSH Receiving Application to send |
| HL7MQ_MSHReceivingFac | varchar |  |  | SI | MSH Receiving Facility to send |
| HL7MQ_MSHSendingFac | varchar |  |  | SI | MSH Sending Facility to send |
| HL7MQ_Message | varchar |  |  | SI | HL7 message queued |
| HL7MQ_RowId | varchar |  |  | NO | - |
| HL7MQ_Sequence | double |  |  | NO | Sequence |
| HL7MQ_Type | varchar |  |  | SI | Message type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*