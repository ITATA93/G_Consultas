# lab.CF_LabtrakDrName

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFLDN_ParRef | bigint | PK |  | NO | CF_LabTrak Parent Reference |
| CFLDN_DoctorNameCase | varchar |  |  | SI | Doctor Name Case |
| CFLDN_DoctorNameField | varchar |  |  | SI | Doctor Name Field |
| CFLDN_DoctorNameOrder | double |  |  | NO | Doctor Name Order |
| CFLDN_DoctorNamePunctuation | varchar |  |  | SI | Doctor Name Punctuation |
| CFLDN_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*