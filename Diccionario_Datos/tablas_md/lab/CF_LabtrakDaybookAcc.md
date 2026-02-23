# lab.CF_LabtrakDaybookAcc

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFLDA_ParRef | bigint | PK |  | NO | CF_LabTrak Parent Reference |
| CFDLA_AccNoOrder | double |  |  | NO | Accession Number Order |
| CFLDA_AccNoCase | varchar |  |  | SI | Accession Number Case |
| CFLDA_AccNoField | varchar |  |  | SI | Accession Number Field |
| CFLDA_AccNoPunctuation | varchar |  |  | SI | Accession Number Punctuation |
| CFLDA_RowID | varchar |  |  | NO | - |
| CFLDA_xxx | varchar |  |  | SI | Numeric Sample |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*