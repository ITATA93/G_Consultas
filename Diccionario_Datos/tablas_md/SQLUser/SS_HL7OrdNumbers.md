# SQLUser.SS_HL7OrdNumbers

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7ON_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7ON_NumberType | varchar |  |  | SI | Number Type |
| HL7ON_RowId | varchar |  |  | NO | - |
| HL7ON_SegmentField | double |  |  | NO | Segment Field Number |
| HL7ON_SegmentType | varchar |  |  | NO | Segment Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*