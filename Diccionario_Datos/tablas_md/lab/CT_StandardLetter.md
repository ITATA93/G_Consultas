# lab.CT_StandardLetter

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSL_RowId | varchar | PK |  | NO | - |
| CTSL_Code | varchar |  |  | NO | Code |
| CTSL_Department_DR | varchar |  | FK | SI | Department |
| CTSL_Desc | varchar |  |  | SI | Description |
| CTSL_DoctorPatient | varchar |  |  | SI | Doctor Patient switch |
| CTSL_FILE_NAME | varchar |  |  | SI | File Name |
| CTSL_ListHeader | varchar |  |  | SI | List Header |
| CTSL_NumberOfDays | double |  |  | SI | Number Of Days |
| CTSL_SingleLetterForPatient | varchar |  |  | SI | Single Letter For Patient |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*