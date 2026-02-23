# SQLUser.PA_SMRExtractErrors

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ERR_ParRef | bigint | PK |  | NO | PA_SMRExtract Parent Reference |
| ERR_Childsub | double |  |  | NO | Childsub |
| ERR_Code | varchar |  |  | SI | Code |
| ERR_Error_DR | bigint |  | FK | SI | Des Ref Error |
| ERR_ExtractBuild_DR | bigint |  | FK | SI | Des Ref ExtractBuild |
| ERR_Id | varchar |  |  | SI | Id |
| ERR_NationalCode | varchar |  |  | SI | National Code |
| ERR_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| ERR_Parameters | varchar |  |  | SI | Parameters |
| ERR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*