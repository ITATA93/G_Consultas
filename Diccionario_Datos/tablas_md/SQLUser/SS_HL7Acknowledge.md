# SQLUser.SS_HL7Acknowledge

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7ACK_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7ACK_ContainError | varchar |  |  | SI | Contains Error Condition |
| HL7ACK_ErrorField | double |  |  | SI | Error Condition Field |
| HL7ACK_Mandatory | varchar |  |  | SI | Mandatory |
| HL7ACK_RowId | varchar |  |  | NO | - |
| HL7ACK_Segment | varchar |  |  | SI | Segment Type |
| HL7ACK_Sequence | double |  |  | NO | Sequence Number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*