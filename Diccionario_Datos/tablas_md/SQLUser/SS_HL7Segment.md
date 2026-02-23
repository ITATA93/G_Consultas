# SQLUser.SS_HL7Segment

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7SEG_ParRef | varchar | PK |  | NO | SS_HL7MessageType Parent Reference |
| HL7SEG_Mandatory | varchar |  |  | SI | Mandatory |
| HL7SEG_MaxNumberOfRepeats | double |  |  | SI | Maximum Number of Repeats |
| HL7SEG_Repeatable | varchar |  |  | SI | Repeat |
| HL7SEG_RowId | varchar |  |  | NO | - |
| HL7SEG_Sequence | double |  |  | NO | Sequence number |
| HL7SEG_Type | varchar |  |  | SI | Segment Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*