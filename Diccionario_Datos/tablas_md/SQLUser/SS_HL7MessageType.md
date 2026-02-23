# SQLUser.SS_HL7MessageType

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7MSG_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7MSG_AlsoSendMsg | varchar |  |  | SI | Also send this message |
| HL7MSG_RowId | varchar |  |  | NO | - |
| HL7MSG_Type | varchar |  |  | NO | Message Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*