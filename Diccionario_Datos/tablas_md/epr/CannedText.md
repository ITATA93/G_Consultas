# epr.CannedText

**Schema:** epr
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Code | varchar |  |  | NO | - |
| FormattedText | longvarchar |  |  | SI | The Formatted Text (HTML Rich Text) |
| FormattedTextEnabled | varchar |  |  | SI | Flag to indicate if the Formatted Text is enabled ... |
| ReferenceID | varchar |  |  | NO | this code is saved against referenced rowid for co... |
| ReferenceType | varchar |  |  | NO | this code is saved against type of: user/group/sit... |
| Text | varchar |  |  | NO | the long text |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*