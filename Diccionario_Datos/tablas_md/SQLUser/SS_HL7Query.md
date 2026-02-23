# SQLUser.SS_HL7Query

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7QU_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7QU_AllowContinuation | varchar |  |  | SI | Allow search continuation |
| HL7QU_Count | double |  |  | NO | Part of RowId - Always 1 |
| HL7QU_DOBSexOnlySearch | varchar |  |  | SI | Allow DOB & Sex only search |
| HL7QU_NumberRecordsRequested | double |  |  | SI | Number of records requested |
| HL7QU_QueryUniqueKey | double |  |  | SI | Unique key counter |
| HL7QU_RowId | varchar |  |  | NO | - |
| HL7QU_SearchTypes | varchar |  |  | SI | Search types allowed |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*