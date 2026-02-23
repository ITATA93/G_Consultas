# lab.CF_LabtrakPatName

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFLPN_ParRef | bigint | PK |  | NO | CF_LabTrak Parent Reference |
| CFLPN_PatientNameCase | varchar |  |  | SI | Patient Name Case |
| CFLPN_PatientNameField | varchar |  |  | SI | Patient Name Field |
| CFLPN_PatientNameOrder | double |  |  | NO | Patient Name Order |
| CFLPN_PatientNamePunctuation | varchar |  |  | SI | Patient Name Punctuation |
| CFLPN_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*