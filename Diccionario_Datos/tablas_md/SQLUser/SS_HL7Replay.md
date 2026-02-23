# SQLUser.SS_HL7Replay

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7RP_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7RP_Message | varchar |  |  | SI | HL7 message to replay |
| HL7RP_RowId | varchar |  |  | NO | - |
| HL7RP_Sequence | double |  |  | NO | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*