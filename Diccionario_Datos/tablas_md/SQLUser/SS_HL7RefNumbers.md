# SQLUser.SS_HL7RefNumbers

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7RN_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7RN_AssignCode | varchar |  |  | SI | Assigning Code |
| HL7RN_AssignType | varchar |  |  | SI | Assigning Type |
| HL7RN_IdentCode | varchar |  |  | SI | Identifier Code |
| HL7RN_NumberType | varchar |  |  | NO | Number Type |
| HL7RN_RowId | varchar |  |  | NO | - |
| HL7RN_SegmentField | double |  |  | SI | Segment Field Number |
| HL7RN_SegmentType | varchar |  |  | SI | Segment Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*