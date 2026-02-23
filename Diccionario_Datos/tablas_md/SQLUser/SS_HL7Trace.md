# SQLUser.SS_HL7Trace

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7MT_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7MT_AckNak | varchar |  |  | SI | Ack/Nak message |
| HL7MT_Date | date |  |  | NO | Date message received/sent |
| HL7MT_Direction | varchar |  |  | SI | Direction of message |
| HL7MT_Message | varchar |  |  | SI | HL7 message received/sent |
| HL7MT_MessageType | varchar |  |  | SI | Type of message in trace |
| HL7MT_RowId | varchar |  |  | NO | - |
| HL7MT_Sequence | double |  |  | NO | Sequence |
| HL7MT_Time | time |  |  | SI | Time message received/sent |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*