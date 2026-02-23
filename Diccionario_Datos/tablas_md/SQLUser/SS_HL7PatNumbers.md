# SQLUser.SS_HL7PatNumbers

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7PN_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7PN_AssignCode | varchar |  |  | SI | Assigning Code |
| HL7PN_AssignType | varchar |  |  | SI | Assigning Type |
| HL7PN_ExpiryDate | varchar |  |  | SI | Expiry Date |
| HL7PN_ExpiryDateField | double |  |  | SI | Expiry Date Field |
| HL7PN_ExpiryDateFormat | varchar |  |  | SI | Expiry Date Format |
| HL7PN_IdentCode | varchar |  |  | SI | Identifier Code |
| HL7PN_IdentCodeCardType | varchar |  |  | SI | Use Card Type as Identifying Code |
| HL7PN_IdentCodeMRType | varchar |  |  | SI | Use MR Type as Identifying Code |
| HL7PN_NumberType | varchar |  |  | NO | Number Type |
| HL7PN_RowId | varchar |  |  | NO | - |
| HL7PN_SegmentField | double |  |  | SI | Segment Field Number |
| HL7PN_SegmentType | varchar |  |  | SI | Segment Type |
| HL7PN_Validate | varchar |  |  | SI | Validate Number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*