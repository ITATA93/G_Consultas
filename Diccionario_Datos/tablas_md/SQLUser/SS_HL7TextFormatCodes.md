# SQLUser.SS_HL7TextFormatCodes

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7TF_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7TF_AsciiConversion | double |  |  | SI | ASCII Conversion number |
| HL7TF_ExternalSystem | varchar |  |  | NO | External System |
| HL7TF_FormatCode | varchar |  |  | NO | Formatting Code |
| HL7TF_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*