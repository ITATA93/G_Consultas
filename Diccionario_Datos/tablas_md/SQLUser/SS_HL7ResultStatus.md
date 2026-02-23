# SQLUser.SS_HL7ResultStatus

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7RS_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7RS_ExtResStatus | varchar |  |  | NO | External System Result Status |
| HL7RS_ExternalSys | varchar |  |  | NO | External System |
| HL7RS_RowId | varchar |  |  | NO | - |
| HL7RS_TrakResStatus | varchar |  |  | SI | TrakCare Result Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*