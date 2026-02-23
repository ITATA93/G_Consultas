# SQLUser.SS_HL7MessageForwarding

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7MF_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7MF_Interface | varchar |  |  | NO | Outbound Interface |
| HL7MF_MsgType | varchar |  |  | NO | Message Type |
| HL7MF_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*